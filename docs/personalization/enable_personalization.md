---
description: Enabling the Personalization service requires an installation key provided by Ibexa.
---

# Enable personalization

The Personalization service is based on a client-server architecture.
The recommendation client that is part of your installation must connect to 
the server that is run and maintained by Ibexa.
To use the service, you must make arrangements with Ibexa to define the initial 
configuration, and then get and set up authentication parameters.

## Request access to the server

After you get the initial configuration from Ibexa, you must accept the terms and conditions of the Personalization service
and create an account to get access to the server.

### Create account

First, you must accept the terms and conditions of the Personalization service.

To do this, in the Back Office, on the left panel. click **Personalization**, and then **Dashboard**.
On the welcome screen, enter the following details:

- A full name of the person responsible for accepting the terms and conditions
- An email address to which you want the confirmation to be sent
- An installation key that can be found on the **Maintenance and Support agreement details** page in the service portal

Select the **I have read and agree to the Terms and Conditions** checkbox, and then click **Submit**.
Your request is sent to Ibexa, and you receive an email with credentials in response.

### Set up service parameters

When you receive the email with credentials, ask your administrator to:

- [add the credentials to your configuration]([[= developer_doc =]]/personalization/enable_personalization/#set-up-customer-credentials)
- [configure events that you wish to track]([[= developer_doc =]]/personalization/enable_personalization/#set-up-item-type-tracking)

-------------------------
The aim of this feature is to reduce the time and not necessary effort when creating new personalization customer account. When customer admin reaching out the Personalization section, there will be an option to create an account in the automated way. First the customer is asked for filling out the form with name, email address and installation key. After T&C acceptance can choose type of the account (commerce or publisher). Next step is to send request to the personalization endpoint and receive customer ID and secret key.


![Basic scenario configuration](img/perso_create_account_1.png "Create account")

![Basic scenario configuration](img/perso_create_account_2.png "Account credentials")