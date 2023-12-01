---
description: Build new product types or modify existing ones.
---

# Create product types

If your [user Role](../permission_management/work_with_permissions.md) has the `ProductType/Edit` permission, you can modify product types and add individual attributes or attribute groups.

1\. In the left panel, go to **Product catalog** -> **Product Types** and click **Create**.

2\. Fill in basic product information: name, identifier and description.

![Defining product type settings](create_product_type.png "Defining product type settings")

Each product has a product code that must be unique. It identifies the product in the system.
Product code can have up to 64 characters. It can contain only letters, numbers, underscores, and dashes.

3\. Add Fields that describe the product by dragging them from the **Field types** 
area to the **Field definitions** section, and then [configure them](../content_management/configure_ct_field_settings.md).

!!! note "VAT rates"

    When you create a new product type, you must define VAT rates that apply to all products of this type.
    In the **Field definitions** section, expand **Product Specification** and select categories for all applicable regions.

4\. Add attributes by dragging them or their groups from the **Library** area to the **Attributes** section.

When you define attributes for the product type, you can add whole attribute groups or individual attributes. 

![Adding attributes to a product type](img/adding_attributes.png "Adding attributes to a product type")

You can also remove whole groups or single attributes from groups that you don't want to use for the given product type.
Do this by clicking the **X** icon next to the group or attribute.

<a name="vat"></a>
For every attribute, you can select **Used for product variants**.
Attributes that have this option are used to [automatically generate product variants](work_with_product_variants.md#generate-variants).
