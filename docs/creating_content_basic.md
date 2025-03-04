---
description: Create content for your site with different Fields, rich text, tags, and then publish it.
---

# Creating content

There are four ways of creating a new Content item:

1. Click **Create** in the right menu while viewing any other content.
The new item appears under the current Content item in the tree.
1. Click the **Create** (plus) icon when you *Browse content*.
Here also you have to choose a location for the new item.
1. Click **Create** in the upper-right corner of the **My dashboard** screen.
In this case you have to select where the content will be located.
1. Drag files onto the **Sub-items** box when viewing any content or click the upload button and select files to upload.
In this way you can upload files such as images, videos, PDF documents, etc.

If you choose the first three options, you have to select the Content Type first.
When uploading files, the Content Type will be chosen automatically.

If you are using [[= product_name_exp =]] or [[= product_name_com =]],
you will have the *Page* Content Type available for selection.
Pages are edited in the Page Builder, see [Pages](site_organization/working_with_page.md).

Each Content item is based on a Content Type. The Content Type defines what Fields you have to fill in when creating a new item.
It may also determine the layout or style in which this item is displayed.

Fields marked with an asterisk (\*) are required. You will not be able to save the Content item without filling them in.

Some Fields, such as *Relation* Fields (which link two Content items) or *Image* Fields
require you to select a different Content item to link to.
A *Location* Field is a point on the map. You can type the place name, enter its coordinates, or select it on the map.

!!! note "Autosave"

    To help you preserve your work, [[= product_name =]] saves drafts of Content items automatically.
    For more information, see [Autosave](publishing/publishing.md#autosave).

!!! note

    When you create or edit a Content item that contains an *Image* or an *Image asset* Field, 
    you can perform basic image editing functions by using an [Image Editor](editing_images.md).

## Editing Rich Text Fields

Rich Text Fields are filled in using a special Online Editor. Its options appear when you click the Field box.

![Online Editor menu](img/online_editor_menu.png "Online Editor menu")

To add a new element to the Field, select the plus icon to the left of the box and choose one of the available elements:

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

### Anchors

For longer texts, insert an anchor linking a fragment of text with another fragment or section
to quickly jump through sections of an article.
Create an anchor by clicking in the area to link to and selecting the anchor icon from the editor menu.
In the modal window, provide the name for the anchor. Scroll to the fragment where you want to insert the link,
and select the text to appear as a link. In the modal window, click the **Link** button.
This will open the window to create the link. In the **Link to** box, enter the anchor name. Click **Save**.

### Images

In image options you can select an image variation.
Variations can include different sizing options and other filters that are applied to images.
Available image variations must be configured at the developer level.
See [Images]([[= developer_doc =]]/guide/images/) for a technical guide on how to do this.

### Tables

![Table options in online editor](img/online_editor_table.png)

In table options you can define the first row and/or column as headers,
add or delete rows and columns in any part of the table, as well as merge and split cells.

### Custom elements

You installation can also have custom elements available in the Rich Text field.
Contact your site administrator about the details of using them.

### Text formatting

When you select a section of text, you get access to text formatting options such as bold or underline.
Here you can also add a link to the text. You can link to an external website, or to another Content item.

## Previewing content

While editing, you can preview what the content will look like by clicking the **Preview** button in the menu.

A Content item can have different looks for different [SiteAccesses](translating_content.md#siteaccess).
You can select a SiteAccess to preview by using a dropdown in the preview screen.

## Publishing content

If you are ready to publish the Content item, in the menu, click **Publish**.
To save the Content item as a draft to finish editing it later, click **Save**.
You can do it even if some required fields are not filled in.
You can then navigate away from the Content item by clicking the **X** icon in the upper left corner, or the browser's **Back button**.
For more details, see [Publishing content](publishing/publishing.md).
