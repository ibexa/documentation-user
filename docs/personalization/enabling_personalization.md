---
description: Enabling the Personalization service requires an installation key provided by Ibexa.
---

# Enabling personalization

The personalization service is based on a client-server architecture.
The recommendation client that is part of your installation must connect to the server 
that is run and maintained by Ibexa.
To use the service, you must get and set up authentication parameters.

## Requesting access to the server

First, you must accept the terms and conditions of the personalization service.

To do this, in the Back Office, select **Personalization**, and then **Dashboard**.
On the welcome screen, enter the following details:

- A full name of the person responsible for accepting the terms and conditions
- An email address to which you want the confirmation to be sent
- An installation key that can be found on the **Maintenance and Support agreement details** page in the service portal

Select the **I have read and agree to the Terms and Conditions** checkbox, and then click **Submit**.
Your request is sent to Ibexa, and you will receive a confirmation email in response.

## Configuring customer credentials

When you receive the confirmation email, ask your administrator to [add the credentials to your configuration](https://doc.ibexa.co/en/latest/guide/personalization/enabling_personalization/#configuring-mandator-credentials).

## Change the installation key

If necessary, you can modify the installation key configured in the personalization settings.
To do this, in the Back Office, select **Personalization** and then **Settings**.
Modify the value in the **Installation key** field and save your changes.

!!! note "Disabling the service"

    Clear the **Installation key** field to temporarily disable the personalization service 
    for your account.
    Entering the same key re-enables the feature.
