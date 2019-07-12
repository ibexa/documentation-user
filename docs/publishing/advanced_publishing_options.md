# Advanced publishing options

!!! enterprise

    There are three ways in which you can schedule content to be published in the future:

    - [Schedule tab](#schedule-tab) in any Page block's configuration
    - [Content Scheduler block](#content-scheduler-block) on a Page
    - [Publish later option](#date-based-publishing) when editing content

    ## Schedule tab

    The Schedule tab is available in the configuration of all Page blocks.
    You can use it to set the date and time when the block becomes visible and when it disappears from a Page.

    ![Schedule tab](img/schedule_tab.png)

    ## Content Scheduler block

    In the Content Scheduler block you can select Content items to be displayed at a selected time.

    For each Content item you can choose an airtime - a date and time in the future.
    At this time the Content item will become visible.

    The Content Scheduler block has a limit of Content items.
    If the limit is filled and a new Content item is displayed, the oldest item will disappear from the block.

    ![Content Scheduler](img/content_scheduler.png)

    ## Date-based publishing

    When editing a Content item, select **Publish Later** in the menu on the right.

    ![Publish Later button in the menu](img/publish_later.png "Publish Later button in the menu")

    You will see a **Future publication setting** window. Choose a date and time and the content will be published at that time.

    If you had planned a future publication date and enter the edit mode of the same Content item,
    you also have a new option in the menu: **Discard publish later**.
    Use it to remove the previously selected publication date.

    ![Discard Publish Date button in the menu](img/discard_publish_date.png "Discard Publish Date button in the menu")
    
    You can also view, [reschedule and cancel](#rescheduling-or-cancelling-events) future publications in the [calendar widget](#calendar-widget).

    ## Timeline

    The timeline in Page mode shows all changes that will happen to the Page in the future.

    You can use the slider to preview what the Page will look like at a given time.
    Use the button on the right of the time to see a list of all upcoming changes.

    ![List of upcoming events in the timeline](img/timeline_list.png)
    
    ## Calendar widget
    
    The calendar widget enables you to view and perform actions on various events.
    Out of the box, it displays Content items scheduled for future publication, but your page administator can configure custom events.
    Therefore, it can contain other events, e.g. national holidays, important dates, etc.
    
    To access the calendar widget, in the **Content Panel**, open the **Calendar** tab.
    
    ![Calendar widget](img/calendar_widget.png "Calendar widget")
    
    You can switch between different views and access filters.
    
    |Button|Description|
    |------|-----------|
    |![Today button](img/calendar_widget_today.png)|Display the current day regardless of the view.|
    |![Arrows](img/calendar_widget_arrows.png)|Navigate through months, weeks, or days.|
    |![Toggle month/week/day](img/calendar_widget_toggler_mwd.png)|Switch between the month, week, or day view.|
    |![Toggle calendar/list](img/calendar_widget_toggler_cal_list.png)|Switch between the calendar and list view,|
    |![Filters](img/calendar_widget_filters.png)|Access and apply calendar filters.|
    
    ### Calendar filters
        
    With numerous events appearing in the calendar widget, you can declutter the view by applying filters.
    You can filter by the events' type or modified language in all three — month, week, and day — views.
        
    Access all available filters by clicking the **Filters** button.
         
    ![Viewing filters](img/calendar_widget_apply_filters.png "Viewing calendar filters")
        
    To apply filters, select or deselect entities from the **Types** or **Modified language** list.
    The calendar view refreshes automatically.
    
    ### Calendar toolbar
    
    The calendar widget toolbar displays events you select and gives you access to actions assigned to them.
    The available actions appear in the upper-right corner of the toolbar when you select an event.
    You can select multiple events of the same type and perform bulk actions on them, e.g. [reschedule or cancel publication](#rescheduling-or-cancelling-events).
    
    !!! note
            
        Actions available in the toolbar may vary depending on the custom configuration.
        For details, contact your page administrator.
                
    
    To select, click on all events you want to add to the toolbar list.
    
    ![Calendar widget toolbar](img/selection_action_bar.png "Calendar widget toolbar")
    
    #### Rescheduling or cancelling events
    
    In case of publishable events (e.g. articles), you can change or cancel their planned publication by using the toolbar buttons.
    
    |Button|Description|
    |------|-----------|
    |![Reschedule button](img/selection_action_bar_reschedule.png)|Reschedule all selected events.|
    |![Discard button](img/selection_action_bar_discard.png)|Cancel the future publication of selected events.|
    
    Select all events to perform a bulk action on them.
    Using the toolbar buttons, perform one of the following actions:
    
    - To change the publication time, click the **Reschedule** button.
    In the **Reschedule** content modal window, select the new date and click **Confirm reschedule**.
    - To cancel event's publication, click the **Unschedule** button.
    In the modal window, confirm the cancellation by clicking **Discard scheduling**.