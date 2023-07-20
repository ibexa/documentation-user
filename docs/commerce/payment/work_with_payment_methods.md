---
description: Define new payment methods or modify existing ones.
edition: commerce
---

# work with payment methods

It will be super.

It is awesome.

it's a test.

## UJ is UTW

If your [user Role](work_with_permissions.md) includes the `Payment method/Create` permission, you can create payment methods. 
With the `Payment method/Edit` permission, you can modify existing ones.

Payment methods describe the way store customers pay for their orders during the checkout process.

!!! note "Payment method limitations"

    By default, you can only create payment methods of type "Offline".
    If your organization needs other payment method types, contact your administrator or development team about [creating a custom payment method type]([[= developer_doc =]]/commerce/payment/extend_payment/#define-custom-payment-method-type).
    
    Payment methods created in legacy Commerce cannot be migrated when you upgrade. You have to define them from scratch.

## Create a new payment method 

1\. In the left panel, go to **Commerce** -> **Payment methods**, and click **Create**.

2\. Select the language for the new payment method and its type.

3\. In the next screen provide information about the new payment method.

![Creating a new payment method](create_new_payment_method.png)

4\. Toggle the **Availability** switch on, so that store customers can select this shipping method during checkout.

5\. Click **Create** to save your changes.

## Edit existing payment method

1\. In the left panel, go to **Commerce** -> **Payment methods**.

![Payment methods list](payment_methods_list.png)

2\. Find the payment method that you want to edit by using the search field and filters.

3\. Click the **Edit** button next to the method in the list.

4\. Edit the necessary details.

5\. Click **Update** to save your changes.

## Delete existing payment method

1\. In the left panel, go to **Commerce** -> **Payment methods**.

2\. Find the payment method that you want to delete by using the search field and filters.

3\. Select a box next to its name and click **Delete**.

!!! note "Payment methods for existing orders"

    You cannot delete a payment method if it is active or if it is used by unpaid orders. 
    You must first deactivate the method that you want to delete by toggling the **Availability** switch off.