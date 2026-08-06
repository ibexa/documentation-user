import os
import pprint
import re
import urllib.request
from mkdocs.structure.pages import Page
from mkdocs.utils import meta
from typing import List

from flavors import current_flavor, is_onprem, is_saas, page_matches

def _absolute_page_url(scheme, site, project, edition, language, version, *parts):
    return scheme + '://' + '/'.join((site, project, edition, language, version) + parts)


CARDS_TEMPLATE = """
<div class="card-wrapper">
    <div>
        <a href="%s" class="card">
            <div>
                <p class="title">%s</p>
                <p class="description">%s</p>
            </div>
        </a>
    </div>
</div>
"""


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    env.macro(is_saas)
    env.macro(is_onprem)

    @env.macro
    def include_file(filename, start_line=0, end_line=None, glue='', remove_indent=False):
        """
        Include a file,
        optionally indicating start_line and end_line (start counting from 0)
        optionally set a glue string to lead every string except the first one (can be used for indent)
        optionally remove common leading whitespace from all lines (remove_indent=True)
        The path is relative to the top directory of the documentation
        project.
        """
        full_filename = os.path.join(env.project_dir, filename)
        with open(full_filename, 'r') as f:
            lines = f.readlines()
        line_range = lines[start_line:end_line]

        if remove_indent:
            non_empty = [l for l in line_range if l.strip()]
            if non_empty:
                indent = min(len(l) - len(l.lstrip()) for l in non_empty)
                line_range = [l[indent:] if l.strip() else l for l in line_range]

        return glue.join(line_range)

    @env.macro
    def cards(pages, columns=1, style="cards", force_version=False):
        current_page = env.variables.page
        absolute_url = current_page.abs_url
        canonical = current_page.canonical_url
        url_parts = re.search(r"^(https?)://([^/]+)/([^/]+)/([^/]+)/([^/]+)/([^/]+)/", canonical)
        (scheme, site, project, edition, language, version) = url_parts.groups()

        version = force_version or version
        version = os.getenv("READTHEDOCS_VERSION_NAME", version)

        rtd_canonical = os.getenv("READTHEDOCS_CANONICAL_URL", "")
        if rtd_canonical:
            rtd_domain = re.search("//([^/]+)/", rtd_canonical)
            if rtd_domain:
                site = rtd_domain.group(1)

        if isinstance(pages, str):
            pages = [pages]
        variables = env.conf.get('extra', {})
        var_start = env.config['j2_variable_start_string']
        var_end = env.config['j2_variable_end_string']
        cards = []
        for page_data in pages:
            if isinstance(page_data, tuple):
                page, custom_title, custom_description = page_data
            else:
                page = page_data
                custom_title = None
                custom_description = None

            path, hash = page.split("#") if "#" in page else (page, "")
            if hash:
                hash = '#' + hash

            if re.search("^https://[^@/]+.ibexa.co", path):
                html = True
                content = urllib.request.urlopen(path).read().decode('utf-8')
            elif re.search(".html$", path):
                html = True
                content = open("docs/%s" % path, "r").read()
                page = _absolute_page_url(scheme, site, project, edition, language, version, page)
            else:
                html = False
                path = path.rstrip('/')
                source = "docs/%s.md" % path
                content = open(source, "r").read()
                # Cards are built by reading the target file straight off disk, which
                # bypasses the flavor filtering applied to the Files collection. Skip
                # targets this build excludes, or the card links to a page that
                # doesn't exist in it.
                if not page_matches(meta.get_data(content)[1], current_flavor(), source):
                    continue
                page = _absolute_page_url(scheme, site, project, edition, language, version, path, hash)

            if html:
                match = re.search("<meta property=\"og:title\" content=\"(.*)\"", content, re.MULTILINE)
                if match:
                    title = match.groups()[0]
                else:
                    match = re.search("<title>(.*)</title>", content, re.MULTILINE)
                    if match:
                        title = match.groups()[0]
                    else:
                        title = ""
                match = re.search("<meta property=\"og:description\" content=\"(.*)\"", content, re.MULTILINE)
                if match:
                    description = match.groups()[0]
                else:
                    match = re.search("<meta name=\"description\" content=\"(.*)\"", content, re.MULTILINE)
                    if match:
                        description = match.groups()[0]
                    else:
                        description = ""
                href = page
                title = custom_title if custom_title else title
                title = title.replace("(Ibexa Documentation)", "").strip()
                description = custom_description if custom_description else description
            else:
                match = re.search("^# (.*)", content, re.MULTILINE)
                if match:
                    header = match.groups()[0]
                else:
                    header = ""
                default_meta = {
                    "title": header,
                    "short": "",
                    "description": ""
                }
                current_meta = {
                    **default_meta,
                    **meta.get_data(content)[1]
                }
                href = page
                title = custom_title if custom_title else current_meta['short'] or current_meta['title']
                description = custom_description if custom_description else current_meta['description'] or "&nbsp;"
                title = resolve_variables(title, var_start, var_end, variables)
                description = resolve_variables(description, var_start, var_end, variables)

            cards.append(
                CARDS_TEMPLATE % (
                    href,
                    title,
                    description
                )
            )

        return """<div class="%s col-%s">%s</div>""" % (style, columns, "\n".join(cards))

    def resolve_variables(text, var_start, var_end, variables):
        """Replace variable references (e.g. [[= var =]]) with variables."""
        pattern = re.escape(var_start) + r'\s*([\w.]+)\s*' + re.escape(var_end)
        def replacer(match):
            key = match.group(1).strip()
            if key not in variables:
                raise KeyError("Undefined variable '%s' used in cards macro" % key)
            return str(variables[key])
        return re.sub(pattern, replacer, text)

def on_pre_page_macros(env):
    """
    Resolve variable references in the page's description front matter field
    so that they are substituted before MkDocs renders the <meta> tag.
    """
    page = env._page
    if page.meta and 'description' in page.meta:
        page.meta['description'] = env.render(
            markdown=page.meta['description'],
            force_rendering=True
        )
