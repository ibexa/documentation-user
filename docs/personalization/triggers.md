---
description: Triggers enable sending recommendations as emails to customers.
---

# Email triggers

With email triggers, you can increase the engagement of your visitors and customers by delivering recommendations straight to their mailboxes.
As a store manager, you can expect that more engaged customers translate to bigger income, improved fulfillment of customer needs, while saving time and effort.

## Email trigger types

There are several email triggers available in [[= product_name =]], including the following two:

- Abandoned basket trigger: Personalization engine monitors the user's cart and pushes a message when cart status remains unchanged for a set time. 
The message contains items that have been abandoned in the cart. 
To remove items that the user is no longer interested in from recommendations, the trigger logic monitors the `deletefrombasket` and `buy` events and filters out items that these events relate to.  

- Reactivation aka. "We miss you" trigger: Personalization engine monitors the user's overall activity and pushes a message when they have not returned to the site for a set time. 
Recommendations are generated based on the user's purchasing and browsing history.

## Trigger calculation frequency

Personalization engine checks user context data against trigger conditions every night.
Email triggers are automatically initiated when a specific user's action, inaction or pattern of actions meet certain conditions that are defined in the service.

## Configuring email triggers

Email trigger calculations are done on a server that is run and maintained by Ibexa. 
Also, [[= product_name =]] does not provide a mechanism to send emails to the recipient, but delivers a response with recommendations to an endpoint provided by your organization, for example, an Ibexa Connect [webhook](https://doc.ibexa.co/projects/connect/en/latest/tools/webhooks/). 
Each response includes a list of recommendations, and a user email address that can be used to route a message to the recipient.

To enable email triggers for your organization, contact your administrator or development team about [preparing a webhook address and processing the response delivered to the webhook]([[= developer_doc =]]/personalization/integrate_recommendation_service/#send-emails-with-recommendations).

You can define one or more email triggers of certain type, to support different use cases.
For each email trigger type, you need to decide on several crucial parameters, for example:

- one or more [types of content](content_types.md)
- [attributes](recommendation_models.md/#nominal-attributes) to be included in the response
- time that must pass before email start being sent
- number of repetitions

For the "Reactivation" model, you can decide what models and events are used to calculate the results.
The following [recommendation models](recommendation_models.md) are used by default, in such order: "Also purchased", "Also clicked", and "Top purchased".
If you do not decide otherwise, model calculations are based on BUY and TRANSFER [events](event_types.md).