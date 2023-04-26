---
description: Use Page Builder to create and edit Customer Portal.
edition: experience
---

# Create and edit Customer Portal

To create and edit Customer Portal with Page Builder, you need to set it up in configuration.
For detailed instructions on how to do it, go to
[Create Customer Portal]([[= developer_doc =]]/customer_management/cp_page_builder/) in Developer Documentation.

The Customer Portal creation and edition are based on Page Builder feature and work on the same principles.
If you are unfamiliar with how Page Builder works follow [Create and edit Pages](create_edit_pages.md).

## Create Customer Portal

To create a new Customer Portal, go to **Content** and from the list select **Content structure**.
There, you should navigate to the root folder for your Customer Portals. 
If you don't have one, you can add it yourself.
Remember to specify its `location_id` in the configuration, you will find it under **Details**.
For more information, see [Configure Page Builder access to Customer Portal.]([[= developer_doc =]]/customer_management/cp_page_builder/#configure-page-builder-access-to-customer-portal)

Inside a root folder you can select **Create content** from the right-side toolbar.
On the list of Content items, you will see two possibilities **Customer Portal** and **Customer Portal Page**.

![Create content tab](img/cp_portal_vs_page.png)

The first one is a container for your Customer Portal pages (this is not a root folder), and the second one represents the actual page.
We highly recommend that you use Customer Portal containers to divide and store your portal pages.

First, select **Customer Portal** and name it appropriately.
Next, navigate to a newly added container and create **Customer Portal Page**. 

![Customer Portal container](img/cp_folder_for_portals.png)

On the **Page creation** modal, you should see the Customer Portal layout where you can 
add dedicated Customer Portal block, Sales Representative, or choose from selection of blocks available to your [[= product_name =]] version.

For a list of blocks available out of the box, see [Block reference](block_reference.md).

![Page Builder view](img/cp_page_builder.png)

If provided ready-to-use Page blocks are not sufficient, you can [add your own blocks]([[= developer_doc =]]/content_management/pages/create_custom_page_block/).

Before you publish or save the Customer Portal page, edit its title and description in the Field view, you can find it in the top-left-side toolbar.

If you are ready to publish the Customer Portal page, click **Publish** in the top-right corner.
You can also save it as a draft, even if some required fields are not filled in, click **Save draft**.

## Add multiple pages

You can have multiple Customer Portal pages available in one Customer Portal by adding them under one Customer Portal container.
If company members have sufficient `content/read` policies and have the portal assigned to their Customer Group, they will see the changes in the left-side menu.

To be able to see the multipage display in the Page Builder, you also need to be a member of the company with sufficient permissions.

![Multiple pages in one portal](img/cp_multiple_pages.png)

You can manipulate the order of pages in a menu by assigning priority to them in the **Customer Portal** container under **View**->**Sub-items**.

![Assigning page priority](img/cp_page_priority.png)

## Grant permissions

Company members need to have below permissions to be able to see custom Customer Portals:

- `user/login` to `custom_portal` SiteAccess
- `content/read` to selected Customer Portals

![Customer Portal permissions](img/cp_permissions.png)

If members of the company don't have sufficient permissions for any Customer Portal, they will be transferred to the default Customer Portal view.

!!! note

    Customer Portal is only available to users that are members of the company. Even if user has all the sufficient permissions but is not a meber of a company, they will not see the Customer Portal.

Customer Portal must also be assigned to the company's Customer Group. To learn more see, [assigning portals to Customer Groups.]([[= developer_doc =]]/customer_management/cp_page_builder/#assigning-portal-to-customer-group)

