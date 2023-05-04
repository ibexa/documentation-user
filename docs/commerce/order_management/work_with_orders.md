---
description: Review order information, change order status.
edition: commerce
---

# Work with orders

In Ibexa DXP, you can view a list of orders and modify their statuses on the **Orders** screen.
By default, depending on your permissions, you can access your own orders or all the orders that exist in the system.

## Filtering orders

1. In the left panel, go to **Commerce** -> **Orders**.
2. Narrow down the list of displayed orders in one of the following ways:
    - search for orders by typing part of customer or company name, or order identifier in the search box
    - filter orders by selecting one or more filters

Available filters are:

- Status - Payment status, by default: Pending, Processing, Completed, Cancelled

!!! note "Order statuses"

    Order statuses visible in the **Status** filter field are defined in the [Order workflow]([[= developer_doc =]]/commerce/order_management/configure_order_management/#order-processing-workflow).

- Created - date when the order was created
- Client type - either B2B or B2C client
- Order source - the shop from which the order comes
- Total value - total value of the order, in a specific currency
- Currency - the currency in which the order was made

![Order list](order_list.png)

## Viewing order details

To view the details of an order, click its line in the order list.

There, you can view more information about the order, such as the details of the customer, payment and shipping.

![Order detail view](order_detail_view.png)

In the **Items** tab you can preview the products included in the order.

![Viewing products included in the order](order_detail_items.png)

## Changing order status

If your [user role](work_with_permissions.md) has the `Order/Update` permission, you can change the status of an existing order:
confirm it if it is in status "Pending", or complete it when it is in status "Processing".
With the `Order/Cancel` permission, you can cancel an existing order.

!!! note "Canceling orders"

    When an order is created, stocks are reduced for the products on that order. When you cancel an order, the stocks are reverted back to their original values.
