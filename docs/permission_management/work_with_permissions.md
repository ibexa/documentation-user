---
description: Modify role settings to control access to different areas of the application.
---

# Work with permissions

You can view and modify all [permissions](permission_system.md) by clicking **Roles** in the **Admin Panel**.

## Create a new role

1. Go to **Admin** -> **Roles** and click **Create**.
1. Provide a name and click **Save and close** to see a list of policies that the role has.
1. Click **+ Add**, select a policy from the list and click **Save and close**.

You then may have an option to add limitations to the policy.
The available limitations depend on the chosen policy.
You can then return to a list of policies by clicking **Save and close** or **Discard**.

![Details of a role](img/role_details.png "Details of a role")

## Assign a role to users

1. Go to **Admin** -> **Roles** and select a role.
1. Go to the **Assignments** tab and click **Assign to Users/Groups**.
1. Choose users and/or groups to be assigned to this role.
1. In the **Limitatons** area, select additional limitations if necessary.
1. To discard your changes and close the window, click **Discard**.
1. To save your changes, click **Save and close**.

![Users assigned to role](img/users_assigned.png "Users assigned to role")

!!! note

    A user or user group may be assigned multiple roles.

For a list of available permissions and limitations, see [Permissions]([[= developer_doc =]]/permissions/permissions/).
