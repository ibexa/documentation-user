---
description: Review payment information, change payment status.
edition: commerce
---

# Work with payments

In [[= product_name =]], you can view a list of payments and modify their statuses on the **Payments** screen.
By default, depending on your permissions, you can access payments for your own orders, or all the payments that exist in the system.

## Filter payments in payment list

1. In the left panel, go to **Commerce** -> **Payments**.
2. Narrow down the list of displayed payments in one of the following ways:
    - search for payments by typing part of order ID or identifier in the search box
    - filter payments by selecting one or more filters

Available filters are:

- Payment method - method used for the payment
- Status - payment status, by default: Pending, Failed, Paid, Cancelled

!!! note "Payment statuses"

    Payment statuses visible in the **Status** filter field are defined in the [Payment workflow]([[= developer_doc =]]/commerce/payment/configure_payment/#default-payment-workflow-configuration).

- Created - a range of dates between which the payment was created
- Updated - a range of dates between which payment status has last changed

![Payment list](payment_list.png)

## View payment details

To view the details of a payment, click its line in the payment list.

On the payment details screen, you can view a summary of information about the payment. Payment details include information about the payment method used, total value and current status of the payment.

![Payment detail view](payment_detail_view.png)

## Change payment details

If your [user role](work_with_permissions.md) includes the `Payment/Edit` permission, you can change the status of an existing payment:
confirm it if the payment has "Pending" status.
