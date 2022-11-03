---
description: Copy, move, remove, or hide Content item, either individually or in bulk.
---

# Copy, move or hide content

## Move or copy

You can move or copy existing Content items by choosing the proper option from the menu on the right.
You can also copy the whole subtree (a Content item with all content under it in the structure).

!!! note

    Copying very large subtrees may take too much time and server effort. That is why the system administrator
    may set a limit on how many Content items can be copied at the same time.

    See [Copy subtree limit]([[= developer_doc =]]/administration/back_office/back_office_configuration/#copy-subtree-limit)
    in the developer documentation on how to set this up.

Copying creates a new Content item.
If you only want to have the same Content item to another place in the Content tree, add another Location to it.

### Multi-file move

To move multiple items, select them and click **Move selected items** from the **Sub-items** top bar.
Then choose a Location from the **Choose Location** modal that opens up.
After choosing and confirming new Location, all selected files are moved to it.

![Multi-file move](img/multi_file_move.png)

## Remove content

You can remove content by clicking **Send to Trash** in the menu.
If you remove a Content item that has children (other content under it in the content tree),
both this item and the children will be removed. This also breaks the connection between the items,
so you will not be able to restore them with the same structure.

Notice that the Content item is not removed completely.
It is moved to Trash, which you can access from the left menu.
In the Trash, you can search for Content items and sort your search results based on different criteria. You can then select removed Content items and restore them to their original Locations or to new Locations you choose.
If the Content item's parent has been removed, you need to select a new parent Location.

![Warning before emptying the trash](img/empty_trash_warning.png "Warning before emptying the Trash")

If a Content item has more than one Location, selecting **Send to Trash** will remove the Content item only from the current Location.
The content will appear in Trash only once you have removed the last Location.

You can permanently remove a Content item by checking it and clicking the trash icon.
You can also permanently remove all content from the Trash by clicking **Empty Trash**.

!!! caution "Warning"

    Emptying the Trash cannot be undone!

## Multi-file delete

To delete multiple items, select them and click **Delete selected items** in the **Sub-items** top bar. Confirm your choice in the pop-up window with the **Send to Trash** button. All selected files will be moved to trash.

![Multi-file delete](img/multi_file_delete.png)

### Hide content

You can hide a Content item by clicking **Hide** in the menu.

![Hide content icon](img/hide_content_icon.png)

When you click **Hide**, you can choose to **Hide later**
and select and date and time when the Content item will be hidden:

![Schedule hiding panel](img/schedule_hiding.png)

A hidden Content item is unavailable for anyone on the front page. It is also grayed out in the Content Tree.

This is different from [hiding Locations](manage_locations_urls.md#hide-locations), because it affects the Content item
in all of its Locations.
