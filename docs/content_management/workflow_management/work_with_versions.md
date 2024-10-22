---
description: Perform various tasks on content item versions, as part of editorial workflow or when comparing edits from different users.
---

# Work with versions

In [[= product_name =]], content items can have one published [version](../content_versions.md), and several draft and archived versions.
You can perform various tasks on content item versions, either to advance them through the workflow or compare edits from different users.


## Edit drafts

If you're assigned to a draft version of a content item for [review](editorial_workflow.md), when you click the **Edit draft** icon in **My dashboard**, the **Review queue** table, you see the **Event(s)** timeline that lists all the transitions that this content has gone through.

![Events timeline](img/workflow_events_timeline.png)

If draft locking is supported, you also see a message that confirms that the draft is now locked to you.

![Draft assignment message](img/lock_message.png)

## Release locked drafts

If you're assigned to a draft version of a content item and have locked it for review, you can release the lock by closing the modal window, publishing the draft, or sending it to another reviewer.
You can also do it in **My dashboard**, the **Review queue** table, by clicking the **Unlock** icon.

If you're not assigned to the draft, depending on the permissions set for your role, in the **Review queue** table, you can either release the lock by clicking the **Unlock** icon, or request that the lock is released by the reviewer by clicking the **Request access** icon.

## Compare versions
You can compare two versions of the same content item.

To do it, [disable the Focus mode](../../getting_started/discover_ui.md#disable-focus-mode).
Then, in the content item details screen, go to the **Versions** tab and click the **Version Compare** icon: ![Version Compare Icon](img/version_compare_icon.png){.inline-image}.

From the drop-down menus at the top of the screen, select the two versions that you want to compare.

![Versions](img/versions.png "Versions drop-down list")

There are two options of the view:

- Split - default, side by side view
- Unified - single column view

![Version comparison in Unified view](img/unified_view.png "Version comparison in Unified view")

When you compare two versions, the system highlights the changes:

- yellow - content updated
- blue - content added
- red - content deleted

![Version comparison in Split view](img/split_view.png "Version comparison in Split view")

You can also compare media field types such as images.

![Image comparison](img/image_comparison.png "Image comparison")

!!! note

    Not all field types are available for comparison.
    You cannot preview the differences in the following field types:

    - Form
    - Landing page
    - User account
