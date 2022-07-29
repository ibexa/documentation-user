# Cross content type recommendations

Cross content type is used to get recommendation items for each input types whe scenario has more than one output type configured.

## Configure scenario output type

To get multiple output types in the recommendation request, go to **Scenarios**.

1. Click the **Edit** icon next to the respective scenario.
1. From the **Output type** multiselect field, select types you want to get recommendations for.
    It contains a list of all content types exported for the specified customer ID.
1. Next, go to Preview Scenario.
1. From the **Output type** drop-down, select **All**. This option can be translated according to your needs.

The **All** option automatically appears after content types are selected in the scenario settings.

The example generated request URL looks like the following:

`GET {host}/api/v2/{mandator}/{userId}/{scenarioId}numrecs={numberOfRecommendations}&categorypath=/&crosscontenttype=1`

Default option for Scenarios with more than two output types, and the default returned output is then cross content type.

## Cross content type in Page Builder blocks

You can 


To get all output types in Personalized block, perform the following:

1. Set the Scenario with configured crosscontent types output.
1. Next, from the drop-down **Select a Content Type to be displayed** -> All
select scenario, set the rest.


Dynamic targeting block

based on a scenario. you cannot set what items will be returned in the dynamic targeting 
 
It returns first  that is set in the scenario
will be: Separate select with an output type

segment, fourth select: output type
segment, scenario, output type

For more information about dynamic targeting block, see.

ibexa_personalization.yaml or config file:

`output_type_attributes` -> link do dev doca

id 
title
image
map field names

blogpost > title

get all outputtypes that are configured here and get attributes from the config in the ibexa_personalization.yaml

Generated URL, with cross content type recommendations, `crosscontenttype` 1

`outputtype`=number

Change/increase the number of returned items. relevance


Page Builder

Personalized and Dynamic targeting blocks

Personalized block

select scenario, set the rest. what responses we want.
Select a content type to be displayed -> All


Dynamic targeting block

based on a scenario. you cannot set what items will be returned in the dynamic targeting 
 
 returned first that is set in the scenario
will be: Separate select with an output type

segment, fourth select: output type
segment, scenario, output type


link to https://doc.ibexa.co/en/latest/guide/personalization/enabling_personalization/#export-item-information



Render recommendations on front 

crosscontenttype parameter = true
if if you want a particulat ct, add output type id, and number

3 methods how to render reco on the front
- parameter outputid
- crosscontenttype
- outputtype with JSON

----------------------


render es poprawic
i dla outputid 
3.3+ 

od 4.2 dodac cross content type


Currently to receive recommendations for a scenario include url scenario name and the output type.

Preview section -> main restriction only one output type ID can be included.
To receive reco for more than one content type, 
remove `outputtype`, add `crosscontent type parameter to the request
will receive recommendations based on all output types configured/supported in the scenario.

When scenario has configured more than one output type (content type) then the `CrossContentType` parameter can be used to get recommendation items for each output type.

Example of the request

`GET {host}/api/v2/{mandator}/{userId}/{scenarioId}numrecs={numberOfRecommendations}&categorypath=/&crosscontenttype=true`

Example of the response

Scenario preview section
Dynamic targeting and Personalization (page builder blocks)