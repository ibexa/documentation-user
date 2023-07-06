---
description: Review shipment information.
edition: commerce
---

# Work with shipments

In Ibexa DXP, on the **Shipments** screen, you can view a list of shipments and modify their statuses.
You can access shipments for your own orders or all the shipments that exist in the system, depending on your permissions.

![Shipment list](shipment_list.png)

## View shipment status

Each shipment has a status due to the stage it is currently at.

Available statuses are:

- Pending
- Ready to ship
- Shipped
- Delivered
- Cancelled

![Shipment status](shipment_status.png)

To view shipment status:

1\. In the left panel, go to **Commerce** -> **Shipments**.

2\. Narrow down the list of displayed shipments in one of the following ways:

- search for shipments by typing part of order ID or identifier in the search box
- filter shipments by selecting one or more filters

Available filters are:

- Shipping method - method used for the shipment
- Status - shipment status
- Created - a range of dates between which the shipment was created
- Updated - a range of dates between which shipment status has last changed

![Shipment filters](shipment_filters.png)

## View shipment details

To view the details of a shipment, click its line in the shipment list.

On the shipment details screen, you can view a summary of information about the shipment. Shipment details include basic information about the shipment and the method used, total value, customer details, shipping address and order ID.

![Shipment detail view](shipment_detail_view.png)

## Change shipment status

If your [user Role](work_with_permissions.md) has the `Payment/Edit` permission, you can change the status of an existing shipment.

- "Pending" -> "Ready to ship" - click **Prepare** button and confirm by clicking **Change** button. 
- "Ready to ship" -> "Shipped" - click **Send** button and confirm by clicking **Change** button.
- "Shipped" -> "Delivered" - click **Deliver** button and confirm by clicking **Change** button.

