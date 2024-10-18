---
description: Use the Personalization service to get recommendation for users based on their behavior and on the scenarios you configure.
---

# Personalization

A cloud-based Personalization service leverages artificial intelligence and machine learning technologies to deliver optimized customer experience.
With Personalization, you capture [events](event_types.md) that represent preferences and interests of your users, apply [models](recommendation_models.md) to quantify these findings, and combine them with [scenarios](scenarios.md) to generate recommendations, which you can then [present](integrate_scenario_results.md) in a form of personalized content to visitors of one or more websites hosted by the [[= product_name =]] instance.

Both event tracking and result publishing is done by users with administrator privileges, according to a procedure [described in Developer Documentation]([[= developer_doc =]]/personalization/integrate_recommendation_service/).

There are different areas where you can apply recommendations.
The most common ones are [eCommerce and content publishing](use_cases.md).

!!! note "eCommerce vs. content publishing"

    Documentation mentions eCommerce use cases more often, but provides a thorough understanding of the content publishing context as well.

    Both products and content items can be referred to as content and the BUY [event](event_types.md) can be understood as
    the CONSUME event.

Before you can use the Personalization service, you must [enable it](enable_personalization.md).
Then, for the service to generate relevant recommendations, you can [change the default configuration](configure_personalization.md).
Finally, you can [feed it with data](content_import.md), or wait until the service gathers enough information about the content and events.
On a website with more than 100 clicks per day, a day of collecting data should be sufficient for the first recommendations to be relevant.
Recommendations become better with time and the amount of data collected.

For more information about Personalization, see [Ibexa blog](https://www.ibexa.co/blog/ibexa-dxp-v3.3-new-feature-preview-personalization-simplified-and-dxp-integrated) or a [downloadable eBook](https://www.ibexa.co/events/ibexa-engage-2021/resources/downloads/the-basics-of-personalization).
