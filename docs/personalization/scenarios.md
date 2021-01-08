# Scenarios

A scenario is a configuration for getting recommendations. 
It consists of:

- a content type to be returned as recommendation 
- a strategy (set of models) that is used for generating recommendations
- a filter configuration

You can preview the results of a scenario by clicking the **Preview** icon next to a scenario listed on the Scenarios tab.

## Content type configuration

Every scenario supports a single input type and multiple output types. 
Every recommendation request delivers only content of one output content type 
(even if multiple are selected in the interface above). 
The output type is set during the recommendation request and must be covered by 
the list of the supported content types in the requested scenario.

![Basic scenario configuration](img/scenario_configuration.png "Basic scenario configuration")

## Strategy configuration

To modify the strategy, you drag model boxes between a list of all available models and the scenario 
matrix on the right side.
To avoid empty or insufficient recommendation results, add several models to a strategy.

![Strategy configuration](img/scenario_configuration_strategy.png "Strategy configuration")

Models within a strategy matrix can be arranged by importance.
Models from each category are used in parallel and strategy results contain an equally 
distributed mixture of both model results. 
If models from a preceding category do not return enough results, models from the 
subsequent categories are used.

In contrast to the model configuration described in [Recommendation Models](recommendation_models.md), 
the configuration performed in this step is applied only to the selected scenario.

## Filter configuration

For every recommendation scenario a set of general filters can be defined that are applied to all recommendations from every model used in the scenario.

![General filters](img/scenario_filters.png "General filters")

For more information, see [General filters](filters.md#general-filters).

For each of the categories from the strategy configuration matrix, you can click the **Configure** icon and configure category filters. 
For a detailed description, see [Category Filter](filters.md#category-filter).
