---
description: Learn about Content item versions and the Autosave feature.
---

# Content versions

## Types of content versions

In [[= product_name =]], Content items can have more than one version.
Versions can be of published, archived, or draft type.

The **published version** is the version that is currently presented to the audience.
Every Content item can have only one published version at a time.

Whenever you edit and publish a Content item again, its previous published version becomes an **archived version**.
It is not available to the visitor and you cannot edit it, but you can create new drafts based on any archived version.

Finally, **drafts** are versions that have not been published yet.
There can be many drafts of the same Content item.
They can be created by the autosave feature, by the reviewer as part of the 
[editorial workflow](workflow_management/editorial_workflow.md), or when you save
the work and close the Content item editing screen.

You can view all versions of a Content item on the Content item details screen.
To do it, [turn the Focus mode off](../getting_started/discover_ui.md#disable-focus-mode), and go to this Content item's **Versions** tab.

![All versions of a Content item](img/content_item_versions.png "All versions of a Content item")

For more information, see [Editorial workflow](workflow_management/editorial_workflow.md) and [Work with versions](work_with_versions.md).

### Autosave

While you edit a Content item or product, [[= product_name =]] saves your work automatically to help you preserve the progress in an event of a failure.
To recover your work, [turn the Focus mode off](../getting_started/discover_ui.md#disable-focus-mode), go to this Content item's **Versions** tab, and open the most recent draft.
Alternatively, open the most recent draft of your work on the **My dashboard** page, the **Drafts** table.

Autosave is enabled by default, and set to save a draft every 60 seconds.
You can toggle autosave or change the time between saving attempts in **User settings**, by changing
the values in the **Autosave draft** and **Autosave interval** fields.
