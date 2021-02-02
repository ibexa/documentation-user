# Data import

Before the system can generate relevant recommendations, it must be fed with data that relates to content items/products that are monitored, and event tracking information.
Some scenarios provide better results if provided with user data.

Data import operations are configured at developer level, based on the arrangements that you make with Ibexa.

## Content import

Basic recommendation algorithms are statistics-based and perform calculations based on information about content items/products, users, and [events](event_types.md) in which they are involved. 

There are two basic areas where the system uses such information, including:

- resolving [recommendation models](recommendation_models.md#model-types) and [submodels](recommendation_models.md#submodels)
- filtering results based on [product characteristics](filters.md#general-filters) or [product category](filters.md#category-path-filter))

There are several ways to import data into the recommendation system, for example, the recommendation 
engine can load an exported file from the specified location in the background. 
This type of import is intended to upload big portions of information, for example, to perform a weekly update of the whole product catalog.
You can track the status of content import operations in the Back Office, on the Import/Export tab.

For detailed information about content item/product data import, see [Content API](https://doc.ibexa.co/en/master/guide/personalization/developer_guide/content_api) in the developer documentation.

# User data import

The recommendation engine has little information about the users of the website. 
Additional attributes, such as the user's age or home city, might help it generate 
a successful recommendation, for example, by enabling the use of [boost filters](filters.md#boost-filters).
User attributes could be retrieved based on the external user ID.
However, it is rarely possible to combine the external user ID within the user's attribute set.

For more information about user attribute import, see [User API](https://doc.ibexa.co/en/master/guide/personalization/developer_guide/user_api) in the developer documentation.
