---
description: Verify that a navigation section is removed when the only page it contains is excluded from the build.
flavor: saas
---

# SaaS only child

This page uses `flavor: saas` and it's the only page in its navigation section.

The on-premises build must therefore drop the whole **SaaS only section** entry, not only
this page.
A section that remains in the navigation without any page fails the build.

For the full contract, see the [flavor test hub](../flavor_test.md), which both flavors
contain.
