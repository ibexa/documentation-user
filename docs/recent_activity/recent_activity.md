---
description: Monitor recent activity logged actions.
---

# Recent activity log

## Activity list

On the Back Office, in **Admin** -> **Activity list**, you can consult what actions were taken by users recently.

!!! note

    - To see the Admin menu, you must have the "Setup / Administrate" [permission](permission_system.md).
    - To see the Activity list, you must have the "Activity Log / Read" permission (this permission might be limitated to only see your own activity).

By default, the following actions are logged:

- [Content](content_items.md) [create](create_edit_content_items.md#create-content-items), [publish](publish_instantly.md#publish-content-instantly), update, trash, recover, [delete](copy_move_hide_content.md#multi-file-move), delete translation, hide and reveal
- Location create, delete, [hide](manage_locations_urls.md#hide-locations), reveal, update, move, [swap](manage_locations_urls.md#swap-locations) and subtree copy
- Product [create](create_edit_product.md), update and delete
- Product variant [create](work_with_product_variants.md#generate-variants), update and [delete](work_with_product_variants.md#delete-variants)
- [Site](work_with_sites.md) [create](work_with_sites.md#create-a-website), [update](work_with_sites.md#edit-an-existing-website) and [delete](work_with_sites.md#delete-an-existing-website)

By default, log entries are kept 30 days.

Log entries are grouped by logical bonds like web requests, events, batches, or sessions.

![Activity list](img/4.6_activity_list.png)

### Filter activities

On the right, a "Filters" block offers:

* to only follow the activity of a user or a list of users,
* to narrow the display to groups having given types of items, or actions.

Select what you want to focus on and click the "Apply" button. Stop filtering by clicking the "Clear" button.

The following setting example lists activity log groups containing a "publish" entry, and occurring withing a week from today.

![Published last week](img/filters.png)

## Dashboard block

You can add a "Recent activity" block to your [dashboard](discover_ui.md#dashboard) (if you have the right permission).

!["Recent activity" block](img/recent_activity_block.png)

You can set the block to display only log groups containing activities by some particular users, or concerning particular object classes.

For example, the following dashboard block focuses on Content and Location activity.

!["Content recent activity" block settings](img/recent_activity_block_settings.png)

## User profile

A user profile displays recent activity from this user
(only if current user has permission to see own or other user activity log).

!["Recent activity" in user profile](img/recent_activity_user_profile.png)
