---
description: Fine-tune the access control by using the permission system.
---

# Permission system

An overview of the permission system in [[= product_name =]] is best presented by using an example.

### Example permission system

Let us assume you are managing a newspaper website. Your crew consists of an editor-in-chief
and several editors responsible for particular sections of the paper: general news, local news, sports, etc.
You also have contributors who occasionally add new articles.
You want to give the editor-in-chief access to most parts of your website,
but the individual editors will only work with their own sections.
To the contributors you want to give the permissions to create new content, but not to modify or delete the existing content.

In order to have this setup, you need to create a number of different Roles: Editor-in-Chief, different Editor(s), and Contributor.

Even if you plan on having only one editor-in-chief, it is good practice to create a User group to contain this user,
and assign a Role to it instead of assigning permissions directly to the user.

To each of these Roles you need to assign proper Policies, giving them the right to perform certain actions.

The Editor-in-Chief Role would have the most Policies (although you may want to reserve some more advanced permissions only for system administrators).
Regular Editors need Policies allowing them to create, modify, and delete content.
Contributors can be given Policies permitting them to only create content.

If you want to prohibit Editors from accessing content in newspaper sections other than their own, you can add Limitations to their Policies.
This means that instead of one Editor, you need to have separate Roles for each editor profile:
Local Editor, Sports Editor, etc. All of these Roles will have the same Policies,
but to each Policy you need to assign a Limitation which would mean that the permission covers only one Section
(Sports Section, Local News Section etc.) that the editor works in.

Aside from Policies that define access to Content items, there are also many other Policy types concerned with administrating the system.
They cover actions such as activating new Users, creating Sections, modifying Content Types, etc.
