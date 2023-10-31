---
description: Pick from a list of dynamic Page blocks to create landing pages.
edition: experience
---

# Block reference

The following blocks are provided with a clean installation of [[= product_name =]]:

|Block|Description|
|-----|-----------|
|[Banner](#banner-block)|Displays an image Content item with a URL attached to it.|
|[Bestsellers](#bestsellers-block)|Displays a list of products that were recently a bestseller.|
|[Catalog](#catalog-block)|Displays products from a specific catalog to a selected customer group.|
|[Code](#code-block)|Enables you to place text, links, images, etc. on your Page using custom HTML.|
|[Collection](#collection-block)|Displays a set of Content items you select manually from the Content structure. |
|[Content List](#content-list-block)|Displays Content items of a chosen Content Type (or Types) that are contained in a selected folder. |
|[Content Scheduler](schedule_publishing.md#content-scheduler-block)|Displays Content items at a pre-defined time. |
|[Dynamic targeting](#dynamic-targeting-block)|Embeds recommended items based on the [Segment](content_organization/classify_content.md#segments) the user belongs to. |
|[Embed](#embed-block)|Embeds a Content item of any Content Type on the Page. |
|[Form](#form-block)|Embeds a Form Content item that you select from the Content Structure. |
|[Gallery](#gallery-block)|Displays all images contained in a selected folder. |
|[Ibexa Connect](#ibexa-connect-block)|Retrieves and displays data from an Ibexa Connect webhook. |
|[Last purchased](#last-purchased-block)|Displays a list of products that were recently purchased from PIM. |
|[Last viewed](#last-viewed-block)|Displays a list of products from PIM that were recently viewed. |
|[Orders](#orders-block)|Displays a list of orders associated with a particular company or individual customer. |
|[Personalized](#personalized-block)|Displays a list of Content items/products that are recommended to end users when specific scenarios are triggered. |
|[Product collection](#product-collection-block)|Displays a list of specifically selected products.|
|[Recently added](#recently-added-block)|Displays a list of products that were recently added to PIM. |
|[RSS](#rss-block)|Loads and displays news from RSS feeds (channels). |
|[Sales representative](#sales-representative)|Loads and displays company's sales representative.|
|[SeenThis!](#seenthis-block)|Displays video with exceeded standard video restrictions of 3.5MB.|
|[Targeting](#targeting-block)|Embeds an Content item based on the [Segment](content_organization/classify_content.md#segments) the user belongs to. |
|[Text](#text-block)|Enables you to add to the Page a Rich Text block. |
|[Video](#video-block)|Embeds a video into the Page with standard playback controls. |

[[= include_file('docs/content_management/create_edit_pages.md', 86, 96) =]]

## Banner block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Image** - Click **Select content**, navigate through the content and select an image to display.
- **URL** - Enter a URL to open when clicking the selected image.

## Bestsellers block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Personalization scenario** – Select "Bestsellers" to display products that were recently a bestseller.
- **Product Types to be displayed** – Select the type of products to be displayed on the list.
- **Limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Catalog block

Before you configure this block, make sure that there are [catalogs](../pim/work_with_catalogs.md) that are defined 
and published in your PIM.

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Default catalog** – Select a catalog that is displayed to end-users who are either 
anonymous or do not belong to any of the customer groups assigned to specific catalogs.
- **Setup customer group and catalog matching priority rules** - Create at least one assignment: add a row, then select a customer group and a matching catalog. 
- **Limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Code block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Content** - Enter the HTML code for the content you want to display.

## Collection block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Location list** - Click **Select content**, navigate through the content
and add to the collection Content items of any Content Type you want.
All selected Content items appear in the **Selected items** box at the bottom of the window.
When done selecting, click **Confirm**.

## Content List block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Parent** - Click **Select content**, navigate through the content and select a folder containing Content items
to display on the list. Click **Confirm**.
- **Limit** - Set the number of products to be displayed.
- **Content Types to be displayed** - Select Content Type(s) to be displayed.
The block will display Content items of the selected Content Types that are in the selected parent folder.

## Dynamic targeting block

Dynamic targeting block provides recommended items based on users related to the configured Segments.

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Select default scenario** - Select the default scenario for recommended items that should be rendered if the current user
is not assigned to any Segment.
- **Setup segment and scenario matching priority rules** - Select a Segment group, a Segment identifier and Scenario that you want to display recommendations from.
- **Display limit** - Set the number of products to be displayed.

The rules are checked in order, so when a user belongs to more than one Segment, the first rule applies.

![Dynamic targeting](img/page_builder_dynamic_targeting.png)

## Embed block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Content** - Click **Select content**, navigate through the content and select a Content item. Click **Confirm**.

## Form block

Note that completing the settings of the Form block requires at least one Form Content item created.

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Form** - Click **Select content**, navigate through the content and select a Form Content item to append it to the block.

!!! caution "Known limitation"

    To present two or more identical forms on one Page, ask your developer to create several identical form blocks that you can then use. Otherwise you may encounter issues with duplicate data submission.
    
    For more information about creating form blocks, see [Creating a newsletter form]([[= developer_doc =]]/content_management/pages/create_custom_page_block/) in developer documentation.

## Gallery block

On the **Basic** tab, set values in the following fields:

- **Name** - Enter a name for the Page block.
- **Folder** - Click **Select content**, navigate through the content, select a folder containing images to display and click **Confirm**.
After submitting the settings, all images in the folder will appear in the Gallery block.
Note that selecting a folder containing Content items other than images results in displaying only a link to the folder they are stored in.

## Ibexa Connect block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Webhook link** - Enter the link for the Ibexa Connect webhook.

On the **Design** tab, in the **View** field, select the template to be used to present the webhook.

!!! caution "Using Ibexa Connect scenario block"
    
    For more information about using Ibexa Connect scenario block, see [Ibexa Connect scenario block]([[= developer_doc =]]/content_management/pages/ibexa_connect_scenario_block/) in developer documentation.

## Last purchased block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Personalization scenario** – Select "Last purchased" to display products that were recently purchased from PIM by any user, or "Last purchased by user" to display products that were recently purchased by the current user.
- **Product Types to be displayed** – Select the type of products to be displayed on the list.
- **Limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Last viewed block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Personalization scenario** – Select "Last viewed" to display products that were recently viewed by any user, or "Last viewed by user" to display products that were recently viewed by the current user.
- **Product Types to be displayed** – Select the type of products to be displayed on the list.
- **Limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Orders block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Columns** - Select columns that should be displayed in the orders table. Some columns are preselected, example: Order ID, Customer name, Total value etc.
- **Statuses** - Set the statuses of orders that should be included in the list.
- **Limit** - Set the number of orders to be displayed.
- **Sort order** - Set the sort order for the displayed orders.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of orders and submit your changes.

## Personalized block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Select a scenario** – Select "Landing page" or "Top clicked".
- **Select a Content Type to be displayed** – Select "Product".
- **Display limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, change the layout to "Products" and submit your changes.

## Product collection block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Product list** - create a list of products. Enter a comma separated list of product/variant codes and click **Add** or click **Select product**. Then, in content browser, select products and click **Confirm**.

!!! note

    Due to a technical limitation, content browser does not display product variants.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## Sales representative

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## SeenThis! block

Integration with (SeenThis!)[https://seenthis.co/] service. SeenThis! block provides an adaptive streaming technology with no limitations as conventional streaming service. It allows to preserve the best video quality with minimum amount of data transfer.

!!! note
    This page block is in an opt-in bundle, to use it, install `ibexa/connector-seenthis` bundle first.

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the page block.
- **Video ID** – Enter the ID of the video to be streamed.
- **Tracker ID** – Enter the tracking code.
- **Big play button** – Set to display large play button.
- **Autoplay** – Configure whether the video starts automatically.
- **Muted** – Configure whether the video starts muted.
- **Play button** – Set the number of products to be displayed.
- **Mute button** – Set whether the mute button is displayed or not.
- **Loop** – Set to play a video in a loop mode.
- **Loop count** – Set the number of loop repetitions.
- **Include audio** – Set to include or not audio with the video.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.


!!! note

    SeenThis technology might be blocked by some ad blocker solutions. If you can't see the block once configured, check ad blocker configuration.

## Recently added block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Product Types to be displayed** – Select the type of products to be displayed on the list.
- **Display limit** – Set the number of products to be displayed.

On the **Design** tab, in the **View** field, select the layout to be used to present a list of products and submit your changes.

## RSS block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **URL** - Enter the URL for the RSS news feed.
- **Limit** - Set the number of news items to be displayed.
- **Offset** - Set the limit of featured news items to be displayed.

## Targeting block

Targeting block provides recommendation of content based on users related to the configured Segments.

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Select default content** - Click **Select content**, navigate through the content
and select the default Content item that will be displayed when no priority rules are valid.
- **Setup segment and content matching priority rules** - Select a Segment Group and a Segment,
then click **Select content** and navigate to the Content item that you want to display for the selected group.

The rules are checked in order, so when a user belongs to more than one Segment, the first rule applies.

You can preview the Page for each of the available Segments:

![Previewing Page for a given Segment](img/page_builder_segment_preview.png)

## Text block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Content** - Enter text, images, videos, etc. using Online Editor.
For details, see [Editing Rich Text Fields](create_edit_content_items.md#edit-rich-text-fields).

## Video block

On the **Basic** tab, set values in the following fields:

- **Name** – Enter a name for the Page block.
- **Video** - Click **Select content**, navigate through the content, select a video to display in the block and click **Confirm**.
On the **Basic** tab you can preview the selected video before adding it to the Page.