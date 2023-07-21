---
description: Build new product Types or modify existing ones.
---

# Create Product Types

If your [user Role](../permission_management/work_with_permissions.md) has the `ProductType/Edit` permission, you can modify Product Types and add individual attributes or attribute groups.

1\. In the left panel, go to **Product catalog** -> **Product Types** and click **Create**.

2\. From the drop-down list choose "Physical" or "Virtual" type and click **Add**.

![Selecting a type of Product Type](virtual_product_type.png "Selecting a type of Product Type")

3\. Fill in basic product information: name, identifier and description.

![Defining Product Type settings](create_product_type.png "Defining Product Type settings")

Each product has a product code that must be unique. It identifies the product in the system.
Product code can have up to 64 characters. It can contain only letters, numbers, underscores, and dashes.

4\. Add Fields that describe the product by dragging them from the **Field types** 
area to the **Field definitions** section, and then [configure them](../content_management/configure_ct_field_settings.md).

!!! note "VAT rates"

    When you create a new product type, you must define VAT rates that apply to all products of this type.
    In the **Field definitions** section, expand **Product Specification** and select categories for all applicable regions.

5\. Add attributes by dragging them from the **Library** area to to the **Attributes** section.

When you define attributes for the Product Type, you can add or remove either whole attribute groups or individual attributes. 

![Adding attributes to a Product Type](img/adding_attributes.png)

You can also remove whole groups, or single attributes from groups that you don't want to use for the given Product Type.
Do this by clicking the **X** icon next to the group or attribute.

For every attribute, you can select **Used for product variants**.
Attributes that have this option are used to [automatically generate product variants](work_with_product_variants.md#generate-variants).
