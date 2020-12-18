# 3. Dashboard

The administration dashboard is the entry point to configure and control the Personalization Solution. 
It is split into several sections:

- The top section contains tiles with the most important metrics, such as a number of recommendation calls, number of successful recommendations and so on.
- The diagrams section presents statistical information on how the recommendation engine is used and how successful - depending on the KPIs - recommendations are.
- The bottom section is made up of tables with detailed information, such as the most popular items, or top purchases.

## Statistics

The diagram part consists of four main blocks:

- Collected events:
    The input data (clicks, buy, clickrecommended, ...) which is going into the recommendation engine for the customer website. For more information, see [Event Types](event_types.md).
- Recommendation calls:
    The number of recommendation calls (total and per scenario).
- Revenue:
    The effectiveness of recommendations regarding clicked recommendations, revenue through recommendations.
- Conversion rate:
     An absolute number of converted/sold recommendations.

The conversion (or click-through) rate is an **indicator of the acceptance** and therefore 
the **quality of recommendations**. 
It is calculated as follows: The total number of clicked recommended products divided by the amount of 
recommendation calls. 
This statistic only delivers reliable information if the tracking is implemented correctly.

The revenue-through-recommendations is a **monetary value** which was additionally created by recommendations. 
It is calculated as follows: If a user buys product A and has clicked on it as a recommendation within 
30 minutes before we assume it was sold through a recommendation.

Purchased recommendations is the **plain number of sold recommendations** without any revenue/price information.

All statistical information can be downloaded in MS Excel format. 
The timeframes depend on the selection of the diagram period (day, week, month, 3 months and year) but 
can also be customized.

## Configuration Settings

The top bar provides you with access to the following pages, where you can configure the 
Personalization Solution.

### Models

This tab allows you to see all available models and configure them. 
For more information, see [Recommendation Models](recommendation_models.md).

![Dashboard models](img/dashboard_models.png)

### Scenarios

The scenario overview shows all available scenarios. Additional info like a description 
and the delivered recommendations in the selected timeframes are also presented.

Scenarios with green status bars indicate that all models can provide recommendations. 
Yellow bars indicate that only a part of the configured models can provide recommendations 
and red ones indicate that no recommendations can be delivered. 
For more infromation, see [Scenarios](scenarios.md).

### Import/Export

Item import jobs are used to fetch data from a customer system. 
Data-mappings and schedule times are defined here.
