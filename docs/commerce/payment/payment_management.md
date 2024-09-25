---
description: Payment management module handles payment methods and payments, and allows interacting with them in the system.
edition: commerce
---

# Payment management

The Payment management module allows users to track the status of payments for orders placed by store customers.

On the back office **Payments** screen, you can search for payments, filter the search results, and review payment details.
Depending on configuration and permissions, you may also be allowed to cancel payments.

If the permissions assigned to your [user role](permissions_and_users.md) allow, you may also have access to the **Payment methods** screen, where you define, enable, and disable offline payment methods.

![Payments list](payment_list.png "Payments list")

The Payment management module interacts with other packages of the system, so that payment processing is cancelled automatically when you cancel your order.

[[= cards([
    "commerce/payment/work_with_payments",
    "commerce/payment/work_with_payment_methods"
], columns=3) =]]
