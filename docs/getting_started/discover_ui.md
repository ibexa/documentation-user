---
description: Take a quick tour of the back office.
---

# User interface

## Top bar

At the top of the main screen you can see a top bar.

![Top bar](img/top_bar_all.png "Top bar")

Depending on your location within the back office, it can contain the following important features:

A\. Logo in the left corner, which is a direct link to the [dashboard](#dashboard)

B\. "Focus mode" badge which informs you that the [focus mode](#focus-mode) is on

C\. Global search field that allows you to [find content](../search/search_for_content.md) by checking all searchable fields

D\. Drop-down that changes the site context

![Top bar with site context selector](img/top_bar.png "Top bar with site context selector")

E\. Notification icon that informs you about incoming assignments, for example, items assigned for [your review](../content_management/workflow_management/editorial_workflow.md#review-queue)

F\. App switcher which includes links to official websites of the QNTM group ecosystem companies, world-class ad-tech and mar-tech solution providers

![App switcher](img/app_switcher.png "App switcher")

G\. User avatar with a drop-down menu with access to [user profile and settings](get_started.md#view-and-edit-user-profile)

!!! note "Site context"

    Changing the site context results in the [content tree](#content-tree) showing content items that belong to the selected website.
    The appearance of content items can also change if they use different designs or languages depending on the [SiteAccess](../website_organization/multisite.md#siteaccess) settings.

## Dashboard

The first screen that you see after logging in is [Dashboard](dashboard.md).
It's the default dashboard and contains selected blocks.

![Dashboard](dashboard.png "Dashboard")

You can customize the dashboard by changing the blocks and the layout.
For more information, see [Work with dashboard](work_with_dashboard.md).

## Main menu

The main menu allows you to move between important sections of the application.

![Main menu](img/side_menu.png "Main menu")

You can adjust the size of the menu sidebar.
To do this, click on the side edge of the panel, then drag and adjust to the desired size.
You can also hide it by clicking the button in the down right corner.

![Main menu - adjust](img/menu_adjust.png "Adjust main menu or hide it")

Depending on the product edition and your [permissions](../permission_management/permission_system.md), the main menu may include, for example:

- **Content**, which gives you access to the content repository.
It lets you navigate the content tree, and, for example, create, edit, move, copy, or delete content.
- [[% include 'snippets/experience_badge.md' %]] [[% include 'snippets/commerce_badge.md' %]] **Site management**, which enables you to create and edit block-based Pages and manage multiple websites.
- **PIM**, which enables you to handle products presented on the website, including their specifications and pricing.
- **Admin**, which is the administration panel where you can manage, for example, Users, Sections, or permissions.

## Content tree

If you want to navigate through your website with a menu, in the main menu, go to the **Content** -> **Content structure**.
The **Content Tree** area is an expandable content menu of your website.

![Content tree in the menu](img/left_menu_tree.png "Content tree in the menu")

Unique icons for each content type instantly show you what type of content you're selecting.
To add custom icons to your content tree, follow [configuration tutorial in Developer Documentation]([[= developer_doc =]]/administration/back_office/back_office_elements/custom_icons/#customize-content-type-icons).

Hidden content is greyed out in the tree view.

To simplify the content tree, big lists are collapsed and include a **Show more** icon.
You can select it to expand the branches of the tree.
**Collapse all** option, which is available in the context menu, closes all expanded sections.

For more information on custom configuration, go to [Content tree]([[= developer_doc =]]/administration/back_office/content_tree/) in Developer Documentation.

## Content browser

During your work with [[= product_name =]] you might need to select content from the repository.
This happens, for example, when you want to move or copy a content item, embed an image, or link two content items.
In such cases, you use the **Content Browser**.

To access the **Content Browser**, go to the **Content** tab and select **Content structure** or **Media**.
Then, select a file you want to copy or move and click the corresponding button in the top right corner.
The Content Browser window opens, and you can select the new destination of the selected file or its copy.

![Content Browser](img/udw.png "Content Browser")

With the **Content Browser**, you can switch between the Grid, Panels and Tree views to navigate through the content of the website.
Depending on your permissions, you might be able to see the regular content, media, forms, site skeletons, and user accounts.
You can also use the **Content Browser** to search the repository for content, edit content, create bookmarks, and create new content when needed.

!!! note

    If you have administrator permissions, you can also view and manage user accounts and site skeletons in the **Admin** tab.

    For more information about users and permissions, see [Users](../permission_management/permissions_and_users.md).

    For more information about site skeletons, see [Site skeletons]([[= developer_doc =]]/multisite/site_factory/site_factory_configuration/#site-skeletons).

## Focus mode

Focus mode helps editors focus on information that is only relevant to their line of work and omit technical details that would distract.
It's enabled by default, after you log in.
If you need access to certain settings or technical details, you can [disable the focus mode](#disable-focus-mode) at any time.

- **Dark theme for content tree**
: In areas where the content tree is displayed, for example, in **Content structure**, the tree is displayed on a dark background.

![Dark theme for content tree](img/FM_dark_content_tree.png "Dark theme for content tree")

- **Content item view**
: If you select a specific [SiteAccess](translate_content.md#siteaccess) from the **Site context** drop-down list on the right side of the top bar and then browse content items in content tree, they're displayed in full view, with a limited set of actions available.
To display the content item details view with more actions, click **Exit full view**.

![Content item in full view](img/FM_content_item_full_view.png "Content item in full view")

!!! tip

    Even when you're out of the full view or not in Focus mode, you can still preview the content item in the **View** tab.

- **Different details view tabs**
: In Focus mode, the tabs in content item's detail view are different than the ones visible when it's disabled.
Additionally, they're displayed in different order to expose the ones that are more important from the editor's perspective.

![Content item tabs in Focus mode](img/FM_less_ci_tabs.png "Content item tabs in Focus mode")

- **Different columns available for selection**
: You can decide which columns are displayed in the **Sub-items** table, to adjust the view to your use case.
The list of columns available for selection is limited in Focus mode.

![Columns in Sub-items table](img/FM_subitems_column_list.png "Columns in Sub-items table")

### Disable Focus mode

Focus mode is enabled by default when you first log into [[= product_name =]], but you can toggle it in two places:

- in user settings

![Focus mode user setting](img/FM_user_settings.png "Focus mode user setting")

- in the drop-down menu on the right side of the top bar

![Focus mode switch](img/FM_switch.png "Focus mode switch")
