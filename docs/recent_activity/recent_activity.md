---
description: Monitor recent activity logged actions.
---

# Recent activity log [[% include 'snippets/experience_badge.md' %]] [[% include 'snippets/commerce_badge.md' %]]

## Activity list

In the Back Office, **Admin** -> **Activity list**, you can see a list of recent activity of all or selected users.

!!! note

    To see the **Admin** menu, you need the **Setup / Administrate** [permission](permission_system.md).
    To see the Activity list, you need the **Activity Log / Read** permission (this permission can be limited to allow seeing your own activity only).

By default, the following actions are displayed:

- [Content](content_items.md) create, create draft, publish, update, trash, recover, delete, delete translation, hide, and reveal
- [Location](manage_locations_urls.md#content-locations) create, delete, hide, reveal, update, move, swap, and subtree copy
- [Product](products.md) create, update, and delete
- [Product variant](work_with_product_variants.md) create, update, and delete
- [Site](work_with_sites.md) create, update, and delete

By default, log entries are kept 30 days.

Log entries are grouped by logical bonds like web requests, events, batches, or sessions.

![Activity list](img/4.6_activity_list.png)

!!! note

    With some development, some other actions could be logged, see [custom log entry developer documentation]([[= developer_doc =]]/administration/recent_activity/recent_activity/#adding-custom-activity-log-entries)

    The log entries' life time can be shorten or extended through configuration, see [configuration developer documentation]([[= developer_doc =]]/administration/recent_activity/recent_activity/#configuration-and-cronjob)

### Filter activities

You can filter the activities to:

* follow the activity of selected users or user group,
* narrow the results to selected item types, or actions.

To do it, on the right side, in the **Filters** menu, choose selected filters, and click the **Apply** button.
Click the **Clear** button to reset all the filters.

The following example shows, how to narrow the results by selecting **Action** and **Time** filters.
With these settings, activity list displays only `Publish` actions from `Last week` time period.

![Published last week](img/filters.png)

## Recent activity dashboard block [[% include 'snippets/experience_badge.md' %]] [[% include 'snippets/commerce_badge.md' %]]

You can add a **Recent activity** block to your [dashboard](discover_ui.md#dashboard).
To be able to customize a dashboard, you need the **Dashboard / Customize** permission.
To be able to see the content of this block, you need the **Activity Log / Read** permission.

!["Recent activity" block](img/recent_activity_block.png)

You can set the block to display only activities of selected users, or concerning particular object classes.

For example, the following dashboard block focuses on Content and Location activity.

!["Content recent activity" block settings](img/recent_activity_block_settings.png)

## User profile

User profile displays recent activity of the user.
To be able to see recent activity log, you need the **Activity Log / Read** permission.

![Recent activity in the user profile](img/recent_activity_user_profile.png)
