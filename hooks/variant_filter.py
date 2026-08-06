"""Drop pages that don't belong to the delivery flavor being built.

See flavors.py for the `flavor` front matter contract. This hook removes excluded pages
from the navigation *and* from the file collection: `mkdocs.yml` sets
`validation.omitted_files: warn` and `.readthedocs.yml` sets `fail_on_warning: true`, so a
nav entry pointing at a page that was filtered out fails the build.

The navigation is pruned in `on_config` rather than in `on_files`, because `hooks.py`
derives the llmstxt `sections` config from `nav` during its own `on_config`. Hooks run in
the order they're listed in `mkdocs.yml`, so this one has to stay ahead of `hooks.py`.
"""

import logging
import os
import re
import sys

from mkdocs.structure.files import Files
from mkdocs.utils import meta

# MkDocs imports hooks by file path, so the repository root isn't necessarily importable.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flavors import config_excluded_paths, current_flavor, page_matches  # noqa: E402

log = logging.getLogger("mkdocs.hooks.variant_filter")

#: Pages excluded from the current build, as source URIs relative to `docs_dir`.
#: Computed in `on_config` and reused in `on_files`, and recomputed on every rebuild
#: when running `mkdocs serve`.
_excluded = set()


def _front_matter(path):
    with open(path, encoding="utf-8-sig") as handle:
        return meta.get_data(handle.read())[1]


def _excluded_pages(docs_dir, flavor, flavor_paths=None):
    """Source URIs this flavor excludes, from front matter and from `flavor_paths`."""
    excluded = set()
    src_uris = []

    for root, _dirs, filenames in os.walk(docs_dir):
        for filename in filenames:
            path = os.path.join(root, filename)
            src_uri = os.path.relpath(path, docs_dir).replace(os.sep, "/")
            src_uris.append(src_uri)
            if filename.endswith(".md") and not page_matches(
                _front_matter(path), flavor, src_uri
            ):
                excluded.add(src_uri)

    # Files without front matter, such as generated API reference bundles.
    excluded |= config_excluded_paths(flavor_paths, flavor, src_uris)

    return excluded


def _prune_nav(items, excluded):
    """Copy a nav tree without the excluded pages, dropping sections left empty."""
    pruned = []

    for item in items:
        if isinstance(item, str):
            if item not in excluded:
                pruned.append(item)
        elif isinstance(item, dict):
            for title, target in item.items():
                if isinstance(target, str):
                    if target not in excluded:
                        pruned.append({title: target})
                elif isinstance(target, list):
                    children = _prune_nav(target, excluded)
                    # An entire section disappears with its last remaining page.
                    if children:
                        pruned.append({title: children})
                else:
                    pruned.append({title: target})
        else:
            pruned.append(item)

    return pruned


def _retarget_llmstxt(config):
    """Point the generated llms.txt at the SaaS version of the site.

    `plugins.yml` pins `base_url` to the release branch. The `saas` branch is a
    byte-identical copy of that branch, so this can't be fixed by editing the file.
    """
    plugin = config["plugins"].get("llmstxt")
    if plugin is None:
        return

    base_url = plugin.config.get("base_url")
    if not base_url:
        return

    saas_url = re.sub(r"/en/[^/]+/?$", "/en/saas/", base_url)
    plugin.config["base_url"] = saas_url
    # The plugin snapshots base_url into `_base_url` in its own `on_config`, which runs
    # before any hook, so the config value alone would no longer be read.
    plugin._base_url = saas_url


def on_config(config, **kwargs):
    global _excluded

    flavor = current_flavor()
    _excluded = _excluded_pages(
        config["docs_dir"], flavor, (config["extra"] or {}).get("flavor_paths")
    )

    if flavor == "saas":
        _retarget_llmstxt(config)

    if not _excluded:
        return config

    log.info(
        "[variant_filter] flavor '%s' excludes %d page(s): %s",
        flavor,
        len(_excluded),
        ", ".join(sorted(_excluded)),
    )

    if config["nav"]:
        config["nav"] = _prune_nav(config["nav"], _excluded)

    return config


def on_files(files, config):
    if not _excluded:
        return files

    return Files([file for file in files if file.src_uri not in _excluded])
