---
description: You can display recommendation results in your Pages using the Personalized block.
edition: experience
---

# Integrate scenario results

When the Personalization service is [enabled](enable_personalization.md) and properly [configured](configure_personalization.md), as an editor, you can embed the recommendations that come from the service, to show them to the end users.
You can, for example, modify a Page to include a block that shows what content items/products are recommended to end users when specific [scenarios](scenarios.md) are triggered.
One such example is the [Personalized block](../content_management/block_reference.md#personalized-block), where you can choose from a number of scenarios, but there are also other blocks that are tailored to display the results of scenarios
of specific types, like [Recently added block](../content_management/block_reference.md#recently-added-block) or [Bestsellers block](../content_management/block_reference.md#bestsellers-block).
Depending on the scenario type, you may need to provide additional information to see the recommendation results.

The blocks, the number, and selection of available scenarios within these blocks depend on the arrangements that your organization makes with [[= product_name_base =]] when defining the initial configuration.

Follow these steps to add and configure the Personalized block to a Page:

1. In [content tree](discover_ui.md#content-tree), navigate to the page in which you want to place a personalization block.

1. From the **Page blocks** toolbox, drag and drop the **Personalized** block to a location on the page layout.

1. Click the **Block settings** icon to modify the **Personalized** block:
 
    1. On the **Basic** tab, set values in the following fields:
        -	**Block name** – Optionally, enter a name for the page block, for example, "Bestsellers".
        -	**Select a scenario** – Select "Landing page" or "Top clicked".
        -	**Select a content type...** – Select "Product".
        -	**Display limit** – Set the number of products to be displayed, for example, 4.

    1. On the **Design** tab, in the **View** field, change the layout to "Products" and submit your changes.

      The preview of the Page changes to display a list of products recommended by the Personalization service.

1. Save your changes to the draft or publish the Page.

For more information about collecting events and embedding recommendation results, see [Integrate recommendation service]([[= developer_doc =]]/personalization/integrate_recommendation_service/).

## Use cross content type in Page Builder blocks

When scenarios are configured to display [cross content type recommendations](configure_scenarios.md#configure-cross-content-type-recommendations), you can use them in the following Page Builder blocks: [Dynamic targeting](../content_management/block_reference.md#dynamic-targeting-block) and [Personalized](../content_management/block_reference.md#personalized-block).

To get all output types in the Dynamic targeting block:

1. In the block settings, set the scenario with configured cross content type output.
1. From the **Output type** drop-down, select **All**.
1. Next, set the rules according to your needs.
1. Click **Submit**.

To get all output types in the Personalized block, in Page Builder, perform the following actions:

1. In the block settings, set the scenario with configured cross content type output.
1. Next, from the drop-down **Select a content type to be displayed**, select **All**.
1. Increase the display limit to make sure all recommendations are shown.
1. Click **Submit**.

For more information, see [Parameters]([[= developer_doc =]]/personalization/enable_personalization/#parameters) in developer documentation.
