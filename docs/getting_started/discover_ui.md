---
description: Take a quick tour of the Back Office.
---

# User interface

## My dashboard

The first screen that you see after logging in is **My dashboard**.
It is default dashboard and contains blocks:

- **Recent activity** - contains the list of last activities (maximum 10), including timestamp, user data and activity type. 
Available filters are: User(s), Activity type (create, update, publish, delete, hide , show) and Activity area (product, content).

- **Quick actions** - displays most popular/used actions and shortcuts, for example, **Create content**. 

- **Ibexa news** - contains the list of recent blog posts or articles published at `ibexa.co` blog.  
It includes title, image, timestamp, and link to article details. List can containt minimum 1 and maximum 10 links.

- **Review queue**

- **My content**

- **Common content**

You can select any of these items and view them in detail or start [editing them](create_edit_content_items.md) from this point.
You can also [reschedule or cancel planned publications](../content_management/schedule_publishing.md#reschedule_or_cancel_publications) using the dashboard.

![My dashboard](img/dashboard.png "My dashboard")

You can always return to the **My dashboard** screen by clicking the logo in the upper left corner.

## Customizable dashboard

You can customize the dashboard depending on your needs.

Customized dashboard previews a set of widgets selected by user.

It provides quick overview of these areas, that are commonly used, excluding those that are not used or used rarely.
This solution improves productivity, allows to enhance the default dashboard with additional widgets, and helps to make better business decisions based on data.

By easily accessing important information, users can work more efficiently with a clear view of tasks and deadlines.

Customization includes also choosing one of predefined layouts and adding custom ones to use them in dashboards.

### Customize dashboard

To customize dashboard, on the main page, click **Go to dashboard builder**. 
This action opens an online editor - Dashboard builder.

#### Dashboard builder interface

Dashboard builder user interface consists of:

A. Drop zone

B. Page blocks / Structure view toolbar

C. Buttons:

|![Editing dashboard](page_builder_toolbar_editpreview.png)|Edit basic information, like Title and Description.|
|![Switch layout](page_builder_toolbar_devicestoggler.png)|Switch layout for the dashboard.|
|![Elements menu](page_builder_toolbarelements.png)|Move Page blocks / Structure view to the other side of the screen.|
|![Undo](page_builder_toolbar_undo.png)|Undo latest change.|
|![Redo](page_builder_toolbar_redo.png)|Redo latest change.|

Dashboard builder has two main views that you can use while creating a page:

- Page blocks toolbar - consists of all available blocks that you can use by dragging them and dropping on a drop zone.

![Page blocks](img/page_blocks_toolbar.png)

- Structure view - shows a structure of your dashboard, including their division into zones and the blocks that they contain.

![Structure view](img/structure_view.png)

### Choose layout

For new dashboard you can choose layout which defines the available zones.

Applying a layout divides the dashboard into the defined zones. The zones are placeholders for page blocks.

To choose layout, click **Swicth layout** button in the left side of the upper toolbar. 

![Switch layout](img/switch_layout_window.png)

Choose one of the available layouts and click **Save**.

#### Add blocks

In Dashboard builder you can access a menu of **Page blocks** — a set of blocks of content that you can add to the zones of the Dashboard.

You can choose from available blocks from the categories below:

1\. General:

- Recent activity
- Quick actions
- Ibexa news

2\. Content:

- My content
- Review queue
- Common content

3\. Product [[% include 'snippets/experience_badge.md' %]]:

- Products by category
- 	Products with the lowest stock

4.\ Commerce [[% include 'snippets/commerce_badge.md' %]]:

- Recent orders
- Orders by status

5\. Personalization:

- Top clicked items

6\. Others:

- Permissions
- Default role with Dashboard permissions
- PHP API Dashboard service

Add a block by dragging it from the menu to an empty place on a zone.
Do not worry about placing blocks in the proper place from the start.
You can reorder them at any time by dragging and dropping them in the desired location.
You can reorder blocks in a few ways:

- drag and drop block in the desired location on a drop zone
- select block and use up and down arrow on the keyboard
- access Structure view and use 'Move up' and 'Move down' function in the settings of the block

When you add a new block to the drop zone, drop it in the blue highlighted area. Before you drop it, a bold line appears  - it helps you see the position of the newly added block in relation to other, already added blocks.

![Drop zone line](drop_zone_line.png)

When you add a block by dragging it from Page blocks menu into the drop zone,
the block settings panel open immediately where you can configure all block properties.

![Block properties](block_properties.png)

This is a default behavior. You can globally turn off automatic opening of the block settings panel in the user settings.
First, access your user settings on the right side of the top bar:

![Elements menu](img/user_settings.png "User settings")

Then, go to **My preferences** tab, **Edit** section.
Here, you can find `Automatically open block settings in builder` setting, which, by default, is set up to `enabled` value.
To change this behavior, click on **Edit** icon, find the setting, and change its value to `disabled`.

![Elements menu](img/user_settings_blocks.png "User settings - blocks settings")

#### Work with blocks

Each kind of block has its special properties.
You can access them by placing the cursor on the added block and clicking the **Block settings** icon.

## Menu

The left side menu allows you to move between important sections of the application.

![Side menu](img/top_bar.png "Side menu")

Depending on the product edition and your [permissions](../permission_management/permission_system.md), the top level sections on the leftmost pane may include, for example:

- **Content**, which gives you access to the content Repository.
It lets you navigate the Content Tree, create, edit, move, copy, delete content, etc.
- [[% include 'snippets/experience_badge.md' %]] [[% include 'snippets/commerce_badge.md' %]] **Site**, which enables you to create and edit block-based Pages and manage multiple websites.
- **PIM**, which enables you to handle products presented on the website, including their specifications and pricing.
- **Admin**, which is the administration panel where you can manage Users, Sections, permissions, etc.

## Content Tree

If you want to navigate through your website with a menu, go to the **Content** tab, and select **Content structure**.
**Content Tree** in the left sidebar opens an expandable content menu of your website.

![Content Tree in the menu](img/left_menu_tree.png "Content Tree in the menu")

Unique icons for each Content Type instantly show you what type of content you are selecting. To add custom icons to your Content Tree, follow [configuration tutorial in developer documentation.]([[= developer_doc =]]/administration/back_office/back_office_elements/custom_icons/#customize-content-type-icons)

Hidden content is greyed out in the tree view.

To simplify the Content Tree, big lists are collapsed and include a **Show more** icon. 
You can select it to expand the branches of the tree.
Available from the context menu, the **Collapse all** option that closes all expanded sections.

For more information on custom configuration, go to [Content Tree]([[= developer_doc =]]/administration/back_office/content_tree/) in developer documentation.

## Content browser

During your work with [[= product_name =]] you might need to select content from the Repository.
This happens, for example, when you want to move or copy a Content item, embed an image, link two Content items, etc.
In such cases, you use the **Content Browser**.

To access the **Content Browser**, go to the **Content** tab and select **Content structure** or **Media**.
Then, select a file you want to copy or move and click the corresponding button in the top right corner.
The Content Browser window opens, and you can select the new location of the selected file or its copy.

![Content Browser](img/udw.png "Content Browser")

With the **Content Browser**, you can switch between the Grid, Panels and Tree views to navigate through the content of the website.
Depending on your permissions, you might be able to see the regular content, media, forms, site skeletons and User accounts.
You can also use the **Content Browser** to search the Repository for content, edit content, create bookmarks, and create new content when needed.

!!! note

    If you have administrator permissions, you can also view and manage User accounts and site skeletons in the **Admin** tab.
    
    For more information about users and permissions, see [Users](../permission_management/permissions_and_users.md).
    
    For more information about site skeletons, see [Site skeletons]([[= developer_doc =]]/multisite/site_factory/site_factory_configuration/#site-skeletons).
