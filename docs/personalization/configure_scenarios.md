---
description: Configure models by setting up a timeframe, segments and other settings that define which Content items are recommended.
---

# Configure scenarios

The **Scenarios** page contains a list of all available scenarios.
It also provides additional information, such as a description of each of the scenarios, models 
that the scenario uses, or indication of whether the scenario is operational or not.

![Scenarios page in the Back Office](img/dashboard_scenarios.png "Scenarios page")

 Click the **Edit** icon to access the scenario configuration screen, where you can configure 
 a number of settings, for example:
 
 - The type of content used as input data and recommended items
 - Primary, secondary and provisional models used to calculate results
 - User profile-based settings, boost settings and other filters that can be used to eliminate or promote specific results
 
Here, you can also click the **Preview** icon to see an example of recommendations that 
the scenario returns.
You may need to provide additional information to see the results.

For more information, see [Scenarios](scenarios.md).

## Configure filters

With filters you can eliminate, demote or promote specific recommendation results.

![General filters](img/scenario_filters.png "General filters in a scenario")

For a complete list of available filter types and their meaning, see [Filters](filters.md)

## Configure cross content type recommendations

Cross content type option is used to combine best recommendation items from 
different [content types](content_types.md). 
It applies to scenarios which have more than one output type configured.

To get multiple output types in the recommendation request, perform the following actions:

1\. Go to **Personalization** -> **Scenarios**.
2\. Click the **Edit** icon next to the scenario for which you want to set cross content type recommendations.
3\. In the **Output type** multiselect field, select the types for which you want to get recommendations in the request.

    It contains a list of all content types exported for the specified customer ID.
4\. Next, go to Preview Scenario.
5\. From the **Output type** drop-down, select **All**. 

The **All** option automatically appears after content types are selected in the scenario settings.

!!! note

    The **All** option can be translated according to your needs.

![Cross content type](img/perso_cross_content_type.png)
