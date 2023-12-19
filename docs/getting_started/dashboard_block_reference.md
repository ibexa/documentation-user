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
|[Orders by status](#orders-by-status-block)|Displays a list of orders by their status.|
|[Products by category](#products-by-category-block)|Displays a list of products by their category.|
|[Products with lowest stock](#products-by-category-block)|Displays a list of products with the lowest stock.|
|[Quick actions](#quick-actions-block)|Displays most popular/used actions and shortcuts.|
|[Recent activity](#recent-activity-block)|Displays a list of recent activity.|
|[Recent orders](#recent-orders-block)|Displays a list of recent orders.|
|[Review queue](#review-queue-block)|Displays a list of Content items which user or User group can review.|
|[Top 10 clicked items](#top-10-clicked-items-block)|Displays a list of top 10 clicked items.|

!!! note 

    Before you add a block that involves products, product types, or product categories, make 
    sure your that your [user Role](../permission_management/permissions_and_users.md) has 
    the `Product/View` and `Product type/View` permission.

## Common content block

Displays a list of content items created by all the organization that the user belongs to.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content and submit your changes.

## Ibexa News block

Presents a list of recent blog posts or articles published at `ibexa.co` blog.
It includes title, image, timestamp, and link to article details.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **News limit** - Set the maximum number of news to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of news and submit your changes.

## My content block

Displays a list of content items created by the user currently logged in.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content and submit your changes.

## Orders by status block

Displays a list of orders by their status.
The chart presents orders in selected statuses: Pending, Processing, Cancelled, Completed.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Statuses** - Set the statuses of orders that should be included in the list: Pending, Processing, Cancelled, Completed.
- **Periods** - Set the time period: All time, Last day, Last week, This month, this year, Last month.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of orders and submit your changes.

## Products by category block

Displays a list of products by their category.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Categories limit** - Set the maximum number of categories to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Products with lowest stock block

Displays a list of products with the lowest stock.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Number of products to be displayed** - Set the number of products to be displayed.
- **Stock** - Enter the stock number for a product.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Quick actions block

Displays most popular/used actions and shortcuts, for example, **Create content**.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Actions** - Select actions to be displayed as shortucts: Create content, Create form, Create product, Create catalog, Create company.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of quick actions and submit your changes.

## Recent orders block

Shows table presenting recent orders with the newest creation date/recently placed.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Statuses** - Set the statuses of orders that should be included in the list: Pending, Processing, Cancelled, Completed.
- **Limit** - Set the maximum number of orders to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of orders and submit your changes.

## Recent activity block

Displays a list of Content items which user or User group can review.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Results limit** - Set the maximum number of activity logs to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.

## Recent orders block

Displays a list of recently placed orders along with their statuses.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Statuses** - Set the statuses of orders that should be included in the list: Pending, Processing, Cancelled, Completed.
- **Limit** - Set the maximum number of orders to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.

## Review queue block

Displays a list of Content items which user or User group can review.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.

## Top 10 clicked items block

Displays a list of top 10 clicked items in connection with the Id of a specific customer.

On the **Properties** tab, set values in the following fields:

- **Name** - Enter a name for the block.
- **Customer Id** - Select customer Id whose top 10 clicks are displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of content items for review and submit your changes.