# Content Model

At the heart of eZ Platform is a repository that stores all Content.
In eZ Platform everything is Content: not just the actual pages that are displayed in the website,
but also all media (images, videos, etc.) and User accounts.

eZ Platform lets you customize and adapt the content model depending on the type of website you create and your needs.

Depending on your organization, if you are an editor or a content creator,
it is possible that the content model for your installation has already been created by your administrator or content manager.
However, even a non-technical user can easily create or modify the Content Model through the editing interface.

## Content Types

A **Content Type** can be compared to a pattern or a template on which you base Content items.
Whenever you create a new Content item, you must choose its Content Type.

The Content Type defines what Fields will be available in the Content item.
A Content item may only contain the Fields that are defined in the Content Type.

eZ Platform allows you to create, edit and delete Content Types and their Fields.
A clean installation contains a few basic Content Types.

To see what a larger set of Content Types and their Fields looks like in practice, you can take a look at the Demo Bundle.
[Demo is a separate installation with a sample website](https://github.com/ezsystems/ezplatform-demo) in which you can preview different features of eZ Platform.

## Content items

A **Content item** is a single piece of content: an article, a blog post, an image, a product, etc.
Each Content item has general characteristics such as name and identifier. It also contains **Fields**.
These Fields will differ depending on what kind of Content you are dealing with.
An *article* Content item may have Fields such as *title*, *name*, *author*, *body*, *image*, *subscriber teaser*, etc.
A *product* Content item may have *product name*, *category*, *price*, *size*, *color*, etc. as Fields.

## Content items versus Content Types

A Content item is an instance of a particular Content Type, in other words a single object created based on a Content Type template.

When a Content item is created, it inherits the Fields from its Content Type.
However, the values of the Fields (their "contents") are empty and you need to fill them separately for each Content item.
The Fields in a Content Type are only definitions. This means that they describe what Fields of what kinds will be present in a Content item,
but as a rule they do not provide these Fields' values.

As a consequence, all Content items of the same Content Type will share the same set of Fields, but their Field values will be different.

For example, you need to store book information.
You create a new Content Type called "Book" and give it Fields such as Title, Author, Genre, ISBN, etc.
Next, based on this Content Type, you can create any number of Content items.
The empty Fields will be ready to be filled in with the information about each specific book:

![Content model diagram](img/content_model_diagram.png "Content model diagram")

## Fields and Field Types

A Field Type defines what kind of data is stored in a Field.
For example, a Field with a TextLine Field Type stores a single line of text, an Image Field Type stores an image file,
and Author Field Type holds information about author details (like name, email).
By default, the system comes with a large set of Field Types that cover most common needs
(e.g. Text line, Rich text, Email, Author list, Content relation, Map location, Float, etc.)

## Content model in summary

**Content Types:**

- A Content Type defines Fields that a Content item will be composed of.
- Every Field is modeled after a Field Type which defines the kind of data it contains.

**Content Items:**

- A Content item consists of a number of Fields.
- Every Content item is based on a Content Type.

**Fields and Field Types:**

- eZ Platform comes with a collection of essential Field Types.
- It is possible to extend the system by creating custom Field Types for special needs.

## Content and media

When you are in the Back Office, you can view the content in your repository in three places:

- Content structure
- Media library
- User list

They represent three categories of Content Types that you can create
(see [Content Types](organizing_the_site.md#content-types)).

### Content tree and the Content browser

If you want to get an overview of the content currently in your website, go to the Content tab
and select **Content structure** or **Media**.
A **Browse** option on the left enables you to browse through all the content of the respective category.
User accounts, which are also considered content in eZ Platform, you can view through the Admin Panel
(see [Users](organizing_the_site.md#users)).

![Content browser in the menu](img/left_menu.png "Content browser in the menu")

During your work with eZ Platform you will often be asked to select content from the repository.
This happens for example when you want to move or copy, a Content item, embed an image, link two Content items, etc.
In such cases you will make use of the **Content Browser**.

The Content Browser enables you to navigate through all content in the site, including regular content, media and User accounts.
You can also use it to search the repository for content, and to create new content when needed.

![Universal Discovery Widget](img/udw.png "Universal Discovery Widget")
