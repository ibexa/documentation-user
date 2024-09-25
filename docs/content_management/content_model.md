---
description: The Ibexa DXP content model relies on content items that are based on predefined content types.
---

# Content model

At the heart of [[= product_name =]] is a repository that stores all content.
In [[= product_name =]] everything is a content item — not just the actual pages displayed in the website,
but also all media (images, videos, etc.) and user accounts.

[[= product_name =]] lets you customize and adapt the content model depending on your needs and the type of website you create.

Depending on your organization, if you are an editor or a content creator,
it is possible that the content model for your installation has already been created by your administrator or content manager.
However, even a non-technical user can easily create or modify the content model through the editing interface.

## Content types

A **content type** is comparable to a pattern or a template on which you base [content items](content_items.md).
Whenever you create a new content item, you must choose its content type.

The content type defines what Fields are available in the content item.
A content item may only contain the Fields that are defined in the content type.

[[= product_name =]] allows you to create, edit, and delete content types and their Fields.
A clean installation contains a few basic content types.

## Content items versus content types

A [content item](content_items.md) is an instance of a particular content type, in other words, a single object created based on a content type template.

When a content item is created, it inherits the Fields from its content type.
However, the values of the Fields (their "contents") are empty, and you need to fill them separately for each content item.
The Fields in a content type are only definitions. This means that they describe what Fields of what kinds will be present in a content item, but as a rule they do not provide these Fields' values.

As a consequence, all content items of the same content type will share the same set of Fields, but their Field values will be different.

For example, you need to store book information.
You create a new content type called "Book" and add to it Fields such as Title, Author, Genre, ISBN, etc.
Next, based on this content type, you can create any number of content items.
The empty Fields will be ready to be filled in with the information about each specific book:

![Content model diagram](img/content_model_diagram.png "Content model diagram")

## Fields and Field Types

A Field Type defines what kind of data is stored in a Field.
For example, a Field with a TextLine Field Type stores a single line of text, an Image Field Type stores an image file,
and Author Field Type holds information about author details (like name and email).
By default, the system comes with a large set of Field Types that cover the most common needs,
e.g. Text line, Rich text, Email, Author list, Content relation, Map location, Float, etc.

## Content model in summary

**content types:**

- A content type defines Fields that a content item will be composed of.
- Every Field is modeled after a Field Type which defines the kind of data it contains.

**Content items:**

- A content item consists of a number of Fields.
- Every content item is based on a content type.

**Fields and Field Types:**

- [[= product_name =]] comes with a collection of essential Field Types.
- It is possible to extend the system by creating custom Field Types for special needs.

!!! note "More information"

    For detailed information about the content model, see [the developer documentation]([[= developer_doc =]]/content_management/content_model/#content-information).
