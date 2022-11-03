---
description: Build new product Types or modify existing ones.
---

# Create Product Types

If your [user role](../permission_management/manage_permissions.md) has the `ProductType/Edit` permission, you can modify Product Types and add individual attributes or attribute groups.

1\. Go to **Product catalog** -> **Product Types** and click **Create**.

![Adding a Product Type](img/create_product_type.png)

2\. Fill in basic product information: name, identifier and description.

Each product has a product code that must be unique. It identifies the product in the system.
Product code can have up to 64 characters. It can contain only letters, numbers, underscores, and dashes.

3\. If needed, [add Fields that describe the product](../content_management/work_with_content_types.md).

4\. Add attributes by dragging them from the toolbox on the right.

## Work with product attributes

When adding attributes to Product Types, you can add both individual attributes, 
and whole groups. 
You can also remove while groups, or single attributes from groups that you do not 
want to use for the given Product Type. Do this by clicking the trash icon next 
to the group or attribute.

![Creating an attribute in a group](img/create_attribute.png)

You can also remove whole groups, or single attributes from groups that you do not 
want to use for the given Product Type.
Do this by clicking the trash icon next to the group or attribute.

![Adding attributes to a Product Type](img/adding_attributes.png)

For every attribute, you can select **Used for product variants**.
Attributes that have this option are used to [automatically generate product variants](work_with_product_variants.md#generate-variants).
