# Importing data

Before the system can generate relevant recommendations, it must be fed with data that 
relates to content items/products that are monitored, and event tracking information.
Some scenarios provide better results if provided with user data.

Data import operations are configured at developer level, based on the arrangements that you make with Ibexa. Content item import jobs fetch data from the recommendation client, which tracks events, 
to the recommendation engine.
The recommendation engine then processes the events and calculates the recommendations.


## Content data import

There are several ways to import data into the personalization service, for example, one can
load an exported file to the recommendation engine from a specified location. 
This type of import is intended to upload big portions of information, and can be used 
to perform a weekly update of the whole product catalog.

For detailed information about content data import, see [Content API](https://doc.ibexa.co/en/master/guide/personalization/developer_guide/content_api) in the developer documentation.

## User data import

The personalization service has little information about the users of the website. 
Additional attributes, such as the user's age or home city, might help the service generate 
a successful recommendation, for example, by enabling the use of [boost filters](filters.md#boost-filters).
User attributes could be retrieved based on the external user ID.
However, it is rarely possible to combine the external user ID within the user's attribute set.

For more information about user attribute import, see [User API](https://doc.ibexa.co/en/master/guide/personalization/developer_guide/user_api) in the developer documentation.

## Viewing a list of import operations

In the Back Office, from the top bar under **Personalization**, you can access 
the **Import** page that displays a list of historical import operations and their details, 
such as a number of imported content items/products, their type and language.

![Import tab in the Back Office](img/dashboard_import.png "Import tab")
