---
description: Triggers enable sending recommendations as push messages to customers.
---

# Triggers

Triggers are push messages delivered to end users, for example, through email.
With triggers, you can increase the engagement of your visitors and customers by delivering recommendations straight to their mailboxes.
As a store manager, you can expect bigger income, and improved fulfillment of customer needs.
All this while saving time and effort.

## Trigger types

[[= product_name =]] lets you use several triggers, including the following ones:

- Abandoned basket trigger: Personalization engine monitors the user's cart and pushes a message when cart status remains unchanged for a set time.
The message contains items that have been abandoned in the cart.
The Personalization service monitors [events](event_types.md) to avoid recommending items that the end user has bought or removed from basket.

- Reactivation aka. "We miss you" trigger: Personalization engine monitors the user's overall activity and pushes a message when they haven't returned to the site for a set time.
Recommendations are generated based on the user's purchasing and browsing history.

- Price drop trigger: Personalization engine monitors the user's wishlist and pushes a message when a price of the product that has been put there decreases.

- Post visit trigger: Personalization engine monitors the user's browsing activity and pushes a message with products that are similar to the ones the customer has looked at.

## Trigger calculation frequency

Personalization engine checks user context data against trigger conditions every night.
Trigger messages are automatically initiated when a specific user's action, inaction or pattern of actions meet certain conditions that are defined in the service.

## Configuring triggers

Trigger message calculations are done on a server that is run and maintained by [[= product_name_base =]].
The server delivers a response with recommendations to an endpoint provided by your organization, for example, an [[= product_name_connect =]] [webhook](https://doc.ibexa.co/projects/connect/en/latest/tools/webhooks/).
You may then deliver the message to the end users using a method of your choice, for example, email.
Apart from a list of recommendations, the response can include an email address for routing a message to the recipient.

To enable triggers for your organization, contact your administrator or development team about [preparing a webhook address and processing the response delivered to the webhook]([[= developer_doc =]]/personalization/integrate_recommendation_service/#send-messages-with-recommendations), and [[= product_name_base =]] about the configuration specifics.

You can define one or more triggers of certain type, to support different use cases.
For each trigger type, you need to decide on several crucial parameters, for example:

- one or more [types of content](content_types.md)
- [attributes](recommendation_models.md#nominal-attributes) to be included in the response
- time that must pass before messages start being sent
- number of repetitions
- message frequency
- number of recommended items
- what events set off the trigger
- what [recommendation models](recommendation_models.md), together with their context, are used to calculate the response.
"Also purchased", "Also clicked", and "Top purchased" are used by default.

If you don't decide otherwise, trigger recipients are selected based on an analysis of BUY and TRANSFER events, except for the "Price drop" trigger, where the WISHLIST event is analyzed.
