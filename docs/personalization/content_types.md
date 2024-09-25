---
description: Types of content in the Personalization service allow building different recommendations for different parts of our content model.
---

# Types of content

With the Personalization service, you can build different recommendation domains. 
You do this by splitting all the products into different types of content. 
There are several possible use cases for types of content, for example:

- A publisher can track articles, pictures and videos as three different types.
- A store can split all the products into food and non-food product groups.
- An owner of several web stores can use a single account for all of them.

Based on the types of content concept, it's possible to make so-called cross 
content type recommendations (like "Users who watched this film also read this 
book" or "Users who bought these wallets also bought these belts").

Apart from the logical separation of the content domains, types of content provide another 
important advantage. 
You can use them to adjust recommendation weight if different types of products/content items 
are not equally popular but must be recommended equally often. 
For example, on a content publisher's page, users watch videos less often than they read articles. 
If the most popular products were requested without splitting the types of content, 
there would most likely be no videos in the recommendation result. 
If articles and videos are split into different types of content, you can explicitly request 
popular videos and/or popular articles.

Here is a comparison of different approaches that you can take when defining types of content:

|Use case|Types of content solution (domain context)|Attribute based sub-models (group context)|Different Personalization service accounts|
|---|---|---|---|
|Cross-group recommendation requests are possible|yes|yes|no|
|Products must belong to one group|mandatory|optional|mandatory|
|Products can belong to multiple groups|no|yes|no|
|Single recommendation request can contain products from different groups|no|yes|no|
|Product can change the group it belongs to|no|yes|no|
|Different types of content share the scenario and model configuration|yes|yes|no|

### Types of content and scenarios

If multiple types of content are enabled in your configuration, for every scenario that 
should recommend a specific type, you must enable this output type.
For more information about scenario configuration, see [Configure scenarios](configure_scenarios.md).
