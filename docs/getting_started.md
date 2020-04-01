# Getting started

eZ Platform is an open-source, Symfony-based CMS.

eZ Platform consists of the technical platform for developers
(including a Web framework, APIs and a Content Repository)
and provides a user interface to work with the content and administer the platform.

!!! enterprise "eZ Platform Enterprise Edition"

    eZ Platform Enterprise Edition is a commercial product built on top of the open-source eZ Platform.
    It offers additional functionalities and enhancements to the editing experience.

    eZ Enterprise provides advanced editorial capabilities such as [in-page editing](working_with_page.md), creation of [block-based Pages](working_with_page.md#adding-blocks), [editorial workflow](publishing/editorial_workflow.md), etc.

## Quick start

eZ Platform must be [installed by administrator](https://doc.ezplatform.com/en/latest/getting_started/install_ez_platform/).
They should provide you with the address of the installation.

To access the Back Office (the editor interface), add `/admin` to this address.
For example, if your website's URL is `www.my-site.com`, you enter the editing interface through `www.my-site.com/admin`.

**The default administrator account information is:**

- username: `admin`
- password:` publish`

![Login screen](img/login_form.png "Login screen")

The first screen after logging in is the Dashboard. It contains shortcuts to most commonly used content:
review queue, your drafts, the content you have created, recently modified content, etc.
You can select any of these items and view them in detail or start editing them from this point.
You can also reschedule or cancel planned publications using the Dashboard.

![Dashboard](img/dashboard.png "Dashboard")

You can always return to the Dashboard by selecting the logo in the upper left corner.

The top bar allows you to move between important sections of the application.

![Top bar](img/top_bar.png "Top bar")

- **Content** gives you access to the content Repository.
It lets you navigate the Content Tree, create, edit, move, copy, delete content, etc.
- **Site** enables you to create and edit block-based Pages and manage multiple sites. It is only available for eZ Enterprise users.
- **Forms** enables you to place a survey, questionnaire, sign-up form, etc. on your website. It is only available for eZ Enterprise users.
- **Admin** is the administration panel where you can manage Users, Sections, permissions, etc.

### User settings

You can access your User Settings on the right side of the top bar:

![User preferences menu](img/user_preferences.png)

Here you can change your user password and define your user preferences,
such as preferred timezone, date and time format, or Back Office language.
