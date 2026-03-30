---
description: Recommendation blocks - Raptor integration.
edition: experience
---

# Recommendation block reference

One of the Raptor Integration elements is the introduction of recommendation blocks available in the [Page Builder]([[= developer_doc =]]/content_management/pages/page_builder_guide/).

Each Content, Product, or Commerce recommendation can be added to a landing page using blocks divided into categories:

## Recommendations: Content

The following blocks can be used to present content recommendations:

|Block|Description|
|-----|-----------|
|[Most popular content](#most-popular-content-block)|Highlights the most frequently viewed content.|
|[Other customers have also seen this content](#other-customers-have-also-seen-this-content-block)|Displays content viewed by other users with similar behavior.|
|[Personalized content recommendations](#personalized-content-recommendations-block)|Provides personalized content recommendations based on user behavior and preferences.|

### Most popular content block

Highlights the content most frequently viewed by users.
It helps to find popular and relevant content items.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page** - Enter a name fot the block to be displayed on page.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

### Other customers have also seen this content block

Highlights content viewed by other users with similar behavior.
Helps identify related and relevant content.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Select content for recommendations** - Select content to be used for recommendations.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

### Personalized content recommendations block

Presents content tailored to each user based on their behavior and preferences.
Increases relevance and engagement through personalized suggestions.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

## Recommendations: Product

The following blocks can be used to display product suggestions based on visitors’ browsing history:

|Block|Description|
|-----|-----------|
|[Most popular products](#most-popular-products-block)|Presents trending and highly popular products.|
|[Most popular products in category](#most-popular-products-in-category-block)|Presents trending and highly popular products.|
|[Other customers have also seen](#other-customers-have-also-seen-block)|Shows content or products also viewed by other customers.|

### Most popular products block

Presents products that are currently trending and widely popular among users.
Helps quickly identify top-performing and popular items.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

Toggle the **Enable showing only available items** option on to display only products that are currently in stock.

### Most popular products in category block

Displays the most popular products within a selected category.
Helps identify most popular items within a specific category.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Product category** - Select product categories.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

Toggle the **Enable showing only available items** option on to display only products that are currently in stock.

### Other customers have also seen block

Shows products viewed by users with similar behavior.
Enhances user experience by suggesting related products.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Product code** - Enter a product code for a base product or select base product from the Product Catalog.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

Toggle the **Enable showing only available items** option on to display only products that are currently in stock.


## Recommendations: Commerce

The following blocks can be used to show recommendations based on visitors purchase history (buy and basket events):

|Block|Description|
|-----|-----------|
|[The Personal Shopping Assistant](#the-personal-shopping-assistant-block)|Assists users by suggesting relevant products in real time based on their activity.|
|[User's item history or current basket items sorted by recent items or top items](#users-item-history-or-current-basket-items-sorted-by-recent-items-or-top-items-block)|Displays the user’s item history or current basket, sorted by recent or top items.|

### The Personal Shopping Assistant block

Provides real-time product recommendations based on user behavior.
Helps users see relevant items while browsing.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Product id (optional)** - Add or select base product.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

Toggle the **Enable showing only available items** option on to display only products that are currently in stock.

### User's item history or current basket items sorted by recent items or top items block

Shows the user’s past or current basket items, sorted by recent activity or top items.
Makes it easier to find and review previously viewed or added products.
On the **Properties** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Name displayed on page (optional)** - Enter a name fot the block to be displayed on page.
- **Visit history** - Set whether to include or exclude visit history.
- **Current basket** - Set whether to include or exclude current basket.
- **Buy history** - Set whether to include or exclude buy history.
- **Sort history** - Set whether to sort the history by recent or top items.
- **Recommendations limit** - Set the number of recommendations to be displayed (default = 4).

Toggle the **Enable showing only available items** option on to display only products that are currently in stock.

For the list of all available blocks in Page Builder, see [Block reference](block_reference.md) page.
