# Glossary

Entries in ***italics*** are legacy terms (terms used in earlier versions of eZ) included here for reference reasons.

## A

#### Access control

The mechanism of granting and prohibiting access to different parts of the website; see [Policy](#policy), [Role](#role), [Access function](#access-function), [User](#user), [User group](#user-group).

More information (User Guide): [Managing permissions](organizing_the_site.md#permissions).

More information (Developer documentation): [Permissions](https://doc.ezplatform.com/en/latest/guide/repository/#permissions).

#### Access function

The smallest element of the [permissions](#access-control) system: a single component of a [policy](#policy).

#### Action bar

A menu in the right pane of the [Content mode](#content-mode). It allows you to create, modify and manipulate Content.

#### *Attribute*

Legacy term for [Field Type](#field-type).

## B

#### Block

The basic segment of a [Landing Page](#landing-page). Blocks can be placed on a Landing Page using drag-and-drop and later customized.

More information (User Guide): [Working with a Landing Page](creating_content_basic.md#working-with-a-landing-page).

#### Bundle

A directory containing a set of files (PHP files, stylesheets, JavaScripts, images, etc.) that implement a single feature (for example a blog or a forum). This is a term used in [Symfony](#symfony), which distributes both its main framework and extensions or addins in the form of bundles.

## C

#### CLA

Contributor Licensing Agreement. An agreement which needs to be signed before contributing to the development of eZ.

#### CMS

Content Management System. This is the basic type of software that eZ offers.

#### CXM

Customer Experience Management. The whole of marketing and business activities, processes and tools connected with interaction between a company and its customers.

#### Cloud Services

A commercial component of eZ with options for gathering and using content intelligence, including capabilities such as recommendations or marketing automation.

Cloud Services is also available as a standalone solution.

#### Clustering

The way of setting up an installation to have several web servers running eZ.

More information (Developer documentation): [Clustering](https://doc.ezplatform.com/en/latest/guide/clustering/).

#### Community

The [Community Gateway](http://share.ez.no/) for eZ users. Also, the open-source version of the [previous generation](#ez-publish-community) of eZ products.

#### *Components*

A library of independent components for Web applications. In the current versions of eZ replaced by [Twig](#twig) templates and [Symfony](#symfony) [bundles](#bundle).

#### Composer

A PHP packaging system to manage dependencies. It is used in the installation and update mechanism of eZ. See <https://getcomposer.org/>.

More information (Developer documentation): [About Composer](https://doc.ezplatform.com/en/latest/getting_started/about_composer/).

#### Content items

**1.** In the broad sense, content items is everything that is placed on a site for the visitor to see.

**2.** (*sing*. a Content item, *Pl.* Content items) In the narrow sense, a Content item is a single object used on a site. It can be, for example, an article, a photo gallery or a blog post. Technically, a Content item is an instance of a [Content Type](#content-type) (that is, it is a single object created on the basis of a "blueprint" which is the Content Type).

Occasionally, the term "regular Content" is used to refer to any type of Content other than a[Landing Page](#landing-page).

More information (User Guide): [Under the hood, concepts and organization](under_the_hood.md).

#### *Content Class*

Legacy term for [Content Type](#content-type).

#### Content mode

The editing mode used in eZ Platform. The Content mode concentrates on creating, editing and managing Content items.

More information (User Guide): [Content mode interface](getting_started.md#work-modes).

#### Content state

The status of a Content item version. Each version can have the status of Draft (created but not published yet), Published or Archived (removed or replaced by a newer version).

See also [Content versioning](#content-versioning).

#### Content tree

The structure into which Content is organized in the system.

#### Content Type

A template or blueprint for [Content](#content-items). It defines [Fields](#field) and their [Field Types](#field-type) which are then assigned [Field Values](#field-value) when a Content item is created based on this Content Type.

Content Type is conceptually similar to a class in object-oriented programming.

More information (User Guide): [Content Types](under_the_hood.md#content-types).

#### Content versioning

A control mechanism for changes made to content. Whenever a piece of [Content](#content-items) is modified, its previous version is preserved with an Archived state. You can view an earlier version of Content and revert to it if you decide to undo the changes.

See also [Content state](#content-state).

#### CSS

Cascading Style Sheets used to create and apply styles to websites. Can be used in conjunction with [Twig](#twig).

## D

#### *Data Type*

Legacy term for [Field Type](#field-type).

#### Demo Bundle

A bundle containing a demonstration version of a website created using eZ. You can use it to familiarize yourself with the system, or to create your own website on its basis.

There is a separate Demo Bundle for eZ Platform and eZ Enterprise.

#### Discovery bar

A menu in the left pane of the [Content mode](#content-mode). It allows you to navigate the repository.

#### Dynamic page

One of the types of [Landing Page](#landing-page): a page with dynamically generated content.

## E

#### *Extension*

Legacy term for [Bundle](#bundle).

#### eZ Enterprise

The current commercial stack of eZ. It contains the open-source [eZ Platform](#ez-platform) component as well as [Studio](#studio).

#### eZ Platform

Open-source component of eZ.

#### eZ Publish Community

Open-source version of the previous edition of eZ.

#### eZ Publish Enterprise

Commercial version of the previous edition of eZ.

## F

#### Field

The smallest unit for storing data in the content structure. A [Content item](#content-items) can contain multiple Fields, each of them with a [Field Value](#field-value). The Field Value must correspond to the [Field Type](#field-type) as defined in the [Content Type](#content-type).

#### Field Type

The type of data which can be stored in a [Field](#field). Field Types which make up [Content](#content-items) are defined in the [Content Type](#content-type).

Field Type is conceptually similar to a data type in programming. However, the available Field Types include both simple data types (for example integer or float numbers) and more complex structures (for example image, media file or binary file).

More information (User Guide): [Field Types](under_the_hood.md#fields-and-field-types).

#### Field Value

The value which is assigned to a [Field](#field) when [Content](#content-items) is created based on a [Content Type](#content-type). The type of value is defined by the [Field Type](#field-type).

#### Flex workflow

A functionality for managing the Content review process. It allows you to ask other users to review your content and send the reviewers mail notifications.

More information (User Guide): [Review workflow](publishing.md#review-workflow).

## L

#### Landing Page

In online marketing, the part of the website that a customer is directed to first when reaching a webpage through a search engine or a marketing link.

In eZ terms, a special form of [Content](#content-items) . It allows you to organize the page using specially tailored blocks of content.

Landing Pages can be created in [Page mode](#page-mode).

More information (User Guide): [Working with a Landing Page](creating_content_basic.md#working-with-a-landing-page).

More information (Developer documentation): [Landing Page Field Type](https://doc.ezplatform.com/en/latest/guide/field_type_reference/#landing-page-field-type-enterprise).

#### Layout

The way in which a [Landing Page](#landing-page) is divided into [zones](#zone). Each zone can contain a number of [blocks](#block). See also [Dynamic page](#dynamic-page).

#### Legacy

General term for previous versions of eZ, from 3.x to 5.x.

#### Location

The place in which [Content](#content-items) is located in the content structure, indicated by a Location ID. A Content item can be assigned to more than one Location (have more than one Location ID), but a single Location ID can have only one Content item in it.

More information (User Guide): [Content Locations](organizing_the_content.md#content-locations).

## M

#### Marketing Automation

A part of [Cloud Services](#cloud-services) offering marketing automation capabilities: functionalities for generating and managing leads and sales management.

#### Media library

The place where all media (for example images, videos, etc.) are stored in the content structure. When choosing a piece of media to place in your content, you will use the [Universal Discovery Widget](#universal-discovery-widget).

#### Multisite setup

A configuration where one eZ installation serves multiple websites (for example, different versions of a company website for different international markets).

## N

#### *Node*

Legacy term for [Location](#location).

## O

#### Object-oriented content structure

The fundamental idea behind structuring content in eZ. Based on the concepts of object-oriented programming, this structure treats every Content item as an object, an instance of a predefined [Content Type](#content-type), with a number of [Fields](#field) reflecting its properties.

See [Content](#content-items), [Content Type](#content-type), [Field](#field), [Field Type](#field-type).

More information (User Guide): [Under the hood, concepts and organization](under_the_hood.md).

## P

#### Page mode

The editing mode available in [eZ Enterprise](#ez-enterprise). Allows you to plan, create and modify content live, while previewing the effects of the changes in real time.

#### Permissions

See [Policies](#policy), [Roles](#role).

#### Policy

The basic element of the permissions system: a rule defining access to one functionality of one module (for example modifying articles), with possible further limitations. Can be assigned to [users](#user) and [user groups](#user-group).

#### Public API

A PHP API which exposes a Repository, allowing you to create, read, update, manage and delete all objects available in eZ, both Content and related objects such as Sections, Locations, Content Types etc.

More information (Developer documentation): [Public API Guide](https://doc.ezplatform.com/en/latest/api/public_php_api/#public-api-guide).

## R

#### Recommendation

A part of [Cloud Services](#cloud-services) containing an engine for gathering customer information and presenting recommendations. Powered by [YOOCHOOSE!](https://yoochoose.com/).

#### Repository

Storage place for all content in an eZ installation. It can be interacted with using the public API.

Can also refer to a GitHub repository (eZ uses GitHub to [store and share its open-source code](https://github.com/ezsystems/ezplatform)).

#### REST API

An API which allows you to interact with an eZ installation using the HTTP protocol, following a [REST](http://en.wikipedia.org/wiki/Representational_state_transfer) interaction model.

#### Role

An element of the permissions system: a collection of [Policies](#policy) assigned to a particular user function (for example a sports section editor). Can be assigned to [Users](#user) and [User groups](#user-group).

## S

#### Section

A demarcated part of the [Content tree](#content-tree). Sections can be used to control permissions granted to users (for example, a "Sports Editors" group can be assigned Roles which only grant access to the "Sports" Section of website).

More information (User Guide): [Sections](organizing_the_content.md#sections).

#### Service life

Support and maintenance cycle of different versions of eZ. See <https://support.ez.no/Public/Service-Life> for detailed information.

#### Siteaccess

A collection of configuration settings provided when accessing a website. A single site can have multiple siteaccesses which define the content and design of the page that will be displayed. This functionality can be used for example to create separate versions of the website for visitors and for administrators.

More information (Developer documentation): [SiteAccess](https://doc.ezplatform.com/en/latest/guide/siteaccess/).

#### Smart Analytics

A part of [Cloud Services](#cloud-services) containing an engine for tracking and analyzing visitor behavior on the website.

#### Stash

An open-source technology used for caching. See <http://www.stashphp.com/index.html>.

More information (Developer documentation): [Persistence cache](https://doc.ezplatform.com/en/latest/guide/repository/#persistence-cache), [Persistence cache configuration](https://doc.ezplatform.com/en/latest/guide/repository/#persistence-cache-configuration).

#### Studio

Commercial component of eZ, together with [eZ Platform](#ez-platform) it constitutes [eZ Enterprise](#ez-enterprise).

#### Studio Toolbar

An action toolbar at the top of the screen in [Studio](#studio) which allows you to create, edit and view content.

#### Symfony

A PHP framework for web applications and a set of reusable PHP components. eZ has been using Symfony as its framework since eZ Publish 5.0. See <https://symfony.com/>.

## T

#### Template

An instrument for customizing the visual aspect of a website. A template is applied to the content and defines the layout, themes and other graphical features with which content will be displayed on the page. eZ uses [Twig](#twig) as its main template engine.

More information (Developer documentation): [Design](https://doc.ezplatform.com/en/latest/guide/design/), [Content Rendering](https://doc.ezplatform.com/en/latest/guide/content_rendering/).

#### Twig

A PHP [template](#template) engine used as the main template engine in current versions of eZ. See <http://twig.sensiolabs.org/> for more information.

## U

#### Universal Discovery Widget

A tool for browsing, searching and selecting content in the [Content tree](#content-tree) and [Media library](#media-library).

#### User

An account in which information about a user is contained in the system.

Technically, a User is a Content item of a special [Content Type](#content-type).

More information (User Guide): [Users](organizing_the_site.md#users).

#### User group

A collection of users grouped together for efficiency reasons. You can assign [policies](#policy) and [roles](#role) to User groups as well as individual [Users](#user).

Technically, a User group is a Content item of a special [Content Type](#content-type).

## X

#### XML

A markup language for encoding documents (short for Extensible Markup Language). One of the formats for storing configuration data in eZ, as well as an output form for REST API.

## Y

#### YAML

A data serialization language (short for YAML Ain't Markup Language). One of the formats for storing configuration data in eZ.

## Z

#### Zone

A basic part of a [Landing Page](#landing-page) layout. Zones are are deployed over a [layout](#layout) in a particular position and can in turn contain [blocks](#block).
