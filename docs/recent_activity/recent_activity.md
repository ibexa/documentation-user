---
description: Monitor recent activity logged actions.
edition: experience
---

# Recent activity log

[[= product_name =]] logs various operations on the repository and in the application.

If you have **Setup / Administrate** and **Activity Log / Read** [permissions](permission_system.md), you can review the most recent activity log in  the back office, **Admin** -> **Recent activity**.

![Recent activity](recent_activity.png "Recent activity")

By default, actions on the following items are displayed:

- [Content](content_items.md)
- [Location](manage_locations_urls.md#content-locations)
- [Product](products.md)
- [Product variant](work_with_product_variants.md)
- [Site](work_with_sites.md)

!!! note

    If your implementation requires that other actions are logged, see [custom log entry Developer Documentation]([[= developer_doc =]]/administration/recent_activity/recent_activity/#add-custom-activity-log-entries).

    By default, log entries are kept for 30 days.
    This time can be modified through configuration.
    For more information, see [Developer Documentation]([[= developer_doc =]]/administration/recent_activity/recent_activity/#configuration-and-cronjob).

Log entries are grouped by date, then by logical bond (like web request, or migration file).

Each activity log entry shows:

- when the action was performed,
- who performed it (avatar, first name, last name),
- the action itself as a verb,
- and the item the action was performed on.

Depending on the system configuration, activity logs may also be shown:

- on the dashboard with the [Recent activity block](dashboard_block_reference.md#recent-activity-block)
- within the [user profile](get_started.md#view-and-edit-user-profile)

## Filter activities

You can filter the activities to:

* follow the activity of selected users or user group,
* narrow the results to selected item types, or actions.

To do it, on the right side, in the **Filters** menu, choose selected filters, and click the **Apply** button.
Click the **Clear** button to reset all the filters.

The following example shows, how to narrow the results by selecting **Action** and **Time** filters.
With these settings, activity list displays only `Publish` actions from `Last week` time period.

![Published last week](recent_activity_filters.png "Published last week filter set")

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(51.27314814814815% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/IAJrEyQUizSxnei6kSis?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Recent activity" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
