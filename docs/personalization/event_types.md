---
description: Recommendations rely on tracking different events that describe users' behavior on the website.
---

# Events

Before the Personalization service can generate implicit recommendations, it must collect events and calculate the results based on user behavior.
The most important events collected by the service are CLICK and BUY events.
They're enough for providing basic recommendations.
Additional events exist for creating more complex [scenarios](scenarios.md) and providing [statistics](review_perso_performance.md#statistical-information) about the acceptance of recommendations, such as conversion rate or revenue. 

![Events in a purchase process](img/events_overview.png "Events in a purchase process")

The table below lists all possible events that could be used in the system.

|Event|Description|
|---|---|
|BASKET|Sent when the user adds the specified product to the shopping cart. Enables creating recommendations for products that customers are interested in but ultimately did not purchase.|
|BLACKLIST|Allows a user to suppress currently displayed recommendations. When the Personalization service receives this event, the product or item is no longer recommended to the specified user. By default, recommendations are suppressed for one year.|
|BUY|Sent if something was purchased.|
|CLICK|Sent to the Personalization service when a user opens a page on the website.|
|CLICKRECOMMENDED / FOLLOW|Sent when a user clicks the recommended product. Used in acceptance statistics.|
|CLICKTRIGGERED|Sent when a user clicks the link delivered in a trigger message to see the recommended item. Used in statistics.|
|CONSUME|Similar to the BUY event but without a payment. Designed for content publisher websites. Sent when an article or a web page is consumed (read or watched).|
|DELETEFROMBASKET|Sent when the end user removes items from their shopping cart. Helps eliminate recommendations for products that the customer is no longer planning to buy.|
|DELETEFROMWISHLIST|Sent when the end user removes items from their wishlist. Used to eliminate recommendations for products that the customer has either lost interest in or already purchased elsewhere.|
|OWNS|Same as BUY, but doesn't influence the statistics. Can be sent when a user already owns the product that was purchased somewhere else, to avoid recommending it again.|
|RATE|Additional [models](recommendation_models.md) can be created with this type of events. Allows building recommendations not only for implicit tracking events like CLICK or BUY, but also for events with explicit value like "rated" or "liked". These events need additional integration into the web page to allow the user to give an appropriate feedback. The event is triggered as a result of this user feedback.|
|RENDERED|Sent when a recommendation is shown on the web page. This information is used by [filters](filters.md) to suppress repeated recommendations of the same item.|
|TRANSFER / LOGIN|A special type of event to deal with user login after the user already surfed on the web page anonymously. Always sent when the identifier of the user changes. As a result, the anonymous history of the user is transferred to the new identifier. This happens automatically in the Personalization service.|
|TRIGGEROPENED|Sent when a user opens a [trigger message](triggers.md), for example, an email. Used in statistics.|
|WISHLIST|Sent when the user adds a product to their wishlist. Enables creating recommendations for products that the customer considers purchasing in the future.|

All events require the current user ID and the ID of one or more context items.
Some events require additional information.
Sophisticated algorithms and result filtering require event types with additional parameters.
The table below provides a brief overview of additional parameter information.

|Event|Additional information|
|---|---|
|CLICK|Category path of the product a customer clicked on can be attached to the event. It's an alternative way to provide this information for a product without having a catalogue/export. Ignored if an export is available to be fed into the Personalization service.|
|BUY|The price that a user paid for the product, an important parameter for the statistics. For revenue statistics, it must be sent together with a quantity of the products bought.|
|TRIGGEROPENED /CLICKTRIGGERED|An identifier of the trigger that the trigger and recommendations originate from.|
|FOLLOW / CLICKRECOMMENDED|The scenario which provided the recommendations must be sent in this event.|
|RATE|The rating (for example 1 to 5 stars) can be sent as an additional parameter.|
