---
description: Enabling the Personalization service requires an installation key provided by Ibexa.
---

# Enable personalization

The Personalization service is based on a client-server architecture.
The recommendation client that is part of your installation must connect to 
the server that is run and maintained by Ibexa.
To use the service, you must make arrangements with Ibexa to define the initial 
configuration, and then register your account and set up authentication parameters.

## Request access to the server

After you get the initial configuration from Ibexa, you must accept the terms and conditions of the Personalization service
and create an account to get access to the server.

### Create account

First, you must accept the terms and conditions of the Personalization service.


1. Go to the Back Office.
1. On the left panel, go to **Personalization** > **Dashboard**.
1. On the welcome screen, provide the following details:

    - A full name of the person responsible for accepting the terms and conditions
    - An email address to which you want the confirmation to be sent
    - An installation key that can be found on the **Maintenance and Support agreement details** page in the [Service Portal](https://support.ibexa.co/)

1. Select the **I have read and agree to the Terms and Conditions** checkbox, and then click **Submit**.
1. Next, enter the project name or your brand name.
1. From the **Type** drop-down, select the account type (Commerce or Publisher).
1. To proceed, click **Next**. After a few moments, a screen with your ID and license key displays.

![Create account](img/perso_create_account_1.png "Create account")
![Basic scenario configuration](img/perso_create_account_2.png "Account credentials")
### Set up service parameters

When you receive the the credentials, ask your administrator to:

- [add the credentials to your configuration]([[= developer_doc =]]/personalization/enable_personalization/#set-up-customer-credentials)
- [configure events that you wish to track]([[= developer_doc =]]/personalization/enable_personalization/#set-up-item-type-tracking)