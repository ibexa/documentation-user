---
description: 
---

# Segment management

Segments allow getting personalized content suitable for particular user groups. They compute models based on segment attribute factor.
Information with user segment is provided in each event which comes from the tracking script.

## Configure segments

With segment groups you can assign users to different recommendation groups based on data gathered and deliver recommendations to these user groups.

The **Segment** list displays only active segments and is generated from the events collected for relevant history (the actual data from recommendation engine, not what is added using the Back Office).

The value of each segment is transfered to the event.

Models are displayed only for a selected time period. 
If a group is inactive for a certain period of time, the segments get `Inactive` status and cannot be used.

![Time period](img/models_time_period.png "Time period configuration")

!!! segment name unique

### Operators and segmentation logic

Segmentation logic in segment groups allows you to divide target audience according into their specific demographic traits, behaviors, age to provide narrowed,
and better tailored recommendations.
You can build complex segment groups using parent and nested (child) segments connected with operators which enable precise filtering.

With operators you can establish filtering rules for recommendations based on segments, and create nested groups withing
parent groups.

!!! tip

    You can add unlimited number of children in the parent group.

**AND** - use when you want to intersect two or more values for a particular segment. All set conditions must be met.

**OR** - use when you want to broaden results; one of the conditions must be fullfiled.

Nested (child) segments inside can have different conditions than their parent. However the relation between parent and child is always `AND`.
Use them to create sub segment groups which narrow filtering of recommendations to very specific traits of your users.

![Parent segment group](img/perso_segment_group_and_parent.png "Parent segment group")




### Create segment group with AND logic condition

![AND segment group logic](img/perso_segment_group_sales_hunters.png "AND segment group logic")




A regular recommendation is based on different clicks form different segments.

zwykla rekomendacja jest oaprta o rozne kliki z roznymi segmentami. 

w respnsie:

z duzym relevance dla 587
```json
    {
   "contextItems": [],
   recommendationItems: [
      {
         itemId: 581,
         itemType: 57,
         relevance: 3,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/581?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/581?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Traditional Living room"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/1/5/7/0/751-1-eng-GB/dee342e92e16-living-room2.jpg"
               ]
            }
         ]
      },
      {
         itemId: 578,
         itemType: 57,
         relevance: 2,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/578?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/578?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Transitional kitchen inspiration"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/7/2/7/0/727-1-eng-GB/909a45e396c2-kitchen2.jpg"
               ]
            }
         ]
      },
      {
         itemId: 579,
         itemType: 57,
         relevance: 2,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/579?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/579?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Refresh your home for spring"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/8/4/7/0/748-1-eng-GB/b651740b00d9-living-room.jpg"
               ]
            }
         ]
      },
      {
         itemId: 587,
         itemType: 57,
         relevance: 2,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/587?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/587?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Woods edge living room"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/4/5/7/0/754-1-eng-GB/245d16d84164-living-room3.jpg"
               ]
            }
         ]
      },
      {
         itemId: 580,
         itemType: 57,
         relevance: 1,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/580?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/580?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Find place for work in a busy home"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/4/8/7/0/784-1-eng-GB/698eab8423d9-office3.jpg"
               ]
            }
         ]
      },
      {
         itemId: 582,
         itemType: 57,
         relevance: 1,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/582?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/582?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=9aac3a40-dea2-11ed-8c58-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Landscape and Backyards"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/3/9/7/0/793-1-eng-GB/81e502566448-outside.jpg"
               ]
            }
         ]
      }
   ]
}
```

z malym relevance dla 587

```json
    {
   "contextItems": [],
   recommendationItems: [
      {
         itemId: 587,
         itemType: 57,
         relevance: 1,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/587?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=276a5930-dea3-11ed-8cdf-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/587?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=276a5930-dea3-11ed-8cdf-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Woods edge living room"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/4/5/7/0/754-1-eng-GB/245d16d84164-living-room3.jpg"
               ]
            }
         ]
      },
      {
         itemId: 588,
         itemType: 57,
         relevance: 1,
         links: {
            clickRecommended: "//event.test.perso.ibexa.co/api/41307/clickrecommended/someuser/57/588?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=276a5930-dea3-11ed-8cdf-92a64ae30943",
            rendered: "//event.test.perso.ibexa.co/api/41307/rendered/someuser/57/588?scenario=landing_page&modelid=10316421&categorypath=&requestuuid=276a5930-dea3-11ed-8cdf-92a64ae30943"
         },
         attributes: [
            {
               key: "title",
               values: [
                  "Minimalist luxury in a small and stylish bedroom"
               ]
            },
            {
               key: "teaser_image",
               values: [
                  "/var/site/storage/images/0/0/7/0/700-1-eng-GB/de8a98767362-bedroom2.jpg"
               ]
            }
         ]
      }
   ]
}
```

AND, czyli
   women
      Polska
AND
   sales hunters
wysłałem event do
id 587 z segments=7,11,14
oraz
id 588 z segments=7,9,11,14
reco call gdzie mamy segments=7,11,14 powinien zwraca te dwa itema

w item 587 klikala kobieta z Polski ktora jest przypisana w segmencie sales hunters
w item 588 klikala kobieta  wiek 45-50, z polski, sales hunters

mamy grupe: kobiety z polski ktore sa sales hunters.

dlatego te dwa eventy kwalifikuja sie do tej grupy segmentow/konfiguracji

te itemy matchuja sie z nasza segment grupa.


### OR logic condition


relevance mniejszy po segmencie bo mniej klikow od userow
natomiast w requescie bez segmentow skonfigurowanych, relevance tego itemu bedzie wyzsze (587)


