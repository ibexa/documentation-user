---
description: Quable PIM integration allows you to use products managed in Quable as the source of product data in Ibexa DXP.
month_change: true
---

# Quable PIM integration

[[= product_name =]] can be connected to [[[= pim_product_name =]]](https://www.quable.com/en) as an external product information management (PIM) system.
After the feature is [configured]([[= developer_doc =]]/product-catalog/install-quable), [[= pim_product_name =]] becomes the central place for managing product data.
All product information is maintained in [[= pim_product_name =]] and automatically made available in [[= product_name =]].

This allows teams to work with consistent product data in the [[= product_name =]] interface, without duplicating or manually transferring information between systems.

## Work with [[= pim_product_name =]] products

When [[= pim_product_name =]] is configured as the source of product information, you can use product data directly in [[= product_name =]].

### Browse and search products

Products from [[= pim_product_name =]] are available in [[= product_name =]] and can be browsed and searched for using categories and filters.
This makes it easier to find and work with the right products when creating content.

### Use products in content

You can select and [embed products in content items](../content_management/create_edit_content_items.md#embed-products), for example when creating articles or promotional pages.
Product data is always up to date and reflects the current state in [[= pim_product_name =]].

### Manage prices and availability

[Product prices](manage_prices.md) and [availability and stock](manage_availability_and_stock.md) can be managed in [[= product_name =]].

You can define pricing rules, such as [discounts](discounts.md) for specific regions or customer groups.

## Managing product data

When [[= pim_product_name =]] is the source of product information, product data is not managed in [[= product_name =]].

The following actions must be performed in [[= pim_product_name =]]:

- creating, editing, or deleting products
- updating product attributes and translations
- managing product categories

This ensures that product data remains consistent across all systems and channels.

To learn more about the limitations of the integration with [[= pim_product_name =]], see [known limitations]([[= developer_doc =]]/product_catalog/quable/quable_guide/#known-limitations) in the developer documentation.
