---
description: Get started with Ibexa DXP by logging in to the Back Office.
---

# Get started

[[= product_name =]] consists of the technical platform for creating and managing 
online experiences, designed for developers and end-users alike.
It includes a Web framework, APIs and a Content Repository.
It features a customizable user interface where you can work with the content, 
products, media, as well as manage other functionalities and administer the platform.

Depending on the product edition, [[= product_name =]] can provide advanced capabilities in such areas as:

- content editing: [editing and creating pages](../content_management/create_edit_pages.md), [editorial workflow](../content_management/workflow_management/editorial_workflow.md), etc.
- product management: [managing catalogs](../pim/work_with_catalogs.md), [managing product categories](../pim/work_with_product_categories.md)
- customer data management: [managing customers](../customer_management/manage_customers.md), etc.

!!! note "Installation"

    [[= product_name =]] must be [installed by the administrators]([[= developer_doc =]]/getting_started/install_ibexa_dxp/).
    They should provide you with the address of the installation.

## Access the Back Office

To access the Back Office (or the user/editor interface), add `/admin` to the address provided by the administrator.
For example, if your website's URL is `www.my-site.com`, you enter the editing interface through `www.my-site.com/admin`.

If you are the administrator, the default administrator account information is:

- username: `admin`
- password:` publish`

Otherwise, to login, you must get your user credentials from the administrator and enter them on the login screen.

![Login screen](img/login_form.png "Login screen")

### View and edit user profile

If you are an editor, depending on the system configuration, you may be able to view and edit the user profile, which can contain the following information:

- Avatar image
- First and last name
- Email
- Department
- Position
- Location
- Signature
- Roles the user is assigned to
- Recent activity

!!! note

    For the [recent activity](recent_activity.md) log to be displayed, your [user role](../permission_management/permissions_and_users.md) must have the **Activity Log / Read** permission.

![User profile](img/user_profile_preview.png "User profile")

To access your user profile, in the upper-right corner of the screen, click your avatar icon.
Then, from the drop-down menu, select **Profile**.

To edit your user profile, in the **User profile** screen, in the **Summary** section, click **Edit**.

You can now modify the following entries:

- Avatar image
- First and last name
- Signature
- Department

!!! note

    The fields may differ depending on your system configuration.

To edit your avatar, in the **Image** area, click **Upload file** or drag and drop your photo.
If necessary, you can [edit the photo with the Image Editor](edit_images.md).
After you finish, the avatar is uploaded and is visible in the Back Office.

![Edit avatar](img/user_profile_avatar.png "Edit avatar")

!!! note

    If you don't set your own image, a default avatar with your initials is displayed.

To save changes to the user profile, click **Update**.

### User settings

You can access your user settings on the right side of the top bar:

![User preferences menu](img/user_preferences.png)

Here you can [change your user password](get_started.md#change-the-password) and define your user preferences,
such as preferred timezone, short and full date and time format, or Back Office language.

**Location**

|Setting|Description|
--------|-----------|
|Default currency|Sets the default currency used in the Back Office.|
|Toggle In-Context translation feature|Enables or disables integration with Crowdin to navigate the interface while translating.|
|User Time Zone|Sets time zone in the Back Office.|
|Short date and time format|Sets short date and time format used in the Back Office.|
|Full date and time format|Sets full date and time format used in the Back Office.|
|Language|Sets the default language used in the Back Office.|


**Content authoring**

|Setting|Description|
--------|-----------|
|[Autosave draft every given period](../content_management/content_versions.md/#autosave)|Enables or disables autosaving drafts.|
|Seconds till next draft autosave|Sets time period for next autosave.|
|Enable character count in Online Editor|Enables or disables charactes count.|
|Automatically open block settings in builders|Enables or disables the behavior of blocks used in builders.|

**Browsing**

|Setting|Description|
--------|-----------|
|Number of items displayed in the table|Sets the number of items displayed in sub-items.|
|Location preview|Enables or disabled a thumbnail preview on the Content Tree.|

**Mode**

|Setting|Description|
--------|-----------|
|Focus mode|Enables or disables the [focus mode](discover_ui.md#focus-mode).|

**Dashboard**

|Setting|Description|
--------|-----------|
|Active dashboard|Sets which dashboard is displayed after you log in.|

### Change the password

You can change your user password at any time.
To do it, first, access your user profile, and go to **Account settings** tab.
Then, click **Change password**.

![Change password](img/change_password.png "Change password")

Fill out all the required fields and click **Save and close** to save changes.
Click **Discard** to remove your changes and return to the previous screen.

![Editing password](img/editing_password.png "Editing password")