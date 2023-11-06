---
description: The Ibexa DXP content model relies on Content items that are based on predefined Content Types.
---

# Content model

At the heart of [[= product_name =]] is a repository that stores all content.
In [[= product_name =]] everything is a Content item — not just the actual pages displayed in the website,
but also all media (images, videos, etc.) and User accounts.

[[= product_name =]] lets you customize and adapt the content model depending on your needs and the type of website you create.

Depending on your organization, if you are an editor or a content creator,
it is possible that the content model for your installation has already been created by your administrator or content manager.
However, even a non-technical user can easily create or modify the content model through the editing interface.

## Content Types

A **Content Type** is comparable to a pattern or a template on which you base [Content items](content_items.md).
Whenever you create a new Content item, you must choose its Content Type.

The Content Type defines what Fields are available in the Content item.
A Content item may only contain the Fields that are defined in the Content Type.

[[= product_name =]] allows you to create, edit, and delete Content Types and their Fields.
A clean installation contains a few basic Content Types.

## Content items versus Content Types

A [Content item](content_items.md) is an instance of a particular Content Type, in other words, a single object created based on a Content Type template.

When a Content item is created, it inherits the Fields from its Content Type.
However, the values of the Fields (their "contents") are empty, and you need to fill them separately for each Content item.
The Fields in a Content Type are only definitions. This means that they describe what Fields of what kinds will be present in a Content item, but as a rule they do not provide these Fields' values.

As a consequence, all Content items of the same Content Type will share the same set of Fields, but their Field values will be different.

For example, you need to store book information.
You create a new Content Type called "Book" and add to it Fields such as Title, Author, Genre, ISBN, etc.
Next, based on this Content Type, you can create any number of Content items.
The empty Fields will be ready to be filled in with the information about each specific book:

![Content model diagram](img/content_model_diagram.png "Content model diagram")

## Fields and Field Types

A Field Type defines what kind of data is stored in a Field.
For example, a Field with a TextLine Field Type stores a single line of text, an Image Field Type stores an image file,
and Author Field Type holds information about author details (like name and email).
By default, the system comes with a large set of Field Types that cover the most common needs,
e.g. Text line, Rich text, Email, Author list, Content relation, Map location, Float, etc.

## Content model in summary

**Content Types:**

- A Content Type defines Fields that a Content item will be composed of.
- Every Field is modeled after a Field Type which defines the kind of data it contains.

**Content Items:**

- A Content item consists of a number of Fields.
- Every Content item is based on a Content Type.

**Fields and Field Types:**

- [[= product_name =]] comes with a collection of essential Field Types.
- It is possible to extend the system by creating custom Field Types for special needs.

!!! note "More information"

    For detailed information about the content model, see [the developer documentation]([[= developer_doc =]]/content_management/content_model/#content-information).
