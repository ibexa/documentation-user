---
description: Products are containers that aggregate information about the items you offer, their specs, variants, availability, etc.
---

# Products

With **PIM**, [[= product_name =]] handles products offered in the website, 
including their specifications, attributes, assets, variants and pricing.

PIM's features are available from the left menu.

![PIM in the menu](img/catalog_menu.png "PIM in the menu")

To create a product you must first decide which product type it belongs to.

## Product types

Product types are templates that contain a combination of [Fields](../content_management/content_model.md#fields-and-field-types) and [attributes](#attributes) that constitute a product definition.
By default, each product type contains such Fields as name, specification, image or category, but you can change it as required.
You need different product types, because products of type "Laptops" contain different Fields and attributes than those of type "White appliances".

When you create a new product type, you can choose between two available product type flavors: Physical and Virtual:

- Physical - tangible products.
They can use measurement attributes. They require shipment in the online purchase process.
Examples: heaters, laptops, phones.
- Virtual - non-tangible items. They can be sold individually, or as part of a product bundle.
They don't require shipment in the online process. Examples: memberships, services, warranties. 

A Product Types also defines the attributes that all products of this type can have.

If your [user Role](../permission_management/work_with_permissions.md) has the `ProductType/Edit` 
permission, you can [modify Product Types and add individual attributes or attribute groups](create_product_types.md).

### Attributes

Attributes describe product characteristics.
Customers can use them to filter and search for products.
Attribute types define what kind of information you can store in an attribute.
Typical product attribute examples include dimensions, weight, color, or format.

For more information, see [Work with product attributes](work_with_product_attributes.md).

## Products

Products are instances of a particular product type.
A product is an object that's based on a product type template.
Products can have variants that you build around attributes.
They can be categorized and organized into catalogs.

Also, for each product and product variant, you can define its availability, stock and price.

For more information about creating products, see [Create product](create_edit_product.md#create-and-edit-products).

### Product assets

When you create or edit products, you can add assets in a form of images.
Assets [can be assigned](work_with_product_assets.md) to the base product, and to one or more of its variants.

### Product completeness

When you create or edit a product, under the product name, you can see visual indication
of what part of product information (tasks) you have completed, and what part is still missing.

![Quick view of product completeness](img/product_completeness_bar.png "Quick view of product completeness")

Here you can see full information about completed tasks in the product view's **Completeness** tab.

This tab lists all tasks required for product configuration, including:

- content (such as images and descriptions)
- attributes
- assets
- variants (if any of the attributes is enabled for variants)
- availability
- prices in different currencies
- translations

![Product completeness screen](img/product_completeness.png "Product completeness screen")

You can click the edit button next to an unfinished task in the Completeness table
to move directly to the screen where you can add the missing information.


## Product categories

With product categories you can organize products within PIM and create relationships between them. 
One of the reasons for applying product categories is assisting users in searching for products.

Each category can be assigned to multiple products, and each product can belong to multiple categories of different or similar character, for example:

- Business Laptops
- Windows OS Devices
- Stock clearance

You can enable the use of product categories, assign products to categories and vice versa, and [define your own categories](work_with_product_categories.md).

## Product variants

Product variants enable you to have multiple versions of one product, differing in some characteristics.

Typical examples are a t-shirt in different colors, or a laptop with different hard disk sizes.

You can [create variants based on product attributes](work_with_product_variants.md).

## Product prices

 You can [set a base price and custom prices](manage_prices.md) for the product and for its variants.
 Prices can differ depending on [customer group](../customer_management/manage_customers.md) and [currency](../pim/manage_currencies.md) and be applied according to the rules.

## Product availability and stock

You can [control a product's availability](manage_availability_and_stock.md), which translates into 
whether it's being offered for purchase, and the available stock.
You can either set the exact number of product pieces available in stock or indicate 
that availability is infinite, for example, for digital, downloadable products. 

## Product catalogs

You can [create special catalogs](work_with_catalogs.md), for example, to differentiate the offering 
that's presented to B2B and B2C users, retailers and distributors or different regions.
Catalogs contain a sub-set of products from the system.

![Catalog menu with a sample catalog](img/catalog.png "Catalog menu with a sample catalog")
