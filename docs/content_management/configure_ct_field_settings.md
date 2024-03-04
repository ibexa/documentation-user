---
description: Configure Field settings in content types.
---

# Configure content type Fields

When you work with a [content type](content_model.md#content-types) to add or modify [Fields](content_model.md#fields-and-field-types), 
you must configure different settings that control the way [[= product_name =]] 
treats the contents of each Field. Apart from general settings, certain Field Types, for example, [Landing Page](#default-configuration-of-pages) and [Content relation](#content-relation-settings) Field Types may have additional settings.

You can only create or modify content types when your [user Role](../permission_management/work_with_permissions.md) has the `ContentType/Create` or `ContentType/Update` permission.

1\. [Create or open a content type](create_edit_content_types.md) for editing.

2\. In the **Field definitions** area, find a section, for example, **Content**. 

3\. If your application requires a more granular organization of Fields within a content type, click **+ Add** to add more sections.

When you add a **Metadata** section, it is later presented as an additional tab in [Content item](content_items.md) editing screen.
You can use it for tags, product categories, and so on.
When you add other sections, they are later presented as anchors in Content item editing screen.
All sections are later presented as headers on the Content item details screen, the **View** tab.

4\. Add, reorder or remove Fields as required:

- To add a Field, from the **Field types** area, drag the required Field tile to the section on the left. 
- To reorder Fields, drag and drop them within the section or between sections on the left.
- To remove Fields from the section completely, click the **X** icon in the Field's header.

![Adding a Field](img/add_field.png "Adding a Field")

5\. Expand the header of a Field that you want to modify, then [change its settings](#general-settings). 

6\. To save your changes:

- Click **Save** and continue editing.
- Click **Save and close** to close the window.

7\. To discard your changes and close the window:

- If you are creating a new content type, click **Discard**.
- If you are updating an existing content type, click **Delete draft**.

## General settings

Depending on their type, Fields can have different combinations of the following general settings. 

|Setting|Description|Use|
--------|-----------|---|
|Name|A user-friendly name that describes the Field, used in the interface. It can be up to 255 characters long and consist of letters, digits, spaces and special characters.|Required|
|Identifier|An identifier for system use in configuration files, templates, or PHP code. It can be up to 50 characters long and can only contain lowercase letters, digits and underscores. Also used in name patterns for the content type.|Required|
|Description|A detailed description of the Field. It is displayed next to it when the user edits the Content item.|Optional|
|Required|Indicates whether a value of the Field is required for the Content item to be saved or published.|Optional|
|Searchable|Indicates whether a value of the Field is included in the search.|Optional|
|Translatable|Indicates whether a value of the Field can be translated.|Optional|
|Can be a thumbnail|Indicates whether the Field can be a thumbnail.|Optional|

## Default configuration of pages

The following settings control the behavior of Content items of [Page](../content_management/create_edit_pages.md) type. 
You modify them in the **Field definitions** section, the **Landing Page** Field.

### Block display

You can define which page blocks are available to an editor in the page edit mode.
You do it, for example, when a [developer creates a new block]([[= developer_doc =]]/content_management/pages/create_custom_page_block/) and you want to allow adding it to the page.

Expand the **Select blocks** section and select page blocks that you want to be included in the page.

![Page blocks](img/select_page_blocks.png "Select page blocks")

Now, only selected page blocks are available in the edit mode.

![Elements menu](img/page_blocks_toolbar.png "Elements menu")

!!! caution

    When you deselect blocks, any related blocks that are included in the Page 
    hide as well. 
    To publish the Page, the editor has to remove these blocks from the Page, too.

### Available page layouts

You can decide which page layouts are available for an editor.

Expand the **Select layouts** section, and define which layouts are available 
for this Page.

![Layouts](img/select_layouts.png "Layouts")

If you deselect a layout that is currently used on a Page, the editor has to change 
the layout to be able to edit the Page.

### Preferred editing mode

You can set the editing mode that is launched when an editor starts editing the Page.
To do it, in the **Select Editor launch mode** section, select one of the available options.

![Editor launch mode](img/select_editor_mode.png "Select Editor launch mode")

## Content relation settings

When you add or modify a **[Content relation](create_edit_content_items.md#relation_field)** or **Content relation (multiple)** 
Field in a content type, you can decide:

- which Content Tree location opens in the 
[Content Browser](content_model.md#content-browser) when the user browses to a related 
Content item 
- whether relations can be to Content items of a specific type only, or any content type

#### Relation starting location

In the **Select starting Location** area, select from the available options:

- **Default** - the starting location is automatically assigned to the default location in the tree of a created Content item.
- **Browse** - use to manually select the location from the Content Browser.
- **Content location** - the starting location is the location of the Content item that is edited by the user. For example, if the user edits the Content item with the location `50`, it sets the starting location to this value with children under this location.
- **Root default location** - use if you want the Content Browser to start at the defined location with only children available for selection.

![Select starting location](img/select_start_location.png "Selecting a starting location")

#### Allowed content types

In the **Allowed content types** area, expand the drop-down list and select from the available content types.
No selection means that relations to all content types are allowed.
