---
description: In the Back Office you can preview what results are recommended by the Personalization service.
---

# Previewing scenario results

If your [user Role](../site_organization/organizing_the_site.md#permissions) includes 
the `Personalization/View` Policy, you can see what Content items/products are recommended 
to the end user when specific [scenarios](scenarios.md) are triggered. 
Depending on the scenario type, you may need to provide additional information 
to see the recommendation results.

The number and selection of available scenarios depends on the arrangements that 
your organization makes with Ibexa when defining the initial configuration.

1. Navigate to the **Personalization** > **Scenarios** tab, and then click the **Preview** 
icon next to a scenario that you want to preview.

1. If your scenario is based on models of [popularity type](recommendation_models.md#popularity-models), such as, for example, 
**Landing page** or **Top clicked**, skip to the last step. 

    No further configuration is required.

1. If your scenario is based on models of [collaborative type](recommendation_models.md#collaborative-models), such as, for example, 
**Also clicked**, in the **Context items** area, click **Add items**, and select a Content item/product from the content browser:

    1. Navigate to the Content item/product to be used as a context item for your recommendation results, for example, **Sites** > **My site** > **Products** > **Category 1** > **Product 1**.
    1. Click the **Add** icon to select the Content item/product, and then click the **Confirm selection** icon.

1. If your collaborative scenario has [category-path filtering](filters.md#category-path-filters) 
enabled, for example, **Also clicked - category**, in the **Category path filter** 
area, click **Select path**, and select a category to filter the results:

    1. Navigate to the category to be used as a filter, and then click the **Confirm selection** icon.

1. If your collaborative scenario uses the end user’s history as context, like, for example, 
**Also clicked - user**, enter an end user identifier in the **User id** field, for example, 500.

1. If your scenario has the use of [submodels](recommendation_models.md#submodels) enabled, 
in the **Custom parameters** field, enter the phrase that defines a set of items 
based on a specific attribute, for example "material=wood", and then click the **Add** button.

1. Click **Send request** to display the results.

!!! note "Display response"

    You can preview the exact data object that is returned from the recommendation server 
    and then used by the personalization service to generate the response. 
    To see the data object, click **See response code**.
