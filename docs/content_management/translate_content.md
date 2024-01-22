---
description: Create multiple language versions of Content items.
---

# Translate content

The content on your website can be translated into different languages. Each Content item can have different language versions.
The version visible to a visitor depends on the way your installation is set up (see [SiteAccess concept](#edit-page-for-different-language-versions-of-a-website)).

## Add website languages

You can only add translations in languages that have been set up for your website in the **Admin Panel**.
If your user [Role](work_with_permissions.md) has the right permissions, you can create a new language for the website.
To do it, go to the **Admin Panel**, open the **Languages** tab, and click **Add language**.

Every new language must have a name and a language code written in the xxx-XX format, for example, eng-US, fre-FR, nor-NO, etc.
After adding a language, you may have to reload the application to be able to use it.

!!! caution

    Depending on the way the website is set up, additional configuration may be necessary
    for the new translations to be displayed properly.
    Contact your administrator and inform them that you need to add a new language to the website
    (see [the technical documentation on language versions]([[= developer_doc =]]/multisite/languages/languages/)).

## Add translations

1\. In the left panel, go to **Content** -> **Content structure**. Then select a Content item.

2\. Go to **Translations** tab and click **+ Add**.

3\. Select the source and target languages and click **Create**.

All the Fields are then pre-filled with the values they have in the base translation.
If you do not choose a base translation, the Fields remain empty.

While working, you can save your work and continue or click **Delete draft** to discard your changes.
When done, you can save your work and close the window, publish the translated article immediately, or pick another publication date.

Every time you add or edit a translation, a new version of the Content item is created,
the same way as when editing only one language.

![Adding a new translation](img/adding_translation.png "Adding a new translation")

## Translation comparison

You can compare different versions of the translations of the Content item.

1. [Turn the Focus mode off](../getting_started/discover_ui.md#disable-focus-mode).

1. In the left panel, go to **Content** -> **Content structure**. Then select a Content item.

1. Go to **Versions** tab and click the **Version compare** icon: ![Version Compare Icon](img/version_compare_icon.png){.inline-image}.

1. In the **Comparing versions** screen, pick the split view by using the switcher in the top right corner:

![View switcher](img/view_switcher.png "View switcher")

1. From the dropdowns, select two different language versions of the same Content item.
The screen refreshes to display the side by side view of its Fields.

![Compare translations screen](img/compare_translations.png "Compare translations screen")

For more information, see [Work with versions](work_with_versions.md#compare-versions).

## Edit Page for different language versions of a website [[% include 'snippets/experience_badge.md' %]] [[% include 'snippets/commerce_badge.md' %]]

When you edit a Page, a bar at the top of the screen lists the most recently used [SiteAccesses](https://doc.ibexa.co/projects/userguide/en/master/website_organization/multisite/#siteaccess) on your website. Use this bar to switch between the different versions and work on them.

<a name="siteaccess"></a>

!!! note "SiteAccess concept"

    SiteAccesses are a means to present different versions of the website to different 
    categories of users.
    You could treat SiteAccesses as different "entrance points" to your website. 
    They allow you to show different content or design to visitors, for example, 
    to serve different language versions to visitors from different countries.
    
    See [Work with websites](../website_organization/work_with_sites.md) for more information about setting up websites.