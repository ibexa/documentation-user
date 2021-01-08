# Content Types

With the recommendation engine you can build different recommendation domains. 
You do this by splitting all the products into different content types. 
There are several possible use cases for content types, for example:

- a publisher can track articles, pictures and videos as three different types
- a store can split all the products into food and non-food product groups
- an owner of several web shops can use a single account for all of them

Based on the content types concept, it is possible to make so-called cross domain recommendations (like 
"Users who watched this film also read this book" or 
"Users who read this article also liked these photos").

Apart from the logical separation of the content domains, content types provide another important advantage. 
They play a role if different types of products are not equally popular but must be recommended equally often. 
For example, on a publisher's page, users watch videos less often than they read articles. 
If the most popular products are requested without content type splitting, 
there will be most likely no videos in the result. 
If articles and videos are split into different content types, it is possible to explicitly request 
popular videos and/or popular articles.

Below is a comparison for different ways of splitting content in the recommendation engine.

|Use case|Content types solution (domain context)|Attribute based sub-models (group context)|Different recommendation engine accounts|
|---|---|---|---|
|Cross-group recommendation requests are possible|yes|yes|no|
|Products must belong to one group|mandatory|optional|mandatory|
|Products can belong to multiple groups|no|yes|no|
|Single recommendation request can contain products from different groups|no|yes|no|
|Product can change the group it belongs to|no|yes|no|
|Different content types share the scenario and model configuration|yes|yes|no|
|Required Recommender Edition|single advanced|-|multiple basic|

If multiple content types are enabled, for every scenario that should recommend a specific type, you must enable this output type.
For more information about scenario configuration, see [Scenarios](scenarios.md). 

For more information about fetching recommendations, see [Recommendation API](https://doc.ibexa.co/en/master/guide/personalization/developer_guide/recommendation_api) in developer documentation.
