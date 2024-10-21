---
description: Use Site Factory to easily create multiple websites, with different designs and subsets of content, based on common skeletons.
edition: experience
---

# Work with websites

If multisite support is enabled for your instance of [[= product_name =]], you can use Site Factory to create and manage multiple websites from one place.
These websites can, for example, be in different languages, or customized for different audiences, and still be kept in the repository of your installation.
To be able to use it, the Site Factory has to be enabled and configured by the administrator.
For more information, see Developer Documentation on [Site Factory]([[= developer_doc =]]/multisite/site_factory/site_factory).

## Create a website

To access Site Factory, in the left panel, click the **Site Management** icon and then **Sites**.
If Site Factory is enabled, and you have sufficient permissions, you should see the **Create** button.
Click it to access the **Creating New Site** modal.

![Site Factory icon](img/site_factory_icon.png)

Here, you can create an entirely new website or a different language version of an already existing website.
First, select a name, a predefined design, and a Parent location for your website.

![Create a new website step one](img/site_factory_new_site_step_1.png)

If the design defines a Site skeleton, you can choose if you want to copy the entire content structure of the design with a toggle.
To preview the Site skeleton architecture, click **Site management**, and then **Site skeletons**.

Next, you can decide if the website goes live after creation or is offline with the Status switcher.
In this section you also define the SiteAccess URL addresses with their main languages, fallback languages, and optional paths for the website.

!!! note "Path limitation"

    The path can be only one directory deep.
    Do not use paths that have more than one element, for example, `/en/articles`.

For more information about SiteAccesses, see [Multisite]([[= developer_doc =]]/multisite/multisite/).

![Create a new website step two](img/site_factory_new_site_step_2.png)

If all required fields are filled out you can select **Create**, and the website is be added to the website list in the **Site management** area.

!!! note

    A SiteAccess that you create in Site Factory is always treated with lower priority than a SiteAccess defined by the administrator as part of [configuration]([[= developer_doc =]]/multisite/multisite_configuration/#siteaccess-configuration).
    For example, if you create a website that uses the `fr` path in Site Factory, and the administrator defines a French website manually in configuration files, your website is ignored by the system.

## Edit an existing website

To edit the website select **Site settings** icon that is situated next to the website name.
Here, you can edit all the elements you selected during creation of the website:

- name
- design
- visibility
- URL
- language

## Delete an existing website

To enable deleting a website you have to change the website status to offline.
Live websites cannot be deleted. Next, select the **Delete** icon and confirm your choice.

![Site list](img/site_factory_site_list.png)
