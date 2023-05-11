---
description: Define new shipping methods or modify existing ones.
edition: commerce
---

# Create and edit shipping methods

If your [user role](work_with_permissions.md) includes the `Shipping method/Create` permission, you can create shipping methods. 
With the `Shipping method/Edit` permission, you can modify existing ones.

!!! note "Shipping method limitations"

    By default, you can only create shipping methods of 'Flat rate' and 'Free shipping' type. 
    
    Shipping methods created in legacy Commerce cannot be migrated when you upgrade. You have to define them from scratch.

## Create a new shipping method 

1\. In the left panel, go to **Commerce** -> **Shipping methods**, and click **Create**.

2\. Select the language for the new shipping method, its type, and region it will apply to.

3\. In the next screen provide information about the new shipping method.

![Creating a nw shipping method](create_new_shipping_method.png)

Details about shipping cost differ between shipping methods:

- Flat rate requires setting a specific fixed cost for shipping for a given currency.
- Free shipping required setting the minimum order value (in a given currency) above which the shipping is free.

![Configuring free shipping](free_shipping.png)

4\. Click **Create** to save your changes.

## Edit an existing shipping method

1\. In the left panel, go to **Commerce** -> **Shipping methods**.

![Shipping methods list](shipping_methods_list.png)

2\. Find the shipping method that you intend to edit by using the search field and filters.

3\. Click the **Edit** button next to the method in the list.

4\. Edit the necessary details.

5\. Click **Update** to save your changes.
