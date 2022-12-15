---
description: Create new products or modify existing ones.
---

# Create products

[Products](products.md#products) are a specific kind of [Content items](../content_management/content_items.md#content-items) that you use 
to present your offer in the website, including product specification, and pricing.

Individual products are instances of [product types](create_product_types.md#create-product-types).

You can only create or modify products when your [user role](../permission_management/work_with_permissions.md) has the `Product/Edit` permission.

To create a product, depending on the configuration, you [may need to provide](products.md#product-completeness) certain pieces of information, 
such as a name, SKU, description and images, attributes, assets, availability, prices, and translations.

You can create product by using manual or bulk method.
Bulk method can be used only at the developer level. See [Products](https://doc.ibexa.co/en/latest/pim/product_api/#products) for a technical guide on how to do this.

## Manually create product

You can create product in several ways:

1. Click **Create** in the upper-right corner of the [Products](products.md) screen. 
2. While viewing a **Product Catalog** in the [Content Tree](../getting_started/discover_ui.md#content-tree), click **Create content** at the top of the screen.
The new item appears in the tree.
3. Click **Create content** in the upper-right corner of the [My dashboard](../getting_started/discover_ui.md) screen. In this case you have to choose Content Type and select where the content will be located.

1\. If you are adding a new product use one of the methods mentioned above and continue with the procedure.
If you want to edit existing product, click the **Edit** button next to a name of the product item that you want to modify and skip to step 3.

![Adding a Product](img/add_product.png "Adding a Product")

![Editing a product](img/edit_product.png "Editing a product")

2\. From their lists, select the language and the product type, and then click the **Add** button.

3\. Fill in or edit content fields of the product, for example, name, specification and description.
The [Fields](../content_management/content_model.md#fields-and-field-types) that you have to populate depend on how the Product Type is defined. 
Fields marked with an asterisk (*) are required.

4\. If you are adding new product, click **Create** button.
If you are editing existing one, click **Update** button.

![Creating a product](img/create_product.png "Creating a product")

You can also [add image assets](work_with_product_assets.md) to products.

## Work with products

For each product you can:

- [Add specific attributes](create_product_types.md#work-with-product-attributes)
- [Set availability, stock and price](manage_prices_and_stock.md#work-with-availability-stock-and-prices)
- [Assign it to specific category](work_with_product_categories.md)
- [Create variants](work_with_product_variants.md)

For more information, see [Products](https://doc.ibexa.co/en/latest/pim/products/).
