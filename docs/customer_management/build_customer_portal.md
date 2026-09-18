---
description: Use Page Builder to create and edit a Customer Portal.
---

# Create and edit Customer Portal

To create and edit a Customer Portal with Page Builder, you need to first set it up in configuration.

The Customer Portal creation and edition are based on Page Builder and work on the same principles.
If you're unfamiliar with how Page Builder works, see [Create and edit Pages](create_edit_pages.md).

## Create Customer Portal

To create a new Customer Portal, go to **Content** and from the menu select **Content structure**.
There, navigate to the root folder for your Customer Portals.
If you don't have one, you can add it yourself.

Inside a root folder you can select **Create content** from the right-side toolbar.
On the list of content items, you can see two possibilities: **Customer Portal** and **Customer Portal Page**.

![Create content tab](img/cp_portal_vs_page.png)

The first one is a container for your Customer Portal pages (this is not a root folder), and the second one represents the actual page.
It's recommended to use Customer Portal containers to divide and store your portal pages.
If your project requires it, the Customer Portal containers can also be defined as root folders in the configuration.

First, select **Customer Portal** and name it appropriately.
Next, navigate to the newly added container and create **Customer Portal Page**.

![Customer Portal container](img/cp_folder_for_portals.png)

In the **Page creation** box, you should see the Customer Portal layout where you can add dedicated Customer Portal block, Sales Representative, or choose from selection of blocks available to your [[= product_name =]] version.

For a list of blocks available out of the box, see [Block reference](block_reference.md).

![Page Builder view](img/cp_page_builder.png)

If provided ready-to-use Page blocks aren't sufficient, your integration partner can add custom blocks.

Before you publish or save the Customer Portal page, edit its title and description in the field view, you can find it in the top toolbar on the left side.

If you're ready to publish the Customer Portal page, click **Publish** in the top right corner.
You can also save it as a draft, even if some required fields aren't filled in.
To do it, click **Save draft**.

## Add multiple pages

You can have multiple Customer Portal pages available in one Customer Portal by adding them under one Customer Portal container.
If company members have sufficient `content/read` policies and have the portal assigned to their customer group, they can see the changes in the left menu.

![Multiple pages in one portal](img/cp_multiple_pages.png)

You can manipulate the order of pages in a menu by assigning priority to them in the **Customer Portal** container under **View**->**Sub-items**.

![Assigning page priority](img/cp_page_priority.png)

## Grant permissions

Company members need to have the following permissions to be able to see custom Customer Portals:

- `user/login` to `custom_portal` SiteAccess
- `content/read` to selected Customer Portals

![Customer Portal permissions](img/cp_permissions.png)

If members of the company don't have sufficient permissions for any Customer Portal, they're transferred to the default Customer Portal view.

!!! note

    Customer Portal is only available to users that are members of the company.
    Even if a user has all sufficient permissions but is not a member of a company, they cannot see the Customer Portal.

Customer Portal must also be assigned to the company's Customer Group.
