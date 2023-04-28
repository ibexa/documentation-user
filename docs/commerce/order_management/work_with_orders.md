---
description: Review order information, change order status.
edition: commerce
---

# Work with orders

In Ibexa DXP, you can view a list of orders and modify their statuses on the **Orders** screen.
By default, depending on your permissions, you can access your own orders or all the orders that exist in the system.

## Viewing order status

1\. In the left panel, go to **Commerce** -> **Orders**.

// use search to find orders and filters narrow down the search results list
...

!!! note "Filter availability"

    Depending on your role, some of the filters may be unavailable.

/// confirm

![Order list](img/order_list.png)

Note: Order statuses visible in the xxx filter field are defined in Order workflow (link to dev doc).

## Changing order details

If your [user role](../permission_management/work_with_permissions.md) has the `Order/Update` permission, you can modify an existing order. 
With the `Order/Cancel` permission, you can cancel an existing order.

![Order details view](img/order_list.png)

!!! note "Canceling orders"

    When an order is created, stocks are reduced for the products on that order. When you cancel an order, the stocks are reverted back to their original values.