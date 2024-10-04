---
description: Define new shipping methods or modify existing ones.
edition: commerce
---

# Work with shipping methods

If your [user role](work_with_permissions.md) includes the `Shipping method/Create` permission, you can create shipping methods.
With the `Shipping method/Edit` permission, you can modify existing ones.

Shipping methods describe how goods can be shipped to a store customer, with different rates for different geographic locations.
Example shipping methods are overnight delivery, self-pickup, or DHL.

!!! note "Shipping method limitations"

    By default, you can only create shipping methods of 'Flat rate' and 'Free shipping' type.
    
    Shipping methods created in legacy Commerce cannot be migrated when you upgrade. You have to define them from scratch.

"Flat rate" shipping means delivering goods at a fixed, predefined cost, regardless of the number, and type of items in the cart.

## Create new shipping method 

1\. In the left panel, go to **Commerce** -> **Shipping methods**, and click **Create**.

2\. Select the language for the new shipping method, its type, and region that it applies to.

3\. In the next screen provide information about the new shipping method.

![Creating a new shipping method](create_new_shipping_method.png)

Details about shipping cost differ between shipping methods:

- Flat rate requires setting a specific fixed cost for shipping, expressed as net value in a given currency.
This value is then displayed during checkout and added to the total order amount when the store customer selects a specific shipping method.
- Free shipping requires setting the minimum order value (in a given currency) above which the shipping is free.

![Configuring free shipping](free_shipping.png)

4\. Toggle the **Availability** switch on, so that store customers can select this shipping method during checkout.

5\. Click **Create** to save your changes.

## Edit existing shipping method

1\. In the left panel, go to **Commerce** -> **Shipping methods**.

![Shipping methods list](shipping_methods_list.png)

2\. Find the shipping method that you intend to edit or delete by using the search field and filters.

3\. Click the **Edit** button next to the method in the list.

4\. Edit the necessary details.

5\. Click **Update** to save your changes.

## Delete existing shipping method

1\. In the left panel, go to **Commerce** -> **Shipping methods**.

2\. Find the shipping method that you want to delete by using the search field and filters.

3\. Select a box next to its name and click **Delete**.

!!! note "Shipping methods for existing orders"

    You cannot delete a shipping method if it's active or if it's used by open orders.
    You must first deactivate the method that you want to delete by toggling the **Availability** switch off.

## Filter shipping methods

1. In the left panel, go to **Commerce** -> **Shipping methods**.
2. Narrow down the list of displayed shipping methods in one of the following ways:

    - search for shipping method by typing part of its name or identifier in the search box
    - filter shipping methods by selecting one or more filters

    Available filters are:

    - Method type - method of the shipping
    - Availability - shipping method availability: Active, Inactive
    - Region - region that the shipping method applies to

3. Click **Apply** to confirm.