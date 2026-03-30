---
description: Quable PIM integration allows you to use products managed in Quable as the source of product data in Ibexa DXP.
---

# [[= pim_product_name =]] PIM integration

[[= product_name =]] integrates with [[[= pim_product_name =]]](https://www.quable.com/en) as an external Product Information Management (PIM) source.
When the integration is active, [[= pim_product_name =]] becomes the authoritative source for product data.
Product types, products, variants, categories, and assets all come from [[= pim_product_name =]].

[[= product_name =]] reads this data and makes it available for digital experiences: storefronts, landing pages, personalized campaigns, and APIs.
Product management — creating, updating, or deleting product data — happens entirely in [[= pim_product_name =]], not in [[= product_name =]].

## Working with [[= pim_product_name =]] products

When [[= pim_product_name =]] is configured as the product data source, you can use the following [[= product_name =]] features with [[= pim_product_name =]] products:

### Browse and search products

All products from your [[= pim_product_name =]] instance appear in the product catalog, organized by type and category.

### Market your products

You can [embed [[= pim_product_name =]] products in content items](create_edit_content_items.md#embed-products) and [landing pages](block_reference.md#product-embed), for example to create product-focused articles or promotional pages.

### Manage prices and availability

[Product prices](manage_prices.md) and [availability and stock](manage_availability_and_stock.md) are stored and managed in [[= product_name =]], even when using [[= pim_product_name =]] PIM.
Use [discounts](discounts.md) to define advaned pricing strategies, for example for different regions or customer groups.

## Managing product data

When [[= pim_product_name =]] is the PIM source, the following operations are not available in [[= product_name =]] and must be performed in the [[= pim_product_name =]] interface instead:

- Create, edit, or delete products
- Create, edit, or delete product types
- Edit product assets
- Create or modify product categories
- Modify product attributes

To learn more about the limitations of the [[= pim_product_name =]] integration, see [[[= pim_product_name =]]]([[= dev_doc =]]) in the developer documentation.
