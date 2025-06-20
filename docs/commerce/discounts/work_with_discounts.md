---
description: Create and edit discounts, toggle discount status.
edition: commerce
---

# Work with discounts

In [[= product_name =]], you can view a list of discounts and modify their statuses on the **Discounts** screen.
By default, depending on your permissions, you can access your own discounts, or all the discounts that exist in the system.

## Filter discounts in discount list

1. In the left panel, go to **Commerce** -> **Discounts**.
2. Narrow down the list of displayed discounts in one of the following ways:
    - search for discounts by typing part of customer or company name, or discount identifier in the search box
    - filter discounts by selecting one or more filters

Available filters are:

- Statuses - multiselect list of discount statuses, by default: Pending, Processing, Completed, Cancelled

!!! note "Discount statuses"

    Discount statuses visible in the **Status** filter field are defined in the [Discount workflow]([[= developer_doc =]]/commerce/discount_management/configure_discount_management/#configure-discount-processing-workflow).

- Created - a range of dates between which the discount was created
- Client type - either B2B or B2C client
- Discount source - the store from which the discount comes
- Total value - a range of values that includes the total value of the discount, in a selected currency
- Currency - the currency in which the discount was made

![Discount list](discount_list.png)

## View discount details

To view the details of an discount, click its line in the discount list.

On the discount details screen, you can view more information about the discount, such as customer, payment, and shipment details.

![Discount detail view](discount_detail_view.png)

In the **Items** tab you can see a list of products included in the discount.

![Viewing products included in the discount](discount_detail_items.png)

The fields have the following meaning:

- **Subtotal (net)** - a sum of all product prices without taxes
- **Shipping cost** - a net cost of the selected shipping method
- **Taxes** - a total value of all taxes, including those that apply to the selected shipping method and the products
- **Total value (gross)** - a total value of the discount, including all discounts, taxes, and service charges

!!! note "Discounting virtual products"

    If the discount includes only virtual products then the Shipment and Shipping address sections aren't available.
    Virtual products don't require shipment when they're the only product in a purchase.

## Change discount status

If your [user role](work_with_permissions.md) includes the `Discount/Update` permission, you can change the status of an existing discount: confirm it if the discount has "Pending" status, or complete it when it's in "Processing" status.
With the `Discount/Cancel` permission, you can cancel an existing discount.

!!! note "Canceling discounts"

    When you create an discount, stocks are reduced for the products on that discount.
    When you cancel an discount, the stocks are reverted back to their original values.
