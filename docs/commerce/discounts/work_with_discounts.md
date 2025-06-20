---
description: Create and edit discounts, toggle discount status.
editions:
    - lts-update
    - commerce
month_change: true
---

# Work with discounts

In [[= product_name =]], on the **Discounts** screen, you can either view a list of discounts, or update existing discounts and create new ones depending on permissions assigned to your [user role](work_with_permissions.md).

## View discount information in discounts list

1. In the left panel, go to **Commerce** -> **Discounts**.

    Here, you can see a list of discounts, together with information about their validity period, status, type, and their authors.

2. Narrow down the list of displayed discounts in one of the following ways:

    - search for a discount by typing in a part of its name or identifier in the search field
    - filter discounts by selecting one or more of the following filters:
        - Applicability: catalog or cart products
        - Availability: active, inactive or disabled
        - Creation date range: start and end of date range within which the discount was created
        - Validity dates range: start and end of date range within which the discount is in force

    ![Discount filters](discount_filters.png)

3. Click **Apply** to confirm your choices.

4. To clear all the filters, click **Clear filters**.

### Instantly disable active discount

When working with discounts it may happen that a discount has been created or enabled in error and you notice that it has negative impact on your business.

To disable the offending discount, find it in the discount list and, in its line, click the **Disable** icon.

![Discount filters](discount_disable_icon.png)

### View discount details

To view the details of a discount, click its line in the discount list.
On the discount details screen, you can see an overview of the discount's details.

Discount details include basic information about the discount: 

- validity period and value of the discount
- region and currency that the discount applies to
- products subject to the the discount
- whether the discount applies to all customers or a selected customer group,
- whether any conditions apply

![Discount detail view](discount_detail_view.png)

### Add translations

If your store supports multiple languages and you want different discount names and/or descriptions to appear to customers from different markets, while [viewing discount details](#view-discount-details), you can go to the **Translations** tab and [add translations](../../content_management/translate_content.md#add-translations).

## Create new discount

When you create discounts, you must first decide whether they apply to all [products](../../pim/products.md) from the catalog, or the products that the customer has put into their cart.
You are then taken through a series of steps, where you define the discount, for example, decide if it applies to selected [customer groups]([[= developer_doc =]]/users/customer_groups/) and specific products.
Cart discount applicability can be further limited by setting a number of conditions, such as:

- a number of products in the cart
- total purchase value
- a discount code

!!! note "Navigating through the steps"

    When you define discount details, you can go back to change your choices.
    To do it, click a step header at the top of the screen.

    ![Discount creator steps](discount_creator_headers.png)

1. In the left panel, go to **Commerce** -> **Discounts**, and click **Create**.

2. Select whether the discount applies to catalog or cart products and the product's type.

    Choose **Fixed amount** to deduct a specific amount of money from the base price of the product, or **Percentage** to calculate the deducted amount based on a specific percent value.

    ![New discount](new_discount.png)

3. Provide general information about the new discount:

    1. In the **Global properties** area, provide an internal name of the discount and set the validity period.
    Toggle the **Permanent discount** on to make the discount valid until you manually disable it.
    1. Then, select discount [priority]([[= developer_doc =]]/discounts/discounts_guide/#discounts-priority) to help the system choose the right discount to apply when calculating the final price.
    1. If your store supports multiple markets, you can select a region that the discount applies to, and decide whether the discount applies to all or selected currencies.
    1. In the **Promotion label** field, provide a name of the campaign, as it should be shown to customers, for example "Summer Sale" or "DACH Conference".
    1. Click **Next** to go to the next screen.
    
    ![Creating a new discount](create_new_discount.png)

4. Select customers that the new discount is targeted at.
You can choose everyone, or select one or more customer groups.

    ![Customer selection](discounts_select_customers.png)

5. Select products that the discount applies to. You can choose between:
    
    - all products from the catalog, for example, to clear stock before the end of year
    - products from a specific category, for example, promotional gadgets for company partners
    - specific products or even product variants, to promote a specific brand

    In the latter case, you select products by using a Product picker, where you can use search and filters to pinpoint the exact product or product variant that you want the discount to apply to.

    ![Product picker](product_picker.png)

6. If you are creating a cart discount, in the next you screen, you can set the conditions that limit the discount's availability to customers who have:

    - added to cart no less than a specific number of certain items
    - added products to a cart for no less than a specified total value
    - entered a specified discount code

    If you set the discount code, you can also set the number of times that the code can be used.

    ![Cart discount conditions](cart_discount_conditions.png)

7. If you are creating a percentage- based discount, in **Customer gets discount value**, enter the percent value that the system uses to calculate the amount deducted from the base price of the product.
Otherwise, enter the monetary value to be deducted from the base price. 

8. Click **Save and close** to save the newly created discount.

## Edit existing discount

You may find that an existing discount needs to be modified, for example, to change its validity period or target group.

1. In the left panel, go to **Commerce** -> **Discounts**.

    ![Discounts list](discount_list.png)

2. Use the search field and filters to find the discount that you want to edit.

3. Click the **Edit** button next to the discount in the list.

4. Edit the necessary details as described in [Create new discount](#create-new-discount).

5. **Save and close** to save your changes.

## Delete existing discount

When there are too many discounts in the system, you may want to delete historic, unused ones.
You can only delete disabled discounts.

1. In the left panel, go to **Commerce** -> **Discounts**.

2. Use the search field and filters to find the discount that you want to delete.

3. If the discount that you want to delete is not disabled, use the *Disable** to [disable it](#instantly-disable-active-discount).

4. Select a box next to the discounts name and click **Delete**.
