---
description: Create content for your website with different Fields, rich text, tags, and then publish it.
---

# Create and edit Content items

## Create Content items

1. Start creating a new Content item in one of the following ways:

    - In the left panel, go to **Content** -> **Content structure**. Then select a parent Content item and click **Create content**. 
    
        The new Content item becomes a child of the Content item that you originally selected.
    
    - In the upper-right corner of the [My dashboard](../getting_started/discover_ui.md#my-dashboard) screen, click **Create content**.
    Then choose a location for the new item in [Content Browser](../getting_started/discover_ui.md#content-browser) and click **Create**.

    !!! tip

        An alternative way of creating Content items is to [drag one or more files](#upload-multiple-content-items) onto the **Sub-items** tab when viewing any Content item in a [Content Tree](../getting_started/discover_ui.md#content-tree). 

1. In a slide-out pane, make initial choices in the following fields, and click **Create**:

    - **Select a language** - from a drop-down list, select the base language for the Content item.
    - **Select a Content Type** - use this field to narrow down the list of choices displayed below. Then select a Content Type to serve as a template for the Content item.

    !!! note
       
        If you're using [[= product_name_exp =]] or [[= product_name_com =]], the options include forms and pages.
        You then [build forms](work_with_forms.md) and [create pages](create_edit_pages.md) by using their respective specialist tools.

1. [Fill in the Fields](#edit-new-or-existing-content-items) of the Content item.

1. Click **Preview** to see how the Content item could look to an end-user.
       
    !!! tip
    
        A Content item can look different on different [SiteAccesses](translate_content.md#siteaccess).
        You can select a SiteAccess to preview by using a drop-down in the preview screen.

1. To discard your changes and close the window, click **Delete draft**.

1. To save your changes:

    - Click **Save** to continue editing.
    - Click **Save and close** to close the window.

1. To send your changes to another editor [for review](editorial_workflow.md), click **Send to review**. 

1. When the Content item is ready for publication:

    - Click **Publish** to publish it immediately.
    - Click **Publish later** to set a specific publication date.

    For more information, see [Publish content](publish_content.md).

!!! note "Versioning and autosave"

    Whenever you edit a Content item, a [new version](content_versions.md) is created in the repository.

    To help you preserve your work, [[= product_name =]] saves drafts of Content items automatically.
    For more information, see [Autosave](content_versions.md#autosave).

##### Upload multiple Content items

When you view the Content item details in the Content Tree, you can upload files such as images, videos, PDF documents, and so on.
This way you can add multiple sub-items without editing the original Content item.
To do it, on the Content item details screen, in the **Sub-items** tab, click **Upload** and choose all items that you want to upload.
When a file is uploaded with multi-file upload, it is automatically stored in a Field of the Content item.

!!! note

    The Content Type for the uploaded files is selected automatically by the system.

![Multi-file upload](img/multi_file_upload.png)

## Edit new or existing Content items

Each Content item is based on a [Content Type](create_edit_content_types.md). The Content Type defines what Fields 
you have to fill in when creating a new item.
It may also determine the layout or style in which this item is displayed.

Fields marked with an asterisk (\*) are required. 
You can't save the Content item without filling them in.

Some Fields, such as *Relation* Fields (which link two Content items) or *Image* Fields
require you to select a different Content item to link to.
A *Location* Field is a point on the map. You can type the place name, enter its coordinates, or select it on the map.

<a name="relation_field"></a>

!!! note

    When you create or edit a Content item that contains an *Image* or an *Image asset* Field, 
    you can perform basic image editing functions by using an [Image Editor](edit_images.md).

### Edit Rich Text Fields

Rich Text Fields are filled in using a special Online Editor. Its options appear when you click the Field box.

![Online Editor menu](img/online_editor_menu.png "Online Editor menu")

To add a new element to the Field, choose one of the available elements:

- Heading
- Paragraph
- Unordered list
- Ordered list
- Image
- Embed
- Table
- YouTube
- Twitter
- Facebook

![Available Rich Text block elements](img/rich_text_block_elements.png "Available Rich Text block elements")

Each of these elements can have its own settings, such as text formatting.
The option bar also lets you reorder or remove any elements in the Rich Text Field.

#### Edit embedded Content items

You can edit embedded Content items without leaving current window.

To do it, first insert selected Content item in the Rich Text Field.
Then, click the three dots icon on the right side and click **Edit**.

![Edit embedded Content item](img/edit_embedded_item_richtext.png "Edit embedded Content item")

If the Content item has more than one translation available, you need to select the language.

![Edit embedded Content item - select language](img/edit_embedded_item_language_richtext.png "Edit embedded Content item - select language")

This action opens a new browser tab with an editing screen of the selected Content item.
When you finish editing the item, click **Publish**.
To see implemented changes refresh the browser page.

This option is also available when you want to set up a [relation](../configure_ct_field_settings/#content-relation-settings) with another Content item.

![Edit embedded Content item - set up a relation](img/edit_embedded_items_relation.png "Edit embedded Content item - set up a relation")

#### Distraction free mode

While editing Rich Text Fields, you can switch to distraction free mode.

Distraction free mode expands the workspace to full screen and shows only editor toolbar.
It's helpful when you need to work with longer texts that take more space and when you want to focus your attention on editing text.

![Distraction free mode](img/distraction_free_mode.png "Distraction free mode")

To access distraction free mode, click **Distraction free mode** on the right side above the workspace.

![Access distraction free mode](img/access_distraction_free_mode.png "Access distraction free mode")

To exit distraction free mode, click **Exit distraction free mode** or press Esc on the keyboard.

![Exit distraction mode](img/exit_distraction_free_mode.png "Exit distraction free mode")

#### Anchors

For longer texts, insert an anchor linking a fragment of text with another fragment or section
to quickly jump through sections of an article.
Create an anchor by clicking in the area to link to and selecting the anchor icon from the editor menu.
In the modal window, provide the name for the anchor. Scroll to the fragment where you want to insert the link,
and select the text to appear as a link. In the modal window, click the **Link** button.
This opens the window to create the link. In the **Link to** box, enter the anchor name. Click **Save**.

#### Images

In image options you can select an image variation.
Variations can include different sizing options and other filters that are applied to images.
Available image variations must be configured at the developer level.
See [Images]([[= developer_doc =]]/content_management/images/images/) for a technical guide on how to do this.

#### Tables

![Table options in online editor](img/online_editor_table.png)

In table options you can define the first row and/or column as headers,
add or delete rows and columns in any part of the table, as well as merge and split cells.

#### Custom elements

Your installation can also have custom elements available in the Rich Text field.
Contact your website administrator about the details of using them.

### SeenThis! streaming

!!! note
    This custom tag is in an opt-in bundle, to use it, install `ibexa/connector-seenthis` bundle first.

Use SeenThis! tag to enable displaying of video with maximum quality regardless of connection and server integration.

For more information, see [SeenThis! page block](block_reference.md#seenthis-block) documentation.

### Text formatting

When you select a section of text, you get access to text formatting options such as bold or underline.
Here you can also add a link to the text. You can link to an external website, or to another Content item.

### Add taxonomy entries

To keep your content organized and easy to find, you can add taxonomy entries to a Content item while creating or editing it.
For this feature to work as described, the Content Type must have a **Metadata** section, with a **Taxonomy Entry** field in it.

1. Switch to the **Meta** tab.
1. Click the **Select path** button.
1. In the pop-up window, select the tags you want to add.

![Selecting Taxonomy entries](img/taxonomy_select_taxonomy_entries.png "Selecting Taxonomy entries")

For more information, see [Assign tag to content from taxonomy tree](taxonomy/work_with_tags.md#assign-tag-to-content-from-taxonomy-tree).

## Preview Content items

There are several places where you can see how the Content item could look to an end-user. 
For example, you can click **Preview** in the Content item's details screen and then use a drop-down menu to switch between [SiteAccesses](translate_content.md#siteaccess).

Additionally, if you select a specific SiteAccess from the **Site context** drop down list on the right side of the top bar, three things happen:

- in Focus mode, when you browse Content items in Content Tree, their full screen preview is displayed
- if you [turn the Focus mode off](../getting_started/discover_ui.md#disable-focus-mode) or click **Exit full view**, the **View** tab appears in the Content item's details view, where you can quickly preview the Content item
- regardless of mode, when you hover over Content items in the Content Tree, miniature previews appear

