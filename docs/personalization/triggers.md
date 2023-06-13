---
description: Triggers enable sending recommendations as emails to customers.
---

# E-mail triggers

With e-mail triggers, you can increase the engagement of your visitors and customers by delivering recommendations straight to their mailboxes.
As a store manager, you can expect that more engaged customers translate to bigger income, improved fulfillment of customer needs, while saving time and effort.

## E-mail trigger types

There are several e-mail triggers available in [[= product_name =]], including the following two:

- Abandoned basket trigger: Personalization engine monitors the user's cart and pushes a message when cart status remains unchanged for a set time. The message contains items that have been abandoned in the cart.

- Reactivation aka. "We miss you" trigger: Personalization engine monitors the user's overall activity and pushes a message when they have not returned to the site for a set time. Recommendations come from the [also purchased and also clicked](recommendation_models.md#also-clicked--purchased) models, while the [top purchased](recommendation_models.md#popularity-models) model is used as fallback.

## Trigger calculation frequency

Personalization engine checks user context data against trigger conditions every night.
E-mail triggers are automatically initiated when a specific user's action, inaction or pattern of actions meet certain conditions that are defined in the service.

## Configuring e-mail triggers

E-mail trigger calculations are done on a server that is run and maintained by Ibexa. 
Also, [[= product_name =]] does not provide a mechanism to send e-mails to the recipient, but delivers a response with recommendations to an Ibexa Connect [webhook](https://doc.ibexa.co/projects/connect/en/latest/tools/webhooks/). Each response includes a list of recommendations, and a user email address that can be used to route a message.

To enable e-mail triggers for your organization, contact your administrator or development team about [preparing a webhook address and processing the response delivered to the webhook]([[= developer_doc =]]/personalization/recommendation_integration/#send-emails).

For each e-mail trigger type, you set up several crucial parameters, for example:

- [types of content](content_types.md)
- [attributes](recommendation_models.md/#nominal-attributes) to be included in the response
- time that must pass before e-mails start being sent 
- number of e-mails

