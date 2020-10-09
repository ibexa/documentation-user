# Shop administration

eZ Commerce provides the following eCommerce functions in the top menu of the backend.

Depending on the chosen data provider and whether an ERP is connected, some tabs may contain no data.

![](img/backend_menu.png)

|Tab|Description|
|--- |--- |
|[Cockpit](cockpit.md)|Basic statistics|
|[Order Management](manage_orders.md)|Basic order management|
|[Components](components.md)|A folder where [translations](translations.md) are stored. Can provide additional content which is used by the shop for project-specific information which is not displayed directly (as a full page) in the shop.|
|[Configuration Settings](configuration_settings.md)|Basic shop configuration|
|[Price and stock management](manage_prices_and_stock.md)|Product price and stock management|

## Control Center

![](img/backend_menu_center.png)

### ERP request log

This section is available only if an ERP system is connected.

All communication (request and response messages), that is sent between shop and ERP system is recorded and displayed here.

![](img/erprequest_log.png)
 
### ERP Performance

If an ERP system is connected, the ERP performance viewer shows the efficiency of the connection between the shop and the ERP system.
It displays the number of the different requests per date and time.

The monitoring tool regularly checks the connection to the ERP with a test request.

If the connection fails, the administrator receives an email.
If the connection is successful again, the alarm is ended by another email.

![](img/erp_performance.png)

### eMail archive

In the **eMail archive** tab the shop owner/admin can find all emails which were automatically sent from the shop,
with date of sending, recipient, subject and status. They can see the emails and resend them.

![](img/email_archive.png)

### eContent

If eContent is used as data provider, in the **eContent tasks** tab the administrator can see how many products and product groups there are in the shop.
They can create a new index, import a backup into the database and create a backup from the database.

![](img/econtent.png)

In the **eContent types** tab the administrator can see the eContent types with their associated attributes (`product_group` and `product`) and the mapping information.

![](img/econtent_types.png)

### eCommerce jobs

The shop uses jobs to perform recurring tasks such as imports, backups etc.
The job system lists the last jobs and shows the status and result of the job.

![](img/ecommerce_jobs.png)
