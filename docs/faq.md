# FAQ: Frequently Asked Questions about eZ Products

## General Questions

### Product

**What is the difference between [[= product_name_oss =]] and [[= product_name_ee =]]?**

[[= product_name_oss =]] is open-source. [[= product_name_ee =]] bases on [[= product_name_oss =]], but features new functionalities.

**Which parts of eZ are open source and which are commercial?**

[[= product_name_oss =]] is fully open-source and available at [GitHub](https://github.com/ezsystems/ezplatform).

[[= product_name_ee =]] is a commercial solution.

**What technologies do I need to know to use eZ?**

If you are using eZ as an editor or content manager, you do not need to have any programming knowledge.

Installing and configuring eZ requires at least basic familiarity with web development. Some more advanced customization possibilities may require programming skills (such as knowledge of PHP or Twig).

**What are the technical requirements for installing eZ?**

See [requirements](https://doc.ezplatform.com/en/latest/getting_started/requirements_and_system_configuration/) for the configuration required for installing eZ.

**How do I install eZ?**

See [installation](https://doc.ezplatform.com/en/latest/getting_started/install_ez_platform/) for a guide on how to install eZ products.

### Editing

**In what modes can I work with my content?**

eZ offers two different work modes: **Content mode** and **Page mode**.

**What is Content mode?**

Content mode gives you the access to the content repository. It is mostly the role of [[= product_name_oss =]], but for users of [[= product_name_ee =]] it is enriched with specific Studio functionalities.

Its focus is on creating, modifying, organizing, and publishing Content items. Content mode is an interface for the repository, a place in which eZ stores all the content.

This mode lets you navigate the Content tree and edit any content present in it, as well as to move, copy, and delete it. You can also create new content using the previously defined Content Types.

You can preview any Content within the tree, but the Content mode does not allow you to edit a Content item directly from this preview.

**What is Page mode?**

Page mode allows you to manage website pages and website content from the pages themselves. It is only available for [[= product_name_ee =]] users. It can be enriched by eZ Services functionalities for users subscribed to them.

It provides the front-end editing, that is modifying pages directly from their preview. Using a special Timeline toolbar, you can also preview and modify the content of a page at a future date.

The Page mode offers a special functionality of creating a Page - a special kind of Content with advanced customization options.

### Administration

**How do I grant and restrict access to my website?**

You can restrict access to your website per User or User group. Each User (or group) can be assigned Roles and Policies which define the operations they can perform on the website.
You can assign them globally or only to parts of the website by applying [Sections](site_organization/organizing_the_content.md#sections).

See [Permissions](site_organization/organizing_the_site.md#permissions) for more information.

**What are Policies?**

Policies are basic elements of the permissions system. They are rules defining access to one functionality of one module (for example modifying articles), with possible further limitations.

See [Permissions](site_organization/organizing_the_site.md#permissions) for more information.

**What are Roles?**

Roles are an element of the permissions system. They are collections of Policies assigned to a particular user Role (for example a sports section editor).

See [Permissions](site_organization/organizing_the_site.md#permissions) for more information.

**How do I assign Roles and Policies to a User?**

You can do it in the **Admin Panel**, in the **Roles** tab.

See [Permissions](site_organization/organizing_the_site.md#permissions) for more information.

**What are Sections used for?**

Sections can be used to divide your content tree into separate parts, allowing you to limit the access to its parts for selected Users or User groups.

See [Sections](site_organization/organizing_the_content.md#sections) for more information.

**How can I use Sections to control access to my website?**

You can divide your Content tree into sections in the **Admin Panel**. See [Sections](site_organization/organizing_the_content.md#sections).

Then you can create Policies applicable to only this Section.

**Can I have different language versions of one Content item?**

Yes, every Content item can have multiple language versions. See [Languages](creating_content_advanced.md#languages) for more information.

**What is a SiteAccess?**

It is a collection of configuration settings provided when accessing a website. A single site can have multiple SiteAccesses which define the content and design of the page that will be displayed. This functionality can be used for example to create separate versions of the website for visitors and for administrators, or for different language versions.

See [SiteAccess](https://doc.ezplatform.com/en/master/guide/siteaccess/) for more technical information.

**How can I customize the look of my website?**

You can control the look of your website with great precision by creating and applying Twig templates. You can also create custom layouts for Pages.

See [Design](https://doc.ezplatform.com/en/master/guide/design_engine/) for more technical information.

### Support

**Where is the technical documentation?**

Technical documentation for [[= product_name_oss =]] and [[= product_name_ee =]] is available in [eZ Developer documentation](https://doc.ezplatform.com).

You can find the technical documentation for eZ Publish 5.x (an earlier version) in [eZ Publish 5.x Developer Documentation](https://doc.ez.no/display/EZP/eZ+Publish+5.x+Developer+Documentation).

**Where can I find more information about eZ?**

To find more information about the company and products, go to [ez.no](http://ez.no/).

**Where can I ask for help?**

If you need more questions answered, have a look at our [Support and Maintenance](http://ez.no/Services/Support-Maintenance) services.

If you would like to share your questions or ideas with other eZ users, you can do it on:

- [[[= product_name_oss =]] portal](https://ezplatform.com/).
- [eZ Community Slack channel](http://ez-community-on-slack.herokuapp.com/) where you can discuss the software and ask for help or support.

**How can I contact eZ representatives?**

If you would like to contact eZ or any of our offices, you can find the [contact information here](http://ez.no/About-eZ/Contact-Us).

## [[= product_name_oss =]]

### Product

**Where can I get [[= product_name_oss =]]?**

You can download the current version of [[= product_name_oss =]] from: <https://ezplatform.com>.

**How do I install [[= product_name_oss =]]?**

Here is a [guide to installing eZ products](https://doc.ezplatform.com/en/latest/getting_started/install_ez_platform/) (covering both [[= product_name_oss =]] and [[= product_name_ee =]]).

### Content model

**What does eZ understand by "Content"?**

In the broad sense, content is everything that is placed on a website for the visitors to see.

In the narrow sense, a Content item is a single object used on a website. It can be, for example, an article, a photo gallery or a blog post. Technically, a Content item is an instance of a Content Type (that is, it is a single object created on the basis of a "blueprint" which is the Content Type).

**What are Content Types?**

Content Types can be treated as templates or blueprints for Content items.
They define Fields and their Field Types which are then assigned values when a Content item is created on the basis of a particular Content Type.

Content Types are conceptually similar to classes in object-oriented programming.

**What Content Types do I have available?**

A small set of ready-to-use Content Types is provided with the Demo Bundle.

**Can I modify Content Types?**

Yes, you can adjust to your needs any Content Type provided in the Demo Bundle. See [Content Types](site_organization/organizing_the_site.md#content-types) for more information.

**Can I make my own Content Types?**

Yes, you can freely create any new Content Type. See [Content Types](site_organization/organizing_the_site.md#content-types) for more information.

**What are Field Types?**

Field Types define type of data which can be stored in a Field. Field Types which make up Content are defined in the Content Type.

Field Type is conceptually similar to a data type in programming. However, the available Field Types include both simple data types (for example integer or float numbers) and more complex structures (for example image, media file, or binary file).

**Can I make my own Field Types?**

Yes, you can create custom Field Types. However, this is not available from the **Admin Panel** (like creating Content Types). Instead, they have to be created using PHP.

### Editing

**How do I create new content?**

You can create a new Content item in the Content mode by clicking **Create**. See [Creating content](creating_content_basic.md) for more information.

**What is the Location of a Content item and how is it determined?**

A Content item in itself does not have a place in the Content tree and is not visible for a visitor of the website. To take its place on the website, it has to be assigned a Location ID.

A single Content item can have more than one Location ID, that is, it will be shown in more than one place in the Content tree. A single Location, however, can only have one Content item in it.

When you create a new Content item, it will automatically be given a Location ID and placed as a child of the Content item you were viewing when you clicked **Create**.

**How can I hide and unhide content?**

You can limit the visibility of a Content item by hiding the Location it is placed in. Hiding a Location also hides all other Locations that are under it in the content tree.

**How can I preview content?**

In Content mode you cannot edit Content while previewing it (this option is available only in [[= product_name_ee =]]).

You can preview your content while editing it by clicking one of the icons under **Preview** in the action bar.

**What is the difference between saving and publishing content?**

The **Save** or **Save draft** button (depending on whether you are in a Page Builder, or creating any other Content item)
enables you to save the current working copy as a draft to potentially reuse it later.
You can do it even if some required fields are not filled in.
The new version will not be published and, consequently, will not be visible as published content
on the website or through the API.

The **Publish** function allows you to publish the final version of the content object. As a result, the working copy turns into the published version that is visible on the website and available through the API as a publish content.

## [[= product_name_ee =]]

### Product

**Does [[= product_name_ee =]] contain all features of [[= product_name_oss =]]?**

Yes, [[= product_name_ee =]] is based on [[= product_name_oss =]] and contains it with all of its functionalities.

**What features does [[= product_name_ee =]] offer that are unavailable in [[= product_name_oss =]]?**

[[= product_name_ee =]] offers a number of additional features aside from what is available in [[= product_name_oss =]].

The key of them are:

- Easy creation of Pages
- Intuitive Page mode editing
- Workflow functionality for managing the review process

**How do I install [[= product_name_ee =]]?**

Here is a [guide to installing eZ products](https://doc.ezplatform.com/en/latest/getting_started/install_ez_platform/) (covering both [[= product_name_oss =]] and [[= product_name_ee =]]).

### Editing

**How does a Page differ from a regular Content item?**

A Page is a special kind of a Content item. It is a page designed to be the visitor's entry point into your website.

A Page has a customizable layout with multiple zones where you can place predefined blocks with dynamic content.

**How do I create a Page?**

You can create a new Page in the Page mode by clicking **Create**. See [working with a Page](site_organization/working_with_page.md) for more information.

**What blocks can I add to a Page?**

Here is the list of predefined Page blocks.

You also have the possibility of [creating your own, custom blocks](https://doc.ezplatform.com/en/master/guide/extending_page/#creating-custom-page-blocks).

**How can I have my Content reviewed by other users?**

You can use the Workflow functionality to send your Content to review. You can access it from the Action bar in Content mode. See [Editorial workflow](publishing/editorial_workflow.md) for more information.
