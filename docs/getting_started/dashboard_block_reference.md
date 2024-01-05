---
description: Pick from a list of dynamic blocks to create customized dashboard.
edition: experience
---

# Dashboard block reference

The following blocks are provided with a clean installation of [[= product_name =]]:

|Block|Description|
|-----|-----------|
|[Common content](#common-content-block)|Displays a list of content items created by all the organization that the user belongs to.|
|[Ibexa News](#ibexa-news-block)|Displays a list of recent blog posts or articles published at `ibexa.co` blog.|
|[My content](#my-content-block)|Displays a list of content items created by the user currently logged in.|
|[Orders by status](#orders-by-status-block)|Displays a chart presenting orders and their status.|
|[Products by category](#products-by-category-block)|Displays a chart presenting products by their category.|
|[Products with lowest stock](#products-by-category-block)|Displays a table presenting products with the lowest stock.|
|[Quick actions](#quick-actions-block)|Displays most popular/used actions and shortcuts.|
|[Recent activity](#recent-activity-block)|Displays a list of recent activity.|
|[Recent orders](#recent-orders-block)|Displays a table presenting recent orders.|
|[Review queue](#review-queue-block)|Displays a list of Content items which user or User group can review.|
|[Top 10 clicked items](#top-10-clicked-items-block)|Displays a table presenting top 10 clicked items.|

!!! note

    Before you add a block that involves products, product types, or product categories, make
    sure your that your [user Role](../permission_management/permissions_and_users.md) has
    the `Product/View` and `Product type/View` permission.

## Common content block

Displays a list of content items created by all the organization that the user belongs to.
It shows the following tabs: Content, Scheduled, Media.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content and submit your changes.

## Ibexa News block

Presents a list of recent blog posts or articles published at `ibexa.co` blog.
It includes title, image, timestamp, and link to article details.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **News limit** - Set the maximum number of news to be displayed. Default = 7, minimum value = 1, and maximum = 10.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of news and submit your changes.

## My content block

Displays a list of content items created by the user currently logged in.
It shows the following tabs: Drafts, Scheduled, Content, Media, Drafts to review.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content and submit your changes.

## Orders by status block

Displays a chart presenting the percentage and number of orders with their statuses.
The chart presents orders in selected statuses: Pending, Processing, Cancelled, Completed.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Statuses** - Set the statuses of orders that should be included in the list: Pending, Processing, Cancelled, Completed. Default value = All.
- **Periods** - Set the time period: All time, Last day, Last week, Last month. Default value = Last month.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of orders and submit your changes.

## Products by category block

Displays a chart presenting the percentage of products in selected number of categories.
Some products can be assigned to multiple categories, or be uncategorized.
You can either enable or disable to show or hide uncategorized products in the chart.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Categories limit** - Set the maximum number of categories to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Products with lowest stock block

Displays a table of products with the lowest stock.
Products are sorted based on Stock value (sorted from lowest to highest stock).

Table contains following columns: Name, Image, Code, Category, Type, Variant, Stock.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Number of products to be displayed** - Set the number of products to be displayed. Default value = 10.
- **Stock** - Enter the stock number for a product. Default value = 10.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Quick actions block

Displays most popular/used actions and shortcuts, for example, **Create content**.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Actions** - Select actions to be displayed as shortucts: Create content, Create form, Create product, Create catalog, Create company.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of quick actions and submit your changes.

## Recent activity block

Displays a list of recent activity of Users.
It also includes the link to view All activities available in Admin tab.

Recent activity block contains the following data: Timestamp, User (avatar, first and last name) with link to the user profile,
Activity type with the context.

Available filters are: Users, Activity type, Activity area (default value = All), Number of activities (default value = 5, maximum value = 10).

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Results limit** - Set the maximum number of activity logs to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.

## Recent orders block

Displays a table presenting recent orders with the newest creation date/recently placed.

Table contains following columns: Order ID, Company name, Customer name, Unique items, Total value, Status, Created.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Statuses** - Set the statuses of orders that should be included in the list: Pending, Processing, Cancelled, Completed. Default value = All.
- **Limit** - Set the maximum number of orders to be displayed. Default value = 10.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of orders and submit your changes.

## Review queue block

Displays a list of Content items which user or User group can review.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.

## Top 10 clicked items block

Displays a table presenting top 10 clicked items.

Table contains following columns: Item clicked (including item name), Item type, Recommended (presenting number of recommendations of selected item),
Clicked (presenting total number of clicks on selected item).

Available filters are: Item types, Customer ID, Number of displayed items (default value = 10), Time period.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Customer Id** - Select customer Id whose top 10 clicks are displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.