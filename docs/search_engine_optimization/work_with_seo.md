---
description: Enable search engine optimization and increase content visibility by defining meta tags.
---

# Work with SEO

For the Search Engine Optimization (SEO) feature to help you optimize the searchability 
and visibility of your content, you must enable it first, and
then, define the contents of individual tags.

To do it, make sure you can [edit Content Types](../content_management/content_model.md#content_types).

## Enable SEO

1. Click **Content** to display content management options, and then **Content Types**.
2. Drill down the content group and click the edit icon next to the Content Type that you want to modify.
3. Go to the **SEO** section and switch the **Enable SEO for this content type** toggle.
4. Click **Save** to save your changes.

## Define Meta tags

When you edit the Content Type definition, in the **SEO** section, go to the 
**Meta tags** area, and provide values for the following meta tags:

- **Title**
- **Description**
- **Keywords** 
- **Canonical**

To learn more about the function of each of the tags, see [Meta tags](seo.md#meta-tags).

When you populate the SEO fields, you can create patterns by using a schema with 
attributes which correspond to identifiers of fields that make up the Content Type.
As a result, SEO tags are filled in at Content item generation phase with specific 
contents of such fields. For example, if you enter `<title>.<format> - <author>` 
as a value of the **Title** tag, the search engine will return 
`Silmarillion. Illustrated edition - J.R.R. Tolkien`.

![SEO tags](img/SEO_tags.png)`

You can also fine-tune the way your content is presented when linked from 
a social media platform by populating the social media-specific meta tags 
in the exact same way: 
fill in fields in the **OpenGraph** and **Twitter** sections with patterns 
to configure the Facebook and Twitter presentation respectively. 
<!--If you leave these fields blank, social media snippets are generated based on 
the definitions that you provided in the search engine meta tag fields.-->

## Preview meta tags of Content item

You can preview what the actual SEO tags for a specific Content item 
will look like when they are passed to a search engine or social media platform.

1. In Content Tree, navigate to the Content item.
2. On the Content item details screen, click the SEO tab.
3. Review the contents of the **resolved** fields.

![SEO tab in Content item details](img/SEO_tab.png)`

## Override meta tags of Content item

When you want a specific Content item to appear in search results differently than 
the other items of a specific Content Type, you can override the contents of SEO tags.
You might want, for example, to add a shout out to the title after the author of content 
receives a literary prize.

1. In Content Tree, navigate to the Content item, and click the **Edit** button.
2. Go to the **SEO** section and, in relevant fields, replace the patterns that 
originate from the Content Type definition. 

You can either use plain text or patterns, like in the case of Content Types. 