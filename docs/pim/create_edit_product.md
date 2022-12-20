---
description: Create new products or modify existing ones.
---

# Create and edit products

[Products](products.md#products) are a specific kind of [Content items](../content_management/content_items.md#content-items) that you use 
to present your offer in the website, including product specification, and pricing.
Individual products are instances of [Product Types](create_product_types.md#create-product-types).
You can only create or modify products when your [user role](../permission_management/work_with_permissions.md) has the `Product/Edit` permission.

To create a product, depending on how the Product Type is defined, you [may need to provide](products.md#product-completeness) certain pieces 
of information in their respective [Fields](../content_management/content_model.md#fields-and-field-types).

You can create product by using manual or bulk method.
Bulk method can be used only at the developer level. See [Products](https://doc.ibexa.co/en/latest/pim/product_api/#products) for a technical guide on how to do this.

## Manually create product

You can create product in several ways:

- Click **Create** in the upper-right corner of the [Products](products.md) screen. 
- While viewing a **Product Catalog** in the [Content Tree](../getting_started/discover_ui.md#content-tree), click **Create content** at the top of the screen.
The new item appears in the tree.
- Click **Create content** in the upper-right corner of the [My dashboard](../getting_started/discover_ui.md) screen. In this case you have to choose Content Type and select where the content will be located.

1\. If you are adding a new product, use one of the methods mentioned above and skip to step 3.

![Adding a Product](img/add_product.png "Adding a Product")

2\. If you are editing an existing product, click the **Edit** button next to a name of the product item that you want to modify and skip to step 4.

![Editing a product](img/edit_product.png "Editing a product")

3\. From their lists, select the language and the product type, and then click the **Add** button.

4\. Fill in or edit content fields of the product, for example, name, specification and description.
Fields marked with an asterisk (*) are required.

5\. In the Attributes section, define the product's attributes, for example, dimensions, resolution or capacity.

6\. If you are adding a new product, click the **Create** button.
If you are editing an existing one, click the **Update** button.

![Creating a product](img/create_product.png "Creating a product")


After you create a product, you can [add image assets to a product](work_with_product_assets.md), [create variants to the main product](work_with_product_variants.md), [define product prices](manage_prices_and_stock.md), and [clasify products into different categories](work_with_product_categories.md).

!!! note

    Feature availability may differ depending on the specifics of your installation.

For more information, see [Products](https://doc.ibexa.co/en/latest/pim/products/).