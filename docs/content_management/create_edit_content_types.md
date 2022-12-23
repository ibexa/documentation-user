---
description: Create or edit Content Types by listing Fields that make a Content item.
---

# Create and edit Content Types

[Content Types](content_model.md#content-types) define what Fields are available in [Content items](content_items.md). 
To suit your specific needs, you can modify the default Content Types, or add custom ones.

You can only create or modify Content Types when your [user role](../permission_management/work_with_permissions.md) has the `ContentType/Create` or `ContentType/Update` permission.

When you edit a Content Type, each Content item based on this Content Type changes.
For example, when you add or remove a Field to the Content Type, the change 
is propagated to every Content item of this type.

!!! note

    Rules and templates for displaying content on the website are determined 
    at the developer level.
    That is why content of a new Content Type that you create may not always display 
    correctly or may cause errors.
    It is always best to discuss adding new Content Types with the administrator 
    of your website, to make sure whether they need to add it to the configuration.


!!! caution "Deleting Content Types"

    You can delete a Content Type only when there are no Content items that belong to it.
    This also includes Content items in the Trash.

1\. In the left panel, go to **Content** -> **Content Types** and select a Content Type group by clicking its name, for example, **Content**.

!!! note

    If your application requires a more granular organization of Content Types, in this screen, you can create additional Content Type groups. 

![Content Type list](img/content_types.png "A list of Content Types")

2\. If you are adding a new Content Type, on the Content Type group's detail screen, click **Add new** and skip to step 4.

3\. If you are modifying an existing Content Type, on the Content Type group's detail screen, click the **Edit** icon next to a name of the Content Type.

![Editing a Content Type](img/content_type_general_properties.png "Editing a Content Type")

4\. In the **Global properties** area, fill in global Content Type properties. Each Content Type has the following global properties:

|Setting|Description|Use|
--------|-----------|---|
|Name|A name of the Content Type.|Required|
|Identifier|A unique identifier of the Content Type in the system. Up to 50 characters and can only consist of letters, numbers and underscores.|Required|
|Description|Additional information that is displayed when a Content item is created based on this type.|Optional|
|Content name pattern|Rules for creating a name for the Content item.|Optional|
|URL alias name pattern|Rules for creating the URL alias for a Content item.|Optional|
|Container|When checked, Content of this Type can serve as a container in the Content tree.|Optional|
|Sort children by default by|Criterion by which children of this content will be sorted in the tree.|Required if **Container** is checked|
|Sort children by default in order|Order in which the children will be sorted (ascending or descending).|Required if **Container** is checked|
|Make content available even with missing translations|When checked, content of this Type will by default be always available, even if it does not have a language version corresponding to the current SiteAccess.|Optional|

!!! note "Rules for creating patterns"

    When populating the patterns, you can use a schema with attributes which 
    correspond to the identifiers of Fields that make up the Content Type. 
    This way, when Content Items of this type are created, their names and URL 
    aliases are generated according to the defined pattern. 
    
    For example, if you enter `<short_title>` as a value of the **Content name 
    pattern** field, the resulting items will be identified in the user interface 
    by their short titles.

5\. In the **Field definitions** area, modify Fields that constitute the Content Type.

To add a Field, from the **Field types** area, drag the required Field tile to 
a section on the left. 
To reorder Fields, drag and drop them within the section on the left. 
To remove Fields from the section, click the X icon in the Field's header.

![Adding a Field](img/add_field.png "Adding a Field")

!!! note

    If your application requires a more granular organization of Fields within a Content Type, you can click **Add** to add more Field definition sections. 

6\. Configure [field settings](configure_ct_field_settings.md).

7\. Optionally, [enable and configure SEO for the Content Type](../search_engine_optimization/work_with_seo.md).

8\. To save your changes, if you are creating a new Content Type, click **Create**, and if you are updating an existing Content Type, click **Save**.

Once a confirmation message is displayed, you can use breadcrumbs to navigate back to the Content Type list.

![Confirmation message](img/notification_ct.png "Confirmation message")

!!! note "More information"

    For in-depth information about the content model, see [developer documentation]([[= developer_doc =]]/content_management/content_model).
