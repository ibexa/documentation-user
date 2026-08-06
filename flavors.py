"""Delivery-flavor (SaaS / on-premises) filtering for the user documentation.

One content tree is built twice: once for the self-hosted product and once for the SaaS
offering. The flavor is derived from the Read the Docs version name, which is what lets
the `saas` branch stay a byte-identical fast-forward of the release branch instead of a
content fork.

Pages opt out of a flavor through the `flavor` front matter key, which accepts a single
value or a list:

    (key absent)             both flavors -- the default
    flavor: saas             SaaS only
    flavor: onprem           on-premises only
    flavor: [saas, onprem]   both, stated explicitly

Shared by `main.py` (the mkdocs-macros module, for the `cards` macro) and
`hooks/variant_filter.py` (which drops pages and nav entries), so both apply exactly the
same rules.
"""

import fnmatch
import os

FLAVORS = ("saas", "onprem")
DEFAULT_FLAVOR = "onprem"

#: Read the Docs version name that selects the SaaS flavor.
SAAS_VERSION_NAME = "saas"


def current_flavor():
    """Return the flavor being built.

    `DOC_FLAVOR` wins, for local builds and CI; otherwise the Read the Docs version name
    decides, so no committed file has to differ between the release and `saas` branches.
    """
    override = os.getenv("DOC_FLAVOR")
    if override:
        flavor = override.strip().lower()
        if flavor not in FLAVORS:
            raise ValueError(
                "DOC_FLAVOR is '%s', expected one of %s" % (override, list(FLAVORS))
            )
        return flavor

    version = os.getenv("READTHEDOCS_VERSION_NAME", "").strip().lower()

    return "saas" if version == SAAS_VERSION_NAME else DEFAULT_FLAVOR


def is_saas():
    """Whether the SaaS flavor is being built. Exposed to pages as a macro."""
    return current_flavor() == "saas"


def is_onprem():
    """Whether the on-premises flavor is being built. Exposed to pages as a macro."""
    return current_flavor() == "onprem"


def page_flavors(page_meta, source=None):
    """Return the set of flavors a page belongs to, or None meaning "every flavor".

    Raises ValueError on an unrecognized value. Failing the build is deliberate: a typo
    such as `flavor: sass` would otherwise drop the page from *both* builds, and a page
    that silently ceases to exist is the worst failure mode this mechanism can have.
    """
    value = (page_meta or {}).get("flavor")
    if not value:
        return None

    if isinstance(value, str):
        value = [value]

    flavors = {str(item).strip().lower() for item in value}
    unknown = sorted(flavors - set(FLAVORS))
    if unknown:
        raise ValueError(
            "Unknown flavor %s in %s, expected any of %s"
            % (unknown, source or "front matter", list(FLAVORS))
        )

    return flavors


def page_matches(page_meta, flavor, source=None):
    """Whether a page with this front matter belongs in a build of `flavor`."""
    flavors = page_flavors(page_meta, source)

    return flavors is None or flavor in flavors


def config_excluded_paths(flavor_paths, flavor, src_uris):
    """Paths excluded by the `extra.flavor_paths` config, for files without front matter.

    Generated files such as API reference bundles are plain HTML copied into the site, and
    a generator overwrites them on every run, so they can't carry a `flavor` key.
    `flavor_paths` maps a flavor to the path patterns that it includes:

        extra:
            flavor_paths:
                onprem:
                    - api/php_api/*

    Patterns are matched with fnmatch against paths relative to `docs_dir`, so a single
    `*` also spans directory separators and covers a whole generated tree. A path listed
    under several flavors belongs to all of them, the same as a list-valued `flavor` key.
    """
    declared_flavors = {}

    for declared, patterns in (flavor_paths or {}).items():
        declared_flavor = str(declared).strip().lower()
        if declared_flavor not in FLAVORS:
            raise ValueError(
                "Unknown flavor '%s' in extra.flavor_paths, expected any of %s"
                % (declared, list(FLAVORS))
            )
        for pattern in patterns or []:
            matched = [uri for uri in src_uris if fnmatch.fnmatch(uri, pattern)]
            if not matched:
                raise ValueError(
                    "Pattern '%s' in extra.flavor_paths matches no file under docs" % pattern
                )
            for uri in matched:
                declared_flavors.setdefault(uri, set()).add(declared_flavor)

    return {uri for uri, flavors in declared_flavors.items() if flavor not in flavors}
