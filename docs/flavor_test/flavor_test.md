---
description: Verify how flavor filtering, inline branching, and card grids behave in the SaaS and on-premises builds.
flavor:
    - saas
    - onprem
---

# Flavor test

This page belongs to both the SaaS and the on-premises build, and it demonstrates the
delivery-flavor mechanism.
It uses the list form of the `flavor` front matter key, which states explicitly that both
flavors include the page.

Two separate mechanisms are involved, and they must not be confused.
The `flavor` front matter key selects the builds that contain the whole page, while the
`is_saas()` and `is_onprem()` macros test the flavor being built from inside a page.

Use the macros for conditions.

## Page filtering

The `flavor` front matter key accepts the following values:

|Front matter|Included in|
|------------|-----------|
|no `flavor` key|both flavors, which is the default for all existing pages|
|`flavor: saas`|the SaaS build only|
|`flavor: onprem`|the on-premises build only|
|`flavor: [saas, onprem]`|both flavors, stated explicitly|

An unrecognized value, such as `flavor: sass`, fails the build instead of removing the page
from both flavors.

## Inline branching

The following paragraph differs between the two builds:

[[% if is_saas() %]]
**SaaS build.** Ibexa provisions your instance and provides the address of the back office.
[[% else %]]
**On-premises build.** Your administrator installs the product and provides the address of
the back office.
[[% endif %]]

It's produced by the following source:

[[% raw %]]

```markdown
[[% if is_saas() %]]
Ibexa provisions your instance and provides the address of the back office.
[[% else %]]
Your administrator installs the product and provides the address of the back office.
[[% endif %]]
```

[[% endraw %]]

## Gated cross-links

When a page exists in one flavor only, every link that points to it must be gated as well.
Otherwise the build of the other flavor fails on an unresolved link, because the
documentation is built with strict validation.

[[% if is_saas() %]]

- [SaaS-only page](saas_only.md)
- [SaaS-only child page](saas_only_section/saas_child.md)

[[% endif %]]
[[% if is_onprem() %]]

- [On-premises-only page](onprem_only.md)
- [On-premises HTML reference](onprem_ref/index.html)

[[% endif %]]

## Files without front matter

Generated bundles, such as an API reference, are copied into the site verbatim rather than
rendered, and a generator overwrites them on every run, so they can't carry a `flavor` key.
Their flavor is declared in the `flavor_paths` setting under `extra` in `mkdocs.yml`, which
maps each flavor to the path patterns that it includes:

```yaml
extra:
    flavor_paths:
        onprem:
            - flavor_test/onprem_ref/*
```

Patterns are matched against paths relative to the documentation directory, and a single
`*` also spans directory separators, so one pattern covers a whole generated tree.

The setting is exercised by a fixture bundle of three files, an index page, a nested page,
and a stylesheet.
The on-premises build contains all three, together with a navigation entry for the bundle,
and the SaaS build contains none of them.

## Card grid

The following card grid lists all four test pages.
Cards that point to a page the current build excludes are dropped automatically, so the
grid contains:

- three cards in the SaaS build: this page, SaaS only, and SaaS only child
- two cards in the on-premises build: this page and On-premises only

[[= cards([
    "flavor_test/flavor_test",
    "flavor_test/saas_only",
    "flavor_test/onprem_only",
    "flavor_test/saas_only_section/saas_child"
], columns=2) =]]
