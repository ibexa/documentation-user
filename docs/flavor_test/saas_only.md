---
description: Verify that a page marked as SaaS only is built for the SaaS flavor and excluded from the on-premises flavor.
flavor: saas
---

# SaaS only

This page uses `flavor: saas`, so only the SaaS build contains it.

The on-premises build excludes it from the following:

- the page itself, which isn't rendered
- the navigation, including its parent section
- card grids that reference it
- the search index and the generated `llms.txt` files

For the full contract, see the [flavor test hub](flavor_test.md), which both flavors
contain.
