---
description: Order management module handles orders and allows managing orders in the system.
edition: commerce
---

# Order management

The Order management module allows users to review order details, track order completion status, and cancel orders that are created when store customers purchase products.

Depending on the permissions assigned to your [user role](permissions_and_users.md), you might be able to track and manage orders placed by all the store customers, or only your own ones.

With the back office **Orders** screen, you can search for orders and filter search results.

![Orders list](order_list.png "Orders list")

The Order management package interacts with other packages of the system, so that:

- when store customers pass the checkout stage, stock is decreased and payment and shipment workflows are initiated
- when store customers cancel their orders, the decreased stock is restored and payment and shipment are cancelled

[[= cards([
    "commerce/order_management/work_with_orders"
], columns=3) =]]
