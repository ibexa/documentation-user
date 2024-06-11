---
description: Learn about content item versions and the Autosave feature.
---

# Content versions

## Types of content versions

In [[= product_name =]], content items can have more than one version.
Versions can be of published, archived, or draft type.

You can view all versions of a content item on the content item details screen.
To do it, [disable the Focus mode](../getting_started/discover_ui.md#disable-focus-mode), and go to this content item's **Versions** tab.

![All versions of a content item](img/content_item_versions.png "All versions of a content item")

### Published version

Published version is the version that is currently presented to the visitors.
Every content item can have only one published version at a time.

### Archived versions

Whenever you edit and publish a content item again, its previous published version becomes an archived version.
It is not available to the visitors and you cannot edit it, but you can create new drafts based on any archived version.

### Drafts

Drafts are versions that have not been published yet.
There can be many drafts of the same content item.
Drafts can be created in many ways, including:

- by the [autosave](#autosave) feature
- by reviewers, as part of the [editorial workflow](workflow_management/editorial_workflow.md)
- by editors, when they save a content item while editing it or close a content item's editing screen after making changes, but without publishing them

#### Draft conflicts

Drafts of the same content item that originate from different sources can contain conflicting changes.
Such draft conflicts can be resolved by using the [Version Compare](work_with_versions.md#compare-versions) feature.

For more information about various operations on content versions, see [Work with versions](work_with_versions.md).

## Autosave

While you edit a content item or product, [[= product_name =]] automatically saves your work as a new draft to help you preserve the progress in an event of a failure.
To recover your work, [disable the Focus mode](../getting_started/discover_ui.md#disable-focus-mode), go to this content item's **Versions** tab, and open the most recent draft.
Alternatively, open the most recent draft of your work on the **Dashboard** page, **My content** area.

Autosave is enabled by default, and set to save a draft every 60 seconds.
You can toggle autosave and/or change the time between saving attempts.
To do this, in the upper-right corner of the screen, click your avatar icon, and then click **User settings**, **Preferences**.
In the **Content authoring** section, change the values of the **Autosave draft every given period** and **Seconds till next draft autosave** fields.
