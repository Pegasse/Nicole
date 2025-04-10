# Contacts

## Overview

### End Points
*   `POST /contacts`
*   `PUT /contacts` *(Note: This is likely for bulk/keyed updates, see Update Contact using Custom Field)*
*   `GET /contacts`
*   `PUT /contacts/{contact_id}`
*   `GET /contacts/{contact_id}`
*   `DELETE /contacts/{contact_id}`
*   `POST /contacts/{contact_id}/active`
*   `POST /contacts/{contact_id}/inactive`
*   `POST /contacts/{contact_id}/portal/enable`
*   `POST /contacts/{contact_id}/paymentreminder/enable`
*   `POST /contacts/{contact_id}/paymentreminder/disable`
*   `POST /contacts/{contact_id}/statements/email`
*   `GET /contacts/{contact_id}/statements/email`
*   `POST /contacts/{contact_id}/email`
*   `GET /contacts/{contact_id}/comments`
*   `POST /contacts/{contact_id}/address`
*   `GET /contacts/{contact_id}/address`
*   `PUT /contacts/{contact_id}/address/{address_id}`
*   `DELETE /contacts/{contact_id}/address/{address_id}`
*   `GET /contacts/{contact_id}/refunds`
*   `POST /contacts/{contact_id}/track1099` *(Note: Endpoint not in provided files)*
*   `POST /contacts/{contact_id}/untrack1099` *(Note: Endpoint not in provided files)*

### Attributes
*   **contact_id** (string): ID of the contact
*   **contact_name** (string): Display Name of the contact. Max-length [200]
*   **company_name** (string): Company Name of the contact. Max-length [200]
*   **has_transaction** (boolean): *(unavailable description)*
*   **contact_type** (string): Contact type of the contact
*   **customer_sub_type** (string): Type of the customer
*   **credit_limit** (double): Credit limit for a customer
*   **is_portal_enabled** (boolean): To enable client portal for the contact. Allowed value is true and false.
*   **language_code** (string): language of a contact. allowed values de,en,es,fr,it,ja,nl,pt,pt_br,sv,zh,en_gb
*   **is_taxable** (boolean): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Boolean to track the taxability of the customer.
*   **tax_id** (string): 🇮🇳 , 🇺🇸 only - ID of the tax or tax group that can be collected from the contact. Tax can be given only if is_taxable is true.
*   **tds_tax_id** (string): 🇲🇽 only - ID of the TDS tax.
*   **tax_name** (string): 🇮🇳 only - Enter tax name
*   **tax_percentage** (double): Enter tax percentage.
*   **tax_authority_id** (string): 🇺🇸 only - ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
*   **tax_exemption_id** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - ID of the tax exemption.
*   **tax_authority_name** (string): Enter tax authority name.
*   **tax_exemption_code** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - Enter tax exemption code
*   **place_of_contact** (string): 🇮🇳 only - Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer/vendor.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment of the contact. Allowed Values: `uk` (A business that is located in the UK.), `eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and `overseas` (A business that is located outside UK. Pre Brexit, this was split as eu_vat_registered, eu_vat_not_registered and non_eu ).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment of the contact. Allowed Values: `vat_registered`,`vat_not_registered`,`gcc_vat_not_registered`,`gcc_vat_registered`,`non_gcc`,`dz_vat_registered` and `dz_vat_not_registered` `home_country_mexico` (A business that is located within MX) `border_region_mexico` (A business that is located in the northern and southern border regions in MX) `non_mexico` (A business that is located outside MX). For Kenya Edition: `vat_registered` ,`vat_not_registered` ,`non_kenya`(A business that is located outside Kenya). For SouthAfrica Edition: `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).
*   **tax_exemption_certificate_number** (string): 🇰🇪 only - Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption
*   **tax_regime** (string): 🇲🇽 only - Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.
*   **legal_name** (string): 🇲🇽 only - Legal Name of the contact.
*   **is_tds_registered** (boolean): 🇲🇽 only - Boolean to check if tax is registered.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **is_linked_with_zohocrm** (boolean): *(unavailable description)*
*   **website** (string): Website of the contact.
*   **owner_id** (string): For Customer Only : If a contact is assigned to any particular user, that user can manage transactions for the contact.
*   **primary_contact_id** (string): *(unavailable description)*
*   **payment_terms** (integer): Net payment term for the customer.
*   **payment_terms_label** (string): Label for the paymet due details.
*   **currency_id** (string): Currency ID of the customer's currency.
*   **currency_code** (string): Currency code of the currency in which the customer wants to pay. If currency_code is not specified here, the currency chosen in your Zoho Subscriptions organization will be used for billing. currency_id and currency_symbol are set automatically in accordance to the currency_code.
*   **currency_symbol** (string): Symbol of the currency of the contact_type
*   **opening_balances** (array): Opening balance details.
*   **location_id** (string): Location ID
*   **location_name** (string): Name of the location
*   **outstanding_receivable_amount** (integer): *(definition unavailable)*
*   **outstanding_receivable_amount_bcy** (integer): *(definition unavailable)*
*   **unused_credits_receivable_amount** (integer): *(definition unavailable)*
*   **unused_credits_receivable_amount_bcy** (integer): *(definition unavailable)*
*   **status** (string): The status of the contact.
*   **payment_reminder_enabled** (boolean): *(definition unavailable)*
*   **custom_fields** (array): Custom fields associated with the contact.
*   **billing_address** (object): Billing address of the contact.
*   **shipping_address** (object): Customer's shipping address object.
*   **facebook** (string): Facebook profile account. max-length [100]
*   **twitter** (string): Twitter account. max-length [100]
*   **contact_persons** (array): Contact persons associated with the contact.
*   **default_templates** (object): Default templates associated with the contact.
*   **notes** (string): Comments about the payment made by the contact.
*   **created_time** (string): Time at which the contact was created.
*   **last_modified_time** (string): Time at which the contact was modified

### Example
```json
{
    "contact_id": 460000000026049,
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "has_transaction": true,
    "contact_type": "customer",
    "customer_sub_type": "business",
    "credit_limit": 1000,
    "is_portal_enabled": true,
    "language_code": "string",
    "is_taxable": true,
    "tax_id": 11149000000061058,
    "tds_tax_id": "982000000557012",
    "tax_name": "CGST",
    "tax_percentage": 12,
    "tax_authority_id": 11149000000061052,
    "tax_exemption_id": 11149000000061054,
    "tax_authority_name": "string",
    "tax_exemption_code": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "vat_treatment": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "gst_treatment": "business_gst",
    "is_linked_with_zohocrm": false,
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "primary_contact_id": 460000000026051,
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "currency_id": 460000000000097,
    "currency_code": "USD",
    "currency_symbol": "$",
    "opening_balances": [
        {
            "location_id": "460000000038080",
            "exchange_rate": 1,
            "opening_balance_amount": 1200
        }
    ],
    "location_id": "460000000038080",
    "location_name": "string",
    "outstanding_receivable_amount": 250,
    "outstanding_receivable_amount_bcy": 250,
    "unused_credits_receivable_amount": 1369.66,
    "unused_credits_receivable_amount_bcy": 1369.66,
    "status": "active",
    "payment_reminder_enabled": true,
    "custom_fields": [
        {
            "index": 1,
            "value": "GBGD078",
            "label": "VAT ID"
        }
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "facebook": "zoho",
    "twitter": "zoho",
    "contact_persons": [
        {
            "contact_person_id": 460000000026051,
            "salutation": "Mr",
            "first_name": "Will",
            "last_name": "Smith",
            "email": "willsmith@bowmanfurniture.com",
            "phone": "+1-925-921-9201",
            "mobile": "+1-4054439562",
            "designation": "Sales Executive",
            "department": "Sales and Marketing",
            "skype": "Zoho",
            "is_primary_contact": true,
            "enable_portal": true
        }
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "created_time": "2013-08-05T12:06:10+0530",
    "last_modified_time": "2013-10-07T18:24:51+0530"
}
```

## Add Additional Address

### Description
Add an additional address for a contact using the arguments below.

### Endpoint
`POST /contacts/{contact_id}/address`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Arguments (Body Parameters)
*   **attention** (string)
*   **address** (string): Max-length [500]
*   **street2** (string)
*   **city** (string): City of the customer’s billing address.
*   **state** (string): State of the customer’s billing address.
*   **zip** (string): Zip code of the customer’s billing address.
*   **country** (string): Country of the customer’s billing address.
*   **fax** (string): Customer's fax number.
*   **phone** (string): phone number of the contact person.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "attention": "Mr.John",
    "address": "4900 Hopyard Rd",
    "street2": "Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 94588,
    "country": "U.S.A",
    "fax": "+1-925-924-9600",
    "phone": "+1-925-921-9201"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The address has been created.",
    "address_info": {
        "address_id": 1053791000000186000,
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    }
}
```

## Create a Contact

### Description
Create a contact with given information.

### Endpoint
`POST /contacts`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Arguments (Body Parameters)
*   **contact_name** (string, Required): Display Name of the contact. Max-length [200]
*   **company_name** (string): Company Name of the contact. Max-length [200]
*   **website** (string): Website of the contact.
*   **language_code** (string): language of a contact. allowed values de,en,es,fr,it,ja,nl,pt,pt_br,sv,zh,en_gb
*   **contact_type** (string): Contact type of the contact
*   **customer_sub_type** (string): Type of the customer
*   **credit_limit** (double): Credit limit for a customer
*   **tags** (array): Filter all your reports based on the tag
*   **is_portal_enabled** (boolean): To enable client portal for the contact. Allowed value is true and false.
*   **currency_id** (string): Currency ID of the customer's currency.
*   **payment_terms** (integer): Net payment term for the customer.
*   **payment_terms_label** (string): Label for the paymet due details.
*   **notes** (string): Commennts about the payment made by the contact.
*   **billing_address** (object): Billing address of the contact.
*   **shipping_address** (object): Customer's shipping address object.
*   **contact_persons** (array): default is Contact persons of a contact.
*   **default_templates** (object): Default templates object.
*   **custom_fields** (array): Custom fields of the contact.
*   **opening_balances** (array): Opening balance details.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - For UK Edition: VAT Registration number of a contact with length should be between 2 and 12 characters. For Avalara: If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.
*   **owner_id** (string): For Customer Only : If a contact is assigned to any particular user, that user can manage transactions for the contact.
*   **tax_reg_no** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - For GCC Edition: 15 digit Tax Registration number of a contact with Tax treatment as vat_registered,gcc_vat_registered,dz_vat_registered. For Mexico Edition: 12 digit Tax Registration number of a contact with Tax treatment as home_country_mexico, border_region_mexico, non_mexico. Consumers generic RFC: XAXX010101000, Overseas generic RFC: XEXX010101000. For Kenya Edition: 11 digit Tax Registration number of a contact with Tax treatment as vat_registered For SouthAfrica Edition: 10 digit Tax Registration number of a contact with Tax treatment as vat_registered
*   **tax_exemption_certificate_number** (string): 🇰🇪 only - Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption
*   **country_code** (string): 🇬🇧 , GCC , Avalara Integration only - For UK Edition: Two letter country code of a contact. For Avalara: Two letter country code for the customer country, if your customer is not in US. Refer [AvaTax Codes for Countries and States][2]. For GCC Editions : Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as place of supply. Supported codes for UAE emirates are : Abu Dhabi - AB, Ajman - AJ, Dubai - DU, Fujairah - FU, Ras al-Khaimah - RA, Sharjah - SH, Umm al-Quwain - UM. Supported codes for the GCC countries are : United Arab Emirates - AE, Saudi Arabia - SA, Bahrain - BH, Kuwait - KW, Oman - OM, Qatar - QA.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment of the contact.Allowed Values: `uk` (A business that is located in the UK.), `eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and `overseas` (A business that is located outside UK. Pre Brexit, this was split as eu_vat_registered, eu_vat_not_registered and non_eu ).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment of the contact. Allowed Values: `vat_registered`,`vat_not_registered`,`gcc_vat_not_registered`,`gcc_vat_registered`,`non_gcc`,`dz_vat_registered` and `dz_vat_not_registered` `home_country_mexico` (A business that is located within MX) `border_region_mexico` (A business that is located in the northern and southern border regions in MX) `non_mexico` (A business that is located outside MX). For Kenya Edition: `vat_registered` ,`vat_not_registered` ,`non_kenya`(A business that is located outside Kenya). For SouthAfrica Edition: `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).
*   **tax_regime** (string): 🇲🇽 only - Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.
*   **legal_name** (string): 🇲🇽 only - Legal Name of the contact.
*   **is_tds_registered** (boolean): 🇲🇽 only - Boolean to check if tax is registered.
*   **place_of_contact** (string): 🇮🇳 only - Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer/vendor.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **tax_authority_name** (string): Enter tax authority name.
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number of the customer.
*   **avatax_use_code** (string): Avalara Integration only - Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code.
*   **tax_exemption_id** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - ID of the tax exemption.
*   **tax_exemption_code** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - Enter tax exemption code
*   **tax_authority_id** (string): 🇺🇸 only - ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
*   **tax_id** (string): 🇮🇳 , 🇺🇸 only - ID of the tax or tax group that can be collected from the contact. Tax can be given only if is_taxable is true.
*   **tds_tax_id** (string): 🇲🇽 only - ID of the TDS tax.
*   **is_taxable** (boolean): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Boolean to track the taxability of the customer.
*   **facebook** (string): Facebook profile account. max-length [100]
*   **twitter** (string): Twitter account. max-length [100]
*   **track_1099** (boolean): 🇺🇸 only - Boolean to track a contact for 1099 reporting.
*   **tax_id_type** (string): 🇺🇸 only - Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.
*   **tax_id_value** (string): 🇺🇸 only - Tax ID of the contact.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "website": "www.bowmanfurniture.com",
    "language_code": "string",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "credit_limit": 1000,
    "tags": [
        {
            "tag_id": 462000000009070,
            "tag_option_id": 462000000002670
        }
    ],
    "is_portal_enabled": true,
    "currency_id": 460000000000097,
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "notes": "Payment option : Through check",
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": "Contact persons of a contact.",
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "custom_fields": [
        {
            "index": 1,
            "value": "GBGD078"
        }
    ],
    "opening_balances": [
        {
            "location_id": "460000000038080",
            "exchange_rate": 1,
            "opening_balance_amount": 1200
        }
    ],
    "vat_reg_no": "string",
    "owner_id": 460000000016051,
    "tax_reg_no": 12345678912345,
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "country_code": "string",
    "vat_treatment": "string",
    "tax_treatment": "string",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "tds_tax_id": "982000000557012",
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The contact has been created",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_portal_enabled": true,
        "language_code": "string",
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tds_tax_id": "982000000557012",
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "vat_treatment": "string",
        "tax_treatment": "string",
        "tax_exemption_certificate_number": "KRAEXM0043310521",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balances": [
            {
                "location_id": "460000000038080",
                "exchange_rate": 1,
                "opening_balance_amount": 1200
            }
        ],
        "location_id": "460000000038080",
        "location_name": "string",
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [
            {
                "index": 1,
                "value": "GBGD078",
                "label": "VAT ID"
            }
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [
            {
                "contact_person_id": 460000000026051,
                "salutation": "Mr",
                "first_name": "Will",
                "last_name": "Smith",
                "email": "willsmith@bowmanfurniture.com",
                "phone": "+1-925-921-9201",
                "mobile": "+1-4054439562",
                "designation": "Sales Executive",
                "department": "Sales and Marketing",
                "skype": "Zoho",
                "is_primary_contact": true,
                "enable_portal": true
            }
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}
```

## Delete a Contact

### Description
Delete an existing contact.

### Endpoint
`DELETE /contacts/{contact_id}`

### OAuth Scope
`ZohoBooks.contacts.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The contact has been deleted."
}
```

## Delete Additional Address

### Description
Delete the additional address of a contact.

### Endpoint
`DELETE /contacts/{contact_id}/address/{address_id}`

### OAuth Scope
`ZohoBooks.contacts.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The address has been deleted."
}
```

## Disable Payment Reminders

### Description
Disable automated payment reminders for a contact.

### Endpoint
`POST /contacts/{contact_id}/paymentreminder/disable`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "All reminders associated with this contact have been stopped."
}
```

## Edit Additional Address

### Description
Edit the additional address of a contact using the arguments below.

### Endpoint
`PUT /contacts/{contact_id}/address/{address_id}`

### OAuth Scope
`ZohoBooks.contacts.UPDATE`

### Arguments (Body Parameters)
*   **attention** (string)
*   **address** (string): Max-length [500]
*   **street2** (string)
*   **city** (string): City of the customer’s billing address.
*   **state** (string): State of the customer’s billing address.
*   **zip** (string): Zip code of the customer’s billing address.
*   **country** (string): Country of the customer’s billing address.
*   **fax** (string): Customer's fax number.
*   **phone** (string): phone number of the contact person.
*   **address_id** (string, Required): Address id of the address *(Note: Also present in the URL path)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "attention": "Mr.John",
    "address": "4900 Hopyard Rd",
    "street2": "Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 94588,
    "country": "U.S.A",
    "fax": "+1-925-924-9600",
    "phone": "+1-925-921-9201",
    "address_id": 1053791000000186000
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The address has been updated.",
    "address_info": {
        "address_id": 1053791000000186000,
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    }
}
```

## Email Contact

### Description
Send email to contact.

### Endpoint
`POST /contacts/{contact_id}/email`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Arguments (Body Parameters)
*   **to_mail_ids** (array, Required): Array of email address of the recipients.
*   **subject** (string, Required): Subject of an email has to be sent. Max-length [1000]
*   **body** (string, Required): Body of an email has to be sent. Max-length [5000]
*   **attachments** (binary): Files to be attached to the email. It has to be sent in multipart/formdata

### Query Parameters
*   **send_customer_statement** (boolean): Send customer statement pdf with email.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "subject": "Welcome to Zillium Inc .",
    "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc",
    "attachments": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Email has been sent."
}
```

## Email Statement

### Description
Email statement to the contact. If JSONString is not inputted, mail will be sent with the default mail content.

### Endpoint
`POST /contacts/{contact_id}/statements/email`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Arguments (Body Parameters)
*   **send_from_org_email_id** (boolean): Boolean to trigger the email from the organization's email address
*   **to_mail_ids** (array, Required): Array of email address of the recipients.
*   **cc_mail_ids** (array): Array of email address of the recipients to be cced.
*   **subject** (string, Required): Subject of an email has to be sent. Max-length [1000]
*   **body** (string, Required): Body of an email has to be sent. Max-length [5000]

### Query Parameters
*   **start_date** (string): If start_date and end_date are not given, current month's statement will be sent to contact. Date format [yyyy-mm-dd]
*   **end_date** (string): End date for the statement. Date format [yyyy-mm-dd]
*   **multipart_or_formdata**: Files to be attached along with the statement.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "send_from_org_email_id": true,
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "subject": "Statement of transactions with Zillium Inc",
    "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Statement has been sent to the Customer."
}
```

## Enable Payment Reminders

### Description
Enable automated payment reminders for a contact.

### Endpoint
`POST /contacts/{contact_id}/paymentreminder/enable`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "All reminders associated with this contact have been enabled."
}
```

## Enable Portal Access

### Description
Enable portal access for a contact.

### Endpoint
`POST /contacts/{contact_id}/portal/enable`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Arguments (Body Parameters)
*   **contact_persons** (array, Required): List of contact person IDs to enable portal access for.
    *   **contact_person_id** (string): ID of the contact person.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "contact_persons": [
        {
            "contact_person_id": 460000000026051
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Client Portal preferences have been updated"
}
```

## Get Contact Addresses

### Description
Get addresses of a contact including its Shipping Address, Billing Address and other additional addresses.

### Endpoint
`GET /contacts/{contact_id}/address`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "addresses": [
        {
            "address_id": 1053791000000186000,
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        {...},
        {...}
    ]
}
```

## Get Contact

### Description
Get details of a contact.

### Endpoint
`GET /contacts/{contact_id}`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balances": [
            {
                "location_id": "460000000038080",
                "exchange_rate": 1,
                "opening_balance_amount": 1200
            }
        ],
        "location_id": "460000000038080",
        "location_name": "string",
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "facebook": "zoho",
        "twitter": "zoho",
        "payment_reminder_enabled": true,
        "custom_fields": [
            {
                "index": 1,
                "value": "GBGD078",
                "label": "VAT ID"
            }
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "contact_persons": [
            {
                "contact_person_id": 460000000026051,
                "salutation": "Mr",
                "first_name": "Will",
                "last_name": "Smith",
                "email": "willsmith@bowmanfurniture.com",
                "phone": "+1-925-921-9201",
                "mobile": "+1-4054439562",
                "designation": "Sales Executive",
                "department": "Sales and Marketing",
                "skype": "Zoho",
                "is_primary_contact": true,
                "enable_portal": true
            }
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}
```

## Get Statement Mail Content

### Description
Get the statement mail content.

### Endpoint
`GET /contacts/{contact_id}/statements/email`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Query Parameters
*   **start_date** (string): If start_date and end_date are not given, current month's statement will be sent to contact. Date format [yyyy-mm-dd]
*   **end_date** (string): End date for the statement. Date format [yyyy-mm-dd]

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc",
        "subject": "Statement of transactions with Zillium Inc",
        "to_contacts": [
            {
                "first_name": "Will",
                "selected": true,
                "phone": "+1-925-921-9201",
                "email": "willsmith@bowmanfurniture.com",
                "contact_person_id": 460000000026051,
                "last_name": "Smith",
                "salutation": "Mr",
                "mobile": "+1-4054439562"
            }
        ],
        "file_name": "statement_BowmanandCo.pdf",
        "from_emails": [
            {
                "user_name": "John Smith",
                "selected": true,
                "email": "willsmith@bowmanfurniture.com"
            }
        ],
        "contact_id": 460000000026049
    }
}
```

## List Comments

### Description
List recent activities of a contact.

### Endpoint
`GET /contacts/{contact_id}/comments`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "contact_comments": [
        {
            "comment_id": 460000000053131,
            "contact_id": 460000000026049,
            "contact_name": "Bowman and Co",
            "description": "",
            "commented_by_id": 460000000024003,
            "commented_by": "John David",
            "date": "2013-11-19",
            "date_description": "4 days ago",
            "time": "6:03 PM",
            "transaction_id": 460000000053123,
            "transaction_type": "customer_payment",
            "is_entity_deleted": false,
            "operation_type": "added"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "applied_filter": "Status.All",
        "sort_column": "contact_name",
        "sort_order": "D"
    }
}
```

## List Contacts

### Description
List all contacts with pagination.

### Endpoint
`GET /contacts`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Query Parameters
*   **contact_name** (string): Search contacts by contact name. Max-length [100] Variants: `contact_name_startswith` and `contact_name_contains`. Max-length [100]
*   **company_name** (string): Search contacts by company name. Max-length [100] Variants: `company_name_startswith` and `company_name_contains`
*   **first_name** (string): Search contacts by first name of the contact person. Max-length [100] Variants: `first_name_startswith` and `first_name_contains`
*   **last_name** (string): Search contacts by last name of the contact person. Max-length [100] Variants: `last_name_startswith` and `last_name_contains`
*   **address** (string): Search contacts by any of the address fields. Max-length [100] Variants: `address_startswith` and `address_contains`
*   **email** (string): Search contacts by email of the contact person. Max-length [100] Variants: `email_startswith` and `email_contains`
*   **phone** (string): Search contacts by phone number of the contact person. Max-length [100] Variants: `phone_startswith` and `phone_contains`
*   **filter_by** (string): Filter contacts by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Inactive`, `Status.Duplicate` and `Status.Crm`
*   **search_text** (string): Search contacts by contact name or notes. Max-length [100]
*   **sort_column** (string): Sort contacts. Allowed Values: `contact_name`, `first_name`, `last_name`, `email`, `outstanding_receivable_amount`, `created_time` and `last_modified_time`
*   **zcrm_contact_id** (string): CRM Contact ID for the contact.
*   **zcrm_account_id** (string): CRM Account ID for the contact.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "contacts": [
        {
            "contact_id": 460000000026049,
            "contact_name": "Bowman and Co",
            "company_name": "Bowman and Co",
            "contact_type": "customer",
            "status": "active",
            "payment_terms": 15,
            "payment_terms_label": "Net 15",
            "currency_id": 460000000000097,
            "currency_code": "USD",
            "outstanding_receivable_amount": 250,
            "unused_credits_receivable_amount": 1369.66,
            "first_name": "Will",
            "last_name": "Smith",
            "email": "willsmith@bowmanfurniture.com",
            "phone": "+1-925-921-9201",
            "mobile": "+1-4054439562",
            "created_time": "2013-08-05T12:06:10+0530",
            "last_modified_time": "2013-10-07T18:24:51+0530"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "applied_filter": "Status.All",
        "sort_column": "contact_name",
        "sort_order": "D"
    }
}
```

## List Refunds

### Description
List the refund history of a contact.

### Endpoint
`GET /contacts/{contact_id}/refunds`

### OAuth Scope
`ZohoBooks.contacts.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "creditnote_refunds": [
        {
            "creditnote_refund_id": 982000000567158,
            "creditnote_id": 982000000567134,
            "date": "2013-11-19",
            "refund_mode": "cash",
            "reference_number": 782364,
            "creditnote_number": "CN-00001",
            "customer_name": "Bowman & Co",
            "description": "gf",
            "amount_bcy": 57.15,
            "amount_fcy": 57.15
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Credit Notes Refund",
        "sort_column": "date",
        "sort_order": "D"
    }
}
```

## Mark as Active

### Description
Mark a contact as active.

### Endpoint
`POST /contacts/{contact_id}/active`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The contact has been marked as active."
}
```

## Mark as Inactive

### Description
Mark a contact as inactive.

### Endpoint
`POST /contacts/{contact_id}/inactive`

### OAuth Scope
`ZohoBooks.contacts.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The contact has been marked as inactive."
}
```

## Update a Contact using Custom Field

### Description
Update a contact using a custom field's unique value. A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a contact by providing its API name in the `X-Unique-Identifier-Key` header and its value in the `X-Unique-Identifier-Value` header. Based on this value, the corresponding contact will be retrieved and updated. Additionally, there is an optional `X-Upsert` header. If the `X-Upsert` header is true and the custom field's unique value is not found in any of the existing contacts, a new contact will be created if the necessary payload details are available.

### Endpoint
`PUT /contacts` *(with custom headers)*

### OAuth Scope
`ZohoBooks.contacts.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field for the target contact.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create a new contact if the unique value is not found.

### Arguments (Body Parameters)
*   **contact_name** (string, Required): Display Name of the contact. Max-length [200]
*   **company_name** (string): Company Name of the contact. Max-length [200]
*   **payment_terms** (integer): Net payment term for the customer.
*   **payment_terms_label** (string): Label for the paymet due details.
*   **contact_type** (string): Contact type of the contact
*   **customer_sub_type** (string): Type of the customer
*   **currency_id** (string): Currency ID of the customer's currency.
*   **opening_balances** (array): Opening balance details.
*   **credit_limit** (double): Credit limit for a customer
*   **tags** (array): Filter all your reports based on the tag
*   **website** (string): Website of the contact.
*   **owner_id** (string): For Customer Only : If a contact is assigned to any particular user, that user can manage transactions for the contact.
*   **custom_fields** (array): Custom fields of the contact.
*   **billing_address** (object): Billing address of the contact.
*   **shipping_address** (object): Customer's shipping address object.
*   **contact_persons** (array): Contact persons of a contact.
*   **default_templates** (object): Default templates object.
*   **notes** (string): Commennts about the payment made by the contact.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - For UK Edition: VAT Registration number of a contact with length should be between 2 and 12 characters. For Avalara: If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.
*   **tax_reg_no** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - For GCC Edition: 15 digit Tax Registration number of a contact with Tax treatment as vat_registered,gcc_vat_registered,dz_vat_registered. For Mexico Edition: 12 digit Tax Registration number of a contact with Tax treatment as home_country_mexico, border_region_mexico, non_mexico. Consumers generic RFC: XAXX010101000, Overseas generic RFC: XEXX010101000. For Kenya Edition: 11 digit Tax Registration number of a contact with Tax treatment as vat_registered For SouthAfrica Edition: 10 digit Tax Registration number of a contact with Tax treatment as vat_registered
*   **country_code** (string): 🇬🇧 , GCC , Avalara Integration only - For UK Edition: Two letter country code of a contact. For Avalara: Two letter country code for the customer country, if your customer is not in US. Refer [AvaTax Codes for Countries and States][2]. For GCC Editions : Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as place of supply. Supported codes for UAE emirates are : Abu Dhabi - AB, Ajman - AJ, Dubai - DU, Fujairah - FU, Ras al-Khaimah - RA, Sharjah - SH, Umm al-Quwain - UM. Supported codes for the GCC countries are : United Arab Emirates - AE, Saudi Arabia - SA, Bahrain - BH, Kuwait - KW, Oman - OM, Qatar - QA.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment of the contact. Allowed Values: `vat_registered`,`vat_not_registered`,`gcc_vat_not_registered`,`gcc_vat_registered`,`non_gcc`,`dz_vat_registered` and `dz_vat_not_registered` `home_country_mexico` (A business that is located within MX) `border_region_mexico` (A business that is located in the northern and southern border regions in MX) `non_mexico` (A business that is located outside MX). For Kenya Edition: `vat_registered` ,`vat_not_registered` ,`non_kenya`(A business that is located outside Kenya). For SouthAfrica Edition: `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).
*   **tax_exemption_certificate_number** (string): 🇰🇪 only - Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption
*   **tax_regime** (string): 🇲🇽 only - Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.
*   **legal_name** (string): 🇲🇽 only - Legal Name of the contact.
*   **is_tds_registered** (boolean): 🇲🇽 only - Boolean to check if tax is registered.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment of the contact.Allowed Values: `uk` (A business that is located in the UK.), `eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and `overseas` (A business that is located outside UK. Pre Brexit, this was split as eu_vat_registered, eu_vat_not_registered and non_eu ).
*   **place_of_contact** (string): 🇮🇳 only - Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer/vendor.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **tax_authority_name** (string): Enter tax authority name.
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number of the customer.
*   **avatax_use_code** (string): Avalara Integration only - Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code.
*   **tax_exemption_id** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - ID of the tax exemption.
*   **tax_exemption_code** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - Enter tax exemption code
*   **tax_authority_id** (string): 🇺🇸 only - ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
*   **tax_id** (string): 🇮🇳 , 🇺🇸 only - ID of the tax or tax group that can be collected from the contact. Tax can be given only if is_taxable is true.
*   **is_taxable** (boolean): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Boolean to track the taxability of the customer.
*   **facebook** (string): Facebook profile account. max-length [100]
*   **twitter** (string): Twitter account. max-length [100]
*   **track_1099** (boolean): 🇺🇸 only - Boolean to track a contact for 1099 reporting.
*   **tax_id_type** (string): 🇺🇸 only - Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.
*   **tax_id_value** (string): 🇺🇸 only - Tax ID of the contact.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "currency_id": 460000000000097,
    "opening_balances": [
        {
            "location_id": "460000000038080",
            "exchange_rate": 1,
            "opening_balance_amount": 1200
        }
    ],
    "credit_limit": 1000,
    "tags": [
        {
            "tag_id": 462000000009070,
            "tag_option_id": 462000000002670
        }
    ],
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "custom_fields": [
        {
            "index": 1,
            "value": "GBGD078",
            "label": "VAT ID"
        }
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": [
        {
            "contact_person_id": 460000000026051,
            "salutation": "Mr",
            "first_name": "Will",
            "last_name": "Smith",
            "email": "willsmith@bowmanfurniture.com",
            "phone": "+1-925-921-9201",
            "mobile": "+1-4054439562",
            "designation": "Sales Executive",
            "department": "Sales and Marketing",
            "skype": "Zoho",
            "is_primary_contact": true,
            "enable_portal": true
        }
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "vat_reg_no": "string",
    "tax_reg_no": 12345678912345,
    "country_code": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "vat_treatment": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Contact has been updated successfully",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balances": [
            {
                "location_id": "460000000038080",
                "exchange_rate": 1,
                "opening_balance_amount": 1200
            }
        ],
        "location_id": "460000000038080",
        "location_name": "string",
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [
            {
                "index": 1,
                "value": "GBGD078",
                "label": "VAT ID"
            }
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [
            {
                "contact_person_id": 460000000026051,
                "salutation": "Mr",
                "first_name": "Will",
                "last_name": "Smith",
                "email": "willsmith@bowmanfurniture.com",
                "phone": "+1-925-921-9201",
                "mobile": "+1-4054439562",
                "designation": "Sales Executive",
                "department": "Sales and Marketing",
                "skype": "Zoho",
                "is_primary_contact": true,
                "enable_portal": true
            }
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}
```

## Update a Contact

### Description
Update an existing contact. To delete a contact person, remove it from the contact_persons list.

### Endpoint
`PUT /contacts/{contact_id}`

### OAuth Scope
`ZohoBooks.contacts.UPDATE`

### Arguments (Body Parameters)
*   **contact_name** (string, Required): Display Name of the contact. Max-length [200]
*   **company_name** (string): Company Name of the contact. Max-length [200]
*   **payment_terms** (integer): Net payment term for the customer.
*   **payment_terms_label** (string): Label for the paymet due details.
*   **contact_type** (string): Contact type of the contact
*   **customer_sub_type** (string): Type of the customer
*   **currency_id** (string): Currency ID of the customer's currency.
*   **opening_balances** (array): Opening balance details.
*   **credit_limit** (double): Credit limit for a customer
*   **tags** (array): Filter all your reports based on the tag
*   **website** (string): Website of the contact.
*   **owner_id** (string): For Customer Only : If a contact is assigned to any particular user, that user can manage transactions for the contact.
*   **custom_fields** (array): Custom fields of the contact.
*   **billing_address** (object): Billing address of the contact.
*   **shipping_address** (object): Customer's shipping address object.
*   **contact_persons** (array): Contact persons of a contact.
*   **default_templates** (object): Default templates object.
*   **notes** (string): Commennts about the payment made by the contact.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - For UK Edition: VAT Registration number of a contact with length should be between 2 and 12 characters. For Avalara: If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.
*   **tax_reg_no** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - For GCC Edition: 15 digit Tax Registration number of a contact with Tax treatment as vat_registered,gcc_vat_registered,dz_vat_registered. For Mexico Edition: 12 digit Tax Registration number of a contact with Tax treatment as home_country_mexico, border_region_mexico, non_mexico. Consumers generic RFC: XAXX010101000, Overseas generic RFC: XEXX010101000. For Kenya Edition: 11 digit Tax Registration number of a contact with Tax treatment as vat_registered For SouthAfrica Edition: 10 digit Tax Registration number of a contact with Tax treatment as vat_registered
*   **country_code** (string): 🇬🇧 , GCC , Avalara Integration only - For UK Edition: Two letter country code of a contact. For Avalara: Two letter country code for the customer country, if your customer is not in US. Refer [AvaTax Codes for Countries and States][2]. For GCC Editions : Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as place of supply. Supported codes for UAE emirates are : Abu Dhabi - AB, Ajman - AJ, Dubai - DU, Fujairah - FU, Ras al-Khaimah - RA, Sharjah - SH, Umm al-Quwain - UM. Supported codes for the GCC countries are : United Arab Emirates - AE, Saudi Arabia - SA, Bahrain - BH, Kuwait - KW, Oman - OM, Qatar - QA.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment of the contact. Allowed Values: `vat_registered`,`vat_not_registered`,`gcc_vat_not_registered`,`gcc_vat_registered`,`non_gcc`,`dz_vat_registered` and `dz_vat_not_registered` `home_country_mexico` (A business that is located within MX) `border_region_mexico` (A business that is located in the northern and southern border regions in MX) `non_mexico` (A business that is located outside MX). For Kenya Edition: `vat_registered` ,`vat_not_registered` ,`non_kenya`(A business that is located outside Kenya). For SouthAfrica Edition: `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).
*   **tax_exemption_certificate_number** (string): 🇰🇪 only - Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption
*   **tax_regime** (string): 🇲🇽 only - Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.
*   **legal_name** (string): 🇲🇽 only - Legal Name of the contact.
*   **is_tds_registered** (boolean): 🇲🇽 only - Boolean to check if tax is registered.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment of the contact.Allowed Values: `uk` (A business that is located in the UK.), `eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and `overseas` (A business that is located outside UK. Pre Brexit, this was split as eu_vat_registered, eu_vat_not_registered and non_eu ).
*   **place_of_contact** (string): 🇮🇳 only - Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer/vendor.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **tax_authority_name** (string): Enter tax authority name.
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number of the customer.
*   **avatax_use_code** (string): Avalara Integration only - Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code.
*   **tax_exemption_id** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - ID of the tax exemption.
*   **tax_exemption_code** (string): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 only - Enter tax exemption code
*   **tax_authority_id** (string): 🇺🇸 only - ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
*   **tax_id** (string): 🇮🇳 , 🇺🇸 only - ID of the tax or tax group that can be collected from the contact. Tax can be given only if is_taxable is true.
*   **is_taxable** (boolean): 🇺🇸 , 🇨🇦 , 🇦🇺 , 🇮🇳 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Boolean to track the taxability of the customer.
*   **facebook** (string): Facebook profile account. max-length [100]
*   **twitter** (string): Twitter account. max-length [100]
*   **track_1099** (boolean): 🇺🇸 only - Boolean to track a contact for 1099 reporting.
*   **tax_id_type** (string): 🇺🇸 only - Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.
*   **tax_id_value** (string): 🇺🇸 only - Tax ID of the contact.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'
```

#### Body Parameters
```json
{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "currency_id": 460000000000097,
    "opening_balances": [
        {
            "location_id": "460000000038080",
            "exchange_rate": 1,
            "opening_balance_amount": 1200
        }
    ],
    "credit_limit": 1000,
    "tags": [
        {
            "tag_id": 462000000009070,
            "tag_option_id": 462000000002670
        }
    ],
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "custom_fields": [
        {
            "index": 1,
            "value": "GBGD078",
            "label": "VAT ID"
        }
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": [
        {
            "contact_person_id": 460000000026051,
            "salutation": "Mr",
            "first_name": "Will",
            "last_name": "Smith",
            "email": "willsmith@bowmanfurniture.com",
            "phone": "+1-925-921-9201",
            "mobile": "+1-4054439562",
            "designation": "Sales Executive",
            "department": "Sales and Marketing",
            "skype": "Zoho",
            "is_primary_contact": true,
            "enable_portal": true
        }
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "vat_reg_no": "string",
    "tax_reg_no": 12345678912345,
    "country_code": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "vat_treatment": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Contact has been updated successfully",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balances": [
            {
                "location_id": "460000000038080",
                "exchange_rate": 1,
                "opening_balance_amount": 1200
            }
        ],
        "location_id": "460000000038080",
        "location_name": "string",
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [
            {
                "index": 1,
                "value": "GBGD078",
                "label": "VAT ID"
            }
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [
            {
                "contact_person_id": 460000000026051,
                "salutation": "Mr",
                "first_name": "Will",
                "last_name": "Smith",
                "email": "willsmith@bowmanfurniture.com",
                "phone": "+1-925-921-9201",
                "mobile": "+1-4054439562",
                "designation": "Sales Executive",
                "department": "Sales and Marketing",
                "skype": "Zoho",
                "is_primary_contact": true,
                "enable_portal": true
            }
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}
```

# Estimates

## Overview

### Estimates
An estimate is a quote or a proposal for the products you sell or the services you render to your clients to take your business forward.

### End Points
*   `POST /estimates`
*   `PUT /estimates` *(Note: This is likely for bulk/keyed updates, see Update Estimate using Custom Field)*
*   `GET /estimates`
*   `PUT /estimates/{estimate_id}`
*   `GET /estimates/{estimate_id}`
*   `DELETE /estimates/{estimate_id}`
*   `PUT /estimate/{estimate_id}/customfields`
*   `POST /estimates/{estimate_id}/status/sent`
*   `POST /estimates/{estimate_id}/status/accepted`
*   `POST /estimates/{estimate_id}/status/declined`
*   `POST /estimates/{estimate_id}/submit`
*   `POST /estimates/{estimate_id}/approve`
*   `POST /estimates/{estimate_id}/email`
*   `GET /estimates/{estimate_id}/email`
*   `POST /estimates/email`
*   `GET /estimates/pdf`
*   `GET /estimates/print`
*   `PUT /estimates/{estimate_id}/address/billing`
*   `PUT /estimates/{estimate_id}/address/shipping`
*   `GET /estimates/templates`
*   `PUT /estimates/{estimate_id}/templates/{template_id}`
*   `POST /estimates/{estimate_id}/comments`
*   `GET /estimates/{estimate_id}/comments`
*   `PUT /estimates/{estimate_id}/comments/{comment_id}`
*   `DELETE /estimates/{estimate_id}/comments/{comment_id}`

### Attributes
*   **estimate_id** (string): The unique id of a particular estimate
*   **estimate_number** (string): Search estimates by estimate number. Variants: `estimate_number_startswith` and `estimate_number_contains`
*   **date** (string): Search estimates by estimate date. Variants: `date_start`, `date_end`, `date_before` and `date_after`
*   **reference_number** (string): Search estimates by reference number. Variants: `reference_number_startswith` and `reference_number_contains`
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable for transactions that fall before july 1, 2017
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place where the goods/services are supplied to. (If not given, place of contact given for the contact will be taken) Supported codes for UAE emirates are : Abu Dhabi - AB, Ajman - AJ, Dubai - DU, Fujairah - FU, Ras al-Khaimah - RA, Sharjah - SH, Umm al-Quwain - UM. Supported codes for the GCC countries are : United Arab Emirates - AE, Saudi Arabia - SA, Bahrain - BH, Kuwait - KW, Oman - OM, Qatar - QA.
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment for the Estimate. Allowed Values: `vat_registered`,`vat_not_registered`,`gcc_vat_not_registered`,`gcc_vat_registered`,`non_gcc`. `dz_vat_registered` and `dz_vat_not_registered` supported only for UAE. `home_country_mexico`,`border_region_mexico`,`non_mexico` supported only for MX. For Kenya Edition: `vat_registered` ,`vat_not_registered` ,`non_kenya`(A business that is located outside Kenya). For SouthAfrica Edition: `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is vat_registered) Used to specify whether the transaction is applicable for Domestic Reverse Charge (DRC) or not.
*   **status** (string): Search estimates by status. Allowed Values: `draft`, `sent`, `invoiced` , `accepted`, `declined` and `expired`
*   **customer_id** (string): Search estimates by customer id..
*   **customer_name** (string): Search estimates by customer name. Variants: `customer_name_startswith` and `customer_name_contains`
*   **contact_persons** (array): Array if contact person(S) for whom estimate has to be sent.
*   **currency_id** (string): The id of the customer's currency.
*   **currency_code** (string): Currency code of the currency in which the customer wants to pay. If currency_code is not specified here, the currency chosen in your Zoho Subscriptions organization will be used for billing. currency_id and currency_symbol are set automatically in accordance to the currency_code.
*   **exchange_rate** (double): Exchange rate of the currency.
*   **expiry_date** (string): The date of expiration of the estimates
*   **discount** (double): Discount applied to the estimate. It can be either in % or in amount. e.g. 12.5% or 190.
*   **is_discount_before_tax** (boolean): Used to specify how the discount has to applied. Either before or after the calculation of tax.
*   **discount_type** (string): How the discount is specified. Allowed values are entity_level or item_level. Allowed Values: `entity_level` and `item_level`
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Used to specify whether the line item rates are inclusive or exclusive of tax.
*   **line_items** (array): Line items of an estimate.
*   **location_id** (string): Location ID
*   **location_name** (string): Name of the location.
*   **shipping_charge** (string): Shipping charges applied to the estimate.
*   **adjustment** (double): Adjustments made to the estimate.
*   **adjustment_description** (string): Customize the adjustment description. E.g. Rounding off.
*   **sub_total** (float): The sub total of the all items
*   **total** (double): Search estimates by estimate total. Variants: `total_less_than`, `total_less_equals`, `total_greater_than` and `total_greater_equals`
*   **tax_total** (double): The total amount of the tax levied
*   **price_precision** (integer): The precision value on the price
*   **taxes** (array): List of the taxes levied
*   **billing_address** (object): The billing address
*   **shipping_address** (object): The shipping address
*   **notes** (string): The notes added below expressing gratitude or for conveying some information.
*   **terms** (string): Terms and Conditions.
*   **custom_fields** (array): Custom fields for an estimate.
*   **template_id** (string): ID of the pdf template associated with the estimate.
*   **template_name** (string): Name of the template.
*   **created_time** (string): The time of creation of the estimates
*   **last_modified_time** (string): Last modified time.
*   **salesperson_id** (string): ID of the sales person.
*   **salesperson_name** (string): Name of the sales person.
*   **project** (object): Project details associated with the estimate.

### Example
```json
{
    "estimate_id": 982000000567011,
    "estimate_number": "EST-00002",
    "date": "2013-11-18",
    "reference_number": "QRT-12346",
    "is_pre_gst": false,
    "place_of_supply": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "status": "draft",
    "customer_id": 982000000567001,
    "customer_name": "Bowman & Co",
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ],
    "currency_id": 982000000000190,
    "currency_code": "USD",
    "exchange_rate": 1,
    "expiry_date": "2013-11-30",
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "line_items": [
        {
            "item_id": " ",
            "line_item_id": 982000000567021,
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "item_order": 1,
            "product_type": "goods",
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "bcy_rate": 120,
            "rate": 120,
            "quantity": 1,
            "unit": " ",
            "discount_amount": 0,
            "discount": 0,
            "tax_id": "982000000557028",
            "tds_tax_id": "982000000557012",
            "tax_name": "VAT",
            "tax_type": "tax",
            "tax_percentage": 12.5,
            "tax_treatment_code": "uae_others",
            "item_total": 120,
            "location_id": "460000000038080",
            "location_name": "string"
        }
    ],
    "location_id": "460000000038080",
    "location_name": "string",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "sub_total": 153,
    "total": 40.6,
    "tax_total": 22.6,
    "price_precision": 2,
    "taxes": [
        {
            "tax_name": "VAT",
            "tax_amount": 19.13
        }
    ],
    "billing_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "shipping_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "custom_fields": [
        {
            "index": 1,
            "show_on_pdf": false,
            "value": "15 Dec 2013",
            "label": "Delivery Date"
        }
    ],
    "template_id": 982000000000143,
    "template_name": "Service - Classic",
    "created_time": "2013-11-18T02:17:40-0800",
    "last_modified_time": "2016-06-17T04:46:45-0500",
    "salesperson_id": 982000000567003,
    "salesperson_name": "Will smith",
    "project": {
        "project_id": 90300000087378,
        "project_name": "Sample Project"
    }
}
```

## Add Comment to Estimate

### Description
Add a comment for an estimate.

### Endpoint
`POST /estimates/{estimate_id}/comments`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Arguments (Body Parameters)
*   **description** (string): The comment text.
*   **show_comment_to_clients** (boolean): Boolean to show the comments to contacts in portal.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Estimate marked as sent", "show_comment_to_clients": true}'
```

#### Body Parameters
```json
{
    "description": "Estimate marked as sent",
    "show_comment_to_clients": true
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added"
}
```

## Approve an Estimate

### Description
Approve an estimate.

### Endpoint
`POST /estimates/{estimate_id}/approve`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the estimate."
}
```

## Bulk Export Estimates (PDF)

### Description
Maximum of 25 estimates can be exported in a single pdf.

### Endpoint
`GET /estimates/pdf`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Query Parameters
*   **estimate_ids** (string, Required): Comma separated estimate ids which are to be exported.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates/pdf?organization_id=10234695&estimate_ids=982000000567011,982000000567012' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output estimates_export.pdf
```
*(Note: The response will be the PDF file content)*

### Response Example (on error)
```json
{
    "code": 400, /* Example error code */
    "message": "Invalid value passed for estimate_ids"
}
```
*(Note: A successful response would be the binary data of the PDF file.)*

## Bulk Print Estimates

### Description
Export estimates as pdf and print them. Maximum of 25 estimates can be printed. (Likely returns PDF data intended for printing).

### Endpoint
`GET /estimates/print`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Query Parameters
*   **estimate_ids** (string, Required): Comma separated estimate ids which are to be printed.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates/print?organization_id=10234695&estimate_ids=982000000567011,982000000567012' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output estimates_print.pdf
```
*(Note: The response will likely be the PDF file content suitable for printing)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful response likely returns the binary data of the PDF file, similar to the bulk export.)*

## Create an Estimate

### Description
Create an estimate for your customer.

### Endpoint
`POST /estimates`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): ID of the customer.
*   **currency_id** (string): ID of the currency.
*   **contact_persons** (array): Array of contact person(s) IDs.
*   **template_id** (string): ID of the pdf template.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place where the goods/services are supplied to. (See Overview for codes).
*   **gst_treatment** (string): 🇮🇳 only - (`business_gst`, `business_none`, `overseas`, `consumer`).
*   **gst_no** (string): 🇮🇳 only - 15 digit GST number.
*   **estimate_number** (string): Estimate number (mandatory if auto-gen disabled).
*   **reference_number** (string): Reference number.
*   **date** (string): Estimate date (yyyy-mm-dd).
*   **expiry_date** (string): Expiration date (yyyy-mm-dd).
*   **exchange_rate** (double): Exchange rate.
*   **discount** (double): Discount amount or percentage (e.g., 10.0 or "10%").
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **discount_type** (string): (`entity_level`, `item_level`).
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Are line item rates inclusive of tax.
*   **custom_body** (string): Custom email body content.
*   **custom_subject** (string): Custom email subject.
*   **salesperson_name** (string): Name of the sales person.
*   **custom_fields** (array): Custom fields for the estimate.
*   **line_items** (array, Required): Line items of the estimate.
    *   Include standard line item attributes (item_id, name, description, rate, quantity, tax_id, etc.).
*   **location_id** (string): Location ID.
*   **notes** (string): Notes for the estimate.
*   **terms** (string): Terms and conditions.
*   **shipping_charge** (string): Shipping charges.
*   **adjustment** (double): Adjustments.
*   **adjustment_description** (string): Description for adjustments.
*   **tax_id** (string): ID of the tax/tax group applied overall.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 only - Tax exemption ID.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **avatax_use_code** (string): Avalara Integration only - Avalara use code.
*   **avatax_exempt_no** (string): Avalara Integration only - Avalara exemption number.
*   **vat_treatment** (string): 🇬🇧 only - (`uk`, `eu_vat_registered`, `overseas`).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (See Overview for values).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is `vat_registered`).
*   **accept_retainer** (boolean): Allow automatic retainer invoice creation on acceptance.
*   **retainer_percentage** (integer): Percentage for automatic retainer invoice (0-100).

### Query Parameters
*   **send** (boolean): Send the estimate to the contact person(s) after creation.
*   **ignore_auto_number_generation** (boolean): Ignore auto estimate number generation. Mandates providing `estimate_number`.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "date": "2013-11-18", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ],
    "template_id": 982000000000143,
    "place_of_supply": "TN",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "estimate_number": "EST-00002",
    "reference_number": "QRT-12346",
    "date": "2013-11-18",
    "expiry_date": "2013-11-30",
    "exchange_rate": 1,
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "custom_body": " ",
    "custom_subject": " ",
    "salesperson_name": "Will smith",
    "custom_fields": [
        {
            "index": 1,
            "value": "15 Dec 2013"
        }
    ],
    "line_items": [
        {
            /* item_id can be omitted if creating ad-hoc item */
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "item_order": 1,
            "rate": 120,
            "quantity": 1,
            "tax_id": "982000000557028",
            "tds_tax_id": "982000000557012",
            "tax_treatment_code": "uae_others",
            "location_id": "460000000038080"
        }
    ],
    "location_id": "460000000038080",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "tax_id": "982000000557028",
    "tax_exemption_id": 11149000000061054,
    "tax_authority_id": 11149000000061052,
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "project_id": 90300000087378,
    "accept_retainer": true,
    "retainer_percentage": 10
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The estimate has been created",
    "estimate": {
        "estimate_id": 982000000567011,
        "estimate_number": "EST-00002",
        "date": "2013-11-18",
        "status": "draft",
        /* ... other details ... */
    }
}
```

## Delete an Estimate

### Description
Delete an existing estimate.

### Endpoint
`DELETE /estimates/{estimate_id}`

### OAuth Scope
`ZohoBooks.estimates.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The estimate has been deleted."
}
```

## Delete Estimate Comment

### Description
Delete an existing comment of an estimate. *(Note: Filename was "Update Estimate Comment", content corrected).*

### Endpoint
`DELETE /estimates/{estimate_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.estimates.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been deleted successfully." /* Corrected from update message */
}
```

## Email an Estimate

### Description
Email an estimate to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

### Endpoint
`POST /estimates/{estimate_id}/email`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Arguments (Body Parameters)
*   **send_from_org_email_id** (boolean): Boolean to trigger the email from the organization's email address.
*   **to_mail_ids** (array, Required): Array of email address of the recipients.
*   **cc_mail_ids** (array): Array of email address of the recipients to be cced.
*   **subject** (string): Subject of an email has to be sent.
*   **body** (string): Body of an email has to be sent.

### Query Parameters
*   **attachments**: Files to be attached to the email (sent as multipart/form-data along with JSON body).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"send_from_org_email_id": false, "to_mail_ids": ["willsmith@bowmanfurniture.com"], "cc_mail_ids": ["peterparker@bowmanfurniture.com"], "subject": "Estimate EST-00002 from Zillium Inc", "body": "Dear Customer..."}'
```
*(Note: Attaching files requires sending as multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "send_from_org_email_id": false,
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "subject": "Statement of transactions with Zillium Inc",
    "body": "Dear Customer,   Thanks for your business enquiry.         The estimate EST-000002 is attached with this email.        We can get started if you send us your consent. For any assistance you can reach us via email or phone.         Looking forward to hearing back from you. Here's an overview of the estimate for your reference.        Estimate Overview:        Estimate  : EST-000002         Date : 03 Oct 2013        Amount : $36.47 Regards<br>\\nZillium Inc<br>\\n\"\""
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your estimate has been sent."
}
```

## Email Multiple Estimates

### Description
Send estimates to your customers by email. Maximum of 10 estimates can be sent at once.

### Endpoint
`POST /estimates/email`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Query Parameters
*   **estimate_ids** (string, Required): Comma separated estimate ids which are to be emailed.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/email?organization_id=10234695&estimate_ids=982000000567011,982000000567012' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Mission accomplished! We've sent all the estimates."
}
```

## Get Estimate Email Content

### Description
Get the email content of an estimate based on a template. *(Note: Filename was "Get Estimate Email Contact", corrected here)*.

### Endpoint
`GET /estimates/{estimate_id}/email`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Query Parameters
*   **email_template_id** (string): Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used. *(Note: Param marked Required in original doc, but logic suggests optional)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/email?organization_id=10234695&email_template_id=982000000000079' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": /* Original showed array, likely single object */
    {
        "body": "Dear Customer,   Thanks for your business enquiry.         The estimate EST-000002 is attached with this email.        We can get started if you send us your consent. For any assistance you can reach us via email or phone.         Looking forward to hearing back from you. Here's an overview of the estimate for your reference.        Estimate Overview:        Estimate  : EST-000002         Date : 03 Oct 2013        Amount : $36.47 Regards<br>\\nZillium Inc<br>\\n\"\"",
        "error_list": [],
        "subject": "Statement of transactions with Zillium Inc",
        "emailtemplates": [
            {
                "selected": true,
                "name": "Default",
                "email_template_id": 982000000000079
            }
        ],
        "to_contacts": [
            {
                "first_name": "Sujin",
                "selected": true, /* Original had typo 'fasle' */
                "phone": "+1-925-921-9201",
                "email": "string",
                "last_name": "Kumar",
                "salutation": ":Mr",
                "contact_person_id": "982000000567003",
                "mobile": "+1-4054439562"
            }
        ],
        "file_name": "EST-00001.pdf",
        "from_emails": [
            {
                "user_name": "John Smith",
                "selected": true, /* Original had typo 'fasle' */
                "email": "string"
            }
        ],
        "customer_id": 982000000567001
    }
}
```

## List Estimate Comments and History

### Description
Get the complete history and comments of an estimate.

### Endpoint
`GET /estimates/{estimate_id}/comments`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": 982000000567019,
            "estimate_id": 982000000567011,
            "description": "Estimate created",
            "commented_by_id": 982000000554041,
            "commented_by": "Sujin Kumar",
            "comment_type": "system",
            "date": "2013-11-18",
            "date_description": "yesterday",
            "time": "2:02 AM",
            "operation_type": "Added",
            "transaction_id": " ",
            "transaction_type": "estimate"
        },
        {...},
        {...}
    ]
}
```

## List Estimate Templates

### Description
Get all estimate pdf templates.

### Endpoint
`GET /estimates/templates`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Service - Classic",
            "template_id": 982000000000143,
            "template_type": "classic"
        },
        {...},
        {...}
    ]
}
```

## List Estimates

### Description
List all estimates with pagination.

### Endpoint
`GET /estimates`

### OAuth Scope
`ZohoBooks.estimates.READ`

### Query Parameters
*   **estimate_number** (string): Search by estimate number (variants: `_startswith`, `_contains`).
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`).
*   **customer_name** (string): Search by customer name (variants: `_startswith`, `_contains`).
*   **total** (double): Search by total amount (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **customer_id** (string): Search by customer ID.
*   **item_id** (string): Search by item ID.
*   **item_name** (string): Search by item name (variants: `_startswith`, `_contains`).
*   **item_description** (string): Search by item description (variants: `_startswith`, `_contains`).
*   **custom_field** (string): Search by custom field (variants: `_startswith`, `_contains`).
*   **expiry_date** (string): Search by expiration date.
*   **date** (string): Search by estimate date (variants: `_start`, `_end`, `_before`, `_after`).
*   **status** (string): Search by status. Allowed Values: `draft`, `sent`, `invoiced` , `accepted`, `declined`, `expired`.
*   **filter_by** (string): Filter estimates by status. Allowed Values: `Status.All`, `Status.Sent`, `Status.Draft`, `Status.Invoiced`, `Status.Accepted`, `Status.Declined`, `Status.Expired`.
*   **search_text** (string): Search estimates by estimate number, reference, or customer name.
*   **sort_column** (string): Sort estimates. Allowed Values: `customer_name`, `estimate_number`, `date`, `total`, `created_time`.
*   **zcrm_potential_id** (string): Potential ID of a Deal in CRM.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/estimates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "estimates": [
        {
            "estimate_id": 982000000567011,
            "customer_name": "Bowman & Co",
            "customer_id": 982000000567001,
            "status": "draft",
            "estimate_number": "EST-00002",
            "reference_number": "QRT-12346",
            "date": "2013-11-18",
            "currency_id": 982000000000190,
            "currency_code": "USD",
            "total": 40.6,
            "location_id": "460000000038080",
            "location_name": "string",
            "created_time": "2013-11-18T02:17:40-0800",
            "last_modified_time": "2016-06-17T04:46:45-0500",
            "accepted_date": " ",
            "declined_date": " ",
            "expiry_date": "2013-11-30",
            "has_attachment": false,
            "is_viewed_by_client": true,
            "client_viewed_time": "2016-06-19T05:49:12-0500"
        },
        {...},
        {...}
    ],
    "page_context": /* Original showed array, corrected to object */
    {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Estimates",
        "applied_filter": "Status.All",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Mark an Estimate as Accepted

### Description
Mark a sent estimate as accepted if the customer has accepted it.

### Endpoint
`POST /estimates/{estimate_id}/status/accepted`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/status/accepted?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate status has been changed to Accepted."
}
```

## Mark an Estimate as Declined

### Description
Mark a sent estimate as declined if the customer has rejected it.

### Endpoint
`POST /estimates/{estimate_id}/status/declined`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/status/declined?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate status has been changed to Declined."
}
```

## Mark Estimate as Sent

### Description
Mark a draft estimate as sent.

### Endpoint
`POST /estimates/{estimate_id}/status/sent`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/status/sent?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate status has been changed to Sent"
}
```

## Submit Estimate for Approval

### Description
Submit an estimate for approval.

### Endpoint
`POST /estimates/{estimate_id}/submit`

### OAuth Scope
`ZohoBooks.estimates.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The estimate has been successfully submitted for approval"
}
```

## Update an Estimate

### Description
Update an existing estimate. To delete a line item just remove it from the line_items list. *(Note: Filename was "Get an Estimate", content corrected).*

### Endpoint
`PUT /estimates/{estimate_id}`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Arguments (Body Parameters)
*(Same parameters as Create an Estimate, with `line_item_id` required for updating existing lines)*

### Query Parameters
*   **ignore_auto_number_generation** (boolean): Ignore auto estimate number generation for this estimate. This mandates the estimate number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ],
    "template_id": 982000000000143,
    "place_of_supply": "TN",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "estimate_number": "EST-00002",
    "reference_number": "QRT-12346",
    "date": "2013-11-18",
    "expiry_date": "2013-11-30",
    "exchange_rate": 1,
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "custom_body": " ",
    "custom_subject": " ",
    "salesperson_name": "Will smith",
    "custom_fields": [
        {
            "index": 1,
            "value": "15 Dec 2013"
        }
    ],
    "line_items": [
        {
            "line_item_id": 982000000567021, /* Existing line item ID */
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "item_order": 1,
            "rate": 120,
            "quantity": 1,
            "tax_id": "982000000557028",
            "tds_tax_id": "982000000557012",
            "tax_treatment_code": "uae_others",
            "location_id": "460000000038080"
        }
    ],
    "location_id": "460000000038080",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "tax_id": "982000000557028",
    "tax_exemption_id": 11149000000061054,
    "tax_authority_id": 11149000000061052,
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "project_id": 90300000087378,
    "accept_retainer": true,
    "retainer_percentage": 10
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate information has been updated.",
    "estimate": {
        "estimate_id": 982000000567011,
        "estimate_number": "EST-00002",
        /* ... other updated details ... */
    }
}
```

## Update an Estimate using Custom Field

### Description
Update an estimate using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /estimates` *(with custom headers)*

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field for the target estimate.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create a new estimate if the unique value is not found.

### Arguments (Body Parameters)
*(Same parameters as Create an Estimate, with `line_item_id` required for updating existing lines)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ],
    "template_id": 982000000000143,
    "place_of_supply": "TN",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "estimate_number": "EST-00002",
    "reference_number": "QRT-12346",
    "date": "2013-11-18",
    "expiry_date": "2013-11-30",
    "exchange_rate": 1,
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "custom_body": " ",
    "custom_subject": " ",
    "salesperson_name": "Will smith",
    "custom_fields": [
        {
            "index": 1,
            "value": "15 Dec 2013"
        }
    ],
    "line_items": [
        {
            "line_item_id": 982000000567021, /* Optional: Required only if updating existing line */
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "item_order": 1,
            "rate": 120,
            "quantity": 1,
            "tax_id": "982000000557028",
            "tds_tax_id": "982000000557012",
            "tax_treatment_code": "uae_others",
            "location_id": "460000000038080"
        }
    ],
    "location_id": "460000000038080",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "tax_id": "982000000557028",
    "tax_exemption_id": 11149000000061054,
    "tax_authority_id": 11149000000061052,
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "project_id": 90300000087378,
    "accept_retainer": true,
    "retainer_percentage": 10
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate information has been updated.",
    "estimate": {
        "estimate_id": 982000000567011,
        /* ... updated estimate details ... */
    }
}
```

## Update Billing Address

### Description
Updates the billing address for this estimate alone.

### Endpoint
`PUT /estimates/{estimate_id}/address/billing`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Billing address for the estimate.
*   **city** (string): City of the customer’s billing address.
*   **state** (string): State of the customer’s billing address.
*   **zip** (string): Zip code of the customer’s billing address.
*   **country** (string): Country of the customer’s billing address.
*   **fax** (string): Customer's fax number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "B-1104...", "city": "Beijing", "state": "Beijing", "zip": 1000881, "country": "China", "fax": "+86-10-82637827"}'
```

#### Body Parameters
```json
{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District,",
    "city": "Beijing",
    "state": "Beijing",
    "zip": 1000881,
    "country": "China",
    "fax": "+86-10-82637827"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated"
}
```

## Update Custom Field in Estimate

### Description
Update the value of the custom field in an existing estimate.

### Endpoint
`PUT /estimate/{estimate_id}/customfields`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field to update.
    *   **value** (string): The new value for the custom field.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimate/982000000567011/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "46000000012845", "value": "15 Dec 2013"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "46000000012845",
        "value": "15 Dec 2013"
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```

## Update Estimate Comment

### Description
Update an existing comment of an estimate. *(Note: Filename was "Delete Estimate Comment", content corrected).*

### Endpoint
`PUT /estimates/{estimate_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Arguments (Body Parameters)
*   **description** (string): The updated comment text.
*   **show_comment_to_clients** (boolean): Boolean to show the comments to contacts in portal.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Updated comment text", "show_comment_to_clients": false}'
```

#### Body Parameters
```json
{
    "description": "Estimate created", /* Example value from original docs */
    "show_comment_to_clients": false /* Corrected from original " " */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been updated successfully.",
    "comment": {
        "comment_id": 982000000567019,
        "estimate_id": 982000000567011,
        "description": "Estimate created", /* Shows original text in example */
        "commented_by_id": 982000000554041,
        "commented_by": "Sujin Kumar",
        "date": "2013-11-18",
        "date_description": "yesterday",
        "time": "2:02 AM",
        "comment_type": "system"
    }
}
```

## Update Estimate Template

### Description
Update the pdf template associated with the estimate.

### Endpoint
`PUT /estimates/{estimate_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/templates/982000000000143?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Estimate information has been updated."
}
```

## Update Shipping Address

### Description
Updates the shipping address for an existing estimate alone.

### Endpoint
`PUT /estimates/{estimate_id}/address/shipping`

### OAuth Scope
`ZohoBooks.estimates.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Shipping address for the estimate.
*   **city** (string): City of the customer’s shipping address.
*   **state** (string): State of the customer’s shipping address.
*   **zip** (string): Zip code of the customer’s shipping address.
*   **country** (string): Country of the customer’s shipping address.
*   **fax** (string): Customer's fax number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/estimates/982000000567011/address/shipping?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "4900 Hopyard Rd...", "city": "Pleasanton", "state": "CA", "zip": 94588, "country": "U.S.A", "fax": "+1-925-924-9600"}'
```

#### Body Parameters
```json
{
    "address": "4900 Hopyard Rd, Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 94588,
    "country": "U.S.A",
    "fax": "+1-925-924-9600"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Shipping address updated"
}
```
# Sales Order

## Overview

### Sales Order
A sales order is a financial document that confirms an impending sale. It is raised when an initial estimate is approved and the transaction is underway, and details the exact quantity, price and delivery details of the products or services being sold.

### End Points
*   `POST /salesorders`
*   `PUT /salesorders` *(Note: Seems to be used for 'Update using Custom Field')*
*   `GET /salesorders`
*   `PUT /salesorders/{salesorder_id}`
*   `GET /salesorders/{salesorder_id}`
*   `DELETE /salesorders/{salesorder_id}`
*   `PUT /salesorder/{salesorder_id}/customfields`
*   `POST /salesorders/{salesorder_id}/status/open`
*   `POST /salesorders/{salesorder_id}/status/void`
*   `POST /salesorders/{salesorder_id}/substatus/{status_code}`
*   `POST /salesorders/{salesorder_id}/email`
*   `GET /salesorders/{salesorder_id}/email`
*   `POST /salesorders/{salesorder_id}/submit`
*   `POST /salesorders/{salesorder_id}/approve`
*   `GET /salesorders/pdf`
*   `GET /salesorders/print`
*   `PUT /salesorders/{salesorder_id}/address/billing`
*   `PUT /salesorders/{salesorder_id}/address/shipping`
*   `GET /salesorders/templates`
*   `PUT /salesorders/{salesorder_id}/templates/{template_id}`
*   `POST /salesorders/{salesorder_id}/attachment`
*   `PUT /salesorders/{salesorder_id}/attachment` *(Note: Seems to be used for 'Update Attachment Preference')*
*   `GET /salesorders/{salesorder_id}/attachment`
*   `DELETE /salesorders/{salesorder_id}/attachment`
*   `POST /salesorders/{salesorder_id}/comments`
*   `GET /salesorders/{salesorder_id}/comments`
*   `PUT /salesorders/{salesorder_id}/comments/{comment_id}`
*   `DELETE /salesorders/{salesorder_id}/comments/{comment_id}`

### Attributes
*   **salesorder_id** (string): ID of the Sales Order
*   **documents** (array)
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable for transactions that fall before july 1, 2017
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place where the goods/services are supplied to. (Supported codes listed in description).
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment for the sales order (`uk`, `eu_vat_registered`, `overseas`).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment for the sales order (Allowed values vary by region).
*   **zcrm_potential_id** (string)
*   **zcrm_potential_name** (string)
*   **salesorder_number** (string): Mandatory if auto number generation is disabled.
*   **date** (string): The date the sales order is created. Format [yyyy-mm-dd].
*   **status** (string): Status of the Sales Order (e.g., `draft`, `open`, `invoiced`, `closed`, `void`).
*   **shipment_date** (string): Shipping date of sales order. Format [yyyy-mm-dd].
*   **reference_number** (string): Reference Number of the Sales Order.
*   **customer_id** (string): ID of the customer.
*   **customer_name** (string): Name of the customer.
*   **contact_persons** (array): Array of contact person IDs.
*   **currency_id** (string): ID of the Currency.
*   **currency_code** (string): Code of the Currency.
*   **currency_symbol** (string)
*   **exchange_rate** (double): Exchange rate of the currency.
*   **discount_amount** (double)
*   **discount** (string): Discount applied (e.g., "12.5%" or "190").
*   **discount_applied_on_amount** (integer)
*   **is_discount_before_tax** (boolean): Apply discount before tax calculation.
*   **discount_type** (string): Allowed Values: `entity_level`, `item_level`.
*   **estimate_id** (string): ID of the estimate from which the SO was created.
*   **delivery_method** (string)
*   **delivery_method_id** (string)
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Line item rates inclusive of tax.
*   **location_id** (string): Location ID
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items of the sales order.
*   **shipping_charge** (double)
*   **adjustment** (double)
*   **adjustment_description** (string)
*   **sub_total** (double): Sub Total of the Sales Order
*   **tax_total** (double)
*   **total** (double): Total of the Sales Order
*   **taxes** (array): Taxes applied.
*   **price_precision** (integer)
*   **is_emailed** (boolean): Check if the Sales Order is emailed.
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **notes** (string): Notes for this Sales Order
*   **terms** (string)
*   **custom_fields** (array): Custom fields.
*   **template_id** (string): ID of the pdf template.
*   **template_name** (string): Name of the template
*   **page_width** (string)
*   **page_height** (string)
*   **orientation** (string)
*   **template_type** (string): Type of the template
*   **created_time** (string): Creation Time of the Sales Order
*   **last_modified_time** (string): Last Modified time of the Sales Order
*   **created_by_id** (string)
*   **attachment_name** (string)
*   **can_send_in_mail** (boolean): Can the file be sent in mail.
*   **salesperson_id** (string): ID of the salesperson
*   **salesperson_name** (string): Name of the sales person.
*   **merchant_id** (string): ID of the merchant
*   **merchant_name** (string): Name of the merchant

### Example
```json
[
    {
        "salesorder_id": "460000000039129",
        "documents": [
            "document_id",
            "file_name"
        ],
        "is_pre_gst": false,
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "place_of_supply": "TN",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "zcrm_potential_id": "460000000033001",
        "zcrm_potential_name": "string",
        "salesorder_number": "SO-00001",
        "date": "2014-07-28",
        "status": "open",
        "shipment_date": "string",
        "reference_number": "REF-001",
        "customer_id": "460000000017138",
        "customer_name": "SAF Instruments Inc",
        "contact_persons": [
            "460000000870911",
            "460000000870915"
        ],
        "currency_id": "460000000000097",
        "currency_code": "USD",
        "currency_symbol": "$",
        "exchange_rate": 1.233,
        "discount_amount": 0,
        "discount": "string",
        "discount_applied_on_amount": 0,
        "is_discount_before_tax": true,
        "discount_type": "entity_level",
        "estimate_id": "string",
        "delivery_method": "Air",
        "delivery_method_id": "string",
        "is_inclusive_tax": false,
        "location_id": "460000000038080",
        "location_name": "string",
        "line_items": [
            {
                "item_order": 0,
                "item_id": "460000000017088",
                "rate": 120,
                "name": "Hard Drive",
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
                "quantity": 40,
                "product_type": "goods",
                "hsn_or_sac": 80540,
                "sat_item_key_code": 71121206,
                "unitkey_code": "E48",
                "location_id": "460000000038080",
                "location_name": "string",
                "discount": "string",
                "tax_id": "460000000017094",
                "tds_tax_id": "460000000017098",
                "tags": [
                    {
                        "is_tag_mandatory": false,
                        "tag_id": 462000000009070,
                        "tag_name": "Location",
                        "tag_option_id": 462000000002670,
                        "tag_option_name": "USA"
                    }
                ],
                "unit": "Nos",
                "item_custom_fields": [
                    {
                        "customfield_id": "460000000639129",
                        "index": 1,
                        "value": "Normal",
                        "label": "Priority"
                    }
                ],
                "tax_exemption_id": "string",
                "tax_exemption_code": "string",
                "tax_treatment_code": "uae_others",
                "avatax_exempt_no": "string",
                "avatax_use_code": "string",
                "project_id": 90300000087378
            }
        ],
        "shipping_charge": 2,
        "adjustment": 0.2,
        "adjustment_description": "Adjustment",
        "sub_total": 11800,
        "tax_total": 600,
        "total": 12400,
        "taxes": [
            {
                "tax_id": "460000000017094",
                "tax_name": "string",
                "tax_amount": 600
            }
        ],
        "price_precision": 2,
        "is_emailed": false,
        "billing_address": {
            "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
            "street2": "McMillan Avenue",
            "city": "Beijing",
            "state": "Beijing",
            "zip": "1000881",
            "country": "China",
            "fax": "+86-10-82637827",
            "attention": "string"
        },
        "shipping_address": {
            "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
            "street2": "McMillan Avenue",
            "city": "Beijing",
            "state": "Beijing",
            "zip": "1000881",
            "country": "China",
            "fax": "+86-10-82637827",
            "attention": "string"
        },
        "notes": "string",
        "terms": "string",
        "custom_fields": [
            {
                "customfield_id": "460000000639129",
                "index": 1,
                "value": "Normal",
                "label": "Priority"
            }
        ],
        "template_id": "460000000021001",
        "template_name": "Standard Template",
        "page_width": "8.27in",
        "page_height": "11.69in",
        "orientation": "portrait",
        "template_type": "standard",
        "created_time": "2014-07-28T08:29:07+0530",
        "last_modified_time": "2014-08-25T11:23:26+0530",
        "created_by_id": "460000000053001",
        "attachment_name": "string",
        "can_send_in_mail": true,
        "salesperson_id": "460000000000097",
        "salesperson_name": "John Roberts",
        "merchant_id": "460000000000597",
        "merchant_name": "John Louis"
    }
]
```

## Add Attachment to Sales Order

### Description
Attach a file to a sales order.

### Endpoint
`POST /salesorders/{salesorder_id}/attachment`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Query Parameters
*   **(Form Data) attachment**: The file that is to be added.
*   **(Form Data) can_send_in_mail** (boolean): Allow this attachment to be sent in email.
*   **(Form Data) doc**: Document file (alternative to 'attachment'?).
*   **(Form Data) totalFiles** (integer): Total number of files (used with multipart).
*   **(URL) document_ids** (string): Comma-separated IDs of documents to attach (if already uploaded elsewhere).

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/attachment?organization_id=10234695&can_send_in_mail=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/your/file.pdf"
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file has been successfully attached to the sales order."
}
```

## Add Comment to Sales Order

### Description
Add a comment for a sales order.

### Endpoint
`POST /salesorders/{salesorder_id}/comments`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Arguments (Body Parameters)
*   **description** (string): The comment text.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Customer requested change to item quantity."}'
```

#### Body Parameters
```json
{
    "description": "Customer requested change to item quantity."
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": { /* Corrected: Typically returns the single comment added */
        "salesorder_id": "460000000039129",
        "comment_id": "460000000048023",
        "description": "Customer requested change to item quantity.",
        "commented_by_id": "460000000017003",
        "commented_by": "John",
        "comment_type": "user",
        "date": "2014-07-28",
        "date_description": "Moments ago",
        "time": "2:12 PM",
        "operation_type": "Added",
        "transaction_id": null,
        "transaction_type": "salesorder"
    }
}
```

## Approve Sales Order

### Description
Approve a sales order.

### Endpoint
`POST /salesorders/{salesorder_id}/approve`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the Sales Order."
}
```

## Bulk Export Sales Order (PDF)

### Description
Maximum of 25 sales orders can be exported in a single pdf.

### Endpoint
`GET /salesorders/pdf`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **salesorder_ids** (string, Required): Comma separated sales order IDs to export.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/pdf?organization_id=10234695&salesorder_ids=460000000039129,460000000039130' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output salesorders_export.pdf
```
*(Note: The response will be the PDF file content)*

### Response Example (on success metadata)
*(Note: A successful response actually returns the binary data of the PDF file.)*
```json
{
    "code": 0,
    "message": "success"
}
```

## Bulk Print Sales Order

### Description
Export sales orders as pdf and print them. Maximum of 25 sales orders can be printed. (Likely returns PDF data intended for printing).

### Endpoint
`GET /salesorders/print`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **salesorder_ids** (string, Required): Comma separated sales order IDs to print.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/print?organization_id=10234695&salesorder_ids=460000000039129,460000000039130' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output salesorders_print.pdf
```
*(Note: The response will likely be the PDF file content suitable for printing)*

### Response Example (on success metadata)
*(Note: A successful response likely returns the binary data of the PDF file.)*
```json
{
    "code": 0,
    "message": "success"
}
```

## Create a Sales Order

### Description
Create a sales order for your customer.

### Endpoint
`POST /salesorders`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): ID of the customer.
*   **currency_id** (string): ID of the Currency.
*   **contact_persons** (array): Array of contact person IDs.
*   **date** (string): The date the sales order is created. Format [yyyy-mm-dd].
*   **shipment_date** (string): Shipping date. Format [yyyy-mm-dd].
*   **custom_fields** (array): Custom fields.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply. (Supported codes listed in Overview).
*   **salesperson_id** (string): ID of the salesperson.
*   **merchant_id** (string): ID of the merchant.
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: `business_gst`, `business_none`, `overseas`, `consumer`.
*   **gst_no** (string): 🇮🇳 only - 15 digit GST number.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Line item rates inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **billing_address_id** (string): ID of the Billing Address.
*   **shipping_address_id** (string): ID of the Shipping Address.
*   **crm_owner_id** (string)
*   **crm_custom_reference_id** (string)
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is `vat_registered`).
*   **salesorder_number** (string): Mandatory if auto number generation is disabled.
*   **reference_number** (string): Reference Number.
*   **is_update_customer** (boolean): Update billing address of customer.
*   **discount** (string): Discount applied (e.g., "12.5%" or "190").
*   **exchange_rate** (double): Exchange rate.
*   **salesperson_name** (string): Name of the sales person.
*   **notes_default** (string): Default Notes.
*   **terms_default** (string): Default Terms.
*   **tax_id** (string): Tax ID.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 only - Tax exemption ID.
*   **tax_authority_name** (string): 🇺🇸 , 🇲🇽 only - Tax Authority's name.
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 , 🇲🇽 only - Tax Exemption code.
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number.
*   **avatax_use_code** (string): Avalara Integration only - Avalara use code.
*   **shipping_charge** (double)
*   **adjustment** (double)
*   **delivery_method** (string)
*   **estimate_id** (string): ID of the associated estimate.
*   **is_discount_before_tax** (boolean): Apply discount before tax calculation.
*   **discount_type** (string): Allowed Values: `entity_level`, `item_level`.
*   **adjustment_description** (string)
*   **pricebook_id** (string)
*   **template_id** (string): ID of the pdf template.
*   **documents** (array): Array of document IDs/names to attach.
*   **zcrm_potential_id** (string)
*   **zcrm_potential_name** (string)

### Query Parameters
*   **(Form Data) ignore_auto_number_generation** (boolean): Ignore auto sales order number generation.
*   **(Form Data) can_send_in_mail** (boolean): Can the file be sent in mail (relates to attachment).
*   **(Form Data) totalFiles** (integer): Total number of files (used with multipart attachment).
*   **(Form Data) doc**: Document file(s) to be attached.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "460000000017138", "date": "2014-07-28", "line_items": [...] ...}'
```
*(Note: Attaching files requires sending as multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "customer_id": "460000000017138",
    "currency_id": "460000000000097",
    "contact_persons": [
        "460000000870911",
        "460000000870915"
    ],
    "date": "2014-07-28",
    "shipment_date": "2014-08-04",
    "custom_fields": [
        {
            "customfield_id": "460000000639129",
            "value": "Normal"
        }
    ],
    "place_of_supply": "TN",
    "salesperson_id": "460000000000097",
    "merchant_id": "460000000000597",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "line_items": [
        {
            "item_order": 0,
            "item_id": "460000000017088",
            "rate": 120,
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "quantity": 40,
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "location_id": "460000000038080",
            "discount": "0%",
            "tax_id": "460000000017094",
            "tds_tax_id": "460000000017098",
            "tags": [
                {
                    "tag_id": 462000000009070,
                    "tag_option_id": 462000000002670
                }
            ],
            "unit": "Nos",
            "item_custom_fields": [
                {
                    "customfield_id": "460000000639129",
                    "value": "Normal"
                }
            ],
            "tax_exemption_id": null,
            "tax_exemption_code": null,
            "tax_treatment_code": "uae_others",
            "avatax_exempt_no": null,
            "avatax_use_code": null,
            "project_id": 90300000087378
        }
    ],
    "notes": "Sales Order notes",
    "terms": "Sales Order terms",
    "billing_address_id": 460000000032174,
    "shipping_address_id": null,
    "crm_owner_id": null,
    "crm_custom_reference_id": null,
    "vat_treatment": null,
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "salesorder_number": "SO-00001",
    "reference_number": "REF-001",
    "is_update_customer": false,
    "discount": "0%",
    "exchange_rate": 1.233,
    "salesperson_name": "John Roberts",
    "notes_default": null,
    "terms_default": null,
    "tax_id": "460000000017094",
    "tax_authority_id": null,
    "tax_exemption_id": null,
    "tax_authority_name": null,
    "tax_exemption_code": null,
    "avatax_exempt_no": null,
    "avatax_use_code": null,
    "shipping_charge": 2,
    "adjustment": 0.2,
    "delivery_method": "Air",
    "estimate_id": null,
    "is_discount_before_tax": true,
    "discount_type": "entity_level",
    "adjustment_description": "Adjustment",
    "pricebook_id": null,
    "template_id": "460000000021001",
    "documents": [ /* Include only if attaching existing documents by ID */
       /* { "document_id": "..." } */
    ],
    "zcrm_potential_id": "460000000033001",
    "zcrm_potential_name": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Created Successfully.",
    "salesorder": { /* Corrected: Should return single object for single creation */
        "salesorder_id": "460000000039129",
        /* ... full sales order details ... */
        "status": "draft", /* Or 'open' depending on workflow */
        /* ... */
    }
}
```

## Delete a Sales Order

### Description
Delete an existing sales order. Invoiced sales order cannot be deleted.

### Endpoint
`DELETE /salesorders/{salesorder_id}`

### OAuth Scope
`ZohoBooks.salesorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Deleted Successfully."
}
```

## Delete Sales Order Attachment

### Description
Delete the file attached to the sales order.

### Endpoint
`DELETE /salesorders/{salesorder_id}/attachment`

### OAuth Scope
`ZohoBooks.salesorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file is no longer attached to the sales order."
}
```

## Delete Sales Order Comment

### Description
Delete a sales order comment.

### Endpoint
`DELETE /salesorders/{salesorder_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.salesorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/comments/460000000048023?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Email a Sales Order

### Description
Email a sales order to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

### Endpoint
`POST /salesorders/{salesorder_id}/email`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Arguments (Body Parameters)
*   **from_address_id** (string): From Address of the Email Address. *(Note: Likely user ID or email alias ID)*
*   **send_from_org_email_id** (boolean): Trigger email from the organization's email address.
*   **to_mail_ids** (array, Required): Array of recipient email addresses.
*   **cc_mail_ids** (array): Array of CC recipient email addresses.
*   **bcc_mail_ids** (array): Array of BCC recipient email addresses.
*   **subject** (string, Required): Subject of the mail.
*   **documents** (binary): Documents to attach (sent via multipart). *(Note: This seems wrong, body is usually JSON, attachments are multipart)*
*   **invoice_id** (string): ID of the invoice (if related). *(Note: Unlikely for a Sales Order email)*
*   **body** (string, Required): Body of the mail.

### Query Parameters
*   **attachments**: File(s) to be attached (sent as multipart/form-data).
*   **send_attachment** (boolean): Send the sales order PDF attachment with the email.
*   **file_name**: Name of the file (likely used with `attachments`).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/email?organization_id=10234695&send_attachment=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["john@safInstruments.com"], "subject": "Sales Order SO-00001", "body": "Please find attached..."}'
```
*(Note: Attaching additional files requires sending as multipart/form-data.)*

#### Body Parameters (JSON part)
```json
{
    "from_address_id": "...", /* ID of sender email/user */
    "send_from_org_email_id": true,
    "to_mail_ids": [
        "john@safInstruments.com"
    ],
    "cc_mail_ids": [
        "smith@safInstruments.com"
    ],
    "bcc_mail_ids": [
        "mark@safInstruments.com"
    ],
    "subject": "Sales Order from Zillium Inc (Sales Order #: SO-00001)",
    "body": "<br>Dear SAF Instruments Inc, <br><br>Thanks for your interest in our services. Please find our sales order attached with this mail.<br><br> An overview of the sales order is available below for your reference:  <br><br> ----------------------------------------------------------------------------------------<br> <h2>Sales Order # : SO-00001</h2><br> ----------------------------------------------------------------------------------------<br> <b> Order Date    :  28 Jul 2014</b><br><b> Amount        :   $12,400.00</b><br>----------------------------------------------------------------------------------------<br><br><span>Assuring you of our best services at all times.</span><br><br><br>Regards,<br><br>John<br>Zillium Inc<br><br><br>"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your Sales Order has been sent."
}
```

## Get a Sales Order

### Description
Get the details of a sales order.

### Endpoint
`GET /salesorders/{salesorder_id}`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **print** (boolean): Print the exported pdf. *(Note: Should be used with `accept=pdf`)*
*   **accept** (string): Response format. Allowed Values: `json`, `csv`, `xml`, `xls`, `xlsx`, `pdf`, `jhtml`, `html`. Default: `json`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "salesorder": { /* Corrected: Should return single object */
        "salesorder_id": "460000000039129",
        "customer_id": "460000000017138",
        "billing_address_id": 460000000032174,
        /* ... other sales order details ... */
        "line_items": [
             /* ... line item details ... */
        ],
        /* ... */
        "sub_statuses": [
            {
                "status_id": "460000000000097",
                "status_code": "cs_openshi",
                "parent_status": "open",
                "description": "Packed is shipped.",
                "display_name": "Open Shipped",
                "label_name": "cs_openshi",
                "color_code": "208eff"
            }
        ],
        /* ... */
    }
}
```

## Get Sales Order Attachment

### Description
Returns the file attached to the sales order.

### Endpoint
`GET /salesorders/{salesorder_id}/attachment`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **preview** (boolean): Get a preview of the attachment (if applicable).
*   **inline** (boolean): Request inline disposition (browser attempts to display).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output downloaded_attachment.pdf
```
*(Note: The response will be the binary file content)*

### Response Example (on success metadata)
*(Note: A successful download returns the file data, not this JSON.)*
```json
{
    "code": 0,
    "message": "Success"
}
```

## Get Sales Order Email Content

### Description
Get the email content of a sales order based on a template.

### Endpoint
`GET /salesorders/{salesorder_id}/email`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **email_template_id** (string): Get content based on a specific template ID. If omitted, uses customer's associated template or default template.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/email?organization_id=10234695&email_template_id=460000000001287' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": { /* Corrected: Response data usually wrapped in 'data' */
        "bcc_mails": [ "string" ],
        "body": "<br>Dear SAF Instruments Inc, ...",
        "error_list": [ "string" ],
        "bcc_mails_str": "string",
        "documents": [ { "document_id": "...", "file_name":"..." } ], /* Example structure */
        "subject": "Sales Order from Zillium Inc (Sales Order #: SO-00001)",
        "customer_name": "SAF Instruments Inc",
        "entity_id": "460000000058039",
        "cc_mails_list": [],
        "file_name": "SO-00001.pdf", /* Name of the SO PDF attachment */
        "from_emails": [
            {
                "organization_contact_id": "460000000053003",
                "user_name": "string",
                "selected": true,
                "email": "string",
                "is_org_email_id": true
            }
        ],
        "file_name_without_extension": "SO-00001",
        "to_mails_str": "string",
        "cc_mails_str": "string",
        "from_email": "string",
        "from_address": "string",
        "emailtemplates": [
            {
                "selected": true,
                "name": "Sales Order Notification Template", /* Corrected name */
                "email_template_id": 460000000001287
            }
        ],
        "to_contacts": [
            {
                "first_name": "string",
                "selected": true,
                "phone": "(555) 555-1234",
                "email": "string",
                "last_name": "string",
                "salutation": "Ms.",
                "contact_person_id": "string",
                "mobile": "string"
            }
        ],
        "attachment_name": "string", /* Name of additional attachments? */
        "emailtemplate_documents": [ "string" ], /* Documents from template? */
        "customer_id": "460000000017138"
    }
}
```

## List Sales Order Comments and History

### Description
Get the complete history and comments of sales order.

### Endpoint
`GET /salesorders/{salesorder_id}/comments`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "salesorder_id": "460000000039129",
            "comment_id": "460000000048023",
            "description": "Sales order created.",
            "commented_by_id": "460000000017003",
            "commented_by": "System",
            "comment_type": "system",
            "date": "2014-07-28",
            "date_description": "2 months ago",
            "time": "8:29 AM",
            "operation_type": "Created",
            "transaction_id": null,
            "transaction_type": null
        },
        {
            "salesorder_id": "460000000039129",
            "comment_id": "460000000048025",
            "description": "Customer requested change to item quantity.",
            "commented_by_id": "460000000017004",
            "commented_by": "Jane Doe",
            "comment_type": "user",
            "date": "2014-07-29",
            "date_description": "2 months ago",
            "time": "10:15 AM",
            "operation_type": "Added",
            "transaction_id": null,
            "transaction_type": null
        }
     ]
}
```

## List Sales Order Templates

### Description
Get all sales order pdf templates.

### Endpoint
`GET /salesorders/templates`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Standard Template",
            "template_id": "460000000021001",
            "template_type": "standard"
        },
        {...},
        {...}
    ]
}
```

## List Sales Orders

### Description
List all sales orders.

### Endpoint
`GET /salesorders`

### OAuth Scope
`ZohoBooks.salesorders.READ`

### Query Parameters
*   **sort_column** (string): Sort sales orders. Allowed Values: `customer_name`, `salesorder_number`, `shipment_date`, `last_modified_time`, `reference_number` , `total`, `date`, `created_time`.
*   **search_text** (string): Search by sales order number, reference number, or customer name.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Open`, `Status.Draft`, `Status.OverDue`, `Status.PartiallyInvoiced`, `Status.Invoiced`, `Status.Void`, `Status.Closed`.
*   **salesorder_number** (string): Search by Sales Order Number (variants: `_startswith`, `_not_in`, `_in`, `_contains`). Max Length: 100.
*   **item_name** (string): Search by item name (variants: `_startswith`, `_not_in`, `_in`, `_contains`). Max Length: 100.
*   **item_id** (string): Search by Item ID.
*   **item_description** (string): Search by item description (variants: `_startswith`, `_not_in`, `_in`, `_contains`). Max Length: 100.
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_not_in`, `_in`, `_contains`).
*   **customer_name** (string): Search by customer name (variants: `_startswith`, `_not_in`, `_in`, `_contains`). Max Length: 100.
*   **total** (double): Search by total amount (variants: `_start`, `_end`, `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **date** (string): Search by sales order date (variants: `_start`, `_end`, `_before`, `_after`). Default format: yyyy-mm-dd.
*   **shipment_date** (string): Search by shipment date (variants: `_start`, `_end`, `_before`, `_after`). Default format: yyyy-mm-dd.
*   **status** (string): Search by status. Allowed Values: `draft`, `open`, `invoiced`, `partially_invoiced`, `void`, `overdue`.
*   **customer_id** (string): Search by customer ID.
*   **salesperson_id** (string): ID of the salesperson.
*   **salesorder_ids** (string): Comma separated list of sales order IDs. Max Length: 200.
*   **zcrm_potential_id** (string): CRM Potential ID.
*   **last_modified_time** (string): Filter by last modified time.
*   **accept** (string): Response format. Allowed Values: `json`, `csv`, `xml`, `xls`, `xlsx`, `pdf`, `jhtml`, `html`. Default: `json`.
*   **print** (boolean): Print the exported pdf (used with accept=pdf and salesorder_ids).
*   **customview_id** (string): ID of the custom view.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/salesorders?organization_id=10234695&status=open' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "salesorders": [
        {
            "salesorder_id": "460000000039129",
            "zcrm_potential_id": "460000000033001",
            "zcrm_potential_name": "string",
            "customer_name": "SAF Instruments Inc",
            "customer_id": "460000000017138",
            "status": "open",
            "salesorder_number": "SO-00001",
            "reference_number": "REF-001",
            "date": "2014-07-28",
            "shipment_date": "string",
            "shipment_days": 2, /* Example, not in overview */
            "currency_id": "460000000000097",
            "currency_code": "USD",
            "total": 12400.00,
            "sub_total": 11800.00,
            "bcy_total": 12400.00, /* Base currency total */
            "created_time": "2014-07-28T08:29:07+0530",
            "last_modified_time": "2014-08-25T11:23:26+0530",
            "is_emailed": false,
            "has_attachment": false,
            "custom_fields": [
                {
                    "customfield_id": "460000000639129",
                    "index": 1,
                    "value": "Normal",
                    "label": "Priority"
                }
            ]
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context object */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "SalesOrders",
        "applied_filter": "Status.Open",
        "sort_column": "created_time",
        "sort_order": "A"
     }
}
```

## Mark a Sales Order as Open

### Description
Mark a draft sales order as open.

### Endpoint
`POST /salesorders/{salesorder_id}/status/open`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/status/open?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales order status has been changed to Open."
}
```

## Mark a Sales Order as Void

### Description
Mark a sales order as void.

### Endpoint
`POST /salesorders/{salesorder_id}/status/void`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Arguments (Body Parameters)
*   **reason** (string): Reason to convert sales order as void. Maximum Length: 500.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"reason": "Customer canceled order."}'
```

#### Body Parameters
```json
{
    "reason": "Customer canceled order."
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales order status has been changed to Void."
}
```

## Submit Sales Order for Approval

### Description
Submit a sales order for approval.

### Endpoint
`POST /salesorders/{salesorder_id}/submit`

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The Sales Order has been successfully submitted for approval."
}
```

## Update Sales Order Template

### Description
Update the pdf template associated with the sales order.

### Endpoint
`PUT /salesorders/{salesorder_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/templates/460000000021001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Updated Successfully." /* Message indicates broader SO update, not just template */
}
```

## Update Shipping Address

### Description
Updates the shipping address for this sales order alone.

### Endpoint
`PUT /salesorders/{salesorder_id}/address/shipping`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.
*   **attention** (string): Attention line.
*   **is_one_off_address** (boolean): Use this address only for this transaction.
*   **is_update_customer** (boolean): Update the customer's default shipping address as well.
*   **is_verified** (boolean): Avalara Integration only - Check if the Address is verified.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/address/shipping?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Shipping Address", "city": "Updated City", ...}'
```

#### Body Parameters
```json
{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
    "city": "Beijing",
    "state": "Beijing",
    "zip": "1000881",
    "country": "China",
    "fax": "+86-10-82637827",
    "attention": "string",
    "is_one_off_address": true,
    "is_update_customer": false,
    "is_verified": true
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Shipping address updated."
}
```

## Update Sales Order Sub Status

### Description
Update a sales order sub status.

### Endpoint
`POST /salesorders/{salesorder_id}/substatus/{status_code}`
*(Note: Replace `{status_code}` with the desired sub-status code, e.g., `cs_openshi`)*

### OAuth Scope
`ZohoBooks.salesorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/substatus/cs_openshi?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order status updated successfully."
}
```

## Update Sales Order Comment

### Description
Update existing comment of a sales order.

### Endpoint
`PUT /salesorders/{salesorder_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Arguments (Body Parameters)
*   **description** (string): The updated comment text.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/comments/460000000048023?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Updated comment: Customer confirmed changes."}'
```

#### Body Parameters
```json
{
    "description": "Updated comment: Customer confirmed changes."
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been updated.",
    "comment": { /* Corrected: Should return single updated comment object */
        "salesorder_id": "460000000039129",
        "comment_id": "460000000048023",
        "description": "Updated comment: Customer confirmed changes.",
        "commented_by_id": "460000000017003",
        "commented_by": "John",
        "comment_type": "user",
        "date": "2014-07-28",
        "date_description": "Moments ago",
        "time": "2:15 PM",
        "operation_type": "Updated",
        "transaction_id": null,
        "transaction_type": "salesorder"
    }
}
```

## Update a Sales Order using Custom Field

### Description
Update a sales order using a custom field's unique value. A custom field will have unique values if it's configured to not accept duplicate values. Use that custom field's value to update a sales order by providing its API name in the `X-Unique-Identifier-Key` header and its value in the `X-Unique-Identifier-Value` header. Based on this value, the corresponding sales order will be retrieved and updated. Optionally, use the `X-Upsert` header: if true and the unique value is not found, a new sales order will be created if necessary payload details are available.

### Endpoint
`PUT /salesorders` (with custom headers)

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field for the target sales order.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create a new sales order if the unique value is not found.

### Arguments (Body Parameters)
*(Same parameters as Update a Sales Order)*
*   ...

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "460000000017138", "date": "2014-07-28", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "460000000017138",
    /* ... include all other fields to update or create ... */
    "line_items": [
        {
            "line_item_id": "460000000039131", /* Required if updating existing line */
            /* ... updated line item details ... */
            "quantity": 50 /* Example update */
        }
        /* Omit line items to delete */
        /* Add new line items without line_item_id */
    ],
    "custom_fields": [
         /* Include the custom field specified in headers */
         { "api_name": "cf_unique_cf", "value": "unique Value" },
         /* Include other custom fields to update */
         { "customfield_id": "...", "value": "..." }
    ]
    /* ... */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Updated Successfully.", /* Or "Created" if upserted */
    "salesorder": { /* Corrected: Should return single object */
        "salesorder_id": "...", /* ID of updated or created SO */
        /* ... updated or created sales order details ... */
    }
}
```

## Update a Sales Order

### Description
Update an existing sales order. To delete a line item just remove it from the line_items list.

### Endpoint
`PUT /salesorders/{salesorder_id}`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Arguments (Body Parameters)
*(Same parameters as Create a Sales Order, but `line_items` require `line_item_id` for updates)*
*   ...

### Query Parameters
*   **(Form Data) ignore_auto_number_generation** (boolean): Ignore auto sales order number generation.
*   **(Form Data) can_send_in_mail** (boolean): Can the file be sent in mail (relates to attachment).
*   **(Form Data) totalFiles** (integer): Total number of files (used with multipart attachment).
*   **(Form Data) doc**: Document file(s) to be attached.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "460000000017138", "date": "2014-07-28", "line_items": [...] ...}'
```
*(Note: Attaching files requires sending as multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "customer_id": "460000000017138",
    /* ... include all fields to update ... */
    "line_items": [
        {
            "line_item_id": "460000000039131", /* Required for update */
            "item_id": "460000000017088",
            "rate": 125, /* Updated rate */
            "name": "Hard Drive",
            "description": "Updated description: 500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "quantity": 50 /* Updated quantity */
            /* ... other line item fields ... */
        }
        /* Add new line item objects without line_item_id */
        /* Omit line items to delete them */
    ],
    "notes": "Updated notes",
    "terms": "Updated terms"
    /* ... */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Updated Successfully.",
    "salesorder": { /* Corrected: Should return single updated object */
        "salesorder_id": "460000000039129",
         /* ... updated sales order details ... */
    }
}
```

## Update Attachment Preference

### Description
Set whether you want to send the attached file while emailing the sales order.

### Endpoint
`PUT /salesorders/{salesorder_id}/attachment`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Query Parameters
*   **can_send_in_mail** (boolean, Required): Set to `true` or `false`.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/attachment?organization_id=10234695&can_send_in_mail=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Sales Order Updated Successfully." /* Corrected typo 'Oder' */
}
```

## Update Billing Address

### Description
Updates the billing address for this sales order alone.

### Endpoint
`PUT /salesorders/{salesorder_id}/address/billing`

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **phone** (string): Phone number.
*   **fax** (string): Fax Number.
*   **attention** (string): Attention line.
*   **is_one_off_address** (boolean): Use this address only for this transaction.
*   **is_update_customer** (boolean): Update the customer's default billing address as well.
*   **is_verified** (boolean): Avalara Integration only - Check if the Address is verified.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorders/460000000039129/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Address", "city": "Updated City", ...}'
```

#### Body Parameters
```json
{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
    "city": "Beijing",
    "state": "Beijing",
    "zip": "100088", /* Changed to string */
    "country": "China",
    "phone": "(555) 555-1234",
    "fax": "+86-10-82637827",
    "attention": "string",
    "is_one_off_address": true,
    "is_update_customer": false,
    "is_verified": true
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated."
}
```

## Update Custom Field in Sales Order

### Description
Update the value of the custom field in an existing sales order.

### Endpoint
`PUT /salesorder/{salesorder_id}/customfields` *(Note: Typo in original endpoint path? Should likely be `/salesorders/...`)*

### OAuth Scope
`ZohoBooks.salesorders.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the Custom Field to update.
    *   **index** (integer): Index of the custom field (may not be needed if using ID).
    *   **value** (string): The new value for the custom field.
    *   **label** (string): Label of the custom field (may not be needed if using ID).

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/salesorder/460000000039129/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "460000000639129", "value": "High"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "460000000639129",
        /* "index": 1, Optional if ID is provided */
        "value": "High" /* New value */
        /* "label": "Priority" Optional if ID is provided */
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```
# Invoices

## Overview

### Invoices
Invoice is a document sent to your client that indicates the products/services sold by you with the payment information that the client has to make.

### End Points
*   `POST /invoices`
*   `PUT /invoices` *(Note: Likely for bulk/keyed updates)*
*   `GET /invoices`
*   `PUT /invoices/{invoice_id}`
*   `GET /invoices/{invoice_id}`
*   `DELETE /invoices/{invoice_id}`
*   `POST /invoices/{invoice_id}/status/sent`
*   `POST /invoices/{invoice_id}/status/void`
*   `POST /invoices/{invoice_id}/status/draft`
*   `POST /invoices/email` *(Bulk Email)*
*   `POST /invoices/fromsalesorder`
*   `POST /invoices/{invoice_id}/submit`
*   `POST /invoices/{invoice_id}/approve`
*   `POST /invoices/{invoice_id}/email` *(Single Email)*
*   `GET /invoices/{invoice_id}/email`
*   `POST /invoices/{invoice_id}/paymentreminder`
*   `GET /invoices/{invoice_id}/paymentreminder`
*   `POST /invoices/paymentreminder` *(Bulk Reminder)*
*   `GET /invoices/pdf` *(Bulk PDF Export)*
*   `GET /invoices/print` *(Bulk Print PDF)*
*   `POST /invoices/{invoice_id}/paymentreminder/disable`
*   `POST /invoices/{invoice_id}/paymentreminder/enable`
*   `POST /invoices/{invoice_id}/writeoff`
*   `POST /invoices/{invoice_id}/writeoff/cancel`
*   `PUT /invoices/{invoice_id}/address/billing`
*   `PUT /invoices/{invoice_id}/address/shipping`
*   `GET /invoices/templates`
*   `PUT /invoices/{invoice_id}/templates/{template_id}`
*   `GET /invoices/{invoice_id}/payments`
*   `GET /invoices/{invoice_id}/creditsapplied`
*   `POST /invoices/{invoice_id}/credits` *(Apply Credits - Endpoint not in provided files)*
*   `DELETE /invoices/{invoice_id}/payments/{invoice_payment_id}`
*   `DELETE /invoices/{invoice_id}/creditsapplied/{creditnotes_invoice_id}`
*   `POST /invoices/{invoice_id}/attachment`
*   `PUT /invoices/{invoice_id}/attachment` *(Update Attachment Preference)*
*   `GET /invoices/{invoice_id}/attachment`
*   `DELETE /invoices/{invoice_id}/attachment`
*   `DELETE /invoices/expenses/{expense_id}/receipt`
*   `PUT /invoice/{invoice_id}/customfields` *(Update Custom Fields)*
*   `POST /invoices/{invoice_id}/comments`
*   `GET /invoices/{invoice_id}/comments`
*   `PUT /invoices/{invoice_id}/comments/{comment_id}` *(Update Comment - Endpoint not in provided files)*
*   `DELETE /invoices/{invoice_id}/comments/{comment_id}`
*   `GET /share/paymentlink`

### Attributes
*   **invoice_id** (string): ID of the invoice
*   **ach_payment_initiated** (boolean)
*   **invoice_number** (string): Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length [100]
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable for transactions that fall before july 1, 2017
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place where the goods/services are supplied to. (Supported codes listed in description).
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer.
*   **gst_treatment** (string): 🇮🇳 only - Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are `business_gst` , `business_none` , `overseas` , `consumer` .
*   **cfdi_usage** (string): 🇲🇽 only - Choose CFDI Usage. (Allowed values listed in description).
*   **cfdi_reference_type** (string): 🇲🇽 only - Choose CFDI Reference Type. (Allowed values listed in description).
*   **reference_invoice_id** (string): 🇲🇽 only - Associate the reference invoice.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment for the invoices (`uk`, `eu_vat_registered`, `overseas`).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment for the invoice (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is `vat_registered`).
*   **vat_reg_no** (string): Enter VAT registration number.
*   **date** (string): Search invoices by invoice date. Variants: `date_start`, `date_end`, `date_before`, `date_after`.
*   **status** (string): Search invoices by status. Allowed Values: `sent`, `draft`, `overdue`, `paid`, `void`, `unpaid`, `partially_paid`, `viewed`
*   **payment_terms** (integer): Payment terms in days. Max-length [100]
*   **payment_terms_label** (string): Override default payment terms label. Max-length [100]
*   **due_date** (string): Search invoices by due date. Variants: `due_date_start`, `due_date_end`, `due_date_before`, `due_date_after`.
*   **payment_expected_date** (string)
*   **last_payment_date** (string)
*   **reference_number** (string)
*   **customer_id** (string): ID of the customer.
*   **customer_name** (string): Name of the customer. Max-length [100]
*   **contact_persons** (array): Array of contact person IDs.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **exchange_rate** (float): Exchange rate.
*   **discount** (float): Discount amount or percentage. Max-length [100]
*   **is_discount_before_tax** (boolean): Apply discount before tax calculation.
*   **discount_type** (string): Allowed values: `entity_level`, `item_level`.
*   **is_inclusive_tax** (boolean): Line item rates inclusive of tax.
*   **recurring_invoice_id** (string): ID of the recurring invoice.
*   **is_viewed_by_client** (boolean)
*   **has_attachment** (boolean)
*   **client_viewed_time** (string)
*   **line_items** (array): Invoice line items.
*   **shipping_charge** (string): Shipping charges. Max-length [100]
*   **location_id** (string): Location ID
*   **location_name** (string): Name of the location
*   **adjustment** (double): Adjustments.
*   **adjustment_description** (string): Customize adjustment description.
*   **sub_total** (float): Sub total.
*   **tax_total** (double): Total tax amount.
*   **total** (string): Total amount.
*   **taxes** (array): Taxes applied.
*   **payment_reminder_enabled** (boolean): Reminders enabled.
*   **payment_made** (float): Amount paid.
*   **credits_applied** (float): Credits applied.
*   **tax_amount_withheld** (float): Tax amount withheld.
*   **balance** (string): Unpaid amount.
*   **write_off_amount** (float): Write off amount.
*   **allow_partial_payments** (boolean): Partial payments allowed.
*   **price_precision** (integer): Precision value on price.
*   **payment_options** (object): Payment options.
*   **is_emailed** (boolean): Mail has been sent.
*   **reminders_sent** (integer): Number of reminders sent.
*   **last_reminder_sent_date** (string)
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **custom_fields** (array): Custom fields.
*   **template_id** (string): PDF template ID.
*   **template_name** (string)
*   **created_time** (string): Creation time.
*   **last_modified_time** (string)
*   **attachment_name** (string)
*   **can_send_in_mail** (boolean)
*   **salesperson_id** (string)
*   **salesperson_name** (string): Salesperson name. Max-length [200]
*   **invoice_url** (string)

### Example
```json
{
    "invoice_id": 982000000567114,
    "ach_payment_initiated": false,
    "invoice_number": "INV-00003",
    "is_pre_gst": true,
    "place_of_supply": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "reference_invoice_id": "132738000000126013",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "vat_reg_no": "string",
    "date": "2013-11-17",
    "status": "draft",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "due_date": "2013-12-03",
    "payment_expected_date": " ",
    "last_payment_date": " ",
    "reference_number": " ",
    "customer_id": 982000000567001,
    "customer_name": "Bowman & Co",
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ],
    "currency_id": 982000000000190,
    "currency_code": "USD",
    "exchange_rate": 1,
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "recurring_invoice_id": " ",
    "is_viewed_by_client": false,
    "has_attachment": false,
    "client_viewed_time": "",
    "line_items": [
        {
            "line_item_id": 982000000567021,
            "item_id": 982000000030049,
            "project_id": 90300000087378,
            "sat_item_key_code": 71121206,
            "unitkey_code": "E48",
            "project_name": "Sample Project",
            "time_entry_ids": [],
            "location_id": "460000000038080",
            "location_name": "string",
            "item_type": "goods",
            "product_type": "goods",
            "expense_id": " ",
            "expense_receipt_name": "string",
            "name": "Hard Drive",
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "item_order": 1,
            "bcy_rate": 120,
            "rate": 120,
            "quantity": 1,
            "unit": " ",
            "discount_amount": 0,
            "discount": 0,
            "tags": [
                {
                    "is_tag_mandatory": false,
                    "tag_id": 982000000009070,
                    "tag_name": "Location",
                    "tag_option_id": 982000000002670,
                    "tag_option_name": "USA"
                }
            ],
            "tax_id": 982000000557028,
            "tds_tax_id": "982000000557012",
            "tax_name": "VAT",
            "tax_type": "tax",
            "tax_percentage": 12.5,
            "tax_treatment_code": "uae_others",
            "item_total": 120,
            "header_name": "Electronic devices",
            "header_id": 982000000000670
        }
    ],
    "shipping_charge": 0,
    "location_id": "460000000038080",
    "location_name": "string",
    "adjustment": 0,
    "adjustment_description": " ",
    "sub_total": 10000,
    "tax_total": 22.6,
    "total": 10000,
    "taxes": [
        {
            "tax_name": "VAT",
            "tax_amount": 19.13
        }
    ],
    "payment_reminder_enabled": true,
    "payment_made": 26.91,
    "credits_applied": 22.43,
    "tax_amount_withheld": 0,
    "balance": 40.6,
    "write_off_amount": 0,
    "allow_partial_payments": true,
    "price_precision": 2,
    "payment_options": {
        "payment_gateways": [
            {
                "configured": true,
                "additional_field1": "standard",
                "gateway_name": "paypal"
            }
        ]
    },
    "is_emailed": false,
    "reminders_sent": 1,
    "last_reminder_sent_date": " ",
    "billing_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "street2": "McMillan Avenue",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "shipping_address": {
        "address": "4900 Hopyard Rd, Suit 310",
        "street2": "McMillan Avenue",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 945881,
        "country": "USA",
        "fax": "+1-925-924-9600"
    },
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal"
        }
    ],
    "template_id": 982000000000143,
    "template_name": "Service - Classic",
    "created_time": "2013-11-18T02:17:40-0800",
    "last_modified_time": "2013-11-18T02:02:51-0800",
    "attachment_name": " ",
    "can_send_in_mail": true,
    "salesperson_id": " ",
    "salesperson_name": " ",
    "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
}
```

## Add Attachment to an Invoice

### Description
Attach a file to an invoice.

### Endpoint
`POST /invoices/{invoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Query Parameters
*   **can_send_in_mail** (boolean): True to send the attachment with the invoice when emailed.
*   **attachment**: The file to be attached (sent as multipart/form-data). Allowed Extensions: `gif`, `png`, `jpeg`, `jpg`, `bmp`, `pdf`.

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/your/document.pdf"
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file has been successfully attached to the invoice."
}
```

## Add Comment to Invoice

### Description
Add a comment for an invoice.

### Endpoint
`POST /invoices/{invoice_id}/comments`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Query Parameters
*   **description** (string): The comment text.
*   **payment_expected_date** (string): Expected payment date (can be set via comment?).
*   **show_comment_to_clients** (boolean): Make comment visible in client portal.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695&description=Customer%20called%2C%20confirmed%20payment%20next%20week&show_comment_to_clients=false' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```
*(Note: Sending data via query parameters for POST is less common than using a request body, but shown as per documentation)*

### Response Example
```json
{
    "code": 0,
    "message": "Comments added."
    /* May also include the created comment object */
}
```

## Approve an Invoice

### Description
Approve an invoice.

### Endpoint
`POST /invoices/{invoice_id}/approve`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the invoice."
}
```

## Bulk Export Invoices (PDF)

### Description
Maximum of 25 invoices can be exported in a single pdf.

### Endpoint
`GET /invoices/pdf`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **invoice_ids** (string, Required): Comma separated invoice IDs which are to be exported as pdf.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=982000000567114,982000000567115' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output invoices_export.pdf
```
*(Note: The response will be the PDF file content)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Bulk Invoice Reminder

### Description
Remind your customer about unpaid invoices by email. Reminder mail will be sent, only for invoices in open or overdue status. Maximum 10 invoices can be reminded at once.

### Endpoint
`POST /invoices/paymentreminder`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Query Parameters
*   **invoice_ids** (string, Required): Comma separated array of invoice IDs for which the reminder has to be sent.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=982000000567114,982000000567115' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success", /* Overall success/failure */
    "info": { /* More detailed info */
        "email_success_info": {
            "message": "The reminders were successfully sent",
            "sent_count": 2
        },
        "email_errors_info": [
            {
                "message": "The reminders were successfully sent", /* This message seems wrong for errors */
                "ids": "2000000007037" /* Example ID that might have failed */
            }
        ],
        "code": 4083 /* Internal code? */
    }
}
```

## Bulk Print Invoices

### Description
Export invoices as pdf and print them. Maximum of 25 invoices can be printed. (Likely returns PDF data intended for printing).

### Endpoint
`GET /invoices/print`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **invoice_ids** (string, Required): Comma separated invoice IDs to print.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/print?organization_id=10234695&invoice_ids=982000000567114,982000000567115' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output invoices_print.pdf
```
*(Note: The response will likely be the PDF file content suitable for printing)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Cancel Write Off

### Description
Cancel the write off amount of an invoice.

### Endpoint
`POST /invoices/{invoice_id}/writeoff/cancel`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The write off done for this invoice has been cancelled."
}
```

## Create an Instant Invoice from Sales order

### Description
Create an instant invoice for all the confirmed sales orders you have selected. *(Note: Documentation implies single SO ID in body, but description says "selected" - likely creates one invoice from one SO).*

### Endpoint
`POST /invoices/fromsalesorder`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **salesorder_id** (string): ID of the salesorder to convert to an invoice.
*   **organization_id** (string): *(Note: This seems out of place in the body, usually a query param).*

### Request Example

#### cURL
```curl
curl --request POST \
  --url https://www.zohoapis.com/books/v3/invoices/fromsalesorder?organization_id=10234694 \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"salesorder_id": "2000000014088"}'
```

#### Body Parameters
```json
{
    "salesorder_id": "2000000014088"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The invoice has been created.",
    "invoice": {
        "invoice_id": 982000000567114,
        "salesorder_id": 2000000021993,
        "salesorder_number": "SO-00001",
        /* Note: Example showed nested 'salesorders' object, structure may vary */
        /* ... full invoice details ... */
    }
}
```

## Create an Invoice

### Description
Create an invoice for your customer.

### Endpoint
`POST /invoices`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*(Refer to Overview section for detailed list)*
*   **customer_id** (string, Required)
*   **line_items** (array, Required)
*   ... (other optional parameters)

### Query Parameters
*   **send** (boolean): Send the invoice to contacts upon creation.
*   **ignore_auto_number_generation** (boolean): Ignore auto invoice number generation.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
*(See full example in Overview section)*

### Response Example
```json
{
    "code": 0,
    "message": "The invoice has been created.",
    "invoice": {
        "invoice_id": 982000000567114,
        "status": "draft", /* Or 'sent' if send=true was used */
        /* ... full invoice details ... */
    }
}
```

## Delete an Attachment

### Description
Delete the file attached to the invoice.

### Endpoint
`DELETE /invoices/{invoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file is no longer attached to the invoice."
}
```

## Delete an Invoice

### Description
Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.

### Endpoint
`DELETE /invoices/{invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The invoice has been deleted."
}
```

## Delete Applied Credit

### Description
Delete a particular credit applied to an invoice. This unapplies the credit note from this specific invoice.

### Endpoint
`DELETE /invoices/{invoice_id}/creditsapplied/{creditnotes_invoice_id}`

*Note: `{creditnotes_invoice_id}` is the ID mapping the credit note to *this* invoice (from the List Credits Applied response), not the credit note's own ID.*

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits applied to an invoice have been deleted."
}
```

## Delete Expense Receipt

### Description
Delete the expense receipts attached to an invoice which is raised from an expense. *(Note: The content of the file originally named "Update Custom Field in Invoice.md" matched this description).*

### Endpoint
`DELETE /invoices/expenses/{expense_id}/receipt`

*Note: The URL structure `/invoices/expenses/...` seems slightly inconsistent with other attachment endpoints. It implies an invoice derived from expense `expense_id`. The endpoint might need `{invoice_id}` as well, or it acts globally on the expense attachment regardless of which invoice it was added to.*

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/expenses/EXPENSE_ID_HERE/receipt?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The attached expense receipt has been deleted."
}
```

## Delete Invoice Comment

### Description
Delete an invoice comment.

### Endpoint
`DELETE /invoices/{invoice_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Delete a Payment

### Description
Delete a payment made to an invoice. This effectively unapplies the payment from this specific invoice.

### Endpoint
`DELETE /invoices/{invoice_id}/payments/{invoice_payment_id}`

*Note: `{invoice_payment_id}` is the ID mapping the payment to *this* invoice (from the List Invoice Payments response), not the overall payment ID.*

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment has been deleted."
}
```

## Disable Payment Reminder

### Description
Disable automated payment reminders for an invoice.

### Endpoint
`POST /invoices/{invoice_id}/paymentreminder/disable`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Reminders stopped."
}
```

## Email an Invoice (Single)

### Description
Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

### Endpoint
`POST /invoices/{invoice_id}/email`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **send_from_org_email_id** (boolean): Trigger email from the organization's email address.
*   **to_mail_ids** (array, Required): Array of recipient email addresses.
*   **cc_mail_ids** (array): Array of CC recipient email addresses.
*   **subject** (string): Subject of the mail.
*   **body** (string): Body of the mail.

### Query Parameters
*   **send_customer_statement** (boolean): Send customer statement PDF with email.
*   **send_attachment** (boolean): Send the invoice PDF attachment with the email.
*   **attachments**: File(s) to be attached (sent as multipart/form-data).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["willsmith@bowmanfurniture.com"], "subject": "Invoice INV-00001", "body": "Please find attached..."}'
```
*(Note: Attaching files requires sending as multipart/form-data.)*

#### Body Parameters
```json
{
    "send_from_org_email_id": false,
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
    "body": "Dear Customer,         <br><br><br><br>Thanks for your business.         <br><br><br><br>The invoice INV-00001 is attached with this email. You can choose the easy way out and <a href= https://invoice.zoho.com/SecurePayment?CInvoiceID=... >pay online for this invoice.</a>         <br><br>Here's an overview of the invoice for your reference.         <br><br><br><br>Invoice Overview:         <br><br>Invoice  : INV-00001         <br><br>Date : 05 Aug 2013         <br><br>Amount : $541.82         <br><br><br><br>It was great working with you. Looking forward to working with you again.<br><br><br>\\nRegards<br>\\nZillium Inc<br>\\n\"\""
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your invoice has been sent."
}
```

## Email Invoices (Bulk)

### Description
Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.

### Endpoint
`POST /invoices/email`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **contacts** (array): Array of contact objects for specifying email/snail mail preferences.
    *   **contact_id** (string, Required): ID of the contact.
    *   *(Potentially other fields to specify email vs snail mail per contact - documentation unclear)*

### Query Parameters
*   **invoice_ids** (string, Required): Comma separated invoice IDs to be emailed.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/email?organization_id=10234695&invoice_ids=982000000567114,982000000567115' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"contacts": [{"contact_id": "460000000026049"}]}' /* Example body */
```

#### Body Parameters (Example based on description)
```json
{
    "contacts": [
        /* Define contact preferences here if needed */
        {"contact_id": "460000000026049"}
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Mission accomplished! We've sent all the invoices."
}
```

## Enable Payment Reminder

### Description
Enable automated payment reminders for an invoice.

### Endpoint
`POST /invoices/{invoice_id}/paymentreminder/enable`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Reminders enabled."
}
```

## Generate Payment Link

### Description
This API generates a payment link for the invoice with an expiry date.

### Endpoint
`GET /share/paymentlink`

### OAuth Scope
`ZohoBooks.settings.ALL`

### Query Parameters
*   **transaction_id** (string, Required): The ID of the transaction (Invoice ID).
*   **transaction_type** (string, Required): The type of the transaction (Should be 'invoice').
*   **link_type** (string, Required): The type of the link (`private` or `public`).
*   **expiry_time** (string, Required): The expiry time of the payment link. Supported format: `yyyy-MM-dd`.
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "share_link": "https://zohosecurepay.com/books/Payment/secure?CInvoiceID=..."
    }
}
```

## Get an Attachment

### Description
Returns the file attached to the invoice.

### Endpoint
`GET /invoices/{invoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **preview** (boolean): Get the thumbnail of the attachment (if applicable).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output downloaded_invoice_attachment.pdf
```
*(Note: The response will be the binary file content)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Get an Invoice

### Description
Get the details of an invoice.

### Endpoint
`GET /invoices/{invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **print** (boolean): Get PDF content suitable for printing.
*   **accept** (string): Response format. Allowed values: `json`, `pdf`, `html`. Default: `json`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "invoice": {
        "invoice_id": 982000000567114,
        /* ... full invoice details ... */
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=..."
    }
}
```

## Get Invoice Email Content

### Description
Get the email content of an invoice based on a template.

### Endpoint
`GET /invoices/{invoice_id}/email`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **email_template_id** (string): Get content based on a specific template ID. If omitted, uses customer's associated template or default template.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695&email_template_id=982000000000067' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "bcc_mails": [ "string" ],
        "gateways_configured": true,
        "gateways_associated": true,
        "bcc_mails_str": "",
        "body": "Dear Customer, ...",
        "documents": "",
        "customer_name": "Bowman & Co",
        "attach_pdf": true,
        "entity_id": "2000000007037",
        "cc_mails_list": [ { "user_name": "Sujin Kumar", "email": null } ],
        "file_name_without_extension": "INV-000004",
        "to_mails_str": "",
        "cc_mails_str": "",
        "from_email": "",
        "from_address": "",
        "deprecated_placeholders_used": [],
        "error_list": [],
        "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
        "emailtemplates": [
            {
                "selected": true,
                "name": "Default",
                "email_template_id": "982000000000067"
            }
        ],
        "emailtemplate_documents": [ "string" ],
        "to_contacts": [
            {
                "first_name": "Sujin",
                "selected": true,
                "phone": "+1-925-921-9201",
                "email": null,
                "last_name": "Kumar",
                "salutation": "Mr",
                "contact_person_id": 982000000567003,
                "mobile": "+1-4054439562"
            }
        ],
        "attachment_name": " ",
        "file_name": "INV-00001.pdf",
        "from_emails": [
            {
                "user_name": "Sujin Kumar",
                "selected": true,
                "email": null,
                "organization_contact_id": "2000000002266",
                "is_org_email_id": true
            }
        ],
        "customer_id": 982000000567001
    }
}
```

## Get Payment Reminder Mail Content

### Description
Get the mail content of the payment reminder.

### Endpoint
`GET /invoices/{invoice_id}/paymentreminder`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "body": "<br>Dear Mr. Sujin, ...",
        "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
        /* ... other email content details similar to Get Invoice Email Content ... */
    }
}
```

## List Credits Applied

### Description
Get the list of credits applied for an invoice. *(Note: Filename was "Apply Credits", corrected here based on content)*.

### Endpoint
`GET /invoices/{invoice_id}/creditsapplied`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "credits": [
        {
            "creditnote_id": 982000000567134,
            "creditnotes_invoice_id": "982000000567172", /* ID mapping credit note to this invoice */
            "creditnotes_number": "CN-00001",
            "credited_date": "2013-11-18",
            "amount_applied": 12.2
        },
        {...},
        {...}
    ]
}
```

## List Invoice Comments and History

### Description
Get the complete history and comments of an invoice. *(Note: The content of the file originally named "Update Invoice Comment.md" matched this description).*

### Endpoint
`GET /invoices/{invoice_id}/comments`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": 982000000567019,
            "invoice_id": 982000000567114,
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.", /* Example Text */
            "commented_by_id": 982000000554041,
            "commented_by": "John David",
            "comment_type": "system", /* Or 'user' */
            "operation_type": "Added", /* Or 'Updated', 'Sent', 'Paid', etc. */
            "date": "2013-11-18",
            "date_description": "yesterday",
            "time": "2:38 AM",
            "transaction_id": "982000000567204", /* Related transaction ID, e.g., payment ID */
            "transaction_type": "invoice" /* Or 'payment', 'creditnote' etc. */
        },
        {...},
        {...}
    ]
}
```

## List Invoice Payments

### Description
Get the list of payments made for an invoice.

### Endpoint
`GET /invoices/{invoice_id}/payments`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/payments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "payments": [
        {
            "payment_id": "982000000567190",
            "payment_number": 7,
            "invoice_id": 982000000567036, /* Original invoice ID paid */
            "invoice_payment_id": 982000000567192, /* ID mapping payment to this specific invoice */
            "payment_mode": "cash",
            "description": " ",
            "date": "2013-11-18",
            "reference_number": 99782374,
            "exchange_rate": 1,
            "amount": 10.57,
            "tax_amount_withheld": 0,
            "online_transaction_id": "",
            "is_single_invoice_payment": true
        },
        {...},
        {...}
    ]
}
```

## List Invoice Templates

### Description
Get all invoice pdf templates.

### Endpoint
`GET /invoices/templates`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Service - Classic",
            "template_id": 982000000000143,
            "template_type": "classic"
        },
        {...},
        {...}
    ]
}
```

## List Invoices

### Description
List all invoices with pagination.

### Endpoint
`GET /invoices`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*(Refer to Overview section for detailed list)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695&status=overdue' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "invoices": [
        {
            "invoice_id": 982000000567114,
            /* ... summary invoice details ... */
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Invoices",
        "applied_filter": "Status.Overdue", /* Example */
        "sort_column": "created_time",
        "sort_order": "D",
        "response_option": 0 /* Default example */
    }
}
```
*(Note: Original `page_context` example showed an array, corrected to object).*

## Mark an Invoice as Sent

### Description
Mark a draft invoice as sent.

### Endpoint
`POST /invoices/{invoice_id}/status/sent`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/sent?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Invoice status has been changed to Sent."
}
```

## Mark as Draft

### Description
Mark a voided invoice as draft.

### Endpoint
`POST /invoices/{invoice_id}/status/draft`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/draft?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Status of invoice changed from void to draft"
}
```

## Remind Customer (Single Invoice)

### Description
Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.

### Endpoint
`POST /invoices/{invoice_id}/paymentreminder`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **to_mail_ids** (array): Array of recipient email addresses.
*   **cc_mail_ids** (array, Required): Array of CC recipient email addresses. *(Note: Marked required in original docs, likely optional)*.
*   **subject** (string): Subject of the reminder mail.
*   **body** (string): Body of the reminder mail.
*   **send_from_org_email_id** (boolean): Trigger email from the organization's email address.

### Query Parameters
*   **send_customer_statement** (boolean): Send customer statement PDF with the reminder.
*   **attachments**: File(s) to be attached (sent as multipart/form-data).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["willsmith@bowmanfurniture.com"], "cc_mail_ids": [], "subject": "Payment Reminder for INV-00001", "body": "Gentle reminder..."}'
```
*(Note: Attaching files requires sending as multipart/form-data.)*

#### Body Parameters
```json
{
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
    "body": "<br>Dear Mr. Sujin, ...",
    "send_from_org_email_id": false
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your payment reminder has been sent."
}
```

## Submit an Invoice for Approval

### Description
Submit an invoice for approval.

### Endpoint
`POST /invoices/{invoice_id}/submit`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The invoice has been submitted for approval successfully."
}
```

## Update an Invoice

### Description
Update an existing invoice. To delete a line item just remove it from the line_items list.

### Endpoint
`PUT /invoices/{invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*(Refer to Overview section for detailed list)*
*   **customer_id** (string, Required)
*   **line_items** (array, Required)
    *   **line_item_id** (string): Mandatory if updating existing line item.
*   ... (other optional parameters)

### Query Parameters
*   **ignore_auto_number_generation** (boolean): Ignore auto invoice number generation.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
*(See full example in Overview section, ensure `line_item_id` is provided for lines being updated)*

### Response Example
```json
{
    "code": 0,
    "message": "Invoice information has been updated.",
    "invoice": {
        "invoice_id": 982000000567114,
        /* ... updated invoice details ... */
    }
}
```

## Update an Invoice using Custom Field

### Description
Update an invoice using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /invoices` *(with custom headers)*

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field for the target invoice.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create a new invoice if the unique value is not found.

### Arguments (Body Parameters)
*(Refer to Overview section for detailed list)*
*   **customer_id** (string, Required)
*   **line_items** (array, Required)
    *   **line_item_id** (string): Mandatory if updating existing line item.
*   ... (other optional parameters)

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
*(See full example in Overview section, ensure `line_item_id` is provided for lines being updated)*

### Response Example
```json
{
    "code": 0,
    "message": "Invoice information has been updated.",
    "invoice": {
        "invoice_id": 982000000567114,
        /* ... updated invoice details ... */
    }
}
```

## Update Attachment Preference

### Description
Set whether you want to send the attached file while emailing the invoice.

### Endpoint
`PUT /invoices/{invoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Query Parameters
*   **can_send_in_mail** (boolean, Required): Set to true or false.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Invoice information has been updated." /* Generic update message */
}
```

## Update Billing Address

### Description
Updates the billing address for this invoice alone.

### Endpoint
`PUT /invoices/{invoice_id}/address/billing`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Billing address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Billing Address", "city": "New City", ...}'
```

#### Body Parameters
```json
{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
    "city": "Beijing",
    "state": "Beijing",
    "zip": "1000881", /* Should likely be string */
    "country": "string",
    "fax": "+86-10-82637827"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated"
}
```

## Update Invoice Template

### Description
Update the pdf template associated with the invoice.

### Endpoint
`PUT /invoices/{invoice_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Invoice information has been updated."
}
```

## Update Shipping Address

### Description
Updates the shipping address for this invoice alone.

### Endpoint
`PUT /invoices/{invoice_id}/address/shipping`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Shipping address line(s).
*   **street2** (string): Additional address line.
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Shipping Address", "city": "New Ship City", ...}'
```

#### Body Parameters
```json
{
    "address": "4900 Hopyard Rd, Suit 310",
    "street2": "McMillan Avenue",
    "city": "Pleasanton",
    "state": "CA",
    "zip": "945881", /* Should likely be string */
    "country": "USA",
    "fax": "+1-925-924-9600"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Shipping address updated"
}
```

## Void an Invoice

### Description
Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.

### Endpoint
`POST /invoices/{invoice_id}/status/void`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Invoice status has been changed to Void."
}
```

## Write Off Invoice

### Description
Write off the invoice balance amount of an invoice.

### Endpoint
`POST /invoices/{invoice_id}/writeoff`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Invoice has been written off"
}
```
# Recurring Invoices

## Overview

### Recurring Invoices
Recurring invoices are invoices that are created and sent to your customers on a recurring schedule.

### End Points
*   `POST /recurringinvoices`
*   `PUT /recurringinvoices` *(Note: Likely refers to the 'Update Recurring Invoice using Custom Field' endpoint)*
*   `GET /recurringinvoices`
*   `PUT /recurringinvoices/{recurring_invoice_id}`
*   `GET /recurringinvoices/{recurring_invoice_id}`
*   `DELETE /recurringinvoices/{recurring_invoice_id}`
*   `POST /recurringinvoices/{recurring_invoice_id}/status/stop`
*   `POST /recurringinvoices/{recurring_invoice_id}/status/resume`
*   `PUT /recurringinvoices/{recurring_invoice_id}/templates/{template_id}`
*   `GET /recurringinvoices/{recurring_invoice_id}/comments` *(Note: Endpoint for listing comments/history seems missing from the provided individual files, but is listed here)*

### Attributes
*   **recurring_invoice_id** (string): Unique ID of the recurring invoice generated by the server.
*   **recurrence_name** (string): Unique name for the recurring profile given by the user. Max-length [100]
*   **reference_number** (string): The Order number of the Recurring Invoice.
*   **customer_name** (string): Name of the customer to whom the recurring invoice is raised.
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable for transactions that fall before July 1, 2017 *(Note: Original doc type was string)*.
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the customer.
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: `business_gst`, `business_none`, `overseas`, `consumer`.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment for the contact (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is vat_registered).
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage (Allowed values listed in description).
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply (Supported codes listed in description).
*   **customer_id** (string): Customer ID.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **start_date** (string): Date the recurrence starts.
*   **end_date** (string): Date the recurrence expires.
*   **last_sent_date** (string): Date the last invoice was sent.
*   **next_invoice_date** (string): Date the next invoice is scheduled.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items.
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **custom_fields** (array): Custom fields.
*   **payment_options** (object): Payment options.
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number. Max-length [25]
*   **avatax_use_code** (string): Avalara Integration only - Avalara use code. Max-length [25]

### Example
```json
{
    "recurring_invoice_id": "90300000072369",
    "recurrence_name": "MonthlyInvoice",
    "reference_number": "12314",
    "customer_name": "Sujin Kumar",
    "is_pre_gst": false,
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "cfdi_usage": "acquisition_of_merchandise",
    "vat_treatment": "overseas",
    "place_of_supply": "TN",
    "customer_id": "903000000000099",
    "currency_id": "982000000000190",
    "currency_code": "USD",
    "start_date": "2016-06-12",
    "end_date": "2017-06-12",
    "last_sent_date": "2016-06-12",
    "next_invoice_date": "2016-06-17",
    "location_id": "460000000038080",
    "location_name": "string",
    "line_items": [
        {
            "line_item_id": "982000000567021",
            "quantity": 1,
            "name": "Hard Drive",
            "item_total": 100,
            "sku": "LEV-JN-SL-36-GN",
            "product_type": "goods",
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "location_id": "460000000038080",
            "location_name": "string",
            "tags": [
                {
                    "is_tag_mandatory": false,
                    "tag_id": 982000000009070,
                    "tag_name": "Location",
                    "tag_option_id": 982000000002670,
                    "tag_option_name": "USA"
                }
            ],
            "tax_id": "903000000000356",
            "tax_treatment_code": "uae_others",
            "project_id": 90300000087378,
            "project_name": "Sample Project",
            "header_name": "Electronic devices",
            "header_id": 982000000000670
        }
    ],
    "billing_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "street2": "McMillan Avenue",
        "city": "Pleasanton",
        "state": "CA",
        "zip": "94588",
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "shipping_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": "94588",
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "custom_fields": [
        {
            "value": "129890",
            "label": "label",
            "data_type": "text"
        }
    ],
    "payment_options": {
        "payment_gateways": [
            {
                "configured": true,
                "additional_field1": "standard",
                "gateway_name": "paypal"
            }
        ]
    },
    "avatax_exempt_no": "string",
    "avatax_use_code": "string"
}
```

## Create a Recurring Invoice

### Description
Creating a new recurring invoice.

### Endpoint
`POST /recurringinvoices`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **recurrence_name** (string, Required): Unique name. Max-length [100].
*   **reference_number** (string): Order number.
*   **customer_id** (string, Required): Customer ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact Person IDs.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply (Supported codes in Overview).
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: `business_gst`, `business_none`, `overseas`, `consumer`.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is `vat_registered`).
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage (Allowed values in Overview).
*   **allow_partial_payments** (boolean): 🇲🇽 only - Choose `false` for PPU-Single Payments, `true` for PPD-Installment Payments.
*   **gst_no** (string): 🇮🇳 only - 15 digit GST number.
*   **start_date** (string): Date recurrence starts. Format [yyyy-mm-dd].
*   **end_date** (string): Date recurrence expires. Format [yyyy-mm-dd].
*   **recurrence_frequency** (string, Required): Frequency interval (e.g., 'weeks', 'months').
*   **repeat_every** (integer): Period between frequency (e.g., 2 for every 2 weeks).
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **item_id** (string): Item ID.
    *   **name** (string): Item name. max-length [100].
    *   **description** (string): Item description. Max-length [2000].
    *   **rate** (double): Item rate.
    *   **quantity** (int32): Item quantity.
    *   **unit** (string): Item unit (e.g., kgs, Nos).
    *   **avatax_tax_code** (string): Avalara tax code.
    *   Other attributes like tax_id, discount etc. also apply.
*   **tax_id** (string): Overall tax ID for the recurring invoice.
*   **custom_fields** (array): Custom fields.
*   **email** (string): Customer email address (for sending?).
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **avatax_use_code** (string): Avalara Integration only - Avalara use code. Max-length [25].
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption certificate number. Max-length [25].
*   **template_id** (string): Template ID.
*   **payment_terms** (integer): Payment terms in days.
*   **payment_terms_label** (string): Override default payment terms label.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax exemption ID.
*   **exchange_rate** (double): Exchange rate *(Note: Original doc type was string)*.
*   **payment_options** (object): Payment options.
*   **discount** (string): Discount amount or percentage (e.g., "30%").
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **discount_type** (string): Allowed values: `entity_level`, `item_level`.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Line item rates inclusive of tax.
*   **salesperson_name** (string): 🇺🇸 , 🇦🇺 , 🇨🇦 only - Salesperson name.
*   **shipping_charge** (double): Shipping charges.
*   **adjustment** (double): Adjustments.
*   **adjustment_description** (string): Adjustment description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"recurrence_name": "MonthlyInvoice", "customer_id": "903000000000099", ...}'
```

#### Body Parameters
```json
{
    "recurrence_name": "MonthlyInvoice",
    "reference_number": "12314",
    "customer_id": "903000000000099",
    "currency_id": "982000000000190",
    "contact_persons": [
        "90300000065322"
    ],
    "place_of_supply": "TN",
    "vat_treatment": "overseas",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "cfdi_usage": "acquisition_of_merchandise",
    "allow_partial_payments": true,
    "gst_no": "22AAAAA0000A1Z5",
    "start_date": "2016-06-12",
    "end_date": "2017-06-12",
    "recurrence_frequency": "weeks",
    "repeat_every": 2,
    "location_id": "460000000038080",
    "line_items": [
        {
            /* line_item_id usually not needed for create */
            "item_id": "90300000081501", /* ID of the item being sold */
            "quantity": 1,
            "name": "Hard Drive",
            "item_total": 100,
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "tags": [
                {
                    "tag_id": 982000000009070,
                    "tag_option_id": 982000000002670
                }
            ],
            "location_id": "460000000038080",
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_treatment_code": "uae_others",
            "project_id": 90300000087378,
            "header_name": "Electronic devices"
        }
    ],
    "tax_id": "903000000000356",
    "custom_fields": [
        {
            "value": "129890",
            "label": "label",
            "data_type": "text" /* index or placeholder might be needed instead of label/data_type */
        }
    ],
    "email": "benjamin.george@bowmanfurniture.com",
    "billing_address": { /* ... address details ... */ },
    "shipping_address": { /* ... address details ... */ },
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "template_id": "90300000001336",
    "payment_terms": 0,
    "payment_terms_label": "Next 15 days",
    "tax_authority_id": "903000006345",
    "tax_exemption_id": "903000006345",
    "exchange_rate": 5.5,
    "payment_options": { /* ... payment options ... */ },
    "discount": "30%",
    "is_discount_before_tax": true,
    "discount_type": "entity_level", /* Corrected value */
    "is_inclusive_tax": false,
    /* item_id, name, description, rate, quantity, unit, avatax_tax_code seem redundant here, belong in line_items */
    "salesperson_name": null,
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": "Rounding off"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring invoice has been created.",
    "recurring_invoice": {
        "recurring_invoice_id": "90300000072369",
        "recurrence_name": "MonthlyInvoice",
        "customer_id": "903000000000099",
        /* ... full recurring invoice details ... */
        "status": "active" /* Initial status */
    }
    /* page_context is unusual for a create response */
}
```

## Delete a Recurring Invoice

### Description
Delete an existing recurring invoice.

### Endpoint
`DELETE /recurringinvoices/{recurring_invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring invoice is deleted successfully."
}
```

## Get a Recurring Invoice

### Description
Get the details of a recurring invoice.

### Endpoint
`GET /recurringinvoices/{recurring_invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Details of a recurring invoice is displayed successfully.",
    "recurring_invoice": {
        "recurring_invoice_id": "90300000072369",
        "recurrence_name": "MonthlyInvoice",
        "status": "active",
        /* ... customer details ... */
        "is_pre_gst": false,
        /* ... tax details ... */
        "start_date": "2016-06-12",
        "end_date": "2017-06-12",
        "last_sent_date": "2016-06-12",
        "next_invoice_date": "2016-06-17",
        /* ... location, line items, addresses, payment options ... */
    }
    /* page_context is unusual for a single get response */
}
```

## List all Recurring Invoices

### Description
List the details of all recurring invoices.

### Endpoint
`GET /recurringinvoices`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **recurrence_name** (string): Search by recurrence name. Max-length [100].
*   **item_name** (string): Search by item name (variants: `_startswith`, `_contains`).
*   **item_description** (string): Search by item description (variants: `_startswith`, `_contains`).
*   **customer_name** (string): Search by customer name.
*   **line_item_id** (string): Filter by line item ID.
*   **item_id** (string): Filter by item ID.
*   **tax_id** (string): Filter by tax ID.
*   **notes** (string): Search by notes.
*   **start_date** (string): Filter by start date.
*   **end_date** (string): Filter by end date.
*   **customer_id** (string): Filter by customer ID.
*   **status** (string): Filter by status (`active`, `stopped`, `expired`).
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Stopped`, `Status.Expired`.
*   **search_text** (string): Search by various fields (e.g., invoice number, customer name). Max-length [100].
*   **sort_column** (string): Column to sort by (e.g., `customer_name`, `start_date`, `created_time`).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices?organization_id=10234695&status=active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success", /* Corrected message */
    "recurring_invoices": [
        {
            "recurring_invoice_id": "90300000072369",
            "recurrence_name": "MonthlyInvoice",
            "customer_name": "Sujin Kumar",
            "customer_id": "903000000000099",
            "status": "active",
            "total": 150.00, /* Added example total */
            "currency_id": "982000000000190",
            "currency_code": "USD",
            "start_date": "2016-06-12",
            "end_date": "2017-06-12",
            "last_sent_date": "2016-06-12",
            "next_invoice_date": "2016-06-17",
            "custom_fields": [ /* ... */ ],
            "billing_address": { /* ... */ },
            "shipping_address": { /* ... */ }
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Recurring Invoices",
        "applied_filter": "Status.Active", /* Corrected example */
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## List Recurring Invoice History

*(Note: The file content describes updating the template, not listing history. The title is misleading. The endpoint action aligns with updating the template.)*

### Description
Update the pdf template associated with the recurring invoice.

### Endpoint
`PUT /recurringinvoices/{recurring_invoice_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **recurring_invoice_id** (string): Unique ID of the recurring invoice *(Note: Also present in URL path, likely redundant in body)*.
*   **template_id** (string): Unique ID of the recurring invoice template *(Note: Also present in URL path, likely redundant in body)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369/templates/90300000001336?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{}' /* Empty body likely sufficient */
```

#### Body Parameters (As per example, likely not needed)
```json
{
    "recurring_invoice_id": "90300000072369",
    "template_id": "90300043563547" /* This is the *new* template ID */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The template of the recurring invoice has been updated."
}
```

## Resume a Recurring Invoice

### Description
Resume a stopped recurring invoice.

### Endpoint
`POST /recurringinvoices/{recurring_invoice_id}/status/resume`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **recurring_invoice_id** (string): Unique ID of the recurring invoice *(Note: Also present in URL path, likely redundant in body)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369/status/resume?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{}' /* Empty body likely sufficient */
```

#### Body Parameters (As per example, likely not needed)
```json
{
    "recurring_invoice_id": "90300000072369"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring invoice has been resumed."
}
```

## Stop a Recurring Invoice

### Description
Stop an active recurring invoice.

### Endpoint
`POST /recurringinvoices/{recurring_invoice_id}/status/stop`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **recurring_invoice_id** (string): Unique ID of the recurring invoice *(Note: Also present in URL path, likely redundant in body)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369/status/stop?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{}' /* Empty body likely sufficient */
```

#### Body Parameters (As per example, likely not needed)
```json
{
    "recurring_invoice_id": "90300000072369"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring invoice has been stopped."
}
```

## Update a Recurring Invoice using Custom Field

*(Note: The file content describes creating a recurring invoice, not updating using a custom field. The title is misleading. The endpoint and parameters match the 'Create' operation.)*

### Description
Creating a new recurring invoice. *(Note: This seems to be a duplicate of the standard create endpoint, perhaps intended for upsert via custom field headers similar to other modules, but headers are not shown)*.

### Endpoint
`POST /recurringinvoices` *(Note: Standard create endpoint. Update via custom field typically uses PUT /recurringinvoices with special headers)*.

### OAuth Scope
`ZohoBooks.invoices.CREATE` *(Note: Scope matches Create, not Update)*.

### Arguments (Body Parameters)
*(Same as Create a Recurring Invoice)*
*   ...

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"recurrence_name": "MonthlyInvoice", "customer_id": "903000000000099", ...}'
```
*(Note: Missing X-Unique-Identifier-Key/Value headers expected for update/upsert via custom field)*

#### Body Parameters
*(Same as Create a Recurring Invoice)*
*   ...

### Response Example
*(Same as Create a Recurring Invoice)*
*   ...

## Update Recurring Invoice Template

### Description
Update the pdf template associated with the recurring invoice.

### Endpoint
`PUT /recurringinvoices/{recurring_invoice_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*(None required in body, IDs are in path)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369/templates/90300000001336?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{}' /* Empty body likely sufficient */
```

### Response Example
```json
{
    "code": 0,
    "message": "The template of the recurring invoice has been updated."
}
```

## Update Recurring Invoice

### Description
Update the recurring invoice.

### Endpoint
`PUT /recurringinvoices/{recurring_invoice_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **recurrence_name** (string, Required): Unique name. Max-length [100].
*   **reference_number** (string): Order number.
*   **customer_id** (string, Required): Customer ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact Person IDs.
*   **start_date** (string): Date recurrence starts. Format [yyyy-mm-dd].
*   **end_date** (string): Date recurrence expires. Format [yyyy-mm-dd].
*   **recurrence_frequency** (string, Required): Frequency interval.
*   **repeat_every** (integer): Period between frequency.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **gst_treatment** (string): 🇮🇳 only - GST treatment.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only.
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage.
*   **allow_partial_payments** (boolean): 🇲🇽 only - PPD vs PPU.
*   **gst_no** (string): 🇮🇳 only - GST number.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **email** (string): Customer email address.
*   **custom_fields** (array): Custom fields.
*   **tax_id** (string): Overall tax ID.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **payment_options** (object): Payment options.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax exemption ID.
*   **avatax_use_code** (string): Avalara Integration only - Use code. Max-length [25].
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption number. Max-length [25].
*(Other fields from Create might also be updatable, e.g., template_id, terms, notes, discount, etc.)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringinvoices/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"recurrence_name": "UpdatedName", "customer_id": "903000000000099", ...}'
```

#### Body Parameters
```json
{
    "recurrence_name": "MonthlyInvoiceUpdated",
    "reference_number": "12314-UPDATED",
    "customer_id": "903000000000099",
    "currency_id": "982000000000190",
    "contact_persons": [
        "90300000065322"
    ],
    "start_date": "2016-07-01",
    "end_date": "2017-07-01",
    "recurrence_frequency": "months",
    "repeat_every": 1,
    "place_of_supply": "TN",
    "vat_treatment": "overseas",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "cfdi_usage": "acquisition_of_merchandise",
    "allow_partial_payments": true,
    "gst_no": "22AAAAA0000A1Z5",
    "location_id": "460000000038080",
    "line_items": [
        {
            /* Include line_item_id for existing items */
            "line_item_id": "982000000567021",
            "item_id": "90300000081501",
            "name": "Hard Drive",
            "description": "Updated prorated amount for items",
            "rate": 10, /* Updated rate */
            "quantity": 1,
            "discount": "10%", /* Example discount */
            "tags": [ { /* tag details */ } ],
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_exemption_id": "903000006345",
            "tax_treatment_code": "uae_others",
            "avatax_tax_code": " ",
            "avatax_use_code": "string",
            "item_total": 90, /* Updated item total after discount */
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "location_id": "460000000038080",
            "project_id": 90300000087378,
            "header_name": "Electronic devices",
            "header_id": 982000000000670
        }
        /* Omit line item objects to delete them */
        /* Add new line item objects without line_item_id to add */
    ],
    "email": "benjamin.george@bowmanfurniture.com",
    "custom_fields": [ { /* custom field details */ } ],
    "tax_id": "903000000000356",
    "tax_authority_id": "903000006345",
    "payment_options": { /* payment options */ },
    "tax_exemption_id": "903000006345",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring Invoice has been updated.", /* More specific message */
    "recurring_invoice": {
        "recurring_invoice_id": "90300000072369",
        "recurrence_name": "MonthlyInvoiceUpdated",
        /* ... updated recurring invoice details ... */
    }
}
```
# Credit Notes

## Overview

### Credit Notes
Credit notes are created when a refund is to be made to a customer. A credit note object allows you to keep track of all credit note related information.

### End Points
*   `POST /creditnotes`
*   `PUT /creditnotes` *(Note: This is likely for bulk/keyed updates, see Update Credit Note using Custom Field)*
*   `GET /creditnotes`
*   `PUT /creditnotes/{creditnote_id}`
*   `GET /creditnotes/{creditnote_id}`
*   `DELETE /creditnotes/{creditnote_id}`
*   `POST /creditnotes/{creditnote_id}/email`
*   `GET /creditnotes/{creditnote_id}/email`
*   `POST /creditnotes/{creditnote_id}/status/void`
*   `POST /creditnotes/{creditnote_id}/status/draft`
*   `POST /creditnotes/{creditnote_id}/status/open`
*   `POST /creditnotes/{creditnote_id}/submit`
*   `POST /creditnotes/{creditnote_id}/approve`
*   `GET /creditnotes/{creditnote_id}/emailhistory`
*   `PUT /creditnotes/{creditnote_id}/address/billing`
*   `PUT /creditnotes/{creditnote_id}/address/shipping`
*   `GET /creditnotes/templates`
*   `PUT /creditnotes/{creditnote_id}/templates/{template_id}`
*   `POST /creditnotes/{creditnote_id}/invoices`
*   `GET /creditnotes/{creditnote_id}/invoices`
*   `DELETE /creditnotes/{creditnote_id}/invoices/{creditnote_invoice_id}`
*   `POST /creditnotes/{creditnote_id}/comments`
*   `GET /creditnotes/{creditnote_id}/comments`
*   `DELETE /creditnotes/{creditnote_id}/comments/{comment_id}`
*   `GET /creditnotes/refunds`
*   `POST /creditnotes/{creditnote_id}/refunds`
*   `GET /creditnotes/{creditnote_id}/refunds`
*   `PUT /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`
*   `GET /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`
*   `DELETE /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`

### Attributes
*   **creditnote_id** (string): Unique ID of the credit note.
*   **creditnote_number** (string): Unique number (starts with CN). Max-Length [100].
*   **date** (string): Date credit note is raised. Format [yyyy-mm-dd].
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable before July 1, 2017.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply (Supported codes listed).
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **vat_reg_no** (string): VAT registration number.
*   **gst_no** (string): 🇮🇳 only - 15 digit GST number.
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage (Allowed values listed).
*   **cfdi_reference_type** (string): 🇲🇽 only - CFDI Reference Type (Allowed values listed).
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: `business_gst`, `business_none`, `overseas`, `consumer`.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is vat_registered).
*   **status** (string): Status (`open`, `closed`, `void`, `draft`).
*   **customer_id** (string): Customer ID.
*   **customer_name** (string): Customer name. Max-Length [100].
*   **custom_fields** (array): Additional fields.
*   **reference_number** (string): Reference number. Max-Length [100].
*   **email** (string): Customer email.
*   **total** (double): Total credits.
*   **balance** (double): Unapplied credits.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items.
*   **invoices** (array): List of invoices credited.
*   **taxes** (array): Taxes associated.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **created_time** (string): Creation time.
*   **updated_time** (string): Last updated time.
*   **template_id** (string): Template ID.
*   **template_name** (string): Template name.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms & conditions. Max-length [10000].

### Example
```json
{
    "creditnote_id": "90300000072369",
    "creditnote_number": "CN-29",
    "date": "2016-06-05",
    "is_pre_gst": true,
    "place_of_supply": "TN",
    "vat_treatment": "overseas",
    "vat_reg_no": "string",
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "status": "draft",
    "customer_id": "903000000000099",
    "customer_name": "Bowman Furniture",
    "custom_fields": [
        {
            "index": 1,
            "value": 129890,
            "label": "label",
            "data_type": "text"
        }
    ],
    "reference_number": "INV-384",
    "email": "benjamin.george@bowmanfurniture.com",
    "total": 450,
    "balance": 10,
    "location_id": "460000000038080",
    "location_name": "string",
    "line_items": [
        {
            "item_id": "90300000081501",
            "line_item_id": 903000006245,
            "account_id": "903000000000388",
            "name": "Basic Monthly",
            "description": "prorated amount for items",
            "item_order": 0,
            "rate": 0,
            "quantity": 1,
            "unit": "kgs",
            "discount": 10,
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_exemption_id": "903000006345",
            "tax_exemption_code": "GST FREE",
            "tax_treatment_code": "uae_others",
            "avatax_use_code": "string",
            "avatax_tax_code": "string",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "item_custom_fields": [
                "string"
            ],
            "location_id": "460000000038080",
            "location_name": "string",
            "serial_numbers": "string",
            "project_id": 90300000087378
        }
    ],
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "invoice_number": "INV-384",
            "amount": 450
        }
    ],
    "taxes": [
        {
            "tax_id": "903000000000356",
            "tax_name": "Basic Tax",
            "tax_amount": "2.50"
        }
    ],
    "currency_code": "USD",
    "currency_symbol": "$",
    "billing_address": { /* ... address details ... */ },
    "shipping_address": { /* ... address details ... */ },
    "created_time": "2016-06-05T02:30:08-0700",
    "updated_time": "2016-06-05T02:30:08-0700",
    "template_id": "90300000001336",
    "template_name": "Standard Template",
    "notes": "Offer for the referral",
    "terms": ""
}
```

## Email a Credit Note

### Description
Email a credit note.

### Endpoint
`POST /creditnotes/{creditnote_id}/email`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Arguments (Body Parameters)
*   **to_mail_ids** (array, Required): Recipient email IDs.
*   **cc_mail_ids** (array): CC email IDs.
*   **subject** (string, Required): Email subject. Max-length [1000].
*   **body** (string, Required): Email body. Max-length [5000].

### Query Parameters
*   **customer_id** (string): Customer ID *(Redundant? Implied by creditnote_id)*.
*   **attachments**: Files to attach (sent via multipart/form-data).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["benjamin.george@bowmanfurniture.com"], "subject": "Credit Note CN-29", "body": "Please find attached."}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters
```json
{
    "to_mail_ids": [
        "benjamin.george@bowmanfurniture.com",
        "paul@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "accounts@bowmanfurniture.com"
    ],
    "subject": "Credit note for subscription.",
    "body": "Please find attached the credit note for your subscription."
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your creditnote has been sent."
}
```

## Delete Invoices Created

### Description
Delete the credits applied to an invoice from this credit note.

### Endpoint
`DELETE /creditnotes/{creditnote_id}/invoices/{creditnote_invoice_id}`

*Note: `{creditnote_invoice_id}` is the ID mapping the credit application (from List Invoices Credited), not the invoice ID itself.*

### OAuth Scope
`ZohoBooks.creditnotes.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/invoices/982000000567172?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits applied to an invoice have been deleted."
}
```

## Add a Comment

### Description
Add a comment to an existing credit note.

### Endpoint
`POST /creditnotes/{creditnote_id}/comments`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Arguments (Body Parameters)
*   **description** (string): The comment text.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Applied remaining credit."}'
```

#### Body Parameters
```json
{
    "description": "Credits applied to invoice INV-00004"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added."
    /* May include comment object */
}
```

## Apply Credit to Invoices

### Description
Apply credit note to existing invoices.

### Endpoint
`POST /creditnotes/{creditnote_id}/invoices`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Arguments (Body Parameters)
*   **invoices** (array): List of invoices to apply credit to.
    *   **invoice_id** (string, Required): Invoice ID.
    *   **amount_applied** (double, Required): Amount to apply to this invoice.
*   *(Original documentation also lists `invoice_id` and `amount_applied` separately, which seems redundant if `invoices` array is used).*

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"invoices": [{"invoice_id": "90300000079426", "amount_applied": 41.82}]}'
```

#### Body Parameters
```json
{
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "amount_applied": 41.82
        }
    ]
    /* Redundant separate fields omitted */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits have been applied to the invoice(s)."
}
```

## Approve a Credit Note

### Description
Approve a credit note.

### Endpoint
`POST /creditnotes/{creditnote_id}/approve`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the Credit Note."
}
```

## Convert Credit Note to Draft

### Description
Convert a voided credit note to Draft.

### Endpoint
`POST /creditnotes/{creditnote_id}/status/draft`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/status/draft?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been marked as Draft."
}
```

## Convert to Open

### Description
Convert a credit note in Draft status to Open.

### Endpoint
`POST /creditnotes/{creditnote_id}/status/open`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/status/open?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Status of the credit note has been changed to open."
}
```

## Create a Credit Note

### Description
Create a new credit note.

### Endpoint
`POST /creditnotes`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): Customer ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact Person IDs.
*   **date** (string, Required): Date credit note is raised. Format [yyyy-mm-dd].
*   **is_draft** (boolean): Set true to create in draft status.
*   **exchange_rate** (string): Exchange rate *(Note: Data type string, likely float/double)*.
*   **line_items** (array, Required): Line items.
    *   Include item_id, name, rate, quantity, tax_id etc.
*   **location_id** (string): Location ID.
*   **creditnote_number** (string, Required): Credit note number (Mandatory if auto-gen disabled). Max-Length [100].
*   **gst_treatment** (string): 🇮🇳 only - GST treatment.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only.
*   **gst_no** (string): 🇮🇳 only - GST number.
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage.
*   **cfdi_reference_type** (string): 🇲🇽 only - CFDI Reference Type.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply.
*   **ignore_auto_number_generation** (boolean): Set true to provide your own number.
*   **reference_number** (string): Reference number. Max-Length [100].
*   **custom_fields** (array): Custom fields.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms. Max-length [10000].
*   **template_id** (string): Template ID.
*   **tax_id** (string): Overall tax ID.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax exemption ID.
*   **avatax_use_code** (string): Avalara Integration only - Use code. Max-length [25].
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption number. Max-length [25].
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 , 🇨🇦 - Line item rates inclusive of tax.
*   **avatax_tax_code** (string): Avalara Integration only - Tax code. Max-length [25].

### Query Parameters
*   **invoice_id** (string): Invoice ID to associate the credit note with immediately.
*   **ignore_auto_number_generation** (boolean): Set true to provide your own number *(duplicate of body param)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "date": "2016-06-05", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "currency_id": "982000000567240",
    "contact_persons": [
        "903000006532"
    ],
    "date": "2016-06-05",
    "is_draft": true,
    "exchange_rate": "5.5",
    "line_items": [
        {
            "item_id": "90300000081501",
            "description": "prorated amount for items",
            "name": "Basic Monthly",
            "account_id": "903000000000388",
            "quantity": 1,
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_treatment_code": "uae_others",
            "product_type": "goods",
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "serial_numbers": "string",
            "location_id": "460000000038080",
            "project_id": 90300000087378
        }
    ],
    "location_id": "460000000038080",
    "creditnote_number": "CN-29",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "place_of_supply": "TN",
    "ignore_auto_number_generation": false,
    "reference_number": "INV-384",
    "custom_fields": [
        { "index": 1, "value": "SomeValue" } /* Example structure */
    ],
    "notes": "Offer for the referral",
    "terms": "",
    "template_id": "90300000001336",
    "tax_id": "903000000000356",
    "tax_authority_id": "903000006345",
    "tax_exemption_id": "903000006345",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "overseas",
    "is_inclusive_tax": false, /* Original example 'fasle' is a typo */
    "avatax_tax_code": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been created.",
    "creditnote": {
        "creditnote_id": "90300000072369",
        "status": "draft", /* Or 'open' if is_draft was false/omitted */
        /* ... full credit note details ... */
    }
}
```

## Email History

### Description
Get email history of a credit note.

### Endpoint
`GET /creditnotes/{creditnote_id}/emailhistory`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/emailhistory?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "email_history": [
        {
            "mailhistory_id": 982000000570005,
            "from": "gator@zillum.com",
            "to_mail_ids": [
                "benjamin.george@bowmanfurniture.com",
                "paul@bowmanfurniture.com"
            ],
            "subject": "Credit note for subscription.",
            "date": "2016-06-05"
        },
        {...},
        {...}
    ]
}
```

## Delete a Credit Note

### Description
Delete an existing credit note.

### Endpoint
`DELETE /creditnotes/{creditnote_id}`

### OAuth Scope
`ZohoBooks.creditnotes.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been deleted."
}
```

## Delete Credit Note Refund

### Description
Delete a credit note refund transaction.

### Endpoint
`DELETE /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`

### OAuth Scope
`ZohoBooks.creditnotes.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/refunds/982000000567158?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund has been successfully deleted."
}
```

## Delete a Comment

### Description
Delete a credit note comment.

### Endpoint
`DELETE /creditnotes/{creditnote_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.creditnotes.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/comments/982000000570001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Get a Credit Note

### Description
Get the details of an existing credit note.

### Endpoint
`GET /creditnotes/{creditnote_id}`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Query Parameters
*   **print** (boolean/string): Export pdf with default print option. Allowed Values: `true`, `false`, `on`, `off`.
*   **accept** (string): Response format. Allowed values: `json`, `pdf`, `html`. Default: `json` *(Note: Documentation stated default html)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "creditnote": {
        "creditnote_id": "90300000072369",
        "creditnote_number": "CN-29",
        /* ... full credit note details ... */
    }
}
```

## Get Credit Note Refund

### Description
Get refund details of a particular credit note refund transaction.

### Endpoint
`GET /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/refunds/982000000567158?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund of the credit note is displayed successfully.",
    "creditnote_refund": {
        "creditnote_refund_id": "982000000567158",
        "creditnote_id": "90300000072369",
        "date": "2016-06-05",
        "refund_mode": "cash",
        "payment_form": "cash",
        "reference_number": "INV-384",
        "amount": 450,
        "customer_name": "Bowman Furniture",
        "description": "prorated amount for items"
    }
}
```

## Get Email Content

### Description
Get email content of a credit note based on a template.

### Endpoint
`GET /creditnotes/{creditnote_id}/email`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Query Parameters
*   **email_template_id** (string): Use a specific email template ID. If omitted, uses customer's associated template or default.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/email?organization_id=10234695&email_template_id=460000000000085' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": /* Original response was an array, likely should be single object */
    {
        "body": "The credit note is attached with this email.",
        "error_list": [],
        "subject": "Credit Note from Zillium Inc(Credit Note #: CN-00001)",
        "emailtemplates": [
            {
                "selected": false, /* Original example had typo 'fasle' */
                "name": "Default",
                "email_template_id": "460000000000085"
            }
        ],
        "to_contacts": [
            {
                "first_name": "Will",
                "selected": false, /* Typo */
                "phone": "+1-925-921-9201",
                "email": "willsmith@bowmanfurniture.com",
                "contact_person_id": "460000000026051",
                "last_name": "Parker",
                "salutation": "Mr.",
                "mobile": "+1-4054439760"
            }
        ],
        "file_name": "CN-00001.pdf",
        "from_emails": [
            {
                "user_name": "John Smith",
                "selected": false, /* Typo */
                "email": "willsmith@bowmanfurniture.com"
            }
        ],
        "customer_id": "46000000002609"
    }
}
```

## List all Credit Notes

### Description
List all the Credit Notes.

### Endpoint
`GET /creditnotes`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Query Parameters
*   **creditnote_number** (string): Search by credit note number. Max-Length [100].
*   **date** (string): Search by date (variants: `_start`, `_end`, `_before`, `_after`). Format [yyyy-mm-dd].
*   **status** (string): Search by status (`open`, `closed`, `void`, `draft`).
*   **total** (double): Search by total amount.
*   **reference_number** (string): Search by reference number. Max-Length [100].
*   **customer_name** (string): Search by customer name. Max-Length [100].
*   **item_name** (string): Search by item name (variants: `_startswith`, `_contains`). Max-length [100].
*   **customer_id** (string): Filter by customer ID.
*   **item_description** (string): Search by item description (variants: `_startswith`, `_contains`). Max-length [100].
*   **item_id** (string): Filter by item ID.
*   **line_item_id** (string): Filter by line item ID.
*   **tax_id** (string): Filter by tax ID.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Open`, `Status.Draft`, `Status.Closed`, `Status.Void`.
*   **search_text** (string): Search by credit note number, customer name, or reference number. Max-length [100].
*   **sort_column** (string): Sort results. Allowed Values: `customer_name`, `creditnote_number`, `balance`, `total`, `date`, `created_time`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes?organization_id=10234695&status=open' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "creditnotes": [ /* Original example had single object */
        {
            "creditnote_id": "90300000072369",
            "creditnote_number": "CN-29",
            "status": "draft", /* Example status */
            "reference_number": "INV-384",
            "date": "2016-06-05",
            "total": 450,
            "balance": 10,
            "location_id": "460000000038080",
            "location_name": "string",
            "customer_id": "903000000000099",
            "customer_name": "Bowman Furniture",
            "currency_id": "982000000567240",
            "currency_code": "USD",
            "created_time": "2016-06-05T02:30:08-0700",
            "last_modified_time": "2016-06-05T02:30:08-0700",
            "is_emailed": true
        }
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "CreditNotes",
        "applied_filter": "Status.Open", /* Example filter */
        "sort_column": "date",
        "sort_order": "D"
    }
}
```

## List Credit Note Comments and History

### Description
Get history and comments of a credit note.

### Endpoint
`GET /creditnotes/{creditnote_id}/comments`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments of the credit note are displayed successfully.",
    "comments": [
        {
            "comment_id": "982000000570001",
            "creditnote_id": "90300000072369",
            "description": "Credits applied to invoice INV-00004",
            "commented_by_id": "982000000554041",
            "commented_by": "Sujin Kumar",
            "comment_type": "system", /* or user */
            "date": "2016-06-05",
            "date_description": "7 hours ago",
            "time": "10:43 PM",
            "operation_type": "Updated", /* e.g., Added, Updated, Emailed */
            "transaction_id": "903000002072369", /* Related transaction */
            "transaction_type": "email" /* Type of related transaction */
        },
        {...},
        {...}
    ]
}
```

## List Credit Note Refunds (All)

### Description
List all refunds with pagination across all credit notes.

### Endpoint
`GET /creditnotes/refunds`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Query Parameters
*   **customer_id** (string): Filter refunds by customer ID.
*   **sort_column** (string): Sort refunds list. Allowed Values: `refund_mode`, `reference_number`, `date`, `creditnote_number`, `customer_name`, `amount_bcy`, `amount_fcy`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/refunds?organization_id=10234695&sort_column=date' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The list of credit note refunds are displayed successfully.",
    "creditnote_refunds": [
        {
            "creditnote_refund_id": "982000000567158",
            "creditnote_id": "90300000072369",
            "date": "2016-06-05",
            "refund_mode": "cash",
            "payment_form": "cash",
            "reference_number": "INV-384",
            "creditnote_number": "CN-29",
            "customer_name": "Bowman Furniture",
            "description": "",
            "amount_bcy": 10,
            "amount_fcy": 10
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Credit Notes Refund",
        "sort_column": "created_time", /* Example shows different sort */
        "sort_order": "D"
    }
}
```

## List Credit Note Templates

### Description
Get all credit note pdf templates.

### Endpoint
`GET /creditnotes/templates`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Standard Template",
            "template_id": "90300000001336",
            "template_type": "professional" /* Example shows professional */
        },
        {...},
        {...}
    ]
}
```

## List Invoices Credited

### Description
List invoices to which the credit note is applied.

### Endpoint
`GET /creditnotes/{creditnote_id}/invoices`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "invoices_credited": [
        {
            "creditnote_id": "90300000072369",
            "invoice_id": "90300000079426",
            "creditnote_invoice_id": "982000000567172", /* ID mapping this specific application */
            "date": "2016-06-05",
            "invoice_number": "INV-384",
            "creditnote_number": "CN-29",
            "credited_amount": 12.02
        },
        {...},
        {...}
    ]
}
```

## List Refunds of a Credit Note

### Description
List all refunds of an existing credit note.

### Endpoint
`GET /creditnotes/{creditnote_id}/refunds`

### OAuth Scope
`ZohoBooks.creditnotes.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refunds of the existing credit note are displayed successfully.",
    "creditnote_refunds": [
        {
            "creditnote_refund_id": "982000000567158",
            "creditnote_id": "90300000072369",
            "date": "2016-06-05",
            "refund_mode": "cash",
            "payment_form": "cash",
            "reference_number": "INV-384",
            "creditnote_number": "CN-29",
            "customer_name": "Bowman Furniture",
            "description": "",
            "amount_bcy": 10,
            "amount_fcy": 10
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Credit Notes Refund",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Refund Credit Note

### Description
Refund credit note amount.

### Endpoint
`POST /creditnotes/{creditnote_id}/refunds`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Arguments (Body Parameters)
*   **date** (string): Date of the refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Method of refund (e.g., cash, check, bank_transfer).
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **reference_number** (string): Reference number for the refund. Max-Length [100].
*   **amount** (double): Amount to refund.
*   **exchange_rate** (string): Exchange rate *(Note: Data type string, likely float/double)*.
*   **from_account_id** (string): The account from which the refund is made.
*   **description** (string): Description for the refund.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2016-06-05", "refund_mode": "cash", "amount": 10.0, "from_account_id": "ACCOUNT_ID"}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "payment_form": "cash",
    "reference_number": "INV-384",
    "amount": 450,
    "exchange_rate": "5.5",
    "from_account_id": "ACCOUNT_ID_HERE", /* Example value was empty */
    "description": "prorated amount for items"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note amount is refunded successfully.",
    "creditnote_refund": {
        "creditnote_refund_id": "982000000567158",
        "creditnote_id": "90300000072369",
        "date": "2016-06-05",
        "refund_mode": "cash",
        "payment_form": "cash",
        "reference_number": "INV-384",
        "amount": 450,
        "customer_name": "Bowman Furniture",
        "description": "prorated amount for items"
    }
}
```

## Submit a Credit Note for Approval

### Description
Submit a credit note for approval. *(Note: Documentation title said "estimate", corrected here)*.

### Endpoint
`POST /creditnotes/{creditnote_id}/submit`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The Credit Note has been successfully submitted for approval."
}
```

## Update a Credit Note using Custom Field

### Description
Update a credit note using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /creditnotes` *(with custom headers)*

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE` *(Note: Original scope was invoices.UPDATE)*

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*(Same parameters as Create a Credit Note, with `line_item_id` required for updating existing lines)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "date": "2016-06-05", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "currency_id": "982000000567240",
    "contact_persons": [
        "903000006532"
    ],
    "date": "2016-06-05",
    "is_draft": true,
    "exchange_rate": "5.5",
    "line_items": [
        {
            "line_item_id": 903000006245, /* Required for update */
            "item_id": "90300000081501",
            "account_id": "903000000000388",
            "name": "Basic Monthly",
            "description": "prorated amount for items",
            "item_order": 0,
            "rate": 0,
            "quantity": 1,
            "unit": "kgs",
            "discount": 10,
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_exemption_id": "903000006345",
            "tax_exemption_code": "GST FREE",
            "tax_treatment_code": "uae_others",
            "avatax_use_code": "string",
            "avatax_tax_code": "string",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "item_custom_fields": [ { "index": 1, "value": "UpdatedValue" } ], /* Needs proper structure */
            "location_id": "460000000038080",
            "location_name": "string",
            "serial_numbers": "string",
            "project_id": 90300000087378
        }
    ],
    "location_id": "460000000038080",
    "creditnote_number": "CN-29",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "place_of_supply": "TN",
    "ignore_auto_number_generation": false,
    "reference_number": "INV-384",
    "custom_fields": [ { "index": 1, "value": "UpdatedCF" } ], /* Needs proper structure */
    "notes": "Offer for the referral",
    "terms": "",
    "template_id": "90300000001336",
    "tax_id": "903000000000356",
    "tax_authority_id": "903000006345",
    "tax_exemption_id": "903000006345",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "overseas",
    "is_inclusive_tax": false /* Original example 'fasle' is typo */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been updated.",
    "creditnote": {
        "creditnote_id": "90300000072369",
        /* ... updated credit note details ... */
    }
}
```

## Update a Credit Note

### Description
Update the details of an existing credit note.

### Endpoint
`PUT /creditnotes/{creditnote_id}`

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE`

### Arguments (Body Parameters)
*(Same parameters as Create a Credit Note, with `line_item_id` required for updating existing lines)*

### Query Parameters
*   **ignore_auto_number_generation** (boolean): Set true to provide your own number *(duplicate of body param)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "date": "2016-06-05", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "currency_id": "982000000567240",
    "contact_persons": [
        "903000006532"
    ],
    "date": "2016-06-05",
    "is_draft": true,
    "exchange_rate": "5.5",
    "line_items": [
        {
            "line_item_id": 903000006245, /* Required for update */
            "item_id": "90300000081501",
            "account_id": "903000000000388",
            "name": "Basic Monthly",
            "description": "prorated amount for items",
            "item_order": 0,
            "rate": 0,
            "quantity": 1,
            "unit": "kgs",
            "discount": 10,
            "tax_id": "903000000000356",
            "tds_tax_id": "903000000000357",
            "tax_exemption_id": "903000006345",
            "tax_exemption_code": "GST FREE",
            "tax_treatment_code": "uae_others",
            "avatax_use_code": "string",
            "avatax_tax_code": "string",
            "product_type": "goods",
            "hsn_or_sac": 80540,
            "sat_item_key_code": 71121206,
            "unitkey_code": "box",
            "item_custom_fields": [ { "index": 1, "value": "UpdatedValue" } ], /* Needs proper structure */
            "location_id": "460000000038080",
            "location_name": "string",
            "serial_numbers": "string",
            "project_id": 90300000087378
        }
    ],
    "location_id": "460000000038080",
    "creditnote_number": "CN-29",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "place_of_supply": "TN",
    "ignore_auto_number_generation": false,
    "reference_number": "INV-384",
    "custom_fields": [ { "index": 1, "value": "UpdatedCF" } ], /* Needs proper structure */
    "notes": "Offer for the referral",
    "terms": "",
    "template_id": "90300000001336",
    "tax_id": "903000000000356",
    "tax_authority_id": "903000006345",
    "tax_exemption_id": "903000006345",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "overseas",
    "is_inclusive_tax": false /* Original example 'fasle' is typo */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been updated.",
    "creditnote": {
        "creditnote_id": "90300000072369",
        /* ... updated credit note details ... */
    }
}
```

## Update Billing Address

### Description
Updates the billing address for an existing credit note alone.

### Endpoint
`PUT /creditnotes/{creditnote_id}/address/billing`

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Billing address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Billing Address", "city": "New City", ...}'
```

#### Body Parameters
```json
{
    "address": "4900 Hopyard Rd, Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": "94588", /* Should likely be string */
    "country": "USA",
    "fax": "+1-925-924-9600"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated"
}
```

## Update Credit Note Refund

### Description
Update the refunded transaction.

### Endpoint
`PUT /creditnotes/{creditnote_id}/refunds/{creditnote_refund_id}`

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE`

### Arguments (Body Parameters)
*   **date** (string): Date of the refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Method of refund.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **reference_number** (string): Reference number. Max-Length [100].
*   **amount** (double): Refund amount.
*   **exchange_rate** (string): Exchange rate *(Note: Data type string, likely float/double)*.
*   **from_account_id** (string): Account from which refund was made.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/refunds/982000000567158?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2016-06-06", "amount": 450.00, ...}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "payment_form": "cash",
    "reference_number": "INV-384",
    "amount": 450,
    "exchange_rate": "5.5",
    "from_account_id": "ACCOUNT_ID_HERE", /* Example was empty */
    "description": "prorated amount for items"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note refund is updated successfully.",
    "creditnote_refund": {
        "creditnote_refund_id": "982000000567158",
        "creditnote_id": "90300000072369",
        /* ... updated refund details ... */
    }
}
```

## Update Credit Note Template

### Description
Update the pdf template associated with the credit note.

### Endpoint
`PUT /creditnotes/{creditnote_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE`

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/templates/90300000001336?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been updated."
}
```

## Update Shipping Address

### Description
Updates the shipping address for an existing credit note alone.

### Endpoint
`PUT /creditnotes/{creditnote_id}/address/shipping`

### OAuth Scope
`ZohoBooks.creditnotes.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Shipping address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/address/shipping?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Shipping Address", "city": "New Ship City", ...}'
```

#### Body Parameters
```json
{
    "address": "Suite 125, McMillan Avenue",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94134", /* Should likely be string */
    "country": "USA",
    "fax": "+1-925-924-9600"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Shipping address updated"
}
```

## Void a Credit Note

### Description
Mark the credit note as Void.

### Endpoint
`POST /creditnotes/{creditnote_id}/status/void`

### OAuth Scope
`ZohoBooks.creditnotes.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/creditnotes/90300000072369/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The credit note has been marked as void."
}
```
# Customer Payments

## Overview

### Customer Payments
Payments from Customers towards Invoices.

### End Points
*   `POST /customerpayments`
*   `PUT /customerpayments` *(Note: This is likely for bulk/keyed updates, see Update Payment using Custom Field)*
*   `GET /customerpayments`
*   `PUT /customerpayments/{payment_id}`
*   `GET /customerpayments/{payment_id}`
*   `DELETE /customerpayments/{payment_id}`
*   `POST /customerpayments/{customer_payment_id}/refunds`
*   `GET /customerpayments/{customer_payment_id}/refunds`
*   `PUT /customerpayment/{customer_payment_id}/customfields`
*   `PUT /customerpayments/{customer_payment_id}/refunds/{refund_id}`
*   `GET /customerpayments/{customer_payment_id}/refunds/{refund_id}`
*   `DELETE /customerpayments/{customer_payment_id}/refunds/{refund_id}`

### Attributes
*   **payment_id** (string): Unique ID of the payment. Max-length [2000].
*   **payment_mode** (string): Mode of payment (check, cash, creditcard, banktransfer, etc.). Max-length [100].
*   **amount** (double): Amount paid.
*   **amount_refunded** (double): Amount refunded (Applicable for autotransaction mode).
*   **bank_charges** (double): Additional bank charges.
*   **date** (string): Date payment was made. Format [yyyy-mm-dd].
*   **status** (string): Payment status (success or failure).
*   **reference_number** (string): Reference number. Max-length [100].
*   **description** (string): Payment description.
*   **customer_id** (string): Customer ID.
*   **customer_name** (string): Customer name. Max-length [100].
*   **email** (string): Customer email.
*   **invoices** (array): List of invoices associated with the payment.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **custom_fields** (array): Custom fields.

### Example
```json
{
    "payment_id": "9030000079467",
    "payment_mode": "cash",
    "amount": 450,
    "amount_refunded": 50,
    "bank_charges": 10,
    "date": "2016-06-05",
    "status": "success",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "customer_id": "903000000000099",
    "customer_name": "Bowman Furniture",
    "email": "benjamin.george@bowmanfurniture.com",
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "invoice_number": "INV-384",
            "date": "2016-06-05",
            "invoice_amount": 450,
            "amount_applied": 450,
            "balance_amount": 0
        }
    ],
    "currency_code": "USD",
    "currency_symbol": "$",
    "location_id": "460000000038080",
    "location_name": "string",
    "custom_fields": [
        {
            "index": 1,
            "value": 129890,
            "label": "label",
            "data_type": "text"
        }
    ]
}
```

## Create a Payment

### Description
Create a new payment.

### Endpoint
`POST /customerpayments`

### OAuth Scope
`ZohoBooks.customerpayments.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): Customer ID.
*   **payment_mode** (string, Required): Mode of payment (check, cash, creditcard, etc.). Max-length [100].
*   **amount** (double, Required): Amount paid.
*   **date** (string, Required): Date payment made. Format [yyyy-mm-dd].
*   **reference_number** (string): Reference number. Max-length [100].
*   **description** (string): Payment description.
*   **invoices** (array, Required): List of invoices associated with the payment.
    *   **invoice_id** (string, Required): Invoice ID.
    *   **amount_applied** (double, Required): Amount applied to this invoice.
    *   **tax_amount_withheld** (double): Amount withheld for tax.
*   **exchange_rate** (double, default: 1): Exchange rate if currency differs.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **bank_charges** (double): Bank charges.
*   **custom_fields** (array): Custom fields.
*   **location_id** (string): Location ID.
*   **account_id** (string): ID of the cash/bank account for deposit.
*   **contact_persons** (array): Contact person IDs to trigger thank you mail.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/customerpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "payment_mode": "cash", "amount": 450, "date": "2016-06-05", "invoices": [...] }'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "payment_mode": "cash",
    "amount": 450,
    "date": "2016-06-05",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "amount_applied": 450,
            "tax_amount_withheld": 0 /* Added based on individual params in original doc */
        }
    ],
    "exchange_rate": 1,
    "payment_form": "cash",
    "bank_charges": 10,
    "custom_fields": [
        {
            "label": "label",
            "value": 129890
        }
    ],
    "location_id": "460000000038080",
    "account_id": "VALID_ACCOUNT_ID", /* Original example was empty */
    "contact_persons": [
        "982000000870911",
        "982000000870915"
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment has been created.",
    "payment": {
        "payment_id": "9030000079467",
        /* ... full payment details ... */
    }
}
```

## Delete a Payment

### Description
Delete an existing payment.

### Endpoint
`DELETE /customerpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.customerpayments.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment has been deleted."
}
```

## Delete a Refund

### Description
Delete refund pertaining to an existing customer payment.

### Endpoint
`DELETE /customerpayments/{customer_payment_id}/refunds/{refund_id}`

### OAuth Scope
`ZohoBooks.customerpayments.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467/refunds/3000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund has been deleted."
}
```

## Details of a Refund

### Description
Obtain details of a particular refund of a customer payment.

### Endpoint
`GET /customerpayments/{customer_payment_id}/refunds/{refund_id}`

### OAuth Scope
`ZohoBooks.customerpayments.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467/refunds/3000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The details of the refund are displayed successfully.",
    "payment_refund": { /* Corrected: original showed array */
        "payment_refund_id": "3000000003017",
        "payment_id": "9030000079467",
        "date": "2016-06-05",
        "refund_mode": "cash",
        "reference_number": "INV-384",
        "amount": 450,
        "exchange_rate": 1,
        "payment_form": "cash",
        "description": "Payment has been added to INV-384"
        /* May include customer_name */
    }
}
```

## List Customer Payments

### Description
List all the payments made by your customer.

### Endpoint
`GET /customerpayments`

### OAuth Scope
`ZohoBooks.customerpayments.READ`

### Query Parameters
*   **customer_name** (string): Search by customer name (variants: `_startswith`, `_contains`). Max-len [100].
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`). Max-len [100].
*   **date** (string): Search by date (variants apply, format yyyy-mm-dd).
*   **amount** (double): Search by amount (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **notes** (string): Search by notes (variants: `_startswith`, `_contains`).
*   **payment_mode** (string): Search by payment mode (variants: `_startswith`, `_contains`).
*   **filter_by** (string): Filter by payment mode. Allowed Values: `PaymentMode.All`, `PaymentMode.Check`, ... `PaymentMode.Others`.
*   **sort_column** (string): Column to sort by (e.g., `customer_name`, `date`, `amount`).
*   **search_text** (string): Search by reference number, customer name, or description. Max-length [100].
*   **customer_id** (string): Filter by customer ID.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/customerpayments?organization_id=10234695&payment_mode=cash' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "customer_payments": [
        {
            "payment_id": "9030000079467",
            "payment_number": "2",
            "invoice_number": "INV-384", /* Note: This seems specific to single-invoice payments */
            "date": "2016-06-05",
            "payment_mode": "cash",
            "amount": 450,
            "bcy_amount": 450,
            "location_id": "460000000038080",
            "location_name": "string"
            /* Other payment details like customer_name, customer_id likely included */
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected: original showed null */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "sort_column": "date",
        "sort_order": "D"
    }
}
```

## List Refunds of a Customer Payment

### Description
List all the refunds pertaining to an existing customer payment.

### Endpoint
`GET /customerpayments/{customer_payment_id}/refunds`

### OAuth Scope
`ZohoBooks.customerpayments.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The list of refunds of the customer is displayed successfully.",
    "payment_refunds": [
        {
            "payment_refund_id": "3000000003017",
            "payment_id": "9030000079467",
            "date": "2016-06-05",
            "refund_mode": "cash",
            "reference_number": "INV-384",
            "payment_number": "2", /* Original payment number */
            "customer_name": "Bowman Furniture",
            "amount_bcy": 10, /* Amount in Base Currency */
            "amount_fcy": 10 /* Amount in Foreign Currency */
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Customer Payments Refund",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Refund an Excess Customer Payment

### Description
Refund the excess amount paid by the customer.

### Endpoint
`POST /customerpayments/{customer_payment_id}/refunds`

### OAuth Scope
`ZohoBooks.customerpayments.CREATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Date of refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Method of refund. Max-length [50].
*   **reference_number** (string): Reference number. Max-length [100].
*   **amount** (double, Required): Amount to refund.
*   **exchange_rate** (double, default: 1): Exchange rate if applicable.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **from_account_id** (string, Required): Account from which refund is made.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2016-06-05", "amount": 50.00, "from_account_id": "ACCOUNT_ID", ...}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "reference_number": "INV-384",
    "amount": 50, /* Should be the refund amount */
    "exchange_rate": 1,
    "payment_form": "cash",
    "from_account_id": "VALID_ACCOUNT_ID", /* Needs valid account ID */
    "description": "Refund for overpayment" /* Should describe refund */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information for this payment has been saved.",
    "payment_refund": { /* Corrected: original showed array */
        "payment_refund_id": "3000000003017",
        "payment_id": "9030000079467",
        "date": "2016-06-05",
        "refund_mode": "cash",
        "reference_number": "INV-384",
        "amount": 50,
        "exchange_rate": 1,
        "payment_form": "cash",
        "description": "Refund for overpayment"
    }
}
```

## Retrieve a Payment

### Description
Retrieve details of an existing payment.

### Endpoint
`GET /customerpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.customerpayments.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "payment": {
        "payment_id": "9030000079467",
        "payment_mode": "cash",
        "amount": 450,
        /* ... full payment details ... */
    }
}
```

## Update a Payment using Custom Field

### Description
Update a payment using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found. *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs)*.

### Endpoint
`PUT /customerpayments` *(Note: Example shows this, but typically PUT for update uses ID like `/customerpayments/{payment_id}`. This endpoint might work with headers.)*

### OAuth Scope
`ZohoBooks.customerpayments.UPDATE`

### Headers
*(Assumed based on description, not shown in example)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*(Same parameters as Create a Payment)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/customerpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "payment_mode": "cash", "amount": 450, "invoices": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "payment_mode": "cash",
    "amount": 450,
    "date": "2016-06-05",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "amount_applied": 450,
            "tax_amount_withheld": 0 /* Added based on individual params in original doc */
        }
    ],
    "exchange_rate": 1,
    "payment_form": "cash",
    "bank_charges": 10,
    "custom_fields": [
        {
            "label": "label",
            "value": 129890
        }
    ],
    "location_id": "460000000038080",
    "account_id": "VALID_ACCOUNT_ID" /* Original example was empty */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment details have been updated.",
    "payment": {
        "payment_id": "9030000079467",
        /* ... updated payment details ... */
    }
}
```

## Update a Payment

### Description
Update an existing payment information.

### Endpoint
`PUT /customerpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.customerpayments.UPDATE`

### Arguments (Body Parameters)
*(Same parameters as Create a Payment)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "903000000000099", "payment_mode": "check", "amount": 450, "invoices": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": "903000000000099",
    "payment_mode": "cash",
    "amount": 450,
    "date": "2016-06-05",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "invoices": [
        {
            "invoice_id": "90300000079426",
            "amount_applied": 450,
            "tax_amount_withheld": 0 /* Added based on individual params in original doc */
        }
    ],
    "exchange_rate": 1,
    "payment_form": "cash",
    "bank_charges": 10,
    "custom_fields": [
        {
            "label": "label",
            "value": 129890
        }
    ],
    "location_id": "460000000038080",
    "account_id": "VALID_ACCOUNT_ID" /* Original example was empty */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment details have been updated.",
    "payment": {
        "payment_id": "9030000079467",
        /* ... updated payment details ... */
    }
}
```

## Update a Refund

### Description
Update the refunded transaction.

### Endpoint
`PUT /customerpayments/{customer_payment_id}/refunds/{refund_id}`

### OAuth Scope
`ZohoBooks.customerpayments.UPDATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Date of refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Method of refund. Max-length [50].
*   **reference_number** (string): Reference number. Max-length [100].
*   **amount** (double, Required): Refund amount.
*   **exchange_rate** (double, default: 1): Exchange rate if applicable.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **description** (string): Description.
*   **from_account_id** (string, Required): Account refund was made from.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/customerpayments/9030000079467/refunds/3000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2016-06-06", "amount": 450.00, ...}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "reference_number": "INV-384",
    "amount": 450,
    "exchange_rate": 1,
    "payment_form": "cash",
    "description": "Payment has been added to INV-384", /* Should describe refund */
    "from_account_id": "VALID_ACCOUNT_ID" /* Needs valid account ID */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information has been saved.", /* Message implies save, not update */
    "payment_refund": { /* Corrected: original showed array */
        "payment_refund_id": "3000000003017",
        "payment_id": "9030000079467",
        /* ... updated refund details ... */
    }
}
```

## Update Custom Field in Customer Payment

### Description
Update the value of the custom field in existing customer payments.

### Endpoint
`PUT /customerpayment/{customer_payment_id}/customfields`

### OAuth Scope
`ZohoBooks.customerpayments.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field to update.
    *   **value** (string): The new value for the custom field.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/customerpayment/9030000079467/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "46000000012845", "value": "Updated Value"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "46000000012845",
        "value": 129890 /* New value */
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```
# Expenses

## Overview

### Expenses
A typical expense is incurred when money goes out of your pocket. Whether its a product you buy from your vendor to run your business, or food that you eat while on business trips, it’s important to track the money you spend.

### End Points
*   `POST /expenses` (Create Expense)
*   `PUT /expenses` (Update Expense by Custom Field)
*   `GET /expenses` (List Expenses)
*   `PUT /expenses/{expense_id}` (Update Expense by ID)
*   `GET /expenses/{expense_id}` (Get Expense)
*   `DELETE /expenses/{expense_id}` (Delete Expense)
*   `GET /expenses/{expense_id}/comments` (List Comments & History)
*   `POST /employees` (Create Employee)
*   `GET /employees` (List Employees)
*   `GET /employees/{employee_id}` (Get Employee)
*   `DELETE /employee/{employee_id}` (Delete Employee - *Note: Typo in original endpoint path*)
*   `POST /expenses/{expense_id}/receipt` (Add Receipt)
*   `GET /expenses/{expense_id}/receipt` (Get Receipt)
*   `DELETE /expenses/{expense_id}/receipt` (Delete Receipt)
*   *(Note: POST/DELETE/PUT for comments are missing in the provided files, though GET exists)*
*   *(Note: PUT for custom fields is missing)*

### Attributes
*   **expense_id** (string)
*   **transaction_id** (string)
*   **transaction_type** (string)
*   **gst_no** (string): 🇮🇳 only - 15 digit GST identification number of the vendor.
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: `business_gst` , `business_none` , `overseas` , `consumer` .
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **destination_of_supply_state** (string): 🇮🇳 only - State where goods/services are supplied.
*   **place_of_supply** (string): GCC only - Place of supply for VAT (Supported codes listed).
*   **hsn_or_sac** (string): 🇮🇳 , 🇰🇪 only - HSN/SAC code.
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **paid_through_account_name** (string): Name of the account used for payment.
*   **vat_reg_no** (string): VAT registration number.
*   **reverse_charge_tax_id** (string): ID of the reverse charge tax.
*   **reverse_charge_tax_name** (string): 🇮🇳 only - Name of the reverse charge tax.
*   **reverse_charge_tax_percentage** (double): 🇮🇳 only - Percentage of the reverse charge tax.
*   **reverse_charge_tax_amount** (integer): 🇮🇳 only - Amount of the reverse charge tax.
*   **tax_amount** (double): Tax amount applied.
*   **is_itemized_expense** (boolean): Whether the expense uses line items.
*   **is_pre_gst** (string): 🇮🇳 only - Applicable before July 1, 2017 *(Note: Data type string, likely boolean)*.
*   **trip_id** (string): Trip ID.
*   **trip_number** (string): Trip number.
*   **reverse_charge_vat_total** (double): 🇮🇳 only - Total reverse charge VAT.
*   **acquisition_vat_total** (double): Total acquisition VAT.
*   **acquisition_vat_summary** (array): Summary of Acquisition VAT.
*   **reverse_charge_vat_summary** (array): Summary of Reverse Charge VAT.
*   **taxes** (array): 🇲🇽 only - Taxes associated.
*   **expense_item_id** (string): ID if created from an expense item template.
*   **account_id** (string): ID of the expense account.
*   **account_name** (string): Name of the expense account.
*   **date** (string): Date of the expense. Format [yyyy-mm-dd].
*   **tax_id** (string): ID of the tax applied.
*   **tax_name** (string): Name of the tax applied.
*   **tax_percentage** (double): Percentage of the tax applied.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **exchange_rate** (double): Exchange rate.
*   **sub_total** (double): Subtotal before tax.
*   **total** (double): Total amount including tax.
*   **bcy_total** (double): Total in base currency.
*   **amount** (double): Amount of the Expense *(Note: Might be redundant with total/subtotal depending on context)*.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **reference_number** (string): Reference number. Max-length [100].
*   **description** (string): Description. Max-length [100].
*   **is_billable** (boolean): Is the expense billable to a customer.
*   **is_personal** (boolean): Is this a personal expense.
*   **customer_id** (string): Customer ID (if billable).
*   **customer_name** (string): Customer name (if billable). Max-length [100].
*   **expense_receipt_name** (string): Filename of the attached receipt.
*   **expense_receipt_type** (string): File type of the receipt.
*   **last_modified_time** (string)
*   **status** (string): Expense status (e.g., `unbilled`, `invoiced`, `reimbursed`, `non-billable`).
*   **invoice_id** (string): ID of the invoice if billed.
*   **invoice_number** (string): Number of the invoice if billed.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **project_id** (string): Project ID (if associated).
*   **project_name** (string): Project name.
*   **mileage_rate** (double): Rate for mileage expense.
*   **mileage_type** (string): Type of mileage expense (e.g., `odometer`, `manual`).
*   **expense_type** (string): General expense type.
*   **start_reading** (double): Odometer start reading.
*   **end_reading** (double): Odometer end reading.

### Example
```json
{
    "expense_id": 982000000030049,
    "transaction_id": " ",
    "transaction_type": "expense",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "destination_of_supply": "TN",
    "destination_of_supply_state": "TN",
    "place_of_supply": "DU",
    "hsn_or_sac": 80540,
    "source_of_supply": "AP",
    "paid_through_account_name": "Petty Cash",
    "vat_reg_no": "string",
    "reverse_charge_tax_id": 982000000561063,
    "reverse_charge_tax_name": "intra",
    "reverse_charge_tax_percentage": 10,
    "reverse_charge_tax_amount": 12,
    "tax_amount": 11.85,
    "is_itemized_expense": false,
    "is_pre_gst": "false", /* Corrected typo */
    "trip_id": "",
    "trip_number": "",
    "reverse_charge_vat_total": 1.2,
    "acquisition_vat_total": 0,
    "acquisition_vat_summary": [ { /* ... summary ... */ } ],
    "reverse_charge_vat_summary": [ { /* ... summary ... */ } ],
    "taxes": [ { /* ... tax details ... */ } ],
    "expense_item_id": 982000000567220,
    "account_id": 982000000561057,
    "account_name": "Rent",
    "date": "2013-11-18",
    "tax_id": 982000000566007,
    "tax_name": "SalesTax",
    "tax_percentage": 10.5,
    "currency_id": 982000000567001,
    "currency_code": "USD",
    "exchange_rate": 1,
    "sub_total": 90,
    "total": 100,
    "bcy_total": 100,
    "amount": 112.5,
    "is_inclusive_tax": false,
    "reference_number": null,
    "description": "Marketing",
    "is_billable": true,
    "is_personal": false,
    "customer_id": 982000000567001,
    "customer_name": "Bowman & Co",
    "expense_receipt_name": " ",
    "expense_receipt_type": " ",
    "last_modified_time": " ",
    "status": "unbilled",
    "invoice_id": " ",
    "invoice_number": " ",
    "location_id": "460000000038080",
    "location_name": "string",
    "project_id": 982000000567226,
    "project_name": " ",
    "mileage_rate": " ",
    "mileage_type": "non_mileage",
    "expense_type": "non-mileage",
    "start_reading": " ",
    "end_reading": " "
}
```

## Add Receipt to an Expense

### Purpose
Attach a receipt to an existing expense.

### Endpoint
`POST /expenses/{expense_id}/receipt`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Query Parameters
*   **receipt**: Expense receipt file to attach (allowed extensions: `gif`, `png`, `jpeg`, `jpg`, `bmp`, `pdf`, `xls`, `xlsx`, `doc`, `docx`).

### Response Example
```json
{
    "code": 0,
    "message": "The expense receipt has been attached."
}
```

## Create an Employee

### Purpose
Create a new employee for expenses.

### Endpoint
`POST /employees`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Arguments
*   **name** (string, required): Name of the employee.
*   **email** (string, required): Email address of the employee.

### Request Example
```json
{
    "name": "John David",
    "email": "johnsmith@zilliuminc.com"
}
```
*(Note: A success response example was not provided in the original file, but it would typically include the employee details and ID).*

## Create an Expense

### Purpose
Create a new billable or non-billable expense in Zoho Books.

### Endpoint
`POST /expenses`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Arguments
*   **account_id** (string, required): ID of the expense account.
*   **date** (string, required): Date of the expense (format: `yyyy-mm-dd`).
*   **amount** (double, required): Amount of the expense. *(Note: Always use `amount` argument when creating an expense. Never `total`.)*
*   **tax_id** (string, optional): ID of the tax applied to the expense.
*   **source_of_supply** (string, optional, 🇮🇳 only): Place from where the goods/services are supplied.
*   **destination_of_supply** (string, optional, 🇮🇳 only): Place where the goods/services are supplied to.
*   **place_of_supply** (string, optional, GCC only): Place of supply for VAT purposes (e.g., `AB` for Abu Dhabi).
*   **hsn_or_sac** (string, optional, 🇮🇳, 🇰🇪 only): HSN/SAC code for goods/services.
*   **gst_no** (string, optional, 🇮🇳 only): 15-digit GST identification number of the vendor.
*   **reverse_charge_tax_id** (string, optional): ID of the reverse charge tax.
*   **location_id** (string, optional): ID of the location associated with the expense.
*   **line_items** (array, optional): Array of line items for the expense.
    *   Include standard line item attributes.
*   **taxes** (array, optional, 🇲🇽 only): Array of taxes applied to the expense.
    *   **tax_id** (string): ID of the tax.
    *   **tax_amount** (double): Amount of the tax.
*   **is_inclusive_tax** (boolean, optional): Whether the tax is inclusive in the amount.
*   **is_billable** (boolean, optional): Whether the expense is billable.
*   **reference_number** (string, optional): Reference number of the expense (max length: 100).
*   **description** (string, optional): Description of the expense (max length: 100).
*   **customer_id** (string, optional): ID of the customer associated with the expense.
*   **currency_id** (string, optional): ID of the currency.
*   **exchange_rate** (double, optional): Exchange rate for the currency.
*   **project_id** (string, optional): ID of the project associated with the expense.
*   **mileage_type** (string, optional): Type of mileage (e.g., `odometer`, `manual`).
*   **vat_treatment** (string, optional, 🇬🇧 only): VAT treatment for the expense (e.g., `uk`, `eu_vat_registered`).
*   **tax_treatment** (string, optional, GCC, 🇰🇪, 🇿🇦 only): Tax treatment for the expense (e.g., `vat_registered`).
*   **product_type** (string, optional, 🇬🇧, 🇿🇦 only): Type of the expense (e.g., `goods`, `service`).
*   **acquisition_vat_id** (string, optional, 🇬🇧 only): ID of the acquisition VAT.
*   **reverse_charge_vat_id** (string, optional, 🇬🇧 only): ID of the reverse charge VAT.
*   **start_reading** (double, optional): Start reading for mileage expense (if `mileage_type` is `odometer`).
*   **end_reading** (double, optional): End reading for mileage expense (if `mileage_type` is `odometer`).
*   **distance** (string, optional): Distance traveled for mileage expense (if `mileage_type` is `manual`).
*   **mileage_unit** (string, optional): Unit of distance (e.g., `km`, `mile`).
*   **mileage_rate** (double, optional): Mileage rate for the expense.
*   **employee_id** (string, optional, 🇬🇧 only): ID of the employee who submitted the mileage expense.
*   **vehicle_type** (string, optional, 🇬🇧 only): Type of vehicle (e.g., `car`, `van`).
*   **can_reclaim_vat_on_mileage** (string, optional, 🇬🇧 only): Whether VAT can be reclaimed for the mileage expense.
*   **fuel_type** (string, optional, 🇬🇧 only): Type of fuel (e.g., `petrol`, `diesel`).
*   **engine_capacity_range** (string, optional, 🇬🇧 only): Engine capacity range (e.g., `less_than_1400cc`).
*   **paid_through_account_id** (string, required): ID of the account through which the expense was paid.
*   **vendor_id** (string, optional): ID of the vendor associated with the expense.
*   **custom_fields** (array, optional): Custom fields for the expense.

### Query Parameters
*   **receipt**: Expense receipt file to attach (allowed extensions: `gif`, `png`, `jpeg`, `jpg`, `bmp`, `pdf`, `xls`, `xlsx`, `doc`, `docx`).

### Request Example
```json
{
    "account_id": "982000000561057",
    "date": "2013-11-18",
    "amount": 112.5,
    "tax_id": "982000000566007",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "hsn_or_sac": "80540",
    "gst_no": "22AAAAA0000A1Z5",
    "reverse_charge_tax_id": "982000000561063",
    "location_id": "460000000038080",
    "line_items": [
        {
            /* line_item_id is not needed for create */
            "account_id": "982000000561057",
            "description": "Marketing",
            "amount": 112.5,
            "tax_id": "982000000566007",
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": "",
            "reverse_charge_vat_id": "",
            "reverse_charge_tax_id": "982000000561063",
            "tax_exemption_code": "string",
            "tax_exemption_id": "982000000561067",
            "location_id": "460000000038080"
        }
    ],
    "taxes": [
        {
            "tax_id": "982000000566007",
            "tax_amount": 11.85
        }
    ],
    "is_inclusive_tax": false,
    "is_billable": true,
    "reference_number": null,
    "description": "Marketing",
    "customer_id": "982000000567001",
    "currency_id": "982000000567001",
    "exchange_rate": 1,
    "project_id": "982000000567226",
    "mileage_type": "non_mileage",
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": "",
    "reverse_charge_vat_id": "",
    "start_reading": "",
    "end_reading": "",
    "distance": "",
    "mileage_unit": "",
    "mileage_rate": "",
    "employee_id": "",
    "vehicle_type": "",
    "can_reclaim_vat_on_mileage": "",
    "fuel_type": "",
    "engine_capacity_range": "",
    "paid_through_account_id": "982000000567250",
    "vendor_id": "",
    "custom_fields": []
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The expense has been recorded.",
    "expense": {
        "expense_id": "982000000030049",
        /* ... other expense details ... */
    }
}
```

## Delete a Receipt

### Purpose
Delete the receipt attached to an expense.

### Endpoint
`DELETE /expenses/{expense_id}/receipt`

### OAuth Scope
`ZohoBooks.expenses.DELETE`

### Response Example
```json
{
    "code": 0,
    "message": "The attached expense receipt has been deleted."
}
```

## Delete an Employee

### Purpose
Delete an existing employee by ID.

### Endpoint
`DELETE /employee/{employee_id}`

### OAuth Scope
`ZohoBooks.expenses.DELETE`

### Response Example
```json
{
    "code": 0,
    "message": "Employee has been deleted."
}
```

## Delete an Expense

### Purpose
Delete an existing expense by its ID.

### Endpoint
`DELETE /expenses/{expense_id}`

### OAuth Scope
`ZohoBooks.expenses.DELETE`

### Response Example
```json
{
    "code": 0,
    "message": "The expense has been deleted."
}
```

## Get an Employee

### Purpose
Retrieve the details of a specific employee by ID.

### Endpoint
`GET /employees/{employee_id}`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "employee": {
        "employee_id": "EMPLOYEE_ID_HERE", /* Example was empty */
        "name": "John David",
        "email": "johnsmith@zilliuminc.com"
    }
}
```

## Get an Expense

### Purpose
Retrieve the details of a specific expense by its ID.

### Endpoint
`GET /expenses/{expense_id}`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "expense": {
        "expense_id": "982000000030049",
        /* ... full expense details ... */
    }
}
```

## Get an Expense Receipt

### Purpose
Retrieve the receipt attached to an expense.

### Endpoint
`GET /expenses/{expense_id}/receipt`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Query Parameters
*   **preview**: Get the thumbnail of the receipt.

### Response Example
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful request returns the binary file data, not this JSON metadata).*

## List Employees

### Purpose
Retrieve a list of employees with pagination.

### Endpoint
`GET /employees`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "employees": [
        {
            "employee_id": "EMPLOYEE_ID_HERE", /* Example was empty */
            "name": "John David",
            "email": "johnsmith@zilliuminc.com"
        }
    ],
    "page_context": /* Original showed array, corrected to object */
    {
        "page": 1,
        "per_page": 100
        /* Other context fields like has_more_page, sort_column may be present */
    }
}
```
*(Note: Original `page_context` example seemed misplaced from an expense list).*

## List Expense History and Comments

### Purpose
Retrieve the history and comments of a specific expense.

### Endpoint
`GET /expenses/{expense_id}/comments`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "982000000567272",
            "expense_id": "982000000030049",
            "description": "Marketing",
            "commented_by_id": "982000000554041",
            "commented_by": "John David",
            "date_description": "16 hours ago",
            "time": "4.22AM",
            "operation_type": "Added",
            "transaction_id": "",
            "transaction_type": "expense"
        }
    ]
}
```

## List Expenses

### Purpose
Retrieve a list of all expenses with pagination.

### Endpoint
`GET /expenses`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Query Parameters
*   **description**: Search expenses by description. Variants: `description_startswith`, `description_contains`. Max length: 100.
*   **reference_number**: Search expenses by reference number. Variants: `reference_number_startswith`, `reference_number_contains`. Max length: 100.
*   **date**: Search expenses by expense date. Variants: `date_start`, `date_end`, `date_before`, `date_after`. Format: `yyyy-mm-dd`.
*   **status**: Filter expenses by status. Allowed values: `unbilled`, `invoiced`, `reimbursed`, `non-billable`, `billable`.
*   **amount**: Search expenses by amount. Variants: `amount_less_than`, `amount_less_equals`, `amount_greater_than`, `amount_greater_equals`.
*   **account_name**: Search expenses by account name. Variants: `account_name_startswith`, `account_name_contains`. Max length: 100.
*   **customer_name**: Search expenses by customer name. Variants: `customer_name_startswith`, `customer_name_contains`. Max length: 100.
*   **vendor_name**: Search expenses by vendor name. Variants: `vendor_name_startswith`, `vendor_name_contains`.
*   **customer_id**: Filter expenses by customer ID.
*   **vendor_id**: Filter expenses by vendor ID.
*   **recurring_expense_id**: Search expenses by recurring expense ID.
*   **paid_through_account_id**: Search expenses by paid-through account ID.
*   **search_text**: Search expenses by account name, description, customer name, or vendor name. Max length: 100.
*   **sort_column**: Sort expenses by a specific column. Allowed values: `date`, `account_name`, `total`, `bcy_total`, `reference_number`, `customer_name`, `created_time`.
*   **filter_by**: Filter expenses by status. Allowed values: `Status.All`, `Status.Billable`, `Status.Nonbillable`, `Status.Reimbursed`, `Status.Invoiced`, `Status.Unbilled`.

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "expenses": [
        {
            "expense_id": "982000000030049",
            "date": "2013-11-18",
            "account_name": "Rent",
            "description": "Marketing",
            "currency_id": "982000000567001",
            "currency_code": "USD",
            "bcy_total": 100,
            "bcy_total_without_tax": 100,
            "total": 100,
            "total_without_tax": 100,
            "is_billable": true,
            "reference_number": null,
            "customer_id": "982000000567001",
            "customer_name": "Bowman & Co",
            "status": "unbilled",
            "location_id": "460000000038080",
            "location_name": "string",
            "created_time": "2013-11-18T00:00:00.000Z",
            "last_modified_time": "",
            "expense_receipt_name": "",
            "mileage_rate": "",
            "mileage_unit": "",
            "expense_type": "non-mileage",
            "start_reading": "",
            "end_reading": ""
        }
    ],
    "page_context": /* Corrected: original showed array */
    {
        "page": 1,
        "per_page": 100,
        "has_more_page": false, /* Example */
        "applied_filter": "Status.Billable", /* Example */
        "sort_column": "total", /* Example */
        "search_text": "Rent", /* Example */
        "sort_order": "D" /* Example */
    }
}
```

## Update an Expense by ID

### Purpose
Update an existing expense using its ID.

### Endpoint
`PUT /expenses/{expense_id}`

### OAuth Scope
`ZohoBooks.expenses.UPDATE`

### Arguments
*(Same arguments as Create an Expense)*

### Query Parameters
*   **receipt**: Expense receipt file to attach (allowed extensions: `gif`, `png`, `jpeg`, `jpg`, `bmp`, `pdf`, `xls`, `xlsx`, `doc`, `docx`).
*   **delete_receipt**: Delete the attached receipt.

### Request Example
```json
{
    "account_id": "982000000561057",
    "date": "2013-11-18",
    "amount": 120.5,
    "tax_id": "982000000566007",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "hsn_or_sac": "80540",
    "gst_no": "22AAAAA0000A1Z5",
    "reverse_charge_tax_id": "982000000561063",
    "line_items": [
        {
            "line_item_id": "10763000000140068",
            "account_id": "982000000561057",
            "description": "Marketing - Updated", /* Example update */
            "amount": 112.5,
            "tax_id": "982000000566007",
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": "",
            "reverse_charge_vat_id": "",
            "reverse_charge_tax_id": "982000000561063",
            "tax_exemption_code": "string",
            "tax_exemption_id": "982000000561067",
            "location_id": "460000000038080"
        }
    ],
    "location_id": "460000000038080",
    "taxes": [
        {
            "tax_id": "982000000566007",
            "tax_amount": 11.85
        }
    ],
    "is_inclusive_tax": false,
    "is_billable": true,
    "reference_number": null,
    "description": "Marketing - Updated", /* Example update */
    "customer_id": "982000000567001",
    "currency_id": "982000000567001",
    "exchange_rate": 1,
    "project_id": "982000000567226",
    "mileage_type": "non_mileage",
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": "",
    "reverse_charge_vat_id": "",
    "start_reading": "",
    "end_reading": "",
    "distance": "",
    "mileage_unit": "",
    "mileage_rate": "",
    "employee_id": "",
    "vehicle_type": "",
    "can_reclaim_vat_on_mileage": "",
    "fuel_type": "",
    "engine_capacity_range": "",
    "paid_through_account_id": "982000000567250",
    "vendor_id": "",
    "custom_fields": []
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Expense information has been updated.",
    "expense": {
        "expense_id": "982000000030049",
        /* ... updated expense details ... */
    }
}
```

## Update an Expense Using Custom Field's Unique Value

### Purpose
Update an existing expense by identifying it through a custom field's unique value. If the custom field's unique value is not found and the `X-Upsert` header is set to `true`, a new expense will be created.

### Endpoint
`PUT /expenses`

### OAuth Scope
`ZohoBooks.expenses.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: The API name of the custom field that has a unique value.
*   **X-Unique-Identifier-Value**: The unique value of the custom field to identify the expense.
*   **X-Upsert** (optional): If set to `true`, creates a new expense if the unique value is not found.

### Arguments
*(Same arguments as Create an Expense)*

### Request Example
```json
{
    "account_id": "982000000561057",
    "date": "2013-11-18",
    "amount": 120.5,
    "tax_id": "982000000566007",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "hsn_or_sac": "80540",
    "gst_no": "22AAAAA0000A1Z5",
    "reverse_charge_tax_id": "982000000561063",
    "line_items": [
        {
            "line_item_id": "10763000000140068", /* Optional: Only needed if updating existing line */
            "account_id": "982000000561057",
            "description": "Marketing - Upserted", /* Example update */
            "amount": 112.5,
            "tax_id": "982000000566007",
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": "",
            "reverse_charge_vat_id": "",
            "reverse_charge_tax_id": "982000000561063",
            "tax_exemption_code": "string",
            "tax_exemption_id": "982000000561067",
            "location_id": "460000000038080"
        }
    ],
    "location_id": "460000000038080",
    "taxes": [
        {
            "tax_id": "982000000566007",
            "tax_amount": 11.85
        }
    ],
    "is_inclusive_tax": false,
    "is_billable": true,
    "reference_number": null,
    "description": "Marketing - Upserted", /* Example update */
    "customer_id": "982000000567001",
    "currency_id": "982000000567001",
    "exchange_rate": 1,
    "project_id": "982000000567226",
    "mileage_type": "non_mileage",
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": "",
    "reverse_charge_vat_id": "",
    "start_reading": "",
    "end_reading": "",
    "distance": "",
    "mileage_unit": "",
    "mileage_rate": "",
    "employee_id": "",
    "vehicle_type": "",
    "can_reclaim_vat_on_mileage": "",
    "fuel_type": "",
    "engine_capacity_range": "",
    "paid_through_account_id": "982000000567250",
    "vendor_id": "",
    "custom_fields": []
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Expense information has been updated.",
    "expense": {
        "expense_id": "982000000030049",
        /* ... updated or newly created expense details ... */
    }
}
```
# Recurring Expenses

## Overview

### Recurring Expenses
Recurring expenses are those expenses that repeat itself after a fixed interval of time.

### End Points
*   `POST /recurringexpenses`
*   `PUT /recurringexpenses` *(Note: Likely refers to the 'Update Recurring Expense using Custom Field' endpoint)*
*   `GET /recurringexpenses`
*   `PUT /recurringexpenses/{recurring_expense_id}`
*   `GET /recurringexpenses/{recurring_expense_id}`
*   `DELETE /recurringexpenses/{recurring_expense_id}`
*   `POST /recurringexpenses/{recurring_expense_id}/status/stop`
*   `POST /recurringexpenses/{recurring_expense_id}/status/resume`
*   `GET /recurringexpenses/{recurring_expense_id}/expenses`
*   `GET /recurringexpenses/{recurring_expense_id}/comments`

### Attributes
*   **account_id** (string)
*   **recurrence_name** (string): Name of the Recurring Expense. Max-length [100]
*   **start_date** (string): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable before July 1, 2017.
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **place_of_supply** (string): GCC only - Place of supply for VAT purposes (Supported codes listed).
*   **gst_no** (string): 🇮🇳 only - 15 digit GST number of the vendor.
*   **gst_treatment** (string): 🇮🇳 only - Allowed values: business_gst, business_none, overseas, consumer.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **destination_of_supply_state** (string): 🇮🇳 only - State where goods/services are supplied.
*   **hsn_or_sac** (string): 🇮🇳 , 🇰🇪 only - HSN/SAC code.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (uk, eu_vat_registered, overseas).
*   **reverse_charge_tax_id** (string): 🇮🇳 , GCC , 🇿🇦 only - Reverse charge tax ID.
*   **reverse_charge_tax_name** (string): 🇮🇳 only - Reverse charge tax name.
*   **reverse_charge_tax_percentage** (double): 🇮🇳 only - Reverse charge tax percentage.
*   **reverse_charge_tax_amount** (double): 🇮🇳 only - Reverse charge tax amount.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Applicable for reverse charge payments.
*   **acquisition_vat_total** (double): Total acquisition VAT.
*   **reverse_charge_vat_total** (double): 🇮🇳 only - Total reverse charge VAT.
*   **acquisition_vat_summary** (array): Summary of Acquisition VAT.
*   **reverse_charge_vat_summary** (array): Summary of Reverse Charge VAT.
*   **recurrence_frequency** (string): Frequency (e.g., 'months', 'weeks').
*   **repeat_every** (integer): Interval (e.g., 1, 2). *(Note: Original doc type was string)*.
*   **amount** (double): Recurring Expense amount.
*   **total** (double): Total amount including tax.
*   **sub_total** (double): Subtotal amount before tax.
*   **bcy_total** (double): Total amount in base currency.
*   **product_type** (string): 🇬🇧 , 🇿🇦 only - Type (goods, service, capital_goods, etc. Allowed values vary by region).
*   **acquisition_vat_id** (string): 🇬🇧 only - Acquisition VAT tax ID.
*   **reverse_charge_vat_id** (string): 🇮🇳 , 🇬🇧 only - Reverse charge VAT tax ID.
*   **tax_id** (string): Tax ID applied.
*   **tax_name** (string): Tax name.
*   **tax_percentage** (double): Tax percentage.
*   **created_time** (string): Creation time.
*   **last_modified_time** (string): Last modified time.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **is_billable** (boolean): Is the expense billable to a customer.
*   **customer_id** (string): Customer ID if billable.
*   **currency_id** (string): Currency ID.
*   **exchange_rate** (double): Exchange rate.
*   **project_id** (string): Project ID if associated.
*   **project_name** (string): Project name.
*   **custom_fields** (array): Custom fields.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_item** (object): Line item details *(Note: Usually line items are an array, this might be simplified in original example)*.

### Example
```json
{
    "account_id": 982000000561057,
    "recurrence_name": "Monthly Rental",
    "start_date": "2016-11-19T00:00:00.000Z",
    "end_date": " ",
    "is_pre_gst": false,
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "destination_of_supply_state": "AP",
    "hsn_or_sac": 80540,
    "vat_treatment": "eu_vat_not_registered",
    "reverse_charge_tax_id": 982000000567254,
    "reverse_charge_tax_name": "inter",
    "reverse_charge_tax_percentage": 10,
    "reverse_charge_tax_amount": 10,
    "is_reverse_charge_applied": false,
    "acquisition_vat_total": 0,
    "reverse_charge_vat_total": 10,
    "acquisition_vat_summary": [
        {
            "tax_name": "SalesTax",
            "tax_amount": 11.85
        }
    ],
    "reverse_charge_vat_summary": [
        {
            "tax_name": "SalesTax",
            "tax_amount": 11.85
        }
    ],
    "recurrence_frequency": "months",
    "repeat_every": 1,
    "amount": 112.5,
    "total": 128.25,
    "sub_total": 90,
    "bcy_total": 100,
    "product_type": "goods",
    "acquisition_vat_id": " ",
    "reverse_charge_vat_id": " ",
    "tax_id": 982000000566007,
    "tax_name": "SalesTax",
    "tax_percentage": 10.5,
    "created_time": "2013-11-18T02:17:40.080Z",
    "last_modified_time": " ",
    "is_inclusive_tax": false,
    "is_billable": true,
    "customer_id": 982000000567001,
    "currency_id": 982000000567001,
    "exchange_rate": 1,
    "project_id": " ",
    "project_name": " ",
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal"
        }
    ],
    "location_id": "460000000038080",
    "location_name": "string",
    "line_item": {
        "line_item_id": 10763000000140068,
        "account_id": 982000000561057,
        "account_name": "Rent",
        "description": " ",
        "tax_amount": 11.85,
        "tax_id": 982000000566007,
        "tax_name": "SalesTax",
        "tax_type": "tax",
        "tax_percentage": 10.5,
        "item_total": 100,
        "item_order": 1,
        "hsn_or_sac": 80540,
        "reverse_charge_tax_id": 982000000567254,
        "reverse_charge_tax_name": "inter",
        "reverse_charge_tax_percentage": 10,
        "reverse_charge_tax_amount": 10
    }
}
```

## Create a Recurring Expense

### Description
Create a new recurring expense.

### Endpoint
`POST /recurringexpenses`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Arguments (Body Parameters)
*   **account_id** (string, Required): ID of the expense account.
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **recurrence_frequency** (string, Required): Frequency (e.g., 'weeks', 'months').
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply (Supported codes).
*   **reverse_charge_tax_id** (string): 🇮🇳 , GCC , 🇿🇦 only - Reverse charge tax ID.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items *(Note: If not provided, uses overall amount/tax? Docs unclear)*.
*   **amount** (double, Required): Recurring Expense amount.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **product_type** (string): 🇬🇧 , 🇿🇦 only - Type (goods, service, etc.).
*   **acquisition_vat_id** (string): 🇬🇧 only - Acquisition VAT tax ID.
*   **reverse_charge_vat_id** (string): 🇮🇳 , 🇬🇧 only - Reverse charge VAT tax ID.
*   **tax_id** (string): Overall tax ID.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **is_billable** (boolean): Is the expense billable.
*   **customer_id** (string): Customer ID (if billable).
*   **project_id** (string): Project ID (if billable/associated).
*   **currency_id** (string): Currency ID.
*   **exchange_rate** (double): Exchange rate.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_id": 982000000561057, "recurrence_name": "Monthly Rental", ...}'
```

#### Body Parameters
```json
{
    "account_id": 982000000561057,
    "recurrence_name": "Monthly Rental",
    "start_date": "2016-11-19", /* Using yyyy-mm-dd format */
    "end_date": null, /* Use null or omit if no end date */
    "recurrence_frequency": "months",
    "repeat_every": 1,
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "reverse_charge_tax_id": 982000000567254,
    "location_id": "460000000038080",
    "line_items": [ /* Optional? Base amount might be used if omitted */
        {
            /* line_item_id not needed for create */
            "account_id": 982000000561057, /* Redundant if overall account_id is set? */
            "description": null,
            "amount": 112.5, /* Amount for the line item */
            "tax_id": 982000000566007,
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": null,
            "reverse_charge_vat_id": null,
            "reverse_charge_tax_id": 982000000567254, /* Redundant? */
            "tax_exemption_code": "string",
            "tax_exemption_id": 982000000567267
        }
    ],
    "amount": 112.5, /* Overall amount */
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": null,
    "reverse_charge_vat_id": null,
    "tax_id": 982000000566007, /* Overall tax */
    "is_inclusive_tax": false,
    "is_billable": true,
    "customer_id": 982000000567001,
    "project_id": null,
    "currency_id": 982000000567001,
    "exchange_rate": 1,
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring expense has been created",
    "recurring_expense": {
        "recurring_expense_id": "...",
        "account_id": 982000000561057,
        "recurrence_name": "Monthly Rental",
        /* ... full recurring expense details ... */
    }
}
```

## Delete a Recurring Expense

### Description
Deleting an existing recurring expense.

### Endpoint
`DELETE /recurringexpenses/{recurring_expense_id}`

### OAuth Scope
`ZohoBooks.expenses.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring expense has been deleted."
}
```

## Get a Recurring Expense

### Description
Get the details of the recurring expense.

### Endpoint
`GET /recurringexpenses/{recurring_expense_id}`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "recurring_expense": {
        "recurring_expense_id": 982000000567240,
        "recurrence_name": "Monthly Rental",
        /* ... full recurring expense details ... */
        "line_items": [ /* Corrected: Usually an array */
             {
                 "line_item_id": 10763000000140068,
                 /* ... line item details ... */
             }
        ]
    }
}
```

## List Child Expenses Created

### Description
List child expenses created from recurring expense.

### Endpoint
`GET /recurringexpenses/{recurring_expense_id}/expenses`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Query Parameters
*   **sort_column** (string): Sort expenses. Allowed Values: `next_expense_date`, `account_name`, `total`, `last_created_date`, `recurrence_name`, `customer_name`, `created_time`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240/expenses?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "expenses": [ /* Renamed from "expensehistory" */
        {
            "expense_id": 982000000567250,
            "date": "2013-11-18", /* Date expense was created */
            "account_name": "Rent",
            "customer_name": "Bowman & Co",
            "total": 128.25,
            "status": "invoiced", /* Status of the generated expense (e.g., non-billable, invoiced, reimbursed) */
            "vendor_name": null, /* Vendor if applicable */
            "paid_through_account_name": "Petty Cash" /* If payment recorded */
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected structure from array to object */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "GeneratedExpenses",
        "applied_filter": "", /* Actual applied filter */
        "sort_column": "date",
        "sort_order": "D"
    }
}
```

## List Recurring Expense History (Comments)

### Description
Get history and comments of a recurring expense.

### Endpoint
`GET /recurringexpenses/{recurring_expense_id}/comments`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [ /* Corrected: Should be an array */
        {
            "comment_id": 982000000567272,
            "recurring_expense_id": 982000000567240,
            "description": "Recurring expense created.", /* Comment text or history description */
            "commented_by_id": 982000000554041,
            "commented_by": "John David",
            "comment_type": "system",
            "date": "2013-11-18",
            "date_description": "1 year ago",
            "time": "2.41 AM",
            "operation_type": "Added", /* e.g., Created, Updated, Stopped, Resumed */
            "transaction_id": null, /* Related transaction ID if applicable */
            "transaction_type": null
        },
        {
             "comment_id": "...",
             "recurring_expense_id": 982000000567240,
             "description": "Expense #EXP-001 was created.",
             "commented_by_id": null,
             "commented_by": "System",
             "comment_type": "system",
             "date": "2013-11-18",
             "date_description": "1 year ago",
             "time": "3:00 AM",
             "operation_type": "ChildCreated",
             "transaction_id": "982000000567250", /* ID of generated expense */
             "transaction_type": "expense"
        }
    ]
}
```

## List Recurring Expense

### Description
List all the Recurring Expenses with pagination.

### Endpoint
`GET /recurringexpenses`

### OAuth Scope
`ZohoBooks.expenses.READ`

### Query Parameters
*   **recurrence_name** (string): Search by name (variants: `_startswith`, `_contains`). Max-length [100].
*   **last_created_date** (string): Search by last expense generated date (variants: `_start`, `_end`, `_before`, `_after`). Format [yyyy-mm-dd].
*   **next_expense_date** (string): Search by next expense generation date (variants: `_start`, `_end`, `_before`, `_after`). Format [yyyy-mm-dd].
*   **status** (string): Search by status. Allowed Values: `active`, `stopped`, `expired`.
*   **account_id** (string): Filter by expense account ID.
*   **account_name** (string): Search by expense account name (variants: `_startswith`, `_contains`). Max-length [100].
*   **amount** (double): Search by amount (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **customer_name** (string): Search by customer name (variants: `_startswith`, `_contains`). Max-length [100].
*   **customer_id** (string): Filter by customer ID.
*   **paid_through_account_id** (string): Filter by paid through account ID.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Expired`, `Status.Stopped`.
*   **search_text** (string): Search by account name, description, customer name, or vendor name. Max-length [100].
*   **sort_column** (string): Sort results. Allowed Values: `next_expense_date`, `account_name`, `total`, `last_created_date`, `recurrence_name`, `customer_name`, `created_time`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses?organization_id=10234695&status=active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "recurring_expenses": [
        {
            "recurring_expense_id": 982000000567240,
            "recurrence_name": "Monthly Rental",
            "recurrence_frequency": "months",
            "repeat_every": 1,
            "last_created_date": "2013-11-18",
            "next_expense_date": "2013-12-18",
            "account_name": "Rent",
            "description": null,
            "currency_id": 982000000567001,
            "currency_code": "USD",
            "total": 128.25,
            "is_billable": true,
            "customer_name": "Bowman & Co",
            "custom_fields": [
                {
                    "customfield_id": "46000000012845",
                    "value": "Normal"
                }
            ],
            "status": "active",
            "created_time": "2013-11-18T02:17:40+0530", /* Adjusted timezone for consistency */
            "last_modified_time": null
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected structure from array to object */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "RecurringExpenses",
        "applied_filter": "Status.Active",
        "sort_column": "created_time",
        "sort_order": "A"
    }
}
```

## Resume a Recurring Expense

### Description
Resume a stopped recurring expense.

### Endpoint
`POST /recurringexpenses/{recurring_expense_id}/status/resume`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240/status/resume?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring expense has been activated."
}
```

## Stop a Recurring Expense

### Description
Stop an active recurring expense.

### Endpoint
`POST /recurringexpenses/{recurring_expense_id}/status/stop`

### OAuth Scope
`ZohoBooks.expenses.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240/status/stop?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring expense has been stopped."
}
```

## Update a Recurring Expense

### Description
Update a recurring expense.

### Endpoint
`PUT /recurringexpenses/{recurring_expense_id}`

### OAuth Scope
`ZohoBooks.expenses.UPDATE`

### Arguments (Body Parameters)
*   **account_id** (string, Required): Expense account ID.
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **recurrence_frequency** (string, Required): Frequency.
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **reverse_charge_tax_id** (string): 🇮🇳 , GCC , 🇿🇦 only - Reverse charge tax ID.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **amount** (double, Required): Recurring Expense amount.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **product_type** (string): 🇬🇧 , 🇿🇦 only - Type (goods, service, etc.).
*   **acquisition_vat_id** (string): 🇬🇧 only - Acquisition VAT tax ID.
*   **reverse_charge_vat_id** (string): 🇮🇳 , 🇬🇧 only - Reverse charge VAT tax ID.
*   **tax_id** (string): Overall tax ID.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **is_billable** (boolean): Is the expense billable.
*   **customer_id** (string): Customer ID (if billable).
*   **project_id** (string): Project ID.
*   **currency_id** (string): Currency ID.
*   **exchange_rate** (double): Exchange rate.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_id": 982000000561057, "recurrence_name": "Updated Rental", ...}'
```

#### Body Parameters
```json
{
    "account_id": 982000000561057,
    "recurrence_name": "Monthly Rental",
    "start_date": "2016-11-19", /* Using yyyy-mm-dd */
    "end_date": null,
    "recurrence_frequency": "months",
    "repeat_every": 1,
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "reverse_charge_tax_id": 982000000567254,
    "location_id": "460000000038080",
    "line_items": [
        {
            "line_item_id": 10763000000140068, /* Required for update */
            "account_id": 982000000561057,
            "description": null,
            "amount": 112.5,
            "tax_id": 982000000566007,
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": null,
            "reverse_charge_vat_id": null,
            "reverse_charge_tax_id": 982000000567254,
            "tax_exemption_code": "string",
            "tax_exemption_id": 982000000567267
        }
        /* Omit line item object to delete it */
        /* Add new line item object without line_item_id to add */
    ],
    "amount": 112.5,
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": null,
    "reverse_charge_vat_id": null,
    "tax_id": 982000000566007,
    "is_inclusive_tax": false,
    "is_billable": true,
    "customer_id": 982000000567001,
    "project_id": null,
    "currency_id": 982000000567001,
    "exchange_rate": 1,
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal" /* Updated value */
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring expense information has been updated",
    "recurring_expense": {
        "recurring_expense_id": 982000000567240,
        "account_id": 982000000561057,
        /* ... updated recurring expense details ... */
    }
}
```

## Update Recurring Expense using Custom Field

### Description
Update a recurring expense using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found. *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs)*.

### Endpoint
`PUT /recurringexpenses` *(Note: Example shows this, but typically PUT for update uses ID like `/recurringexpenses/{id}`. This endpoint might work with headers.)*

### OAuth Scope
`ZohoBooks.expenses.UPDATE`

### Headers *(Assumed based on description)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **account_id** (string, Required): Expense account ID.
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **recurrence_frequency** (string, Required): Frequency.
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **reverse_charge_tax_id** (string): 🇮🇳 , GCC , 🇿🇦 only - Reverse charge tax ID.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **amount** (double, Required): Recurring Expense amount.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **product_type** (string): 🇬🇧 , 🇿🇦 only - Type (goods, service, etc.).
*   **acquisition_vat_id** (string): 🇬🇧 only - Acquisition VAT tax ID.
*   **reverse_charge_vat_id** (string): 🇮🇳 , 🇬🇧 only - Reverse charge VAT tax ID.
*   **tax_id** (string): Overall tax ID.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **is_billable** (boolean): Is the expense billable.
*   **customer_id** (string): Customer ID (if billable).
*   **project_id** (string): Project ID.
*   **currency_id** (string): Currency ID.
*   **exchange_rate** (double): Exchange rate.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"account_id": 982000000561057, "recurrence_name": "Monthly Rental", ...}'
```

#### Body Parameters
```json
{
    "account_id": 982000000561057,
    "recurrence_name": "Monthly Rental",
    "start_date": "2016-11-19", /* Using yyyy-mm-dd */
    "end_date": null,
    "recurrence_frequency": "months",
    "repeat_every": 1,
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "reverse_charge_tax_id": 982000000567254,
    "location_id": "460000000038080",
    "line_items": [
        {
            "line_item_id": 10763000000140068, /* Required for update */
            "account_id": 982000000561057,
            "description": null,
            "amount": 112.5,
            "tax_id": 982000000566007,
            "item_order": 1,
            "product_type": "goods",
            "acquisition_vat_id": null,
            "reverse_charge_vat_id": null,
            "reverse_charge_tax_id": 982000000567254,
            "tax_exemption_code": "string",
            "tax_exemption_id": 982000000567267
        }
    ],
    "amount": 112.5,
    "vat_treatment": "eu_vat_not_registered",
    "tax_treatment": "vat_registered",
    "product_type": "goods",
    "acquisition_vat_id": null,
    "reverse_charge_vat_id": null,
    "tax_id": 982000000566007,
    "is_inclusive_tax": false,
    "is_billable": true,
    "customer_id": 982000000567001,
    "project_id": null,
    "currency_id": 982000000567001,
    "exchange_rate": 1,
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal" /* Updated value */
        }
        /* Include the unique custom field specified in headers */
        /* { "api_name": "cf_unique_cf", "value": "unique Value" } */
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring expense information has been updated",
    "recurring_expense": {
        /* Updated or Created Recurring Expense details */
        "recurring_expense_id": "...",
        "account_id": 982000000561057,
        /* ... */
    }
}
```
# Retainer Invoices

## Overview

### Retainer Invoices
A lot of businesses collect an advance payment (or retainer) for products sold or services rendered by them. This amount collected will not be an income but a liability to the company. The revenue is earned only when the product is delivered or the service is completed, if not delivered or completed the advance payment made will be returned to the customer.

### End Points
*   `POST /retainerinvoices`
*   `GET /retainerinvoices`
*   `PUT /retainerinvoices/{retainerinvoice_id}`
*   `GET /retainerinvoices/{retainerinvoice_id}`
*   `DELETE /retainerinvoices/{retainerinvoice_id}`
*   `POST /retainerinvoices/{retainerinvoice_id}/status/sent`
*   `PUT /retainerinvoices/{retainerinvoice_id}/templates/{template_id}`
*   `POST /retainerinvoices/{retainerinvoice_id}/status/void`
*   `POST /retainerinvoices/{retainerinvoice_id}/status/draft` *(Note: Original docs typo reatinerinvoice_id)*
*   `POST /retainerinvoices/{retainerinvoice_id}/submit` *(Note: Original docs typo reatinerinvoice_id)*
*   `POST /retainerinvoices/{retainerinvoice_id}/approve` *(Note: Original docs typo reatinerinvoice_id)*
*   `POST /retainerinvoices/{retainerinvoice_id}/email`
*   `GET /retainerinvoices/{retainerinvoice_id}/email`
*   `PUT /retainerinvoices/{retainerinvoice_id}/address/billing`
*   `GET /retainerinvoices/templates`
*   `POST /retainerinvoices/{retainerinvoice_id}/attachment`
*   `GET /retainerinvoices/{retainerinvoice_id}/attachment`
*   `DELETE /retainerinvoices/{retainerinvoice_id}/documents/{document_id}` *(Note: Endpoint for deleting attachment seems inconsistent with GET/POST)*
*   `POST /retainerinvoices/{retainerinvoice_id}/comments`
*   `GET /retainerinvoices/{retainerinvoice_id}/comments`
*   `PUT /retainerinvoices/{retainerinvoice_id}/comments/{comment_id}`
*   `DELETE /retainerinvoices/{retainerinvoice_id}/comments/{comment_id}`

### Attributes
*   **retainerinvoice_id** (string): ID of the retainerinvoice
*   **retainerinvoice_number** (string): number of the retainer invoice. Max-length [100]
*   **date** (string): The date of creation. Format [yyyy-mm-dd].
*   **status** (string): retainer invoice status (`sent`, `draft`, `overdue`, `paid`, `void`, `unpaid`, `partially_paid`, `viewed`).
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable before July 1, 2017 *(Note: Original doc type was string)*.
*   **place_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied (Supported codes listed).
*   **project_id** (string): ID of the project.
*   **project_name** (string): Name of the project.
*   **last_payment_date** (string): The last payment date.
*   **reference_number** (string): Reference number. Max-length [100].
*   **customer_id** (string): Customer ID.
*   **customer_name** (string): Customer name. Max-length [100].
*   **contact_persons** (array): Array of contact person IDs.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **exchange_rate** (float): Exchange rate.
*   **is_viewed_by_client** (boolean): Viewed by client in portal.
*   **client_viewed_time** (string/timestamp): Client viewed time *(Note: Original doc type was boolean)*.
*   **is_inclusive_tax** (boolean): Is amount inclusive of tax.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items.
*   **sub_total** (float): Sub total.
*   **total** (float): Total amount *(Note: Original doc type was string)*.
*   **taxes** (array): List of taxes.
*   **payment_made** (float): Amount paid.
*   **payment_drawn** (float): Amount drawn (applied to invoices).
*   **balance** (float): Unpaid amount *(Note: Original doc type was string)*.
*   **allow_partial_payments** (boolean): Partial payments allowed.
*   **price_precision** (integer): Precision value on price.
*   **payment_options** (object): Payment options.
*   **is_emailed** (boolean): Email sent status *(Note: Original doc type was string)*.
*   **documents** (array): Attached documents.
*   **billing_address** (object): Billing address details.
*   **shipping_address** (object): Shipping address details.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms & conditions. Max-length [10000].
*   **custom_fields** (array): Custom fields.
*   **template_id** (string): PDF template ID.
*   **template_name** (string): Template name.
*   **page_width** (string): Template page width.
*   **page_height** (string): Template page height.
*   **orientation** (string): Template orientation.
*   **template_type** (string): Template type.
*   **created_time** (string): Creation time.
*   **last_modified_time** (string): Last modified time.
*   **created_by_id** (string): ID of the user who created it.
*   **attachment_name** (string): Name of the primary attachment.
*   **can_send_in_mail** (boolean): Can attachment be sent via email.
*   **invoice_url** (string): URL for online payment/viewing.

### Example
```json
{
    "retainerinvoice_id": 982000000567114,
    "retainerinvoice_number": "RET-00003",
    "date": "2013-11-17",
    "status": "draft",
    "is_pre_gst": false,
    "place_of_supply": "TN",
    "project_id": 982000000567154,
    "project_name": "string",
    "last_payment_date": " ",
    "reference_number": " ",
    "customer_id": 982000000567001,
    "customer_name": "Bowman & Co",
    "contact_persons": [
        "982000000567003"
    ],
    "currency_id": 982000000000190,
    "currency_code": "USD",
    "currency_symbol": "USD",
    "exchange_rate": 1,
    "is_viewed_by_client": true,
    "client_viewed_time": "2013-11-18T03:00:00+0530", /* Example timestamp */
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "location_name": "string",
    "line_items": [
        {
            "line_item_id": 982000000567021,
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "item_order": 1,
            "rate": 120,
            "bcy_rate": 120,
            "tax_id": 982000000557028,
            "tax_name": "VAT",
            "tax_type": "tax",
            "tax_percentage": 12.5,
            "item_total": 120,
            "location_id": "460000000038080",
            "location_name": "string"
        }
    ],
    "sub_total": 153.0,
    "total": 40.6,
    "taxes": [
        {
            "tax_name": "VAT",
            "tax_amount": 19.13
        }
    ],
    "payment_made": 26.91,
    "payment_drawn": 26.91,
    "balance": 40.6,
    "allow_partial_payments": true,
    "price_precision": 2,
    "payment_options": {
        "payment_gateways": [
            {
                "configured": true,
                "additional_field1": "standard",
                "gateway_name": "paypal"
            }
        ]
    },
    "is_emailed": false,
    "documents": [],
    "billing_address": {
        "address": "Suite 125, McMillan Avenue",
        "street2": "McMillan Avenue",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94134",
        "country": "U.S.A",
        "fax": "+86-10-82637827"
    },
    "shipping_address": {
        "address": "Suite 125, McMillan Avenue",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94134",
        "country": "U.S.A",
        "fax": "+86-10-82637827"
    },
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "custom_fields": [
        {
            "index": 1,
            "show_on_pdf": false,
            "value": "The value of the custom field",
            "label": "Delivery Date"
        }
    ],
    "template_id": 982000000000143,
    "template_name": "Service - Classic",
    "page_width": "8.27in",
    "page_height": "11.69in",
    "orientation": "portrait",
    "template_type": "classic",
    "created_time": "2013-11-18T02:31:51-0800",
    "last_modified_time": "2013-11-18T02:31:51-0800",
    "created_by_id": "14909000000072000",
    "attachment_name": "new file",
    "can_send_in_mail": true,
    "invoice_url": "https://invoice.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
}
```

## Add Attachment to Retainer Invoice

### Description
Attach a file to a retainer invoice.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Form Data)
*   **can_send_in_mail** (boolean): Allow sending this attachment via email.
*   **attachment** (file): The file to attach.

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/your/retainer_doc.pdf" \
  -F "can_send_in_mail=true"
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file has been attached."
}
```

## Add Comment to Retainer Invoice

### Description
Add a comment for a retainer invoice.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/comments`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **description** (string): The comment text. Max-length [2000].
*   **payment_expected_date** (string): Expected payment date (can be set via comment?). Format [yyyy-mm-dd].
*   **show_comment_to_clients** (boolean): Make comment visible in client portal.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Client confirmed receipt.", "show_comment_to_clients": false}'
```

#### Body Parameters
```json
{
    "description": "comment added",
    "payment_expected_date": null, /* Omit or set null if not needed */
    "show_comment_to_clients": true
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": { /* Added expected comment object */
        "comment_id": "...",
        "retainerinvoice_id": "982000000567114",
        "description": "comment added",
        "commented_by_id": "...",
        "commented_by": "User Name",
        "comment_type": "user",
        "date": "YYYY-MM-DD",
        "date_description": "Just now",
        "time": "HH:MM AM/PM",
        "show_comment_to_clients": true
    }
}
```

## Approve Retainer Invoice

### Description
Approve a retainer invoice.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/approve` *(Note: URL corrected)*

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the Retainer Invoice."
}
```

## Create a Retainer Invoice

### Description
Create a retainer invoice for your customer.

### Endpoint
`POST /retainerinvoices`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): Customer ID.
*   **reference_number** (string): Reference number. Max-length [100].
*   **date** (string): Creation date. Format [yyyy-mm-dd].
*   **contact_persons** (array): Contact person IDs.
*   **custom_fields** (array): Custom fields.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms. Max-length [10000].
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   Include description, rate etc.
*   **payment_options** (object): Payment options.
*   **template_id** (string): Template ID.
*   **place_of_supply** (string): 🇮🇳 only - Place of supply.

### Query Parameters
*   **ignore_auto_number_generation** (boolean): Ignore auto-generation. Allowed: `true`, `false`.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "customer_id": 982000000567001,
    "reference_number": null,
    "date": "2013-11-17",
    "contact_persons": [
        "982000000567003"
    ],
    "custom_fields": [
        {
            "index": 1,
            "show_on_pdf": false,
            "value": "The value of the custom field",
            "label": "Delivery Date" /* index or placeholder likely needed instead of label */
        }
    ],
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "location_id": "460000000038080",
    "line_items": [
        {
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "item_order": 1,
            "rate": 120
        }
    ],
    "payment_options": {
        "payment_gateways": [
            {
                "configured": true,
                "additional_field1": "standard",
                "gateway_name": "paypal"
            }
        ]
    },
    "template_id": "982000000000143",
    "place_of_supply": "TN"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The retainer invoice has been created.",
    "retainerinvoice": {
        "retainerinvoice_id": 982000000567114,
        "retainerinvoice_number": "RET-00001", /* Example number */
        "customer_id": 982000000567001,
        /* ... full retainer invoice details ... */
        "status": "draft", /* Or 'sent' if created directly */
        /* ... */
    }
}
```

## Delete a Retainer Invoice

### Description
Delete an existing retainer invoice. Invoices which have payment or credits note applied cannot be deleted.

### Endpoint
`DELETE /retainerinvoices/{retainerinvoice_id}`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The retainer invoice has been deleted."
}
```

## Delete Retainer Invoice Attachment

### Description
Delete the file attached to the retainer invoice.

### Endpoint
`DELETE /retainerinvoices/{retainerinvoice_id}/documents/{document_id}` *(Note: Endpoint differs from GET/POST attachment endpoints. May require document ID instead of acting on primary attachment)*.

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/documents/DOCUMENT_ID_HERE?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file is no longer attached to the invoice." /* Generic message */
}
```

## Delete Retainer Invoice Comment

### Description
Delete a retainer invoice comment.

### Endpoint
`DELETE /retainerinvoices/{retainerinvoice_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.invoices.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Email a Retainer Invoice

### Description
Email a retainer invoice to the customer. Input json string is not mandatory. If empty, mail will be sent with default content.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/email`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Arguments (Body Parameters)
*   **send_from_org_email_id** (boolean): Trigger email from organization's email address.
*   **to_mail_ids** (array, Required): Recipient email addresses.
*   **cc_mail_ids** (array): CC email addresses.
*   **subject** (string): Email subject.
*   **body** (string): Email body.

### Query Parameters
*   **send_customer_statement** (boolean): Send customer statement PDF with email.
*   **send_attachment** (boolean): Send retainer invoice PDF attachment with email.
*   **attachments**: File(s) to attach (sent via multipart/form-data).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["willsmith@bowmanfurniture.com"], "subject": "Retainer Invoice RET-00001", "body": "..."}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters
```json
{
    "send_from_org_email_id": false,
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "subject": "Retainer Invoice from Zillium Inc (Retainer Invoice#: RET-00001)",
    "body": "Dear Customer, ... <a href=...>pay online</a> ... Regards<br>\\nZillium Inc<br>\\n"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your retainer invoice has been sent."
}
```

## Get a Retainer Invoice

### Description
Get the details of a retainer invoice.

### Endpoint
`GET /retainerinvoices/{retainerinvoice_id}`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "retainerinvoice": {
        "retainerinvoice_id": 982000000567114,
        "retainerinvoice_number": "RET-00003",
        /* ... full retainer invoice details ... */
    }
}
```

## Get Retainer Invoice Attachment

### Description
Returns the file attached to the retainer invoice.

### Endpoint
`GET /retainerinvoices/{retainerinvoice_id}/attachment`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output retainer_attachment.pdf
```
*(Note: Response is the binary file data)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Get Retainer Invoice Email Content

### Description
Get the email content of a retainer invoice based on a template.

### Endpoint
`GET /retainerinvoices/{retainerinvoice_id}/email`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **email_template_id** (string): Get content based on specific template ID. If omitted, uses customer's associated template or default.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": { /* Added data wrapper */
        "gateways_configured": true,
        "deprecated_placeholders_used": [],
        "body": "Dear Customer, ...",
        "error_list": [],
        "subject": "Retainer Invoice from Zillium Inc (Retainer Invoice#: RET-00001)",
        "to_contacts": [ /* ... contact details ... */ ],
        "attachment_name": "new file",
        "email_template_id": "string", /* Current template ID */
        "file_name": "RET-00001.pdf",
        "from_emails": [ /* ... sender details ... */ ],
        "customer_id": 982000000567001
    }
}
```

## List Retainer Invoice Comments and History

### Description
Get the complete history and comments of a retainer invoice.

### Endpoint
`GET /retainerinvoices/{retainerinvoice_id}/comments`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": 982000000567019,
            "retainerinvoice_id": 982000000567114,
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "commented_by_id": 982000000554041,
            "commented_by": "John David",
            "comment_type": "system",
            "operation_type": "Added",
            "date": "2013-11-17",
            "date_description": "yesterday",
            "time": "2:38 AM",
            "transaction_id": "982000000567204",
            "transaction_type": "retainer_payment"
        },
        {...},
        {...}
    ]
}
```

## List Retainer Invoice Templates

### Description
Get all retainer invoice pdf templates.

### Endpoint
`GET /retainerinvoices/templates`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Service - Classic",
            "template_id": 982000000000143,
            "template_type": "classic"
        },
        {...},
        {...}
    ]
}
```

## List Retainer Invoices

### Description
List all retainer invoices with pagination.

### Endpoint
`GET /retainerinvoices`

### OAuth Scope
`ZohoBooks.invoices.READ`

### Query Parameters
*   **print** (boolean/string): Export PDF with default print option *(Note: Unusual for list endpoint)*.
*   **sort_column** (string): Sort retainer invoices. Allowed Values: `customer_name`, `retainer invoice_number`, `date`, `due_date`, `total`, `balance`, `created_time`.
*   **filter_by** (string): Filter by status or payment expected date. Allowed Values: `Status.All`, `Status.Sent`, ..., `Status.Viewed`, `Date.PaymentExpectedDate`.
*   **sort_order** (string): Sorting order (A/D).
*   **page** (integer): Page number.
*(Many other standard list parameters like `customer_id`, `retainerinvoice_number`, `status`, `total` are likely available but not listed)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices?organization_id=10234695&sort_column=date&sort_order=D' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "retainerinvoices": [
        {
            "retainerinvoice_id": 982000000567114,
            "customer_name": "Bowman & Co",
            "retainerinvoice_number": "RET-00003",
            "customer_id": 982000000567001,
            "status": "draft",
            "reference_number": null,
            "project_or_estimate_name": "new project", /* Likely project_name */
            "date": "2013-11-17",
            "currency_id": 982000000000190,
            "currency_code": "USD",
            "is_viewed_by_client": true,
            "client_viewed_time": "2013-11-18T03:00:00+0530", /* Example timestamp */
            "total": 40.6,
            "balance": 40.6,
            "created_time": "2013-11-18T02:31:51-0800",
            "last_modified_time": "2013-11-18T02:31:51-0800",
            "is_emailed": false,
            "last_payment_date": null,
            "has_attachment": true
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Retainer Invoices",
        "applied_filter": "Status.All", /* Example */
        "sort_column": "date", /* Corrected based on request example */
        "sort_order": "D"
    }
}
```

## Mark Retainer Invoice as Draft

### Description
Mark a voided retainer invoice as draft.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/status/draft` *(Note: URL corrected)*

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/status/draft?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Status of retainer invoice changed from void to draft."
}
```

## Mark Retainer Invoice as Sent

### Description
Mark a draft retainer invoice as sent.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/status/sent`

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/status/sent?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Retainer Invoice status has been changed to Sent."
}
```

## Submit Retainer Invoice for Approval

### Description
Submit a retainer invoice for approval.

### Endpoint
`POST /retainerinvoices/{retainerinvoice_id}/submit` *(Note: URL corrected)*

### OAuth Scope
`ZohoBooks.invoices.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The Retainer Invoice has been successfully submitted for approval."
}
```

## Update a Retainer Invoice

### Description
Update an existing retainer invoice.

### Endpoint
`PUT /retainerinvoices/{retainerinvoice_id}`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **customer_id** (string, Required): Customer ID.
*   **reference_number** (string): Reference number. Max-length [100].
*   **date** (string): Creation date. Format [yyyy-mm-dd].
*   **contact_persons** (array): Contact person IDs.
*   **custom_fields** (array): Custom fields.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms. Max-length [10000].
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **payment_options** (object): Payment options.
*   **template_id** (string): Template ID.
*   **place_of_supply** (string): 🇮🇳 only - Place of supply.
*   **project_id** (string): Project ID.
*(Other fields from Create might also be updatable)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": 982000000567001, "notes": "Updated note", ...}'
```

#### Body Parameters
```json
{
    "customer_id": 982000000567001,
    "reference_number": null,
    "date": "2013-11-17",
    "contact_persons": [
        "982000000567003"
    ],
    "custom_fields": [
        {
            "index": 1,
            "show_on_pdf": false,
            "value": "Updated value",
            "label": "Delivery Date" /* index or placeholder likely needed */
        }
    ],
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "location_id": "460000000038080",
    "line_items": [
        {
            "line_item_id": 982000000567021, /* Required for update */
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
            "item_order": 1,
            "rate": 125 /* Updated rate */
        }
        /* Omit line item object to delete */
        /* Add new line item object without line_item_id */
    ],
    "payment_options": {
        "payment_gateways": [
            {
                "configured": true,
                "additional_field1": "standard",
                "gateway_name": "paypal"
            }
        ]
    },
    "template_id": 982000000000143,
    "place_of_supply": "TN",
    "project_id": 982000000567154
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Retainer Invoice information has been updated.",
    "retainerinvoice": {
        "retainerinvoice_id": 982000000567114,
        /* ... updated retainer invoice details ... */
    }
}
```

## Update Billing Address

### Description
Updates the billing address for this retainer invoice alone.

### Endpoint
`PUT /retainerinvoices/{retainerinvoice_id}/address/billing`

### OAuth Scope
`ZohoBooks.invoices.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/retainerinvoices/982000000567114/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Billing Address", "city": "New City", ...}'
```

#### Body Parameters
```json
{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
    "city": "Beijing",
    "state": "Beijing",
    "zip": "100088", /* Changed to string */
    "country": "China", /* Example country */
    "fax": "+86-10-82637827"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated"
}
```
# Purchase Order

## Overview

### Purchase Order
A purchase order is an official document that a buyer issues to a seller, indicating relevant information about what they want to buy, the quantity, the price agreed for that particular product or service.

### End Points
*   `POST /purchaseorders`
*   `PUT /purchaseorders` *(Note: Seems like the custom field update endpoint)*
*   `GET /purchaseorders`
*   `PUT /purchaseorders/{purchase_order_id}`
*   `GET /purchaseorders/{purchase_order_id}`
*   `DELETE /purchaseorders/{purchase_order_id}`
*   `PUT /purchaseorder/{purchaseorder_id}/customfields`
*   `POST /purchaseorders/{purchaseorder_id}/status/open`
*   `POST /purchaseorders/{purchaseorder_id}/status/billed`
*   `POST /purchaseorders/{purchaseorder_id}/status/cancelled`
*   `POST /purchaseorders/{purchaseorder_id}/submit`
*   `POST /purchaseorders/{purchaseorder_id}/approve`
*   `POST /purchaseorders/{purchaseorder_id}/email`
*   `GET /purchaseorders/{purchaseorder_id}/email`
*   `PUT /purchaseorders/{purchaseorder_id}/address/billing`
*   `GET /purchaseorders/templates`
*   `PUT /purchaseorders/{purchaseorder_id}/templates/{template_id}`
*   `POST /purchaseorders/{purchaseorder_id}/attachment`
*   `PUT /purchaseorders/{purchaseorder_id}/attachment`
*   `GET /purchaseorders/{purchaseorder_id}/attachment`
*   `DELETE /purchaseorders/{purchaseorder_id}/attachment`
*   `POST /purchaseorders/{purchaseorder_id}/comments`
*   `GET /purchaseorders/{purchaseorder_id}/comments`
*   `PUT /purchaseorders/{purchaseorder_id}/comments/{comment_id}`
*   `DELETE /purchaseorders/{purchaseorder_id}/comments/{comment_id}`

### Attributes
*   **purchaseorder_id** (string): ID of the purchase order.
*   **documents** (array): Attached documents.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (uk, eu_vat_registered, overseas).
*   **gst_no** (string): 🇮🇳 only - Vendor's 15 digit GST number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status (business_gst, business_none, overseas, consumer).
*   **tax_treatment**: GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable before July 1, 2017.
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **place_of_supply** (string): GCC only - Place of supply for VAT (Supported codes listed).
*   **pricebook_id** (string): Pricebook ID.
*   **pricebook_name** (string): Pricebook name.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Applicable for reverse charge transactions.
*   **purchaseorder_number** (string): Purchase order number (Mandatory if auto-gen disabled).
*   **date** (string): Creation date.
*   **expected_delivery_date** (string): Expected delivery date.
*   **discount** (string): Discount (e.g., "10%" or "50").
*   **discount_account_id** (string): Account ID for discount.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **reference_number** (string): Reference number.
*   **status** (string): Status (draft, open, billed, cancelled).
*   **vendor_id** (string): Vendor ID.
*   **vendor_name** (string): Vendor name.
*   **crm_owner_id** (string): CRM Owner ID.
*   **contact_persons** (array): Contact person IDs.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **exchange_rate** (double): Exchange rate.
*   **delivery_date** (string): Actual/Confirmed delivery date.
*   **is_emailed** (boolean): Email sent status.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items.
*   **sub_total** (double): Sub total.
*   **tax_total** (double): Total tax amount.
*   **total** (double): Total amount.
*   **taxes** (array): Taxes applied.
*   **acquisition_vat_summary** (array): 🇬🇧 , Europe only - Acquisition VAT summary.
*   **acquisition_vat_total** (double): 🇬🇧 , Europe only - Total Acquisition VAT.
*   **reverse_charge_vat_summary** (array): 🇬🇧 , Europe only - Reverse Charge VAT summary.
*   **reverse_charge_vat_total** (double): 🇬🇧 , Europe only - Total Reverse Charge VAT.
*   **billing_address** (object): Billing address details.
*   **notes** (string): Delivery notes for vendor.
*   **terms** (string): Terms for purchase order.
*   **ship_via** (string): Shipment Preference.
*   **ship_via_id** (string): Shipment Preference ID.
*   **attention** (string): Delivery contact person.
*   **delivery_org_address_id** (string): Delivery Address ID (if delivering to own org address).
*   **delivery_customer_id** (string): Customer ID (if delivering directly to customer).
*   **delivery_address** (object): Delivery address details.
*   **price_precision** (integer): Price precision.
*   **custom_fields** (array): Custom fields.
*   **attachment_name** (string): Name of primary attachment.
*   **can_send_in_mail** (boolean): Can attachment be sent via email.
*   **template_id** (string): PDF template ID.
*   **template_name** (string): Template name.
*   **page_width** (string): Template page width.
*   **page_height** (string): Template page height.
*   **orientation** (string): Template orientation.
*   **template_type** (string): Template type.
*   **created_time** (string): Creation time.
*   **created_by_id** (string): ID of creator user.
*   **last_modified_time** (string): Last modified time.
*   **can_mark_as_bill** (boolean): Can be converted to a bill.
*   **can_mark_as_unbill** (boolean): Can be unbilled (if previously billed).

### Example
```json
{
    "purchaseorder_id": "460000000062001",
    "documents": [ { "document_id": 0, "file_name": "string" } ],
    "vat_treatment": "string",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_pre_gst": false,
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": 460000000026089,
    "pricebook_name": "",
    "is_reverse_charge_applied": false,
    "purchaseorder_number": "PO-00001",
    "date": "2014-02-10",
    "expected_delivery_date": "string",
    "discount": "10",
    "discount_account_id": "460000000011105",
    "is_discount_before_tax": true,
    "reference_number": "ER/0034",
    "status": "draft",
    "vendor_id": "460000000026049",
    "vendor_name": "string",
    "crm_owner_id": "string",
    "contact_persons": [ "460000000026051" ],
    "currency_id": "460000000000099",
    "currency_code": "INR",
    "currency_symbol": "string",
    "exchange_rate": 1,
    "delivery_date": "2014-02-10",
    "is_emailed": false,
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "location_name": "string",
    "line_items": [ /* ... line item details ... */ ],
    "sub_total": 40,
    "tax_total": 0,
    "total": 40,
    "taxes": [ "string" ],
    "acquisition_vat_summary": [ { "tax_name": "string", "tax_amount": 0.1 } ],
    "acquisition_vat_total": 0.1,
    "reverse_charge_vat_summary": [ { "tax_name": "string", "tax_amount": 0.1 } ],
    "reverse_charge_vat_total": 0.1,
    "billing_address": { /* ... address details ... */ },
    "notes": "Please deliver as soon as possible.",
    "terms": "Thanks for your business.",
    "ship_via": "string",
    "ship_via_id": "string",
    "attention": "string",
    "delivery_org_address_id": "string",
    "delivery_customer_id": "string",
    "delivery_address": { /* ... address details ... */ },
    "price_precision": 2,
    "custom_fields": [ { "customfield_id": "46000000012845", "value": "Normal" } ],
    "attachment_name": "7.png",
    "can_send_in_mail": false,
    "template_id": "460000000011003",
    "template_name": "Standard Template",
    "page_width": "8.27in",
    "page_height": "11.69in",
    "orientation": "portrait",
    "template_type": "standard",
    "created_time": "2014-02-10T15:26:26+0530",
    "created_by_id": "460000000053001",
    "last_modified_time": "2014-02-10T15:26:26+0530",
    "can_mark_as_bill": false,
    "can_mark_as_unbill": false
}
```

## Add Attachment to Purchase Order

### Description
Attach a file to a purchase order.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/attachment`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Query Parameters
*   **attachment**: The file to attach (sent via multipart/form-data). Allowed Extensions: gif, png, jpeg, jpg, bmp, pdf, xls, xlsx, doc, docx.

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/your/po_doc.pdf"
```

### Response Example
```json
{
    "code": 0,
    "message": "The document has been attached."
}
```

## Add Comment to Purchase Order

### Description
Add a comment for a purchase order.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/comments`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Arguments (Body Parameters)
*   **description** (string, Required): The comment text.
*   **expected_delivery_date** (string, Required): Expected delivery date *(Note: Seems unusual to require this when adding a general comment)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Vendor confirmed shipment.", "expected_delivery_date": "2024-07-15"}'
```

#### Body Parameters
```json
{
    "description": "string",
    "expected_delivery_date": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": {
        "comment_id": "460000000012345",
        "purchaseorder_id": "460000000062001",
        "description": "string",
        "commented_by_id": "string",
        "commented_by": "string",
        "comment_type": "system", /* or user */
        "date": "2014-02-10",
        "date_description": "22 hours ago.",
        "time": "3.26PM"
    }
}
```

## Approve Purchase Order

### Description
Approve a purchase order.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/approve`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the Purchase Order."
}
```

## Cancel Purchase Order

### Description
Mark a purchase order as cancelled.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/status/cancelled`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/status/cancelled?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The purchase order has been cancelled."
}
```

## Create a Purchase Order

### Description
Create a purchase order for your vendor.

### Endpoint
`POST /purchaseorders`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): ID of the vendor.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact person IDs.
*   **purchaseorder_number** (string): PO number (Mandatory if auto-gen disabled).
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status.
*   **tax_treatment**: GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Vendor's VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor's GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply for VAT.
*   **pricebook_id** (string): Pricebook ID.
*   **reference_number** (string): Reference number.
*   **billing_address_id** (long): Billing Address ID (Use Address API).
*   **crm_owner_id** (string): CRM Owner ID.
*   **crm_custom_reference_id** (long): CRM Custom Reference ID.
*   **template_id** (string): Template ID.
*   **date** (string): Creation date.
*   **delivery_date** (string): Delivery date.
*   **due_date** (string): Delivery date *(Note: Duplicates delivery_date?)*.
*   **exchange_rate** (double): Exchange rate.
*   **discount** (string): Discount (e.g., "10%" or "50").
*   **discount_account_id** (string): Account ID for discount.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **notes** (string): Delivery notes.
*   **notes_default** (string): Default notes.
*   **terms** (string): Terms.
*   **terms_default** (string): Default terms.
*   **ship_via** (string): Shipment preference.
*   **delivery_org_address_id** (string): Delivery Address ID (Org).
*   **delivery_customer_id** (string): Delivery Customer ID.
*   **attention** (string): Delivery contact person.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (string): Update customer address *(Note: Data type string, likely boolean)*.
*   **salesorder_id** (long): Associated Sales Order ID.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
*   **custom_fields** (array): Custom fields.
*   **documents** (array): Documents to attach.

### Query Parameters
*   **attachment**: File(s) to attach (sent via multipart/form-data). Allowed extensions listed.
*   **ignore_auto_number_generation** (boolean): Ignore auto-generation of PO number.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000026049", "date": "2014-02-10", "line_items": [...] ...}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "vendor_id": "460000000026049",
    "currency_id": "460000000000099",
    "contact_persons": [
        "460000000026051"
    ],
    "purchaseorder_number": "PO-00001",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": 460000000026089,
    "reference_number": "ER/0034",
    "billing_address_id": "460000000017491",
    "crm_owner_id": "string",
    "crm_custom_reference_id": 0,
    "template_id": "460000000011003",
    "date": "2014-02-10",
    "delivery_date": "2014-02-10",
    "due_date": "string",
    "exchange_rate": 1,
    "discount": "10",
    "discount_account_id": "460000000011105",
    "is_discount_before_tax": true,
    "is_inclusive_tax": false,
    "notes": "Please deliver as soon as possible.",
    "notes_default": "string",
    "terms": "Thanks for your business.",
    "terms_default": "string",
    "ship_via": "string",
    "delivery_org_address_id": "string",
    "delivery_customer_id": "string",
    "attention": "string",
    "vat_treatment": "string",
    "is_update_customer": "string",
    "salesorder_id": "460000124728314",
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "documents": [ { /* ... document details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Purchase Order has been added.",
    "purchaseorder": {
        "purchaseorder_id": "460000000062001",
        /* ... full purchase order details ... */
        "status": "draft", /* Initial status */
        /* ... */
    }
}
```

## Get a Purchase Order

### Description
Get the details of a purchase order.

### Endpoint
`GET /purchaseorders/{purchase_order_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Query Parameters
*   **print** (boolean/string): Export PDF with default print option.
*   **accept** (string): Response format. Allowed Values: `json`, `pdf`, `html`. Default: `json`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "purchaseorder": {
        "purchaseorder_id": "460000000062001"
        /* ... full purchase order details ... */
    }
}
```

## Email Purchase Order

### Description
Email a purchase order to the vendor. Input json string is not mandatory. If empty, mail will be sent with default content.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/email`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Arguments (Body Parameters)
*   **send_from_org_email_id** (boolean): Trigger email from organization's email address.
*   **from_address_id** (long): ID of the From Address.
*   **to_mail_ids** (array, Required): Recipient email addresses.
*   **cc_mail_ids** (array): CC email addresses.
*   **bcc_mail_ids** (array): BCC email addresses.
*   **subject** (string): Email subject.
*   **body** (string, Required): Email body.
*   **mail_documents** (array): Documents to attach.

### Query Parameters
*   **attachments**: File(s) to attach (sent via multipart/form-data).
*   **send_attachment** (boolean): Send the PO PDF attachment with the email.
*   **file_name**: Name of the file (likely used with `attachments`).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"to_mail_ids": ["willsmith@bowmanfurniture.com"], "subject": "PO from Zillium Inc", "body": "..."}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters
```json
{
    "send_from_org_email_id": true,
    "from_address_id": "460000008392548",
    "to_mail_ids": [
        "willsmith@bowmanfurniture.com"
    ],
    "cc_mail_ids": [
        "peterparker@bowmanfurniture.com"
    ],
    "bcc_mail_ids": [
        "mark@safInstruments.com"
    ],
    "subject": "Purchase Order from Zillium Inc (PO #: PO-00001)",
    "body": "Dear Bowman and Co, <br><br>The purchase order (PO-00001) is attached with this email. ...",
    "mail_documents": [
        {
            "document_id": 0,
            "file_name": "string"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your purchase order has been sent."
}
```

## Delete Purchase Order

### Description
Delete an existing purchase order.

### Endpoint
`DELETE /purchaseorders/{purchase_order_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The purchase order has been deleted."
}
```

## Delete Purchase Order Comment

### Description
Delete a purchase order comment.

### Endpoint
`DELETE /purchaseorders/{purchaseorder_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/comments/460000000012345?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Delete Purchase Order Attachment

### Description
Delete the file attached to the purchase order.

### Endpoint
`DELETE /purchaseorders/{purchaseorder_id}/attachment`

### OAuth Scope
`ZohoBooks.purchaseorders.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The attachment has been deleted."
}
```

## Get Purchase Order Attachment

### Description
Returns the file attached to the purchase order.

### Endpoint
`GET /purchaseorders/{purchaseorder_id}/attachment`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Query Parameters
*   **preview** (boolean): Get the thumbnail of the attachment (if applicable).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output po_attachment.pdf
```
*(Note: Response is the binary file data)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Get Purchase Order Email Content

### Description
Get the email content of a purchase order based on a template.

### Endpoint
`GET /purchaseorders/{purchaseorder_id}/email`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Query Parameters
*   **email_template_id** (string): Use a specific email template ID. If omitted, uses vendor's associated template or default.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
         "body": "Dear Bowman and Co, <br><br>The purchase order (PO-00001) is attached with this email. ...",
         "subject": "Purchase Order from Zillium Inc (PO #: PO-00001)",
         "file_name": "Purchase Order - PO-00001.pdf",
         "to_mail_ids": ["willsmith@bowmanfurniture.com"],
         "cc_mail_ids": ["peterparker@bowmanfurniture.com"],
         "vendor_id": "460000000026049",
         "vendor_name": "Bowman and Co"
         /* Other details like template_id, attachments etc. */
    }
}
```
*(Note: Updated response example based on typical API behavior for email content endpoints)*

## Update Billing Address

### Description
Updates the billing address for this purchase order alone.

### Endpoint
`PUT /purchaseorders/{purchaseorder_id}/address/billing`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.
*   **attention** (string): Attention line.
*   **is_update_customer** (string): Update the vendor's default billing address *(Note: Data type string, likely boolean)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Billing Address", "city": "New City", ...}'
```

#### Body Parameters
```json
{
    "address": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "country": "string",
    "fax": "string",
    "attention": "string",
    "is_update_customer": "string" /* Likely true/false */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated."
}
```

## List Purchase Order Comments and History

### Description
Get the complete history and comments of purchase order.

### Endpoint
`GET /purchaseorders/{purchaseorder_id}/comments`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "460000000012345",
            "description": "string",
            "commented_by_id": "string",
            "commented_by": "string",
            "comment_type": "system", /* or user */
            "date": "2014-02-10",
            "date_description": "22 hours ago.",
            "time": "3.26PM",
            "operation_type": "Updated", /* e.g., Added, Updated, Emailed */
            "transaction_id": "string",
            "transaction_type": "purchaseorder"
        },
        {...},
        {...}
    ]
}
```

## List Purchase Order Templates

### Description
Get all purchase order pdf templates.

### Endpoint
`GET /purchaseorders/templates`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "templates": [
        {
            "template_name": "Standard Template",
            "template_id": "460000000011003",
            "template_type": "standard"
        },
        {...},
        {...}
    ]
}
```

## List Purchase Orders

### Description
List all purchase orders.

### Endpoint
`GET /purchaseorders`

### OAuth Scope
`ZohoBooks.purchaseorders.READ`

### Query Parameters
*   **purchaseorder_number** (string): Search by PO number (variants: `_startswith`, `_contains`).
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`).
*   **date** (string): Search by date.
*   **status** (string): Search by status (`draft`, `open`, `billed`, `cancelled`).
*   **item_description** (string): Search by item description (variants: `_startswith`, `_contains`).
*   **vendor_name** (string): Search by vendor name (variants: `_startswith`, `_contains`).
*   **total** (double): Search by total amount (variants apply).
*   **vendor_id** (string): Filter by vendor ID.
*   **last_modified_time** (string): Filter by last modified time.
*   **item_id** (string): Filter by item ID.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Draft`, `Status.Open`, `Status.Billed`, `Status.Cancelled`.
*   **search_text** (string): Search by PO number, reference number, or vendor name.
*   **sort_column** (string): Sort results. Allowed Values: `vendor_name`, `purchaseorder_number`, `date`, `delivery_date`, `total`, `created_time`.
*   **custom_field** (string): Search by custom field (variants: `_startswith`, `_contains`).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders?organization_id=10234695&status=open' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "purchaseorders": [
        {
            "purchaseorder_id": "460000000062001",
            "vendor_id": "460000000026049",
            "vendor_name": "string",
            "status": "draft", /* Example */
            "purchaseorder_number": "PO-00001",
            "reference_number": "ER/0034",
            "date": "2014-02-10",
            "delivery_date": "2014-02-10",
            "currency_id": "460000000000099",
            "currency_code": "INR",
            "price_precision": 2,
            "total": 40,
            "has_attachment": false,
            "created_time": "2014-02-10T15:26:26+0530",
            "last_modified_time": "2014-02-10T15:26:26+0530",
            "custom_fields": [ /* ... */ ]
        },
        {...},
        {...}
    ],
    "page_context": { /* Standard pagination object */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "PurchaseOrders",
        "applied_filter": "Status.Open",
        "sort_column": "date",
        "sort_order": "A"
     }
}
```
*(Note: Added typical `page_context` object missing from original example)*

## Update a Purchase Order

### Description
Update an existing purchase order.

### Endpoint
`PUT /purchaseorders/{purchase_order_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact person IDs.
*   **purchaseorder_number** (string): PO number (Mandatory if auto-gen disabled).
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status.
*   **tax_treatment**: GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Vendor's VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor's GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply for VAT.
*   **pricebook_id** (string): Pricebook ID.
*   **reference_number** (string): Reference number.
*   **discount** (string): Discount (e.g., "10%" or "50").
*   **discount_account_id** (string): Account ID for discount.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **billing_address_id** (long): Billing Address ID.
*   **crm_owner_id** (string): CRM Owner ID.
*   **crm_custom_reference_id** (long): CRM Custom Reference ID.
*   **template_id** (string): Template ID.
*   **date** (string): Creation/Update date.
*   **delivery_date** (string): Delivery date.
*   **due_date** (string): Delivery date *(Note: Duplicates delivery_date?)*.
*   **exchange_rate** (double): Exchange rate.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **notes** (string): Delivery notes.
*   **notes_default** (string): Default notes.
*   **terms** (string): Terms.
*   **terms_default** (string): Default terms.
*   **ship_via** (string): Shipment preference.
*   **delivery_org_address_id** (string): Delivery Address ID (Org).
*   **delivery_customer_id** (string): Delivery Customer ID.
*   **attention** (string): Delivery contact person.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (string): Update customer address *(Note: Data type string, likely boolean)*.
*   **salesorder_id** (long): Associated Sales Order ID.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **custom_fields** (array): Custom fields.
*   **documents** (array): Documents to attach.

### Query Parameters
*   **attachment**: File(s) to attach (sent via multipart/form-data). Allowed extensions listed.
*   **ignore_auto_number_generation** (boolean): Ignore auto-generation of PO number.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000026049", "date": "2014-02-10", "line_items": [...] ...}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "vendor_id": "460000000026049",
    "currency_id": "460000000000099",
    "contact_persons": [ "460000000026051" ],
    "purchaseorder_number": "PO-00001",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": 460000000026089,
    "reference_number": "ER/0034",
    "discount": "10",
    "discount_account_id": "460000000011105",
    "is_discount_before_tax": true,
    "billing_address_id": "460000000017491",
    "crm_owner_id": "string",
    "crm_custom_reference_id": 0,
    "template_id": "460000000011003",
    "date": "2014-02-10",
    "delivery_date": "2014-02-10",
    "due_date": "string",
    "exchange_rate": 1,
    "is_inclusive_tax": false,
    "notes": "Please deliver as soon as possible.",
    "notes_default": "string",
    "terms": "Thanks for your business.",
    "terms_default": "string",
    "ship_via": "string",
    "delivery_org_address_id": "string",
    "delivery_customer_id": "string",
    "attention": "string",
    "vat_treatment": "string",
    "is_update_customer": "string",
    "salesorder_id": "460000124728314",
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "documents": [ { /* ... document details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Purchase Order has been updated.",
    "purchaseorder": {
        "purchaseorder_id": "460000000062001"
        /* ... updated purchase order details ... */
    }
}
```

## Submit Purchase Order for Approval

### Description
Submit a purchase order for approval.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/submit`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The purchase order has been successfully submitted for approval."
}
```

## Mark Purchase Order as Open

### Description
Mark a draft purchase order as open.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/status/open`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/status/open?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The purchase order has been marked as open."
}
```

## Mark as Billed

### Description
Mark a purchase order as billed.

### Endpoint
`POST /purchaseorders/{purchaseorder_id}/status/billed`

### OAuth Scope
`ZohoBooks.purchaseorders.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/status/billed?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The purchase order has been marked as billed."
}
```

## Update Custom Field in Purchase Order

### Description
Update the value of the custom field in existing purchase orders.

### Endpoint
`PUT /purchaseorder/{purchaseorder_id}/customfields`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field to update.
    *   **value** (string): The new value for the custom field.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorder/460000000062001/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "46000000012845", "value": "Updated Value"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "46000000012845",
        "value": "Normal" /* New value */
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```

## Update Attachment Preference

### Description
Set whether you want to send the attached file while emailing the purchase order.

### Endpoint
`PUT /purchaseorders/{purchaseorder_id}/attachment`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Query Parameters
*   **can_send_in_mail** (boolean, Required): Set to true or false.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/attachment?organization_id=10234695&can_send_in_mail=false' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Purchase Order has been updated."
}
```

## Update Purchase Order Comment

### Description
Update an existing comment of a purchase order.

### Endpoint
`PUT /purchaseorders/{purchaseorder_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Arguments (Body Parameters)
*   **description** (string): The updated comment text.
*   **expected_delivery_date** (string): Update the expected delivery date associated with this comment *(Note: Unusual field for a comment update)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/comments/460000000012345?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Updated comment text.", "expected_delivery_date": "2024-07-16"}'
```

#### Body Parameters
```json
{
    "description": "string",
    "expected_delivery_date": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been updated."
    /* May include updated comment object */
}
```

## Update Purchase Order Template

### Description
Update the pdf template associated with the purchase order.

### Endpoint
`PUT /purchaseorders/{purchaseorder_id}/templates/{template_id}`

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders/460000000062001/templates/460000000011003?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Purchase Order has been updated."
}
```

## Update Purchase Order using Custom Field

### Description
Update a purchase order using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found. *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs)*.

### Endpoint
`PUT /purchaseorders` *(Note: Example shows this, but typically PUT for update uses ID like `/purchaseorders/{id}`. This endpoint might work with headers.)*

### OAuth Scope
`ZohoBooks.purchaseorders.UPDATE`

### Headers *(Assumed based on description)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact person IDs.
*   **purchaseorder_number** (string): PO number (Mandatory if auto-gen disabled).
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status.
*   **tax_treatment**: GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Vendor's VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor's GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply for VAT.
*   **pricebook_id** (string): Pricebook ID.
*   **reference_number** (string): Reference number.
*   **discount** (string): Discount (e.g., "10%" or "50").
*   **discount_account_id** (string): Account ID for discount.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **billing_address_id** (long): Billing Address ID.
*   **crm_owner_id** (string): CRM Owner ID.
*   **crm_custom_reference_id** (long): CRM Custom Reference ID.
*   **template_id** (string): Template ID.
*   **date** (string): Creation/Update date.
*   **delivery_date** (string): Delivery date.
*   **due_date** (string): Delivery date *(Note: Duplicates delivery_date?)*.
*   **exchange_rate** (double): Exchange rate.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **notes** (string): Delivery notes.
*   **notes_default** (string): Default notes.
*   **terms** (string): Terms.
*   **terms_default** (string): Default terms.
*   **ship_via** (string): Shipment preference.
*   **delivery_org_address_id** (string): Delivery Address ID (Org).
*   **delivery_customer_id** (string): Delivery Customer ID.
*   **attention** (string): Delivery contact person.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (string): Update customer address *(Note: Data type string, likely boolean)*.
*   **salesorder_id** (long): Associated Sales Order ID.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **custom_fields** (array): Custom fields.
*   **documents** (array): Documents to attach.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/purchaseorders?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000026049", "date": "2014-02-10", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000026049",
    "currency_id": "460000000000099",
    "contact_persons": [ "460000000026051" ],
    "purchaseorder_number": "PO-00001",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": 460000000026089,
    "reference_number": "ER/0034",
    "discount": "10",
    "discount_account_id": "460000000011105",
    "is_discount_before_tax": true,
    "billing_address_id": "460000000017491",
    "crm_owner_id": "string",
    "crm_custom_reference_id": 0,
    "template_id": "460000000011003",
    "date": "2014-02-10",
    "delivery_date": "2014-02-10",
    "due_date": "string",
    "exchange_rate": 1,
    "is_inclusive_tax": false,
    "notes": "Please deliver as soon as possible.",
    "notes_default": "string",
    "terms": "Thanks for your business.",
    "terms_default": "string",
    "ship_via": "string",
    "delivery_org_address_id": "string",
    "delivery_customer_id": "string",
    "attention": "string",
    "vat_treatment": "string",
    "is_update_customer": "string",
    "salesorder_id": "460000124728314",
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "documents": [ { /* ... document details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Purchase Order has been updated.",
    "purchaseorder": {
        "purchaseorder_id": "460000000062001"
        /* ... updated purchase order details ... */
    }
}
```
# Bills

## Overview

### Bills
When your vendor supplies goods/services to you on credit, you’re sent an invoice that details the amount of money you owe him. You can record this as a bill in Zoho Books and track it until it’s paid.

### End Points
*   `POST /bills`
*   `PUT /bills` *(Note: This is likely for bulk/keyed updates, see Update Bill using Custom Field)*
*   `GET /bills`
*   `PUT /bills/{bill_id}`
*   `GET /bills/{bill_id}`
*   `DELETE /bills/{bill_id}`
*   `PUT /bill/{bill_id}/customfields`
*   `POST /bills/{bill_id}/status/void`
*   `POST /bills/{bill_id}/status/open`
*   `POST /bills/{bill_id}/submit`
*   `POST /bills/{bill_id}/approve`
*   `PUT /bills/{bill_id}/address/billing`
*   `GET /bills/{bill_id}/payments`
*   `POST /bills/{bill_id}/credits`
*   `DELETE /bills/{bill_id}/payments/{bill_payment_id}`
*   `DELETE /bills/{bill_id}/creditsapplied/{creditnotes_invoice_id}` *(Note: Endpoint path likely incorrect, should relate to vendor credits applied)*
*   `POST /bills/{bill_id}/attachment`
*   `GET /bills/{bill_id}/attachment`
*   `DELETE /bills/{bill_id}/attachment`
*   `DELETE /bills/expenses/{expense_id}/receipt` *(Note: Endpoint path seems specific to expense-generated bills)*
*   `POST /bills/{bill_id}/comments`
*   `GET /bills/{bill_id}/comments`
*   `DELETE /bills/{bill_id}/comments/{comment_id}`
*   `GET /bills/editpage/frompurchaseorders` *(Note: This endpoint wasn't in the provided files, but was listed here)*

### Attributes
*   **bill_id** (string): ID of the Bill
*   **purchaseorder_ids** (array): IDs of associated purchase orders.
*   **vendor_id** (string): ID of the vendor.
*   **vendor_name** (string): Name of the Vendor.
*   **vat_treatment** (string): 🇬🇧 only - Vendor's VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - VAT Registration number.
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **place_of_supply** (string): GCC only - Place of supply for VAT (Supported codes listed).
*   **permit_number** (string): 🇦🇪 only - Permit number.
*   **gst_no** (string): 🇮🇳 only - Vendor's 15 digit GST number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status (`business_gst`, `business_none`, `overseas`, `consumer`).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_pre_gst** (boolean): 🇮🇳 only - Applicable before July 1, 2017.
*   **pricebook_id** (string): Price book ID.
*   **pricebook_name** (string): Price book name.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Applicable for reverse charge transactions.
*   **unused_credits_payable_amount** (integer): Unused Credits available for this Vendor.
*   **status** (string): Status of the Bill (`paid`, `open`, `overdue`, `void`, `partially_paid`).
*   **bill_number** (string): The bill number.
*   **date** (string): Bill creation date. [yyyy-mm-dd].
*   **due_date** (string): Bill due date.
*   **payment_terms** (integer): Payment terms in days.
*   **payment_terms_label** (string): Payment terms label.
*   **payment_expected_date** (string): Expected Payment date.
*   **reference_number** (string): Reference Number.
*   **recurring_bill_id** (string): ID of the Recurring Bill.
*   **due_by_days** (string): Days until due (relative).
*   **due_in_days** (integer): Days until due (absolute).
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **documents** (array): Attached documents.
*   **price_precision** (integer): Price precision.
*   **exchange_rate** (double): Exchange rate.
*   **adjustment** (double): Adjustments amount.
*   **adjustment_description** (string): Adjustment description.
*   **custom_fields** (array): Custom fields.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - Check if TDS is applied.
*   **is_item_level_tax_calc** (boolean): Check if tax calculation is at item level.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line item rates inclusive of tax.
*   **filed_in_vat_return_id** (string): 🇬🇧 only - ID of the filed VAT Return.
*   **filed_in_vat_return_name** (string): 🇬🇧 only - Name of the filed VAT Return.
*   **filed_in_vat_return_type** (string): 🇬🇧 only - Type of the filed VAT Return.
*   **is_abn_quoted** (string): 🇦🇺 only - ABN quoted status.
*   **line_items** (array): Line items.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **sub_total** (integer): Sub Total.
*   **tax_total** (integer): Tax Total.
*   **total** (integer): Total amount.
*   **payment_made** (integer): Amount paid.
*   **vendor_credits_applied** (integer): Vendor credits applied.
*   **is_line_item_invoiced** (boolean): Check if line item is invoiced *(Note: Seems out of place, usually for Sales Orders/Estimates)*.
*   **purchaseorders** (array): Associated purchase orders.
*   **taxes** (array): Taxes applied.
*   **acquisition_vat_summary** (array): 🇬🇧 , Europe only - Acquisition VAT summary.
*   **acquisition_vat_total** (double): 🇬🇧 , Europe only - Total Acquisition VAT.
*   **reverse_charge_vat_summary** (array): 🇬🇧 , Europe only - Reverse Charge VAT summary.
*   **reverse_charge_vat_total** (double): 🇬🇧 , Europe only - Total Reverse Charge VAT.
*   **balance** (integer): Balance due.
*   **billing_address** (object): Billing address.
*   **payments** (array): Payments made.
*   **vendor_credits** (array): Vendor credits applied.
*   **created_time** (string): Creation time.
*   **created_by_id** (string): ID of creator user.
*   **last_modified_time** (string): Last modified time.
*   **reference_id** (string): *(Note: Purpose unclear, distinct from reference_number)*.
*   **notes** (string): Notes.
*   **terms** (string): Terms and Conditions.
*   **attachment_name** (string): Name of primary attachment.
*   **open_purchaseorders_count** (integer): Number of linked open POs.

### Example
```json
{
    "bill_id": "460000000098765",
    "purchaseorder_ids": [
        460000000068231,
        460000000068233
    ],
    "vendor_id": "460000000038029",
    "vendor_name": "string",
    "vat_treatment": "string",
    "vat_reg_no": "string",
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "permit_number": "string",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_pre_gst": false,
    "pricebook_id": 460000000038090,
    "pricebook_name": "string",
    "is_reverse_charge_applied": true,
    "unused_credits_payable_amount": 187,
    "status": "open",
    "bill_number": "00454",
    "date": "2013-09-11",
    "due_date": "2013-09-26",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "payment_expected_date": "string",
    "reference_number": "4321133",
    "recurring_bill_id": "string",
    "due_by_days": "string",
    "due_in_days": 0,
    "currency_id": "460000000000099",
    "currency_code": "INR",
    "currency_symbol": "string",
    "documents": [ { "document_id": 0, "file_name": "string" } ],
    "price_precision": 2,
    "exchange_rate": 1.23,
    "adjustment": 0,
    "adjustment_description": " ",
    "custom_fields": [ { "custom_field_id": 0, "index": 0, "label": "string", "value": "string" } ],
    "is_tds_applied": true,
    "is_item_level_tax_calc": false,
    "is_inclusive_tax": false,
    "filed_in_vat_return_id": "string",
    "filed_in_vat_return_name": "string",
    "filed_in_vat_return_type": "string",
    "is_abn_quoted": "string",
    "line_items": [ /* ... line item details ... */ ],
    "location_id": "460000000038080",
    "location_name": "string",
    "sub_total": 40,
    "tax_total": 0,
    "total": 40,
    "payment_made": 0,
    "vendor_credits_applied": 0,
    "is_line_item_invoiced": false,
    "purchaseorders": [ { /* ... PO details ... */ } ],
    "taxes": [ { /* ... tax details ... */ } ],
    "acquisition_vat_summary": [ { /* ... summary ... */ } ],
    "acquisition_vat_total": 0.1,
    "reverse_charge_vat_summary": [ { /* ... summary ... */ } ],
    "reverse_charge_vat_total": 0.1,
    "balance": 40,
    "billing_address": { /* ... address details ... */ },
    "payments": [ { /* ... payment details ... */ } ],
    "vendor_credits": [ { /* ... vendor credit details ... */ } ],
    "created_time": "2013-09-11T17:18:32+0530",
    "created_by_id": "4600000053001",
    "last_modified_time": "2013-09-11T17:18:32+0530",
    "reference_id": "string",
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "attachment_name": "string",
    "open_purchaseorders_count": 1
}
```

## Add Comment to Bill

### Description
Add a comment for a bill.

### Endpoint
`POST /bills/{bill_id}/comments`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Arguments (Body Parameters)
*   **description** (string, Required): The comment text.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Waiting for manager approval."}'
```

#### Body Parameters
```json
{
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": {
        "comment_id": "460000000069037",
        "bill_id": "460000000098765",
        "description": "string",
        "commented_by_id": "460000000053001",
        "commented_by": "John Roberts",
        "comment_type": "internal",
        "date": "2013-09-11",
        "date_description": "few seconds ago",
        "time": "12:09 PM"
    }
}
```

## Add Attachment to Bill

### Description
Attach a file to a bill.

### Endpoint
`POST /bills/{bill_id}/attachment`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Query Parameters
*   **attachment**: The file to attach (sent via multipart/form-data). Allowed Extensions: gif, png, jpeg, jpg, bmp, pdf.

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/your/bill_scan.pdf"
```

### Response Example
```json
{
    "code": 0,
    "message": "The document has been attached."
}
```

## Apply Credits to Bill

### Description
Apply the vendor credits from excess vendor payments to a bill. Multiple credits can be applied at once.

### Endpoint
`POST /bills/{bill_id}/credits`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Arguments (Body Parameters)
*   **bill_payments** (array): Array of excess vendor payments to apply.
    *   **payment_id** (string): ID of the excess vendor payment.
    *   **amount_applied** (double): Amount to apply.
*   **apply_vendor_credits** (array): Array of vendor credits to apply.
    *   **vendor_credit_id** (string): ID of the vendor credit.
    *   **amount_applied** (double): Amount to apply.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/credits?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"bill_payments": [{"payment_id": "...", "amount_applied": 10.0}], "apply_vendor_credits": [{"vendor_credit_id": "...", "amount_applied": 5.0}]}'
```

#### Body Parameters
```json
{
    "bill_payments": [
        {
            "payment_id": "460000000042059",
            "amount_applied": 31.25
        }
    ],
    "apply_vendor_credits": [
        {
            "vendor_credit_id": "4600000053221",
            "amount_applied": 31.25
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits have been applied to the bill(s)."
}
```

## Approve a Bill

### Description
Approve a bill.

### Endpoint
`POST /bills/{bill_id}/approve`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success" /* Likely "Bill approved." */
}
```

## Create a Bill

### Description
Create a bill received from your vendor.

### Endpoint
`POST /bills`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (boolean): Update vendor address *(Note: Parameter name mismatch in original file)*.
*   **purchaseorder_ids** (array): IDs of POs to link.
*   **bill_number** (string, Required): Bill number.
*   **documents** (array): Documents to attach.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **permit_number** (string): 🇦🇪 only - Permit number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **pricebook_id** (string): Price book ID.
*   **reference_number** (string): Reference number.
*   **date** (string): Bill date. [yyyy-mm-dd].
*   **due_date** (string): Due date.
*   **payment_terms** (integer): Payment terms in days.
*   **payment_terms_label** (string): Payment terms label.
*   **recurring_bill_id** (string): Recurring Bill ID.
*   **exchange_rate** (double): Exchange rate.
*   **is_item_level_tax_calc** (boolean): Use item-level tax calculation.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **adjustment** (double): Adjustment amount.
*   **adjustment_description** (string): Adjustment description.
*   **location_id** (string): Location ID.
*   **custom_fields** (array): Custom fields.
*   **line_items** (array): Line items.
    *   Include item_id/account_id, name, rate, quantity, tax_id etc.
*   **taxes** (array): Taxes applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **approvers** (array): Approver details.

### Query Parameters
*   **attachment**: File(s) to attach (sent via multipart/form-data). Allowed extensions listed.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "bill_number": "B-001", "line_items": [...] ...}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "vat_treatment": "string",
    "is_update_customer": false,
    "purchaseorder_ids": [
        460000000068231,
        460000000068233
    ],
    "bill_number": "00454",
    "documents": [ { /* ... document details ... */ } ],
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "permit_number": "string",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "pricebook_id": 460000000038090,
    "reference_number": "4321133",
    "date": "2013-09-11",
    "due_date": "2013-09-26",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "recurring_bill_id": "string",
    "exchange_rate": 1.23,
    "is_item_level_tax_calc": false,
    "is_inclusive_tax": false,
    "adjustment": 0,
    "adjustment_description": " ",
    "location_id": "460000000038080",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "line_items": [ { /* ... line item details ... */ } ],
    "taxes": [ { /* ... tax details ... */ } ],
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "approvers": [ { /* ... approver details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "success", /* Message in example, likely "Bill created." */
    "bill": {
        "bill_id": "460000000098765",
        "status": "open", /* Initial status */
        /* ... full bill details ... */
    }
}
```

## Delete a Bill Payment

### Description
Delete a payment made to a bill. This unapplies the payment from this bill.

### Endpoint
`DELETE /bills/{bill_id}/payments/{bill_payment_id}`

*Note: `{bill_payment_id}` is the ID mapping the payment to *this* bill (from List Bill Payments).*

### OAuth Scope
`ZohoBooks.bills.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/payments/460000000042061?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment has been deleted."
}
```

## Delete Bill Comment

### Description
Delete a bill comment. *(Note: This file was originally named "Get Bill Data from Purchase Orders.md" but contained the content for deleting a comment).*

### Endpoint
`DELETE /bills/{bill_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.bills.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/comments/460000000069037?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Get Bill Attachment

### Description
Returns the file attached to the bill.

### Endpoint
`GET /bills/{bill_id}/attachment`

### OAuth Scope
`ZohoBooks.bills.READ`

### Query Parameters
*   **preview** (boolean): Get the thumbnail of the attachment (if applicable).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --output bill_attachment.pdf
```
*(Note: Response is the binary file data)*

### Response Example (on success metadata)
```json
{
    "code": 0,
    "message": "success"
}
```
*(Note: A successful download returns the file data, not this JSON.)*

## Get a Bill

### Description
Get the details of a bill.

### Endpoint
`GET /bills/{bill_id}`

### OAuth Scope
`ZohoBooks.bills.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bill": {
        "bill_id": "460000000098765",
        /* ... full bill details ... */
    }
}
```

## Delete Bill Attachment

### Description
Delete the file attached to a bill.

### Endpoint
`DELETE /bills/{bill_id}/attachment`

### OAuth Scope
`ZohoBooks.bills.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The attachment has been deleted."
}
```

## Delete a Bill

### Description
Delete an existing bill. Bills which have payments applied cannot be deleted.

### Endpoint
`DELETE /bills/{bill_id}`

### OAuth Scope
`ZohoBooks.bills.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The bill has been deleted."
}
```

## List Bill Comments and History

### Description
Get the complete history and comments of a bill.

### Endpoint
`GET /bills/{bill_id}/comments`

### OAuth Scope
`ZohoBooks.bills.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "460000000069037",
            "bill_id": "460000000098765",
            "description": "string",
            "commented_by_id": "460000000053001",
            "commented_by": "John Roberts",
            "comment_type": "internal",
            "date": "17 Nov 2016",
            "date_description": "few seconds ago",
            "time": "12:09 PM",
            "operation_type": "Added", /* e.g., Added, Updated, Paid */
            "transaction_id": "460000000068015", /* Related transaction ID */
            "transaction_type": "bill_payment" /* Type of related transaction */
        },
        {...},
        {...}
    ]
}
```

## List Bill Payments

### Description
Get the list of payments made for a bill.

### Endpoint
`GET /bills/{bill_id}/payments`

### OAuth Scope
`ZohoBooks.bills.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/payments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "payments": [
        {
            "payment_id": "460000000042059",
            "bill_id": "460000000098765",
            "bill_payment_id": "460000000042061", /* ID mapping payment to this bill */
            "vendor_id": "460000000038029",
            "vendor_name": "string",
            "payment_mode": "Cash",
            "description": "string",
            "date": "2013-09-11",
            "reference_number": "4321133",
            "exchange_rate": 1.23,
            "amount": 31.25,
            "paid_through": "Petty Cash", /* Account name */
            "paid_through_account_id": "460000000000358",
            "is_single_bill_payment": true
        },
        {...},
        {...}
    ]
}
```

## List Bills

### Description
List all bills with pagination.

### Endpoint
`GET /bills`

### OAuth Scope
`ZohoBooks.bills.READ`

### Query Parameters
*   **bill_number** (string): Search by bill number (variants: `_startswith`, `_contains`).
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`).
*   **date** (string): Search by date (variants: `_start`, `_end`, `_before`, `_after`).
*   **status** (string): Search by status. Allowed Values: `paid`, `open`, `overdue`, `void`, `partially_paid`.
*   **description** (string): Search by description (variants: `_startswith`, `_contains`).
*   **vendor_name** (string): Search by vendor name (variants: `_startswith`, `_contains`).
*   **total** (double): Search by total amount (variants apply).
*   **vendor_id** (string): Filter by Vendor ID.
*   **item_id** (string): Filter by Item ID.
*   **recurring_bill_id** (string): Filter by Recurring Bill ID.
*   **purchaseorder_id** (string): Filter by Purchase Order ID.
*   **last_modified_time** (string): Filter by last modified time.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.PartiallyPaid`, `Status.Paid`, `Status.Overdue`, `Status.Void`, `Status.Open`.
*   **search_text** (string): Search by bill number, reference number, or vendor name.
*   **page** (integer): Page number.
*   **sort_column** (string): Sort results. Allowed Values: `vendor_name`, `bill_number`, `date`, `due_date`, `total`, `balance`, `created_time`.
*   **sort_order** (string): Sort order (A/D).

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bills?organization_id=10234695&status=open' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bills": [
        {
            "bill_id": "460000000098765",
            "vendor_id": "460000000038029",
            "vendor_name": "string",
            "status": "open",
            "bill_number": "00454",
            "reference_number": "4321133",
            "date": "2013-09-11",
            "due_date": "2013-09-26",
            "due_days": "string",
            "currency_id": "460000000000099",
            "currency_code": "INR",
            "price_precision": 2,
            "exchange_rate": 1.23,
            "total": 40,
            "balance": 40,
            "location_id": "460000000038080",
            "location_name": "string",
            "created_time": "2013-09-11T17:18:32+0530",
            "last_modified_time": "2013-09-11T17:18:32+0530",
            "attachment_name": "string",
            "has_attachment": false,
            "is_tds_applied": true,
            "is_abn_quoted": "string"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Bills",
        "applied_filter": "Status.All", /* Example */
        "sort_column": "string",
        "sort_order": "D"
    }
}
```

## Mark Bill as Open

### Description
Mark a void bill as open.

### Endpoint
`POST /bills/{bill_id}/status/open`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/status/open?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The status of the bill has been changed to open." /* Typo in original message "chaged" */
}
```

## Submit Bill for Approval

### Description
Submit a bill for approval.

### Endpoint
`POST /bills/{bill_id}/submit`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The bill has been submitted for approval successfully."
}
```

## Update a Bill

### Description
Update a bill. To delete a line item just remove it from the line_items list.

### Endpoint
`PUT /bills/{bill_id}`

### OAuth Scope
`ZohoBooks.bills.UPDATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (boolean): Update vendor address.
*   **purchaseorder_ids** (array): Link PO IDs.
*   **bill_number** (string, Required): Bill number.
*   **documents** (array): Documents to attach.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **permit_number** (string): 🇦🇪 only - Permit number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **pricebook_id** (string): Price book ID.
*   **reference_number** (string): Reference number.
*   **date** (string): Bill date. [yyyy-mm-dd].
*   **due_date** (string): Due date.
*   **payment_terms** (integer): Payment terms days.
*   **payment_terms_label** (string): Payment terms label.
*   **recurring_bill_id** (string): Recurring Bill ID.
*   **exchange_rate** (double): Exchange rate.
*   **is_item_level_tax_calc** (boolean): Use item-level tax.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **adjustment** (double): Adjustment amount.
*   **adjustment_description** (string): Adjustment description.
*   **custom_fields** (array): Custom fields.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **location_id** (string): Location ID.
*   **taxes** (array): Taxes applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **approvers** (array): Approver details.

### Query Parameters
*   **attachment**: File(s) to attach (sent via multipart/form-data). Allowed extensions listed.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "bill_number": "B-001-MODIFIED", "line_items": [...] ...}'
```
*(Note: Attaching files requires multipart/form-data)*

#### Body Parameters (JSON part)
```json
{
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "vat_treatment": "string",
    "is_update_customer": false,
    "purchaseorder_ids": [ 460000000068231, 460000000068233 ],
    "bill_number": "00454",
    "documents": [ { /* ... document details ... */ } ],
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "permit_number": "string",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "pricebook_id": 460000000038090,
    "reference_number": "4321133",
    "date": "2013-09-11",
    "due_date": "2013-09-26",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "recurring_bill_id": "string",
    "exchange_rate": 1.23,
    "is_item_level_tax_calc": false,
    "is_inclusive_tax": false,
    "adjustment": 0,
    "adjustment_description": " ",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "location_id": "460000000038080",
    "taxes": [ { /* ... tax details ... */ } ],
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "approvers": [ { /* ... approver details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Bill information has been updated.",
    "bill": {
        "bill_id": "460000000098765",
        /* ... updated bill details ... */
    }
}
```

## Update a Billing Address

### Description
Updates the billing address for this bill.

### Endpoint
`PUT /bills/{bill_id}/address/billing`

### OAuth Scope
`ZohoBooks.bills.UPDATE`

### Arguments (Body Parameters)
*   **address** (string): Address line(s).
*   **city** (string): City.
*   **state** (string): State/Province.
*   **zip** (string): ZIP/Postal Code.
*   **country** (string): Country.
*   **fax** (string): Fax Number.
*   **attention** (string): Attention line.
*   **is_update_customer** (boolean): Update the vendor's default billing address.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"address": "Updated Address", "city": "Updated City", ...}'
```

#### Body Parameters
```json
{
    "address": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "country": "string",
    "fax": "string",
    "attention": "string",
    "is_update_customer": false
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Billing address updated.",
    "billing_address": {
        "address": "string",
        "street2": "Suite 310",
        "city": "string",
        "state": "string",
        "zip": "string",
        "country": "string",
        "fax": "string",
        "attention": "string"
    }
}
```

## Update Custom Field in Bill

### Description
Update the value of the custom field in existing bills.

### Endpoint
`PUT /bill/{bill_id}/customfields`

### OAuth Scope
`ZohoBooks.bills.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field.
    *   **index** (integer): Index of the custom field.
    *   **label** (string): Label of the Custom Field.
    *   **value** (string): New value for the custom field.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bill/460000000098765/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"custom_field_id": 0, "value": "UpdatedValue"}]'
```

#### Body Parameters
```json
[
    {
        "custom_field_id": 0,
        "index": 0,
        "label": "string",
        "value": "string"
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```

## Update Bill using Custom Field

### Description
Update a bill using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /bills` *(Note: This endpoint is typically for bulk updates or upserts with unique keys)*

### OAuth Scope
`ZohoBooks.bills.UPDATE`

### Headers
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_update_customer** (boolean): Update vendor address.
*   **purchaseorder_ids** (array): Link PO IDs.
*   **bill_number** (string, Required): Bill number.
*   **documents** (array): Documents to attach.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **permit_number** (string): 🇦🇪 only - Permit number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **pricebook_id** (string): Price book ID.
*   **reference_number** (string): Reference number.
*   **date** (string): Bill date. [yyyy-mm-dd].
*   **due_date** (string): Due date.
*   **payment_terms** (integer): Payment terms days.
*   **payment_terms_label** (string): Payment terms label.
*   **recurring_bill_id** (string): Recurring Bill ID.
*   **exchange_rate** (double): Exchange rate.
*   **is_item_level_tax_calc** (boolean): Use item-level tax.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **adjustment** (double): Adjustment amount.
*   **adjustment_description** (string): Adjustment description.
*   **custom_fields** (array): Custom fields.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **location_id** (string): Location ID.
*   **taxes** (array): Taxes applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **approvers** (array): Approver details.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "bill_number": "00454", ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "vat_treatment": "string",
    "is_update_customer": false,
    "purchaseorder_ids": [ 460000000068231, 460000000068233 ],
    "bill_number": "00454",
    "documents": [ { /* ... document details ... */ } ],
    "source_of_supply": "AP",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "permit_number": "string",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "pricebook_id": 460000000038090,
    "reference_number": "4321133",
    "date": "2013-09-11",
    "due_date": "2013-09-26",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "recurring_bill_id": "string",
    "exchange_rate": 1.23,
    "is_item_level_tax_calc": false,
    "is_inclusive_tax": false,
    "adjustment": 0,
    "adjustment_description": " ",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "location_id": "460000000038080",
    "taxes": [ { /* ... tax details ... */ } ],
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "approvers": [ { /* ... approver details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Bill information has been updated.",
    "bill": {
        "bill_id": "460000000098765",
        /* ... updated bill details ... */
    }
}
```

## Void a Bill

### Description
Mark a bill status as void.

### Endpoint
`POST /bills/{bill_id}/status/void`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bills/460000000098765/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The bill has been marked as void."
}
```


# Recurring Bills

## Overview

### Recurring Bills
Recurring Bills are those bills that repeat itself after a fixed interval of time.

### End Points
*   `POST /recurringbills`
*   `PUT /recurringbills` *(Note: Likely refers to the 'Update Recurring Bill using Custom Field' endpoint)*
*   `GET /recurringbills`
*   `PUT /recurringbills/{recurring_bill_id}`
*   `GET /recurringbills/{recurring_bill_id}` *(Note: Path corrected from original `/recurring_bills/`)*
*   `DELETE /recurringbills/{recurring_bill_id}` *(Note: Path corrected from original `/recurring_bills/`)*
*   `POST /recurringbills/{recurring_bill_id}/status/stop`
*   `POST /recurringbills/{recurring_bill_id}/status/resume`
*   `GET /recurringexpenses/{recurring_expense_id}/expenses` *(Note: Original endpoint lists generated Bills, not Expenses. Path seems inconsistent.)*
*   `GET /recurringbills/{recurring_bill_id}/comments`

### Attributes
*   **recurring_bill_id** (string): Unique ID of the recurring bill.
*   **vendor_id** (string): ID of the vendor.
*   **vendor_name** (string): Name of the Vendor.
*   **status** (string): Status of the Recurring Bill (e.g., `active`, `stopped`, `expired`).
*   **recurrence_name** (string): Name of the Recurring Bill. Max-length [100].
*   **currency_id** (string): ID of the Currency.
*   **currency_code** (string): Code of the Currency.
*   **currency_symbol** (string): Symbol of the Currency.
*   **start_date** (string): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **place_of_supply** (string): GCC only - Place of supply for VAT (Supported codes listed).
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status (business_gst, business_none, overseas, consumer).
*   **gst_no** (string): 🇮🇳 only - Vendor's 15 digit GST number.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (uk, eu_vat_registered, overseas).
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - VAT Registration number.
*   **is_abn_quoted** (string): 🇦🇺 only - ABN quoted status.
*   **abn** (string): 🇦🇺 only - ABN number.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Applicable for reverse charge transactions.
*   **pricebook_id** (string): Price book ID.
*   **pricebook_name** (string): Price book name.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line item rates inclusive of tax.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_items** (array): Line items.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - Check if TDS is applied.
*   **notes** (string): Notes for the Bill template.
*   **terms** (string): Terms and Conditions for the Bill template.
*   **payment_terms** (integer): Payment Terms days.
*   **payment_terms_label** (string): Payment Terms label.
*   **custom_fields** (array): Custom fields.
*   **acquisition_vat_summary** (array): 🇬🇧 , Europe only - Acquisition VAT summary.
*   **reverse_charge_vat_summary** (array): 🇬🇧 , Europe only - Reverse Charge VAT summary.
*   **acquisition_vat_total** (double): 🇬🇧 , Europe only - Total Acquisition VAT.
*   **reverse_charge_vat_total** (double): 🇬🇧 , Europe only - Total Reverse Charge VAT.
*   **created_time** (string): Creation time.
*   **created_by_id** (string): ID of creator user.
*   **last_modified_time** (string): Last modified time.
*   **discount** (string): Discount (e.g., "12.5%" or "190").
*   **discount_account_id** (string): Account ID for discount.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   *(Note: Several fields listed under original recurring expense attributes seem related to generated child bills, not the profile itself, like amount, total, tax details. Clarification might be needed in the original documentation.)*

### Example
```json
{
    "recurring_bill_id": 982000000567240,
    "vendor_id": "460000000038029",
    "vendor_name": "string",
    "status": "active",
    "recurrence_name": "Monthly Rental",
    "currency_id": "460000000000099",
    "currency_code": "INR",
    "currency_symbol": "string",
    "start_date": "2013-11-18",
    "end_date": "2013-12-18",
    "source_of_supply": "AP",
    "place_of_supply": "DU",
    "destination_of_supply": "TN",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "tax_treatment": "vat_registered",
    "vat_treatment": "string",
    "vat_reg_no": "string",
    "is_abn_quoted": "string",
    "abn": "string",
    "is_reverse_charge_applied": true,
    "pricebook_id": 460000000038090,
    "pricebook_name": "string",
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "location_name": "string",
    "line_items": [ { /* ... line item details ... */ } ],
    "is_tds_applied": true,
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "acquisition_vat_summary": [ { /* ... summary ... */ } ],
    "reverse_charge_vat_summary": [ { /* ... summary ... */ } ],
    "acquisition_vat_total": 0.1,
    "reverse_charge_vat_total": 0.1,
    "created_time": "2013-09-11T17:18:32+0530",
    "created_by_id": "4600000053001",
    "last_modified_time": "2013-09-11T17:18:32+0530",
    "discount": "30%",
    "discount_account_id": "460000000000403",
    "is_discount_before_tax": true
}
```

## Create a Recurring Bill

### Description
Create a recurring bill.

### Endpoint
`POST /recurringbills`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - VAT Reg number.
*   **is_abn_quoted** (string): 🇦🇺 only - ABN quoted status.
*   **abn** (string): 🇦🇺 only - ABN number.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Apply reverse charge.
*   **pricebook_id** (string): Price book ID.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   Include account_id, description, amount, tax_id etc.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - TDS applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **payment_terms** (integer): Payment terms days.
*   **payment_terms_label** (string): Payment terms label.
*   **custom_fields** (array): Custom fields.
*   **discount** (string): Discount (e.g., "12.5%" or "190").
*   **discount_account_id** (string): Discount account ID.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **recurrence_frequency** (string, Required): Frequency (e.g., 'weeks', 'months').

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringbills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "recurrence_name": "Monthly Office Rent", ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "recurrence_name": "Monthly Rental",
    "start_date": "2013-11-18",
    "end_date": "2013-12-18",
    "source_of_supply": "AP",
    "place_of_supply": "DU",
    "destination_of_supply": "TN",
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "tax_treatment": "vat_registered",
    "vat_treatment": "string",
    "vat_reg_no": "string",
    "is_abn_quoted": "string",
    "abn": "string",
    "is_reverse_charge_applied": true,
    "pricebook_id": 460000000038090,
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details ... */ } ],
    "is_tds_applied": true,
    "notes": "Thanks for your business.",
    "terms": "Terms and conditions apply.",
    "payment_terms": 0,
    "payment_terms_label": "Due on Receipt",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "discount": "30%",
    "discount_account_id": "460000000000403",
    "is_discount_before_tax": true,
    "repeat_every": 1, /* Example value */
    "recurrence_frequency": "months" /* Example value */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring Bill has been created.", /* Updated message */
    "recurring_bill": {
        "recurring_bill_id": 982000000567240,
        /* ... full recurring bill details ... */
    }
}
```

## Delete a Recurring Bill

### Description
Delete an existing recurring bill.

### Endpoint
`DELETE /recurringbills/{recurring_bill_id}` *(Note: Path corrected from original `/recurring_bills/`)*

### OAuth Scope
`ZohoBooks.bills.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring bill has been deleted."
}
```

## Get a Recurring Bill

### Description
Get the details of a recurring bill.

### Endpoint
`GET /recurringbills/{recurring_bill_id}` *(Note: Path corrected from original `/recurring_bills/`)*

### OAuth Scope
`ZohoBooks.bills.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "recurring_bill": {
        "recurring_bill_id": 982000000567240,
        /* ... full recurring bill details ... */
    }
}
```

## List Child Expenses Created

### Description
List child bills generated from recurring bill profile. *(Note: Endpoint name and path seem incorrect in original docs; likely lists Bills not Expenses)*.

### Endpoint
`GET /recurringexpenses/{recurring_expense_id}/expenses` *(Note: Path uses `recurringexpenses`, likely should be `/recurringbills/{recurring_bill_id}/bills` or similar. Also parameter name `{recurring_expense_id}` is likely `{recurring_bill_id}`)*

### OAuth Scope
`ZohoBooks.bills.READ` *(Note: Corrected from original `ZohoBooks.expenses.READ`)*

### Query Parameters
*   **sort_column** (string): Sort results. Allowed Values: `next_expense_date`, `account_name`, `total`, `last_created_date`, `recurrence_name`, `customer_name`, `created_time`. *(Note: Some sort columns might not apply to Bills)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringexpenses/982000000567240/expenses?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bills": [ /* Corrected key from "expensehistory" */
        {
            "bill_id": 982000000567250, /* Corrected key from "expense_id" */
            "bill_number": "BILL-001", /* Example: Added bill number */
            "date": "2013-11-18", /* Date bill was generated */
            "vendor_name": "Vendor Name", /* Example: Added vendor name */
            "total": 128.25,
            "status": "open", /* Status of generated bill */
            "due_date": "2013-12-18" /* Example: Added due date */
            /* Other relevant bill fields */
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected structure from array to object */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "GeneratedBills", /* Example report name */
        "sort_column": "date",
        "sort_order": "D" /* Example sort order */
    }
}
```

## List Recurring Bill History (Comments)

### Description
Get history and comments of a recurring bill.

### Endpoint
`GET /recurringbills/{recurring_bill_id}/comments`

### OAuth Scope
`ZohoBooks.bills.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [ /* Added expected structure */
        {
            "comment_id": "...",
            "recurring_bill_id": "982000000567240",
            "description": "Recurring Bill created",
            "commented_by_id": "...",
            "commented_by": "User Name",
            "comment_type": "system",
            "date": "2013-11-18",
            "date_description": "1 year ago",
            "time": "10:00 AM",
            "operation_type": "Added",
            "transaction_id": null,
            "transaction_type": null
        },
        {
            "comment_id": "...",
            "recurring_bill_id": "982000000567240",
            "description": "Bill #BILL-001 was created",
            "commented_by_id": null, /* System events might not have a user ID */
            "commented_by": "System",
            "comment_type": "system",
            "date": "2013-11-18",
            "date_description": "1 year ago",
            "time": "10:01 AM",
            "operation_type": "ChildCreated", /* Example operation */
            "transaction_id": "982000000567250", /* ID of the generated bill */
            "transaction_type": "bill"
        },
        {...}
    ]
}
```

## Update a Recurring Bill

### Description
Update a recurring bill. To delete a line item just remove it from the `line_items` list.

### Endpoint
`PUT /recurringbills/{recurring_bill_id}`

### OAuth Scope
`ZohoBooks.bills.UPDATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **status** (string): Status (`active`, `stopped`, `expired`).
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - VAT Reg number.
*   **is_abn_quoted** (string): 🇦🇺 only - ABN quoted status.
*   **abn** (string): 🇦🇺 only - ABN number.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Apply reverse charge.
*   **pricebook_id** (string): Price book ID.
*   **pricebook_name** (string): Price book name.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - TDS applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **payment_terms** (integer): Payment terms days.
*   **payment_terms_label** (string): Payment terms label.
*   **custom_fields** (array): Custom fields.
*   **discount** (string): Discount (e.g., "12.5%" or "190").
*   **discount_account_id** (string): Discount account ID.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **recurrence_frequency** (string, Required): Frequency.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "recurrence_name": "Updated Rental Name", ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "status": "active",
    "recurrence_name": "Monthly Rental",
    "start_date": "2013-11-18",
    "end_date": "2013-12-18",
    /* ... other fields to update ... */
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    /* ... */
    "repeat_every": 1, /* Example value */
    "recurrence_frequency": "months" /* Example value */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring Bill information has been updated."
    /* Typically includes the updated recurring_bill object */
}
```

## Stop a Recurring Bill

### Description
Stop an active recurring bill.

### Endpoint
`POST /recurringbills/{recurring_bill_id}/status/stop`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240/status/stop?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring bill has been stopped."
}
```

## Resume a Recurring Bill

### Description
Resume a stopped recurring bill.

### Endpoint
`POST /recurringbills/{recurring_bill_id}/status/resume`

### OAuth Scope
`ZohoBooks.bills.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/recurringbills/982000000567240/status/resume?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The recurring bill has been activated."
}
```

## List Recurring Bills

### Description
List all recurring bills with pagination.

### Endpoint
`GET /recurringbills`

### OAuth Scope
`ZohoBooks.bills.READ`

### Query Parameters
*   **recurring_bill_id** (string): Filter by specific ID.
*   **vendor_id** (string): Filter by Vendor ID.
*   **vendor_name** (string): Search by vendor name (variants: `_startswith`, `_contains`).
*   **status** (string): Filter by status (`active`, `stopped`, `expired`).
*   **recurrence_name** (string): Search by recurrence name (variants: `_startswith`, `_contains`).
*   **currency_id** (string): Filter by Currency ID.
*   **currency_code** (string): Filter by Currency Code.
*   **currency_symbol** (string): Filter by Currency Symbol.
*   **start_date** (string): Search by start date (variants: `_start`, `_end`, `_before`, `_after`).
*   **end_date** (string): Search by end date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Filter by source of supply.
*   **place_of_supply** (string): GCC only - Filter by place of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Filter by destination of supply.
*   **gst_treatment** (string): 🇮🇳 only - Filter by GST treatment.
*   **gst_no** (string): 🇮🇳 only - Filter by vendor GST number.
*   **tax_treatment** (string): GCC , 🇲🇽 only - Filter by VAT treatment.
*   **vat_treatment** (string): 🇬🇧 only - Filter by VAT treatment.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - Filter by VAT number.
*   **is_abn_quoted** (string): 🇦🇺 only - Filter by ABN quoted status.
*   **abn** (string): 🇦🇺 only - Filter by ABN number.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Filter by reverse charge status.
*   **pricebook_id** (string): Filter by Price book ID.
*   **pricebook_name** (string): Filter by Price book name.
*   **is_inclusive_tax** (boolean): Filter by inclusive tax setting.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - Filter by TDS status.
*   **notes** (string): Search by notes.
*   **terms** (string): Search by terms.
*   **payment_terms** (integer): Filter by payment terms days.
*   **payment_terms_label** (string): Filter by payment terms label.
*   **acquisition_vat_total** (double): 🇬🇧 , Europe only - Filter by total Acquisition VAT.
*   **reverse_charge_vat_total** (double): 🇬🇧 , Europe only - Filter by total Reverse Charge VAT.
*   **created_time** (string): Filter by creation time.
*   **created_by_id** (string): Filter by creator user ID.
*   **last_modified_time** (string): Filter by last modified time.
*   **discount** (string): Filter by discount value.
*   **discount_account_id** (string): Filter by discount account ID.
*   **is_discount_before_tax** (boolean): Filter by discount timing.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/recurringbills?organization_id=10234695&status=active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "recurringbills": [
        {
            "recurring_bill_id": 982000000567240,
            "vendor_id": "460000000038029",
            "vendor_name": "string",
            "status": "active",
            "recurrence_name": "Monthly Rental",
            "start_date": "2013-11-18",
            "end_date": "2013-12-18",
            "last_sent_date": "", /* Date last bill was generated */
            "next_invoice_date": "2013-11-18", /* Date next bill will be generated */
            "total": 128.25, /* Total amount of the recurring profile */
            "currency_code": "INR"
            /* ... other recurring bill summary fields ... */
        },
        {...},
        {...}
    ],
    "page_context": { /* Added expected page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "RecurringBills",
        "applied_filter": "Status.Active",
        "sort_column": "created_time",
        "sort_order": "A"
    }
}
```

## Update Recurring Bill using Custom Field

### Description
Update a recurring bill using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /recurringbills` *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs. Typical update uses ID in path)*.

### OAuth Scope
`ZohoBooks.bills.UPDATE` *(Note: Corrected from original `ZohoBooks.settings.UPDATE`)*

### Headers *(Assumed based on description)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **status** (string): Status (`active`, `stopped`, `expired`).
*   **recurrence_name** (string, Required): Name. Max-length [100].
*   **start_date** (string, Required): Start date. Format [yyyy-mm-dd].
*   **end_date** (string): End date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **vat_reg_no** (string): 🇬🇧 , Avalara Integration only - VAT Reg number.
*   **is_abn_quoted** (string): 🇦🇺 only - ABN quoted status.
*   **abn** (string): 🇦🇺 only - ABN number.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Apply reverse charge.
*   **pricebook_id** (string): Price book ID.
*   **pricebook_name** (string): Price book name.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **is_tds_applied** (boolean): 🇮🇳 , 🌎 , 🇦🇺 only - TDS applied.
*   **notes** (string): Notes.
*   **terms** (string): Terms.
*   **payment_terms** (integer): Payment terms days.
*   **payment_terms_label** (string): Payment terms label.
*   **custom_fields** (array): Custom fields.
*   **discount** (string): Discount (e.g., "12.5%" or "190").
*   **discount_account_id** (string): Discount account ID.
*   **is_discount_before_tax** (boolean): Apply discount before tax.
*   **repeat_every** (integer, Required): Interval *(Note: Original doc type was string)*.
*   **recurrence_frequency** (string, Required): Frequency.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/recurringbills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000038029", "recurrence_name": "Updated Rental", ...}'
```

#### Body Parameters
```json
{
    /* recurring_bill_id likely not needed when using unique headers */
    "vendor_id": "460000000038029",
    "currency_id": "460000000000099",
    "status": "active",
    "recurrence_name": "Monthly Rental",
    "start_date": "2013-11-18",
    "end_date": "2013-12-18",
    /* ... other fields to update ... */
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    /* ... */
    "repeat_every": 1, /* Example value */
    "recurrence_frequency": "months" /* Example value */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Recurring Bill information has been updated."
    /* Typically includes the updated or created recurring_bill object */
}
```
# Vendor Credits

## Overview

### Vendor Credits
Vendor credits are credits that you receive from your vendor, and is treated as an equivalent of physical cash that the vendor owes you. This helps you track the money you’re owed until it is either paid by said vendor at a later date i.e refunded, or subtracted from any future bill amount due to that vendor.

### End Points
*   `POST /vendorcredits`
*   `GET /vendorcredits`
*   `PUT /vendorcredits/{vendor_credit_id}`
*   `GET /vendorcredits/{vendor_credit_id}`
*   `DELETE /vendorcredits/{vendor_credit_id}`
*   `POST /vendorcredits/{vendor_credit_id}/email`
*   `GET /vendorcredits/{vendor_credit_id}/email`
*   `POST /vendorcredits/{vendor_credit_id}/status/void`
*   `POST /vendorcredits/{vendor_credit_id}/status/draft` *(Note: Not explicitly listed in files, but implied by GET status filter)*
*   `POST /vendorcredits/{vendor_credit_id}/status/open`
*   `POST /vendorcredits/{vendor_credit_id}/submit`
*   `POST /vendorcredits/{vendor_credit_id}/approve`
*   `GET /vendorcredits/{vendor_credit_id}/emailhistory`
*   `PUT /vendorcredits/{vendor_credit_id}/address/billing`
*   `PUT /vendorcredits/{vendor_credit_id}/address/shipping` *(Note: Endpoint not explicitly listed in provided text, but commonly associated)*
*   `GET /vendorcredits/templates`
*   `PUT /vendorcredits/{vendor_credit_id}/templates/{template_id}`
*   `POST /vendorcredits/{vendor_credit_id}/bills`
*   `GET /vendorcredits/{vendor_credit_id}/bills`
*   `DELETE /vendorcredits/{vendor_credit_id}/bills/{vendor_credit_bill_id}`
*   `POST /vendorcredits/{vendor_credit_id}/comments`
*   `GET /vendorcredits/{vendor_credit_id}/comments`
*   `DELETE /vendorcredits/{vendor_credit_id}/comments/{comment_id}`
*   `GET /vendorcredits/refunds`
*   `POST /vendorcredits/{vendor_credit_id}/refunds`
*   `GET /vendorcredits/{vendor_credit_id}/refunds`
*   `PUT /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`
*   `GET /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`
*   `DELETE /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`
*   *(Note: Some endpoints listed in the original Overview.md, like `PUT /vendorcredits` without ID and `PUT /bill/{bill_id}/customfields`, seemed misplaced and were likely typos/copy-paste errors from other sections)*

### Attributes
*   **vendor_credit_id** (string): Unique ID of the vendor credit.
*   **vendor_credit_number** (string): Unique number (starts with CN/DN?). Max-Length [100].
*   **date** (string): Creation date. Format [yyyy-mm-dd].
*   **source_of_supply** (string): 🇮🇳 only - Place from where goods/services are supplied.
*   **destination_of_supply** (string): 🇮🇳 only - Place where goods/services are supplied to.
*   **place_of_supply** (string): GCC only - Place of supply for VAT (Supported codes listed).
*   **gst_no** (string): 🇮🇳 only - Vendor's 15 digit GST number.
*   **gst_treatment** (string): 🇮🇳 only - Vendor's GST status (business_gst, business_none, overseas, consumer).
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **pricebook_id** (string): Price book ID.
*   **is_reverse_charge_applied** (boolean): 🇮🇳 only - Applicable for reverse charge transactions.
*   **status** (string): Status (open, closed, void, draft).
*   **reference_number** (string): Reference number. Max-Length [100].
*   **vendor_id** (string): Vendor ID.
*   **vendor_name** (string): Vendor name. Max-Length [100].
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **exchange_rate** (double): Exchange rate.
*   **price_precision** (integer): Price precision.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (uk, eu_vat_registered, overseas).
*   **filed_in_vat_return_id** (string): 🇬🇧 only - ID of filed VAT Return.
*   **filed_in_vat_return_name** (string): 🇬🇧 only - Name of filed VAT Return.
*   **filed_in_vat_return_type** (string): 🇬🇧 only - Type of filed VAT Return.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **location_name**: Name of the location.
*   **line_items** (array): Line items.
*   **acquisition_vat_summary** (array): 🇬🇧 , Europe only - Acquisition VAT summary.
*   **acquisition_vat_total** (double): 🇬🇧 , Europe only - Total Acquisition VAT.
*   **reverse_charge_vat_summary** (array): 🇬🇧 , Europe only - Reverse Charge VAT summary.
*   **reverse_charge_vat_total** (double): 🇬🇧 , Europe only - Total Reverse Charge VAT.
*   **documents** (array): Attached documents.
*   **custom_fields** (array): Custom fields.
*   **sub_total** (double): Sub total.
*   **total** (double): Total amount.
*   **total_credits_used** (double): Amount applied to bills.
*   **total_refunded_amount** (double): Amount refunded.
*   **balance** (double): Remaining unapplied/unrefunded amount.
*   **notes** (string): Notes. Max-length [5000].
*   **comments** (array): Comments and history.
*   **vendor_credit_refunds** (array): Refunds made from this credit.
*   **bills_credited** (array): Bills this credit has been applied to.
*   **created_time** (string): Creation time.
*   **last_modified_time** (string): Last modified time.
*   *(Note: Several attributes listed in the original overview (e.g., email, billing/shipping address, template details) seem more related to the vendor/contact rather than the credit note itself, though they might be returned for context).*

### Example
```json
{
    "vendor_credit_id": "3000000002075",
    "vendor_credit_number": "DN-00002",
    "date": "2014-08-28",
    "source_of_supply": "TN",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "pricebook_id": "string",
    "is_reverse_charge_applied": true,
    "status": "open",
    "reference_number": "string",
    "vendor_id": "460000000020029",
    "vendor_name": "Bowman and Co",
    "currency_id": "3000000000083",
    "currency_code": "USD",
    "exchange_rate": 1,
    "price_precision": 2,
    "vat_treatment": "string",
    "filed_in_vat_return_id": "string",
    "filed_in_vat_return_name": "string",
    "filed_in_vat_return_type": "string",
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "location_name": null,
    "line_items": [ /* Example showed object, should be array */
        { /* ... line item details ... */ }
    ],
    "acquisition_vat_summary": [ { /* ... summary ... */ } ],
    "acquisition_vat_total": 0.1,
    "reverse_charge_vat_summary": [ { /* ... summary ... */ } ],
    "reverse_charge_vat_total": 0.1,
    "documents": [ { /* ... document details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "sub_total": 30,
    "total": 30,
    "total_credits_used": 0,
    "total_refunded_amount": 0,
    "balance": 30,
    "notes": "string",
    "comments": [ { /* ... comment details ... */ } ],
    "vendor_credit_refunds": [ { /* ... refund details ... */ } ],
    "bills_credited": [ { /* ... bill credit details ... */ } ],
    "created_time": "2014-08-28T22:53:31-0700",
    "last_modified_time": "2014-08-28T22:53:31-0700"
}
```

## Create a Vendor Credit

### Description
Create a vendor credit for a vendor.

### Endpoint
`POST /vendorcredits`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **vendor_credit_number** (string): Mandatory if auto-gen disabled.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **pricebook_id** (string): Price book ID.
*   **reference_number** (string): Reference number.
*   **is_update_customer** (boolean): Update vendor details *(Note: Parameter name `_customer` inconsistent)*.
*   **date** (string, Required): Creation date. [yyyy-mm-dd].
*   **exchange_rate** (double): Exchange rate.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   Include item_id/account_id, name, rate, quantity, tax_id etc.
*   **notes** (string): Notes. Max-length [5000].
*   **documents** (array): Documents to attach.
*   **custom_fields** (array): Custom fields.

### Query Parameters
*   **ignore_auto_number_generation** (boolean): Ignore auto-generation.
*   **bill_id** (string): Bill ID to associate immediately.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000020029", "date": "2014-08-28", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000020029",
    "currency_id": "3000000000083",
    "vat_treatment": "string",
    "vendor_credit_number": "DN-00002",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "TN",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": "string",
    "reference_number": "string",
    "is_update_customer": false,
    "date": "2014-08-28",
    "exchange_rate": 1,
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details ... */ } ],
    "notes": "string",
    "documents": [ { /* ... document details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Vendor credit has been created.",
    "vendor_credit": {
        "vendor_credit_id": "3000000002075",
        "status": "open", /* Initial status */
        /* ... full vendor credit details ... */
    }
}
```

## List Vendor Credits

### Description
List all the Vendor Credits.

### Endpoint
`GET /vendorcredits`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Query Parameters
*   **vendor_credit_number** (string): Search by number (variants: `_startswith`, `_contains`).
*   **date** (string): Search by date (variants: `_start`, `_end`, `_before`, `_after`). Format [yyyy-mm-dd].
*   **status** (string): Search by status. Allowed: `open`, `closed`, `void`, `draft`.
*   **total** (double): Search by total amount (variants apply).
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`).
*   **customer_name** (string): Search by vendor name *(Note: Parameter name `customer_` mismatch)* (variants: `_startswith`, `_contains`).
*   **item_name** (string): Search by item name (variants: `_startswith`, `_contains`). Max-length [100].
*   **item_description** (string): Search by item description (variants: `_startswith`, `_contains`). Max-length [100].
*   **item_id** (string): Filter by Item ID.
*   **notes** (string): Search by notes (variants: `_startswith`, `_contains`).
*   **custom_field** (string): Search by custom field (variants: `_startswith`, `_contains`).
*   **last_modified_time** (string): Filter by last modified time.
*   **customer_id** (string): Filter by Vendor ID *(Note: Parameter name `customer_` mismatch)*.
*   **line_item_id** (string): Filter by line item ID.
*   **tax_id** (string): Filter by tax ID.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Open`, `Status.Draft`, `Status.Closed`, `Status.Void`.
*   **search_text** (string): Search by number, vendor name, or reference number. Max-length [100].
*   **sort_column** (string): Sort results. Allowed Values: `vendor_name`, `vendorcredit_number`, `balance`, `total`, `date`, `created_time`, `last_modified_time`, `reference_number`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits?organization_id=10234695&status=open' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendorcredits": [
        {
            "vendor_credit_id": "3000000002075",
            "vendor_credit_number": "DN-00002",
            "status": "open",
            "reference_number": "string",
            "date": "2014-08-28",
            "total": 30,
            "balance": 30,
            "vendor_id": "460000000020029",
            "vendor_name": "Bowman and Co",
            "currency_id": "3000000000083",
            "currency_code": "USD",
            "created_time": "2014-08-28T22:53:31-0700",
            "last_modified_time": "2014-08-28T22:53:31-0700",
            "has_attachment": false,
            "exchange_rate": 1
        }
        /* Likely contains multiple vendor credit summaries */
    ]
     /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Get Vendor Credit

### Description
Get details of an existing vendor credit.

### Endpoint
`GET /vendorcredits/{vendor_credit_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Query Parameters
*   **print** (boolean/string): Export pdf with default print option. Allowed Values: `true`, `false`, `on`, `off`.
*   **accept** (string): Response format. Allowed values: `json`, `xml`, `csv`, `xls`, `pdf`, `html`, `jhtml`. Default: `json`. *(Original default 'html' conflicts with API behavior/example)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendor_credit": {
        "vendor_credit_id": "3000000002075"
        /* ... full vendor credit details ... */
    }
}
```

## Update a Vendor Credit

### Description
Update an existing vendor credit.

### Endpoint
`PUT /vendorcredits/{vendor_credit_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.UPDATE` *(Original scope ZohoBooks.debitnotes.UPDATE seems incorrect)*

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **vendor_credit_number** (string): Mandatory if auto-gen disabled.
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **source_of_supply** (string): 🇮🇳 only - Source of supply.
*   **destination_of_supply** (string): 🇮🇳 only - Destination of supply.
*   **place_of_supply** (string): GCC only - Place of supply.
*   **pricebook_id** (string): Price book ID.
*   **reference_number** (string): Reference number.
*   **is_update_customer** (boolean): Update vendor details.
*   **date** (string, Required): Creation date. [yyyy-mm-dd].
*   **exchange_rate** (double): Exchange rate.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **notes** (string): Notes. Max-length [5000].
*   **documents** (array): Documents to attach.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000020029", "date": "2014-08-28", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000020029",
    "currency_id": "3000000000083",
    "vat_treatment": "string",
    "vendor_credit_number": "DN-00002",
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "gst_no": "22AAAAA0000A1Z5",
    "source_of_supply": "TN",
    "destination_of_supply": "TN",
    "place_of_supply": "DU",
    "pricebook_id": "string",
    "reference_number": "string",
    "is_update_customer": false,
    "date": "2014-08-28",
    "exchange_rate": 1,
    "is_inclusive_tax": false,
    "location_id": "460000000038080",
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "notes": "string",
    "documents": [ { /* ... document details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Vendor credit information has been updated.",
    "vendor_credit": {
        "vendor_credit_id": "3000000002075"
        /* ... updated vendor credit details ... */
    }
}
```

## Update Vendor Credit using Custom Field

### Description
Update a vendor credit using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found. *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs. The endpoint itself might need to be `/vendorcredits/{id}`)*.

### Endpoint
`PUT /vendorcredits` *(Note: Endpoint in example; typically PUT for update uses ID like `/vendorcredits/{id}`. This endpoint might work specifically with the custom headers.)*

### OAuth Scope
`ZohoBooks.vendorcredits.UPDATE` *(Original scope ZohoBooks.invoices.UPDATE seems incorrect)*

### Headers
*(Assumed based on description, not shown in example)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **contact_persons** (array): Contact Person IDs.
*   **date** (string, Required): Date credit note is raised. Format [yyyy-mm-dd].
*   **is_draft** (boolean): Set true to keep/change to draft status.
*   **exchange_rate** (double): Exchange rate *(Note: Original data type 'string' incorrect)*.
*   **line_items** (array, Required): Line items.
    *   **line_item_id** (string): Mandatory if updating existing line item. Omit for new. Remove from array to delete.
    *   Include other relevant line item attributes.
*   **location_id** (string): Location ID.
*   **vendor_credit_number** (string, Required): Vendor credit number *(Note: Original parameter name `creditnote_number` mismatch)*. Max-Length [100].
*   **gst_treatment** (string): 🇮🇳 only - Vendor GST status.
*   **tax_treatment** (string): GCC , 🇲🇽 , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only.
*   **gst_no** (string): 🇮🇳 only - Vendor GST number.
*   **cfdi_usage** (string): 🇲🇽 only - CFDI Usage.
*   **cfdi_reference_type** (string): 🇲🇽 only - CFDI Reference Type.
*   **place_of_supply** (string): 🇮🇳 , GCC only - Place of supply.
*   **ignore_auto_number_generation** (boolean): Set true to provide your own number.
*   **reference_number** (string): Reference number. Max-Length [100].
*   **custom_fields** (array): Custom fields.
*   **notes** (string): Notes. Max-length [5000].
*   **terms** (string): Terms. Max-length [10000].
*   **template_id** (string): Template ID.
*   **tax_id** (string): Overall tax ID.
*   **tax_authority_id** (string): 🇺🇸 only - Tax authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax exemption ID.
*   **avatax_use_code** (string): Avalara Integration only - Use code. Max-length [25].
*   **avatax_exempt_no** (string): Avalara Integration only - Exemption number. Max-length [25].
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **is_inclusive_tax** (boolean): Not applicable 🇺🇸 - Line items inclusive of tax.
*   *(Note: Redundant fields listed in original body parameters (item_id, account_id, name, avatax_tax_code, description, unit, rate, quantity) belong within the `line_items` array and are omitted here).*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "903000000000099", "date": "2016-06-05", ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "903000000000099", /* Original parameter name customer_id mismatch */
    "currency_id": "982000000567240",
    "contact_persons": [ "903000006532" ],
    "date": "2016-06-05",
    "is_draft": true,
    "exchange_rate": 5.5, /* Original example value "5.5" suggests double */
    "line_items": [ { /* ... line item details with line_item_id ... */ } ],
    "location_id": "460000000038080",
    "vendor_credit_number": "CN-29", /* Original parameter name creditnote_number mismatch */
    "gst_treatment": "business_gst",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "place_of_supply": "TN",
    "ignore_auto_number_generation": false,
    "reference_number": "INV-384",
    "custom_fields": [ { /* ... Needs proper structure, example had "string" ... */ } ],
    "notes": "Offer for the referral",
    "terms": "",
    "template_id": "90300000001336",
    "tax_id": "903000000000356",
    "tax_authority_id": "903000006345",
    "tax_exemption_id": "903000006345",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "vat_treatment": "overseas",
    "is_inclusive_tax": false /* Original example had typo 'fasle' */
    /* Redundant fields from original example omitted */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The vendor credit has been updated.", /* Original message said credit note */
    "vendor_credit": { /* Original object name creditnote */
        "vendor_credit_id": "90300000072369", /* Original ID name creditnote_id */
        /* ... updated vendor credit details ... */
    }
}
```

## Delete Vendor Credit

### Description
Delete a vendor credit.

### Endpoint
`DELETE /vendorcredits/{vendor_credit_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.DELETE` *(Original scope ZohoBooks.debitnotes.DELETE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The vendor credit has been deleted."
}
```

## Apply Vendor Credit to Bills

### Description
Apply vendor credit to existing bills.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/bills`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Arguments (Body Parameters)
*   **bills** (array, Required): List of bills to apply credits to.
    *   **bill_id** (string): ID of the bill.
    *   **amount_applied** (double): Amount to apply to this bill.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/bills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"bills": [{"bill_id": "460000000057075", "amount_applied": 10.0}]}'
```

#### Body Parameters
```json
{
    "bills": [
        {
            "bill_id": "460000000057075",
            "amount_applied": 10
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits have been applied to the bill(s)."
    /* Original example shows "bills": null, but might return details of applied credits */
}
```

## List Bills Created

### Description
List bills to which the vendor credit is applied.

### Endpoint
`GET /vendorcredits/{vendor_credit_id}/bills`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/bills?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bills_credited": [
        {
            "vendor_credit_id": "3000000002075",
            "bill_id": "460000000057075",
            "vendor_credit_bill_id": "string", /* ID mapping this application */
            "date": "2014-08-28",
            "bill_number": "string",
             "amount": 13 /* Amount applied */
        },
        {...},
        {...}
    ]
}
```

## Delete Bills Credited

### Description
Delete the credits applied to a bill from this vendor credit.

### Endpoint
`DELETE /vendorcredits/{vendor_credit_id}/bills/{vendor_credit_bill_id}`
*Note: `{vendor_credit_bill_id}` is the ID mapping the credit application (from List Bills Credited), not the bill ID itself.*

### OAuth Scope
`ZohoBooks.vendorcredits.DELETE` *(Original scope ZohoBooks.debitnotes.DELETE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/bills/VENDOR_CREDIT_BILL_ID_HERE?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Credits applied to the bill have been deleted."
}
```

## Refund a Vendor Credit

### Description
Refund vendor credit amount.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/refunds`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Arguments (Body Parameters)
*   **date** (string, Required): Date of refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Mode of refund (e.g., cash, check).
*   **reference_number** (string): Reference number.
*   **amount** (double, Required): Amount refunded.
*   **exchange_rate** (double): Exchange rate.
*   **account_id** (string, Required): ID of the account from which refund is made.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2014-08-30", "amount": 13.0, "account_id": "...", ...}'
```

#### Body Parameters
```json
{
    "date": "2014-08-30",
    "refund_mode": "cash",
    "reference_number": "string",
    "amount": 13,
    "exchange_rate": 1,
    "account_id": "460000000020097",
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information for this vendor credit has been saved.",
    "vendor_credit_refund": {
        "vendor_credit_refund_id": "3000000003151",
        "vendor_credit_id": "3000000002075"
        /* ... refund details ... */
    }
}
```

## List Vendor Credit Refunds (All)

### Description
List all vendor credit refunds with pagination.

### Endpoint
`GET /vendorcredits/refunds`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Query Parameters
*   **customer_id** (string): Filter refunds by Vendor ID *(Note: Parameter name `customer_` mismatch)*.
*   **last_modified_time** (string): Filter by last modified time.
*   **sort_column** (string): Sort results. Allowed Values: `vendor_name`, `vendorcredit_number`, `balance`, `total`, `date`, `created_time`, `last_modified_time`, `reference_number`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/refunds?organization_id=10234695&sort_column=date' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendor_credit_refunds": [
        {
            "vendor_credit_refund_id": "3000000003151",
            "vendor_credit_id": "3000000002075",
            "date": "2017-01-22",
            "refund_mode": "cash",
            "reference_number": "string",
            "amount": 13,
            "vendor_credit_number": "DN-00002",
            "customer_name": "Bowman and Co", /* Vendor name */
            "description": "Cheque deposit",
            "amount_bcy": 13,
            "amount_fcy": 13
        },
        {...},
        {...}
    ]
     /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## List Refunds of a Vendor Credit

### Description
List all refunds of an existing vendor credit.

### Endpoint
`GET /vendorcredits/{vendor_credit_id}/refunds`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendor_credit_refunds": [
        {
            "vendor_credit_refund_id": "3000000003151",
            "vendor_credit_id": "3000000002075",
            "date": "2017-01-22",
            "refund_mode": "cash",
            "reference_number": "string",
            "amount": 13,
            "vendor_credit_number": "DN-00002",
            "customer_name": "Bowman and Co", /* Vendor name */
            "description": "Cheque deposit",
            "amount_bcy": 13,
            "amount_fcy": 13
        },
        {...},
        {...}
    ]
    /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Get Vendor Credit Refund

### Description
Get refund details of a particular vendor credit refund.

### Endpoint
`GET /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/refunds/3000000003151?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendor_credit_refund": {
        "vendor_credit_refund_id": "3000000003151"
        /* ... full refund details ... */
    }
}
```

## Update Vendor Credit Refund

### Description
Update the refunded transaction.

### Endpoint
`PUT /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.UPDATE` *(Original scope ZohoBooks.debitnotes.UPDATE seems incorrect)*

### Arguments (Body Parameters)
*   **date** (string, Required): Refund date. Format [yyyy-mm-dd].
*   **refund_mode** (string): Mode of refund.
*   **reference_number** (string): Reference number.
*   **amount** (double, Required): Refund amount.
*   **exchange_rate** (double): Exchange rate.
*   **account_id** (string, Required): Account ID from which refund was made.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/refunds/3000000003151?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2014-08-29", "amount": 13.00, ...}'
```

#### Body Parameters
```json
{
    "date": "2014-08-28",
    "refund_mode": "cash",
    "reference_number": "string",
    "amount": 13,
    "exchange_rate": 1,
    "account_id": "460000000020097",
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information has been saved.", /* Message implies save, not update */
    "vendor_credit_refund": {
        "vendor_credit_refund_id": "3000000003151"
        /* ... updated refund details ... */
    }
}
```

## Delete Vendor Credit Refund

### Description
Delete a vendor credit refund transaction.

### Endpoint
`DELETE /vendorcredits/{vendor_credit_id}/refunds/{vendor_credit_refund_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.DELETE` *(Original scope ZohoBooks.debitnotes.DELETE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/refunds/3000000003151?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund has been successfully deleted."
}
```

## Add Comment to Vendor Credit

### Description
Add a comment to an existing vendor credit.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/comments`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Arguments (Body Parameters)
*   **description** (string, Required): The comment text.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Comment text here"}'
```

#### Body Parameters
```json
{
    "description": "Credits applied to Bill 1"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": {
        "comment_id": "3000000002089",
        "vendor_credit_id": "3000000002075",
        "description": "Credits applied to Bill 1",
        "commented_by_id": "3000000000741",
        "commented_by": "rajdeep.a",
        "date": "2017-01-18"
        /* Missing time, date_description, type, operation_type etc. from original example */
    }
}
```

## List Vendor Credit Comments and History

### Description
Get history and comments of a vendor credit.

### Endpoint
`GET /vendorcredits/{vendor_credit_id}/comments`

### OAuth Scope
`ZohoBooks.vendorcredits.READ` *(Original scope ZohoBooks.debitnotes.READ seems incorrect)*

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "3000000002089",
            "vendor_credit_id": "3000000002075",
            "description": "Credits applied to Bill 1",
            "commented_by_id": "3000000000741",
            "commented_by": "rajdeep.a",
            "comment_type": "system",
            "date": "2017-01-18",
            "date_description": "32 minutes ago",
            "time": "10:52 PM",
            "operation_type": "Added",
            "transaction_id": "460000000069087",
            "transaction_type": "vendor_credit"
        },
        {...},
        {...}
    ]
}
```

## Delete Vendor Credit Comment

### Description
Delete a vendor credit comment.

### Endpoint
`DELETE /vendorcredits/{vendor_credit_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.vendorcredits.DELETE` *(Original scope ZohoBooks.debitnotes.DELETE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/comments/3000000002089?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Submit Vendor Credit for Approval

### Description
Submit a Vendor credit for approval.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/submit`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The vendor credit has been submitted for approval successfully."
}
```

## Approve Vendor Credit

### Description
Approve a Vendor credit.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/approve`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have approved the vendor credit."
}
```

## Convert Vendor Credit to Open

### Description
Change an existing vendor credit status to open.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/status/open`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/status/open?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The status of the vendor credit has been changed to open."
}
```

## Void Vendor Credit

### Description
Mark an existing vendor credit as void.

### Endpoint
`POST /vendorcredits/{vendor_credit_id}/status/void`

### OAuth Scope
`ZohoBooks.vendorcredits.CREATE` *(Original scope ZohoBooks.debitnotes.CREATE seems incorrect)*

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorcredits/3000000002075/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The vendor credit has been voided."
}
```


# Vendor Payments

## Overview

### Vendor Payments
Payments to Vendors towards Bills.

### End Points
*   `POST /vendorpayments`
*   `GET /vendorpayments`
*   `PUT /vendorpayments/{payment_id}`
*   `GET /vendorpayments/{payment_id}`
*   `DELETE /vendorpayments/{payment_id}`
*   `PUT /vendorpayments` *(Note: For update via custom field, requires specific headers)*
*   `POST /vendorpayments/{payment_id}/refunds`
*   `GET /vendorpayments/{payment_id}/refunds`
*   `PUT /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`
*   `GET /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`
*   `DELETE /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`
*   `PUT /vendorpayments/{payment_id}/customfields`

### Attributes
*   **payment_id** (string): Unique ID of the payment. Max-length [2000].
*   **payment_mode** (string): Mode of payment (check, cash, creditcard, etc.). Max-length [100].
*   **amount** (double): Amount paid.
*   **amount_refunded** (double): Amount refunded (from this payment).
*   **bank_charges** (double): Bank charges.
*   **date** (string): Date payment made. Format [yyyy-mm-dd].
*   **status** (string): Payment status (success or failure).
*   **reference_number** (string): Reference number. Max-length [100].
*   **description** (string): Payment description.
*   **vendor_id** (string): Vendor ID.
*   **vendor_name** (string): Vendor name. Max-length [100].
*   **email** (string): Vendor email.
*   **bills** (array): List of bills associated with the payment *(Note: Original attribute name `invoices` was likely a mismatch)*.
*   **currency_code** (string): Currency code.
*   **currency_symbol** (string): Currency symbol.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **custom_fields** (array): Custom fields.

### Example
```json
{
    "payment_id": "9030000079467",
    "payment_mode": "cash",
    "amount": 450,
    "amount_refunded": 50,
    "bank_charges": 10,
    "date": "2016-06-05",
    "status": "success",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "vendor_id": "903000000000099",  /* Original had customer_id */
    "vendor_name": "Bowman Furniture", /* Original had customer_name */
    "email": "benjamin.george@bowmanfurniture.com",
    "bills": [ /* Original had invoices */
        {
            "bill_id": "90300000079426", /* Original had invoice_id */
            "bill_number": "INV-384", /* Original had invoice_number */
            "date": "2016-06-05",
            "bill_amount": 450, /* Original had invoice_amount */
            "amount_applied": 450,
            "balance_amount": 0
        }
    ],
    "currency_code": "USD",
    "currency_symbol": "$",
    "location_id": "460000000038080",
    "location_name": "string",
    "custom_fields": [
        {
            "index": 1,
            "value": 129890,
            "label": "label",
            "data_type": "text"
        }
    ]
}
```

## Create a Vendor Payment

### Description
Create a payment made to your vendor and you can also apply them to bills either partially or fully.

### Endpoint
`POST /vendorpayments`

### OAuth Scope
`ZohoBooks.vendorpayments.CREATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **bills** (array): List of bills to apply payment to.
    *   **bill_id** (string): ID of the bill.
    *   **amount_applied** (double): Amount to apply to this bill.
    *   **tax_amount_withheld** (double): Amount withheld for tax.
*   **date** (string, Required): Date payment made. Format [yyyy-mm-dd].
*   **exchange_rate** (double, default: 1): Exchange rate if currency differs.
*   **amount** (double, Required): Total amount paid.
*   **paid_through_account_id** (string): ID of the cash/bank account payment is made from.
*   **payment_mode** (string): Mode of payment (check, cash, etc.).
*   **description** (string): Description.
*   **reference_number** (string): Reference number. Max-length [100].
*   **check_details** (array): 🇺🇸 , 🇨🇦 only - Check details. *(Needs proper structure)*
*   **is_paid_via_print_check** (boolean): 🇺🇸 , 🇨🇦 , 🇲🇽 only - Paid via Print Check option.
*   **location_id** (string): Location ID.
*   **custom_fields** (array): Custom fields. *(Needs proper structure)*
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment *(Note: Duplicates payment_mode? Might be specific for MX)*.
*   **bank_charges** (double): Bank charges.
*   **contact_persons** (array): IDs of contact persons for thank you mail *(Note: Usually for customer payments, might be mislabeled)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "460000000026049", "amount": 500, "date": "2013-10-07", "bills": [...] ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000026049",
    "bills": [
        {
            /* "bill_payment_id": "460000000053221", /* Not needed for create */
            "bill_id": "460000000053199",
            "amount_applied": 150,
            "tax_amount_withheld": 0.1
        }
    ],
    "date": "2013-10-07",
    "exchange_rate": 1,
    "amount": 500,
    "paid_through_account_id": "460000000000358",
    "payment_mode": "Stripe",
    "description": "string",
    "reference_number": "REF#912300",
    "check_details": [ /* Needs proper structure if used */ ],
    "is_paid_via_print_check": false,
    "location_id": "460000000038080",
    "custom_fields": [ { "index": 0, "value": "string" } ], /* Needs proper structure */
    "payment_form": "cash", /* MX only */
    "bank_charges": 10,
    "contact_persons": [ "982000000870911", "982000000870915" ] /* If applicable */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment made to the vendor has been recorded.",
    "payment": {
        "payment_id": "9030000079467",
        "balance": 300, /* Remaining unapplied amount */
        /* ... full payment details ... */
    }
}
```

## List Vendor Payments

### Description
List all the payments made to your vendor.

### Endpoint
`GET /vendorpayments`

### OAuth Scope
`ZohoBooks.vendorpayments.READ`

### Query Parameters
*   **vendor_name** (string): Search by vendor name (variants: `_startswith`, `_contains`). Max-len [100].
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`). Max-len [100].
*   **payment_number** (string): Search by Payment Number (variants: `_startswith`, `_contains`).
*   **date** (string): Search by date (variants: `_start`, `_end`, `_before`, `_after`). Format yyyy-mm-dd.
*   **amount** (double): Search by amount (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **payment_mode** (string): Search by payment mode (variants: `_startswith`, `_contains`).
*   **notes** (string): Search by notes *(Note: API attribute is `description`)* (variants: `_startswith`, `_contains`).
*   **vendor_id** (string): Filter by vendor ID.
*   **last_modified_time** (string): Filter by last modified time.
*   **bill_id** (string): Filter by associated Bill ID.
*   **description** (string): Search by description (variants: `_startswith`, `_contains`).
*   **filter_by** (string): Filter by payment mode. Allowed Values: `PaymentMode.All`, `PaymentMode.Check`, ... `PaymentMode.Others`.
*   **search_text** (string): Search by reference number, vendor name, or description. Max-length [100].
*   **sort_column** (string): Sort results. Allowed Values: `vendor_name`, `date`, `reference_number`, `amount`, `balance`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments?organization_id=10234695&payment_mode=cash' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendorpayments": [
        {
            "payment_id": "9030000079467",
            "payment_number": "2",
            "bill_numbers": "INV-384", /* Original had invoice_number */
            "date": "2016-06-05",
            "payment_mode": "cash",
            "amount": 450,
            "bcy_amount": 450,
            "location_id": "460000000038080",
            "location_name": "string"
             /* Other summary fields like vendor_name, balance etc. */
        },
        {...},
        {...}
    ]
    /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Retrieve a Vendor Payment

### Description
Get the details of an existing vendor payment.

### Endpoint
`GET /vendorpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.READ`

### Query Parameters
*   **fetchTaxInfo** (boolean): Check if tax information should be fetched.
*   **fetchstatementlineinfo** (boolean): Check if Statement Line Information should be fetched.
*   **print** (boolean): Check if Vendor Payment must be printed *(Note: Unclear how this applies to JSON response)*.
*   **is_bill_payment_id** (boolean): Check if the ID is Bill Payment ID instead of Vendor Payment ID *(Note: Confusing parameter name/description)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/460000000053219?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "vendorpayment": {
        "payment_id": "460000000053219",
        "bills": [ /* Details of bills this payment is applied to */ ],
        "vendorpayment_refunds": [ /* Details of refunds made from this payment */ ]
        /* ... full payment details ... */
    }
}
```

## Update a Vendor Payment

### Description
Update an existing vendor payment. You can also modify the amount applied to the bills.

### Endpoint
`PUT /vendorpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.UPDATE`

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **bills** (array, Required): List of associated bills.
    *   **bill_payment_id** (string): ID mapping payment to this bill (needed for updates).
    *   **bill_id** (string): Bill ID.
    *   **amount_applied** (double): Amount applied.
    *   **tax_amount_withheld** (double): Tax withheld.
*   **date** (string): Date payment made. Format [yyyy-mm-dd].
*   **exchange_rate** (double, default: 1): Exchange rate.
*   **amount** (double, Required): Total amount paid.
*   **paid_through_account_id** (string): ID of the cash/bank account payment made from.
*   **payment_mode** (string, Required): Mode of payment. Max-length [100].
*   **description** (string): Payment description.
*   **reference_number** (string): Reference number. Max-length [100].
*   **is_paid_via_print_check** (boolean): 🇺🇸 , 🇨🇦 , 🇲🇽 only - Paid via Print Check option.
*   **check_details** (array): 🇺🇸 , 🇨🇦 only - Check details. *(Needs proper structure)*
*   **location_id** (string): Location ID.
*   **custom_fields** (array): Custom fields. *(Needs proper structure)*
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **bank_charges** (double): Bank charges.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "903000000000099", "payment_mode": "Check", ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "903000000000099",
    "payment_mode": "cash",
    "amount": 450,
    "date": "2016-06-05",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "bills": [
        {
            "bill_payment_id": "460000000053221", /* Required for update */
            "bill_id": "90300000079426",
            "amount_applied": 450,
            "tax_amount_withheld": 0 /* Added based on individual params */
        }
    ],
    "exchange_rate": 1,
    "payment_form": "cash",
    "bank_charges": 10,
    "custom_fields": [ { "label": "label", "value": 129890 } ], /* Needs proper structure */
    "location_id": "460000000038080",
    "paid_through_account_id": " ", /* Original had account_id, needs valid ID */
    "is_paid_via_print_check": false,
    "check_details": [ /* Needs proper structure if used */ ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The details of the payment made to the vendor has been updated",
    "payment": {
        "payment_id": "9030000079467"
        /* ... updated payment details ... */
    }
}
```

## Update Vendor Payment using Custom Field

### Description
Update a vendor payment using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found. *(Note: Standard PUT endpoint shown in example, custom headers might be missing from docs. Endpoint typically requires ID)*.

### Endpoint
`PUT /vendorpayments` *(Note: Endpoint in example; typically PUT for update uses ID like `/vendorpayments/{payment_id}`. This endpoint might work specifically with the custom headers.)*

### OAuth Scope
`ZohoBooks.vendorpayments.UPDATE`

### Headers
*(Assumed based on description, not shown in example)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   **vendor_id** (string, Required): Vendor ID.
*   **bills** (array, Required): List of bills associated with the payment.
    *   **bill_payment_id** (string): ID mapping payment to this bill (needed for updates).
    *   **bill_id** (string): Bill ID.
    *   **amount_applied** (double): Amount applied.
    *   **tax_amount_withheld** (double): Tax withheld.
*   **date** (string): Date payment made. Format [yyyy-mm-dd].
*   **exchange_rate** (double, default: 1): Exchange rate.
*   **amount** (double, Required): Total amount paid.
*   **paid_through_account_id** (string): ID of the cash/bank account payment made from.
*   **payment_mode** (string, Required): Mode of payment. Max-length [100].
*   **description** (string): Payment description.
*   **reference_number** (string): Reference number. Max-length [100].
*   **is_paid_via_print_check** (boolean): 🇺🇸 , 🇨🇦 , 🇲🇽 only - Paid via Print Check option.
*   **check_details** (array): 🇺🇸 , 🇨🇦 only - Check details. *(Needs proper structure)*
*   **location_id** (string): Location ID.
*   **custom_fields** (array): Custom fields. *(Needs proper structure)*
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **bank_charges** (double): Bank charges.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "903000000000099", "amount": 450, "bills": [...] ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "903000000000099",
    "payment_mode": "cash",
    "amount": 450,
    "date": "2016-06-05",
    "reference_number": "INV-384",
    "description": "Payment has been added to INV-384",
    "bills": [
        {
            "bill_payment_id": "460000000053221", /* Required for update */
            "bill_id": "90300000079426",
            "amount_applied": 450,
            "tax_amount_withheld": 0 /* Added based on individual params */
        }
    ],
    "exchange_rate": 1,
    "payment_form": "cash",
    "bank_charges": 10,
    "custom_fields": [ { "label": "label", "value": 129890 } ], /* Needs proper structure */
    "location_id": "460000000038080",
    "paid_through_account_id": " ", /* Original had account_id, needs valid ID */
    "is_paid_via_print_check": false,
    "check_details": [ /* Needs proper structure if used */ ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The details of the payment made to the vendor has been updated",
    "vendorpayment": { /* Original response showed array */
            "payment_id": "9030000079467"
            /* ... updated payment details ... */
    }
}
```

## Delete a Vendor Payment

### Description
Delete an existing vendor payment.

### Endpoint
`DELETE /vendorpayments/{payment_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/460000000053219?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The payment has been deleted."
}
```

## Refund an Excess Vendor Payment

### Description
Refund the excess amount paid by the vendor *(Note: Title/description mismatch, should be refund *to* the vendor from an excess payment *made*, or refund of a payment *made* to vendor. This endpoint refunds from a payment *made* to a vendor)*.

### Endpoint
`POST /vendorpayments/{payment_id}/refunds`

### OAuth Scope
`ZohoBooks.vendorpayments.CREATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Date of refund. Format [yyyy-mm-dd].
*   **refund_mode** (string): Method of refund. Max-length [50].
*   **reference_number** (string): Reference number. Max-length [100].
*   **amount** (double, Required): Amount refunded.
*   **exchange_rate** (double, default: 1): Exchange rate if applicable.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **from_account_id** (string, Required): The account *from which* the refund was originally paid (e.g., Bank). *(Note: Parameter name `to_account_id` used in Refund a Vendor Credit endpoint seems more logical for the *receiving* account when refunding credits)*.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2016-06-05", "amount": 50.00, "from_account_id": "..." ...}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "reference_number": "INV-384",
    "amount": 50.00, /* Original example amount 450 likely typo */
    "exchange_rate": 1,
    "payment_form": "cash",
    "from_account_id": " ", /* Needs valid account ID */
    "description": "Refund for overpayment INV-384" /* Original description likely typo */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information for this payment has been saved.",
    "vendorpayment_refunds": [ /* Original response name payment_refunds */
        {
            "vendorpayment_refund_id": "3000000003017", /* Original ID name payment_refund_id */
            "payment_id": "9030000079467",
            "date": "2016-06-05",
            "refund_mode": "cash",
            "reference_number": "INV-384",
            "amount": 50.00, /* Assuming refund amount */
            "exchange_rate": 1,
            "payment_form": "cash",
            "description": "Refund for overpayment INV-384" /* Assuming refund description */
        }
        /* Original response might show multiple if called multiple times? Should be single obj */
    ]
}
```

## List Refunds of a Vendor Payment

### Description
List all the refunds pertaining to an existing vendor payment.

### Endpoint
`GET /vendorpayments/{payment_id}/refunds`

### OAuth Scope
`ZohoBooks.vendorpayments.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success", /* Original message mismatch */
    "vendorpayment_refunds": [ /* Original response name payment_refunds */
        {
            "vendorpayment_refund_id": "3000000003017", /* Original ID name payment_refund_id */
            "payment_id": "9030000079467",
            "date": "2016-06-05",
            "refund_mode": "cash",
            "reference_number": "INV-384",
            "payment_number": "2", /* This seems out of place for a refund */
            "vendor_name": "Bowman Furniture", /* Original had customer_name */
            "amount_bcy": 10,
            "amount_fcy": 10
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Vendor Payments Refund", /* Original name mismatch */
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Details of a Vendor Payment Refund

### Description
Obtain details of a particular refund of a vendor payment.

### Endpoint
`GET /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/refunds/460000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success", /* Original message mismatch */
    "vendorpayment_refund": { /* Original response name/structure payment_refunds[0] */
            "vendorpayment_refund_id": "3000000003017", /* Original ID name payment_refund_id */
            "payment_id": "9030000079467",
            "date": "2013-10-07",
            "refund_mode": "cash",
            "reference_number": "REF#912300",
            "amount": 500,
            "exchange_rate": 1,
            "from_account_id": "460000000000385", /* Original had to_account_id */
            "from_account_name": "Petty Cash", /* Original had to_account_name */
            "description": "string"
        }
}
```

## Update a Vendor Payment Refund

### Description
Update the refunded transaction.

### Endpoint
`PUT /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.UPDATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Refund date. Format [yyyy-mm-dd].
*   **refund_mode** (string): Mode of refund. Max-length [50].
*   **reference_number** (string): Reference number. Max-length [100].
*   **amount** (double, Required): Refund amount.
*   **exchange_rate** (double, default: 1): Exchange rate.
*   **payment_form** (string): 🇲🇽 only - Mode of Vendor Payment.
*   **description** (string): Description.
*   **from_account_id** (string, Required): Account refund was made from.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/refunds/460000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2017-01-11", "amount": 450.00, ...}'
```

#### Body Parameters
```json
{
    "date": "2016-06-05",
    "refund_mode": "cash",
    "reference_number": "INV-384",
    "amount": 450,
    "exchange_rate": 1,
    "payment_form": "cash",
    "description": "Payment has been added to INV-384",
    "from_account_id": " " /* Needs valid account ID */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund information has been saved.", /* Message implies save, not update */
    "vendorpayment_refund": { /* Original response name/structure payment_refunds[0] */
            "vendorpayment_refund_id": "3000000003017", /* Original ID name payment_refund_id */
            "payment_id": "9030000079467"
            /* ... updated refund details ... */
        }
}
```

## Delete a Vendor Payment Refund

### Description
Delete refund pertaining to an existing vendor payment.

### Endpoint
`DELETE /vendorpayments/{payment_id}/refunds/{vendorpayment_refund_id}`

### OAuth Scope
`ZohoBooks.vendorpayments.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/refunds/460000000003017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The refund has been deleted."
}
```

## Update Custom Field in Vendor Payment

### Description
Update the value of the custom field in existing vendor payments.

### Endpoint
`PUT /vendorpayments/{payment_id}/customfields`

### OAuth Scope
`ZohoBooks.vendorpayments.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field.
    *   **value** (string): New value.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/vendorpayments/9030000079467/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "46000000012845", "value": "NewValue"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "46000000012845",
        "value": 129890 /* New Value */
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```

# Bank Accounts

## Overview

### Bank Accounts
In Zoho Books, you can track your transactions, have manual and automatic feeds imported for your bank and credit card accounts.

### End Points
*   `POST /bankaccounts`
*   `GET /bankaccounts`
*   `PUT /bankaccounts/{account_id}`
*   `GET /bankaccounts/{account_id}`
*   `DELETE /bankaccounts/{account_id}`
*   `POST /bankaccounts/{account_id}/inactive`
*   `POST /bankaccounts/{account_id}/active`
*   `POST /bankstatements`
*   `GET /bankaccounts/{account_id}/statement/lastimported`
*   `DELETE /bankaccounts/{account_id}/statement/{statement_id}`

### Attributes
*   **account_id** (string): ID of the Bank/Credit Card account
*   **account_name** (string): Name of the account
*   **account_code** (string): Code of the Account
*   **currency_id** (string): ID of the Currency associated with the Account
*   **currency_code** (string): Code of the currency associated with the Bank Account
*   **currency_symbol** (string): Symbol of the Currency associated with the Account
*   **price_precision** (integer): Precision of the Price Values
*   **account_type** (string): Type of the account (e.g., bank, credit_card)
*   **account_number** (string): Number associated with the Bank Account
*   **uncategorized_transactions** (integer): Number of uncategorized transactions
*   **total_unprinted_checks** (integer): Number of unprinted checks.
*   **is_active** (boolean): Check if Account is Active
*   **is_feeds_subscribed** (boolean): Check if feeds are subscribed
*   **is_feeds_active** (boolean): Check if feeds are active
*   **balance** (double): Balance present in the account (Zoho Books balance)
*   **bank_balance** (integer): Balance present in the Bank (from feeds/statements)
*   **bcy_balance** (double): Balance in Base Currency
*   **bank_name** (string): Name of the Bank
*   **routing_number** (string): Routing Number of the Account
*   **is_primary_account** (boolean): Check if the Account is Primary Account in Zoho Books
*   **is_paypal_account** (boolean): Check if the Account is Paypal Account
*   **description** (string): Description of the Account
*   **refresh_status_code** (string): Refresh Status Code of the Bank feeds
*   **feeds_last_refresh_date** (string): Last Refreshed Date of the Feeds
*   **service_id** (string): Service ID of the Account (related to feeds)
*   **is_system_account** (boolean): Check if the account is a system account
*   **is_show_warning_for_feeds_refresh** (boolean): Check if warning should be shown for refreshing Bank Feeds

### Example
```json
{
    "account_id": "460000000050127",
    "account_name": "Corporate Account",
    "account_code": "string",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "currency_symbol": "$",
    "price_precision": 2,
    "account_type": "bank",
    "account_number": "80000009823",
    "uncategorized_transactions": 0,
    "total_unprinted_checks": 0,
    "is_active": true,
    "is_feeds_subscribed": false,
    "is_feeds_active": false,
    "balance": 0,
    "bank_balance": 0,
    "bcy_balance": 0,
    "bank_name": "Xavier Bank",
    "routing_number": "123456789",
    "is_primary_account": false,
    "is_paypal_account": true,
    "description": "Salary details.",
    "refresh_status_code": "string",
    "feeds_last_refresh_date": "string",
    "service_id": "string",
    "is_system_account": false,
    "is_show_warning_for_feeds_refresh": false
}
```

## Delete Last Imported Statement

### Description
Delete the statement that was previously imported.

### Endpoint
`DELETE /bankaccounts/{account_id}/statement/{statement_id}`

### OAuth Scope
`ZohoBooks.banking.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127/statement/460000000049013?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "You have successfully deleted the last imported statement."
}
```

## Get Last Imported Statement

### Description
Get the details of previously imported statement for the account.

### Endpoint
`GET /bankaccounts/{account_id}/statement/lastimported`

### OAuth Scope
`ZohoBooks.banking.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127/statement/lastimported?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "statement": [ /* Should likely be single object, not array */
        {
            "statement_id": "460000000049013",
            "from_date": "2012-01-12",
            "to_date": "2012-01-19",
            "source": "csv",
            "transactions": [
                {
                    "transaction_id": "460000000049023",
                    "debit_or_credit": "credit",
                    "date": "2012-01-14",
                    "customer_id": "460000000026049",
                    "payee": "Bowman and Co",
                    "reference_number": "Ref-2134",
                    "transaction_type": "expense", /* Type assigned in Zoho Books */
                    "amount": 7500,
                    "status": "categorized" /* Status in Zoho Books */
                }
            ]
        }
        /* Unlikely to have multiple "last imported" */
    ]
}
```
*Note: The original example showed the `statement` key holding an array. It's more likely this would return a single object for the "last imported" statement.*

## Import Bank or Credit Card Statement

### Description
Import your bank/credit card feeds into your account.

### Endpoint
`POST /bankstatements`

### OAuth Scope
(Not specified, likely `ZohoBooks.banking.CREATE` or similar)

### Arguments (Body Parameters)
*   **account_id** (string, Required): ID of the Bank/Credit Card account.
*   **start_date** (string): Least date in the transaction set.
*   **end_date** (string): Greatest date in the transaction set.
*   **transactions** (array, Required): List of transactions.
    *   **transaction_id** (string): Unique ID for the transaction within the statement.
    *   **date** (string): Transaction date.
    *   **debit_or_credit** (string): 'debit' or 'credit'.
    *   **amount** (double): Transaction amount.
    *   **payee** (string): Payee name.
    *   **description** (string): Description.
    *   **reference_number** (string): Reference number.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bankstatements?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken YOUR_OAUTH_TOKEN' \
  --header 'content-type: application/json' \
  --data '{"account_id": "460000000050127", "start_date": "2019-01-01", "end_date": "2019-01-02", "transactions": [...] }'
```

#### Body Parameters
```json
{
    "account_id": "460000000050127",
    "start_date": "2019-01-01",
    "end_date": "2019-01-02",
    "transactions": [
        {
            "transaction_id": "XXXXSCD01",
            "date": "2012-01-14",
            "debit_or_credit": "credit",
            "amount": 7500,
            "payee": "Bowman and Co",
            "description": "Electronics purchase",
            "reference_number": "Ref-2134"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your bank statement has been imported."
}
```

## Activate Account

### Description
Make an account active.

### Endpoint
`POST /bankaccounts/{account_id}/active`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been marked as active."
}
```

## Deactivate Account

### Description
Make an account inactive.

### Endpoint
`POST /bankaccounts/{account_id}/inactive`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been marked as inactive."
}
```

## Delete an Account

### Description
Delete a bank account from your organization.

### Endpoint
`DELETE /bankaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.banking.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been deleted."
}
```

## Get Account Details

### Description
Get a detailed look of the specified account.

### Endpoint
`GET /bankaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.banking.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bankaccount": {
        "account_id": "460000000050127"
        /* ... full account details ... */
    }
}
```

## Update Bank Accounts

### Description
Modify the account that was created.

### Endpoint
`PUT /bankaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.banking.UPDATE`

### Arguments (Body Parameters)
*   **account_name** (string, Required): Name of the account.
*   **account_type** (string, Required): Type of the account.
*   **account_number** (string): Account Number.
*   **account_code** (string): Account Code.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency Code.
*   **description** (string): Description.
*   **bank_name** (string): Bank Name.
*   **routing_number** (string): Routing Number.
*   **is_primary_account** (boolean): Set as primary account.
*   **is_paypal_account** (boolean): Is this a PayPal account.
*   **paypal_type** (string): PayPal payment type. Allowed Values: standard, adaptive.
*   **paypal_email_address** (string): PayPal email address.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/460000000050127?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_name": "Updated Corporate Account", ...}'
```

#### Body Parameters
```json
{
    "account_name": "Corporate Account",
    "account_type": "bank",
    "account_number": "80000009823",
    "account_code": "string",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "description": "Salary details.",
    "bank_name": "Xavier Bank",
    "routing_number": "123456789",
    "is_primary_account": false,
    "is_paypal_account": true,
    "paypal_type": "string", /* e.g., "standard" */
    "paypal_email_address": "johnsmith@zilliuminc.com"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The details of the account has been updated.",
    "bankaccount": {
        "account_id": "460000000050127",
        "account_name": "Corporate Account"
        /* ... updated account details ... */
    }
}
```

## List View of Accounts

### Description
List all bank and credit card accounts for your organization.

### Endpoint
`GET /bankaccounts`

### OAuth Scope
`ZohoBooks.banking.READ`

### Query Parameters
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Inactive`.
*   **sort_column** (string): Sort results. Allowed Values: `account_name`, `account_type`, `account_code`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts?organization_id=10234695&filter_by=Status.Active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "bankaccounts": [
        {
            "account_id": "460000000050127",
            "account_name": "Corporate Account",
            "account_code": "string",
            "currency_id": "460000000000097",
            "currency_code": "USD",
            "account_type": "bank",
            "account_number": "80000009823",
            "uncategorized_transactions": 0,
            "total_unprinted_checks": 0,
            "is_active": true,
            "balance": 0,
            "bank_balance": 0,
            "bcy_balance": 0,
            "bank_name": "Xavier Bank",
            "routing_number": "123456789",
            "is_primary_account": false,
            "is_paypal_account": true
        }
        /* ... more accounts ... */
    ]
    /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Create a Bank Account

### Description
Create a bank account or a credit card account for your organization.

### Endpoint
`POST /bankaccounts`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **account_name** (string, Required): Name of the account.
*   **account_type** (string, Required): Type of the account (e.g., 'bank', 'credit_card').
*   **account_number** (string): Account Number.
*   **account_code** (string): Account Code.
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency Code.
*   **description** (string): Description.
*   **bank_name** (string): Bank Name.
*   **routing_number** (string): Routing Number.
*   **is_primary_account** (boolean): Set as primary account in Zoho Books.
*   **is_paypal_account** (boolean): Is this a PayPal account.
*   **paypal_type** (string): PayPal payment type. Allowed Values: standard, adaptive.
*   **paypal_email_address** (string): PayPal email address.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_name": "Corporate Account", "account_type": "bank", ...}'
```

#### Body Parameters
```json
{
    "account_name": "Corporate Account",
    "account_type": "bank",
    "account_number": "80000009823",
    "account_code": "string",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "description": "Salary details.",
    "bank_name": "Xavier Bank",
    "routing_number": "123456789",
    "is_primary_account": false,
    "is_paypal_account": true,
    "paypal_type": "string", /* e.g., "standard" */
    "paypal_email_address": "johnsmith@zilliuminc.com"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been created.",
    "bankaccount": {
        "account_id": "460000000050127",
        "account_name": "Corporate Account"
        /* ... other account details ... */
    }
}
```
# Bank Transactions

## Overview

### Bank Transactions
In many instances, you would wish to record manual entries for your offline transactions for your bank or credit card accounts. These entries might not be a part of your bank feeds but would make an important entry for your business records.

### End Points
*   `POST /banktransactions`
*   `GET /banktransactions`
*   `PUT /banktransactions/{bank_transaction_id}`
*   `GET /banktransactions/{bank_transaction_id}`
*   `DELETE /banktransactions/{bank_transaction_id}`
*   `POST /banktransactions/uncategorized/{transaction_id}/match`
*   `GET /banktransactions/uncategorized/{transaction_id}/match`
*   `POST /banktransactions/{transaction_id}/unmatch`
*   `POST /banktransactions/uncategorized/{transaction_id}/exclude`
*   `POST /banktransactions/uncategorized/{transaction_id}/restore`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize/expenses`
*   `POST /banktransactions/{transaction_id}/uncategorize`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize/vendorpayments`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize/customerpayments`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize/creditnoterefunds`
*   `POST /banktransactions/uncategorized/{transaction_id}/categorize/vendorcreditrefunds`
*   `POST /banktransactions/uncategorized/{statement_line_id}/categorize/paymentrefunds`
*   `POST /banktransactions/uncategorized/{statement_line_id}/categorize/vendorpaymentrefunds`
*   *(Note: PUT /banktransactions without ID seems misplaced in the original list)*

### Attributes
*   **transaction_id** (string): ID of the Transaction
*   **from_account_id** (string): The account ID from which money will be transferred (Mandatory for specific types).
*   **from_account_name** (string): The account Name from which money will be transferred.
*   **to_account_id** (string): ID of the account to which the money gets transferred (Mandatory for specific types).
*   **to_account_name** (string)
*   **transaction_type** (string): Type of the transaction (Allowed values listed in Create section).
*   **currency_id** (string): Currency ID.
*   **currency_code** (string): Currency code.
*   **payment_mode** (string): Mode of payment (e.g., cash, check). Not applicable for some types.
*   **exchange_rate** (integer): Foreign currency exchange rate.
*   **date** (string): Transaction date. Format [yyyy-mm-dd].
*   **customer_id** (string): ID of the customer or vendor.
*   **customer_name** (string): Name of the Customer.
*   **vendor_id** (string): ID of the Vendor.
*   **vendor_name** (string): Name of the Vendor.
*   **reference_number** (string): Reference Number.
*   **description** (string): Description.
*   **bank_charges** (double): Bank Charges.
*   **tax_id** (string): Not applicable 🇺🇸 - ID of the tax applied.
*   **documents** (array): Attached documents.
*   **is_inclusive_tax** (boolean): Check if amount is tax inclusive.
*   **tax_name** (string): Name of the Tax.
*   **tax_percentage** (double): Tax percentage.
*   **tax_amount** (double): Amount of Tax.
*   **sub_total** (integer): Sub Total.
*   **tax_authority_id** (string): 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Authority ID.
*   **tax_authority_name** (string): 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Authority name.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption ID.
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption code.
*   **total** (integer): Total amount.
*   **bcy_total** (integer): Total in Base Currency.
*   **amount** (double): Amount of the transaction.
*   **vat_treatment** (string): 🇬🇧 , Europe only - VAT treatment based on contact location.
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **product_type** (string): 🇬🇧 , Europe , 🇿🇦 only - Type (goods, service, etc.).
*   **acquisition_vat_id** (string): 🇬🇧 , Europe only - Acquisition VAT tax ID.
*   **acquisition_vat_name** (string): 🇬🇧 , Europe only - Acquisition VAT name.
*   **acquisition_vat_percentage** (string): 🇬🇧 , Europe only - Acquisition VAT percentage.
*   **acquisition_vat_amount** (string): 🇬🇧 , Europe only - Acquisition VAT amount.
*   **reverse_charge_vat_id** (string): 🇬🇧 , Europe only - Reverse charge VAT tax ID.
*   **reverse_charge_vat_name** (string): 🇬🇧 , Europe only - Reverse charge VAT name.
*   **reverse_charge_vat_percentage** (string): 🇬🇧 , Europe only - Reverse charge VAT percentage.
*   **reverse_charge_vat_amount** (string): 🇬🇧 , Europe only - Reverse charge VAT amount *(Note: Original description says percentage)*.
*   **reverse_charge_tax_id** (string): 🇮🇳 , GCC , 🇿🇦 only - Reverse charge tax ID.
*   **filed_in_vat_return_id** (string): 🇬🇧 only - ID of filed VAT Return.
*   **filed_in_vat_return_name** (string): 🇬🇧 only - Name of filed VAT Return.
*   **filed_in_vat_return_type** (string): 🇬🇧 only - Type of filed VAT Return.
*   **imported_transactions** (array): Linked imported statement lines.
*   **tags** (array): Tags applied.
*   **line_items** (array): Line items (for split transactions).

### Example
```json
{
    "transaction_id": "460000000048017",
    "from_account_id": "460000000070003",
    "from_account_name": "Sales",
    "to_account_id": "460000000048001",
    "to_account_name": "Corporate Account",
    "transaction_type": "deposit",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "payment_mode": "Cash",
    "exchange_rate": 1,
    "date": "2013-10-01",
    "customer_id": "460000000000111",
    "customer_name": "string",
    "vendor_id": "460000000026049",
    "vendor_name": "Bowmen and co",
    "reference_number": "Ref-121",
    "description": "string",
    "bank_charges": 0,
    "tax_id": "string",
    "documents": [ { "file_name": null, "document_id": null } ],
    "is_inclusive_tax": false,
    "tax_name": "string",
    "tax_percentage": 0,
    "tax_amount": 0,
    "sub_total": 33,
    "tax_authority_id": "string",
    "tax_authority_name": "string",
    "tax_exemption_id": "string",
    "tax_exemption_code": "string",
    "total": 33,
    "bcy_total": 33,
    "amount": 2000,
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "product_type": "string",
    "acquisition_vat_id": "string",
    "acquisition_vat_name": "string",
    "acquisition_vat_percentage": "string",
    "acquisition_vat_amount": "string",
    "reverse_charge_vat_id": "string",
    "reverse_charge_vat_name": "string",
    "reverse_charge_vat_percentage": "string",
    "reverse_charge_vat_amount": "string",
    "reverse_charge_tax_id": 982000000567254,
    "filed_in_vat_return_id": "string",
    "filed_in_vat_return_name": "string",
    "filed_in_vat_return_type": "string",
    "imported_transactions": [ { /* ... imported transaction details ... */ } ],
    "tags": [ { "tag_id": 0, "tag_option_id": 0 } ],
    "line_items": [ { /* ... line item details ... */ } ]
}
```

## Categorize as Credit Note Refund

### Description
Categorize an Uncategorized transaction as a refund from a credit note (money received from vendor).

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize/creditnoterefunds`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **creditnote_id** (string, Required): ID of the vendor credit being refunded *(Note: Parameter name mismatch in original file)*.
*   **date** (string, Required): Refund date.
*   **refund_mode** (string): Mode of refund (e.g., cash, check).
*   **reference_number** (string): Reference number.
*   **amount** (double): Refund amount (should match uncategorized amount).
*   **exchange_rate** (integer): Exchange rate.
*   **from_account_id** (string): The account ID to which the refund is received (the bank/card account with the uncategorized transaction) *(Note: Parameter name `from_account_id` is confusing here)*.
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize/creditnoterefunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"creditnote_id": "VENDOR_CREDIT_ID", "date": "2013-10-01", "amount": 2000, "from_account_id": "BANK_ACCOUNT_ID", ...}'
```

#### Body Parameters
```json
{
    "creditnote_id": "4000000030049", /* Should be Vendor Credit ID */
    "date": "2013-10-01",
    "refund_mode": "Cash",
    "reference_number": "Ref-121",
    "amount": 2000,
    "exchange_rate": 1,
    "from_account_id": "460000000070003", /* Bank Account ID */
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize (Generic)

### Description
Categorize an uncategorized transaction by creating a new transaction (e.g., Transfer Fund, Owner Contribution, Sales Without Invoice).

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   (Same as Create Transaction, specifying the details of the transaction to be created for categorization)
*   **from_account_id** (string): Source account ID.
*   **to_account_id** (string): Destination account ID.
*   **transaction_type** (string, Required): Type of transaction (deposit, transfer_fund, owner_contribution, etc.).
*   **amount** (double): Amount.
*   **date** (string): Transaction date.
*   ... other relevant fields from Create Transaction.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"transaction_type": "transfer_fund", "from_account_id": "...", "to_account_id": "...", "amount": 500, ...}'
```

#### Body Parameters
```json
{
    "from_account_id": "460000000070003",
    "to_account_id": "460000000048001",
    "transaction_type": "deposit", /* Example type */
    "amount": 2000,
    "date": "2013-10-01"
    /* ... other details matching the transaction to create ... */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize as Customer Payment Refund

### Description
Categorizing bank transactions as Payment Refund (money paid to customer from an overpayment).

### Endpoint
`POST /banktransactions/uncategorized/{statement_line_id}/categorize/paymentrefunds` *(Note: Uses `statement_line_id` in path)*

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Refund date.
*   **refund_mode** (string): Mode of refund.
*   **reference_number** (string): Reference number.
*   **amount** (double, Required): Refund amount (should match uncategorized amount).
*   **exchange_rate** (integer): Exchange rate.
*   **from_account_id** (string, Required): The account ID from which the refund is paid (the bank/card account with the uncategorized transaction).
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/STATEMENT_LINE_ID_HERE/categorize/paymentrefunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2013-10-01", "amount": 2000, "from_account_id": "BANK_ACCOUNT_ID", ...}'
```

#### Body Parameters
```json
{
    "date": "2013-10-01",
    "refund_mode": "Cash",
    "reference_number": "Ref-121",
    "amount": 2000,
    "exchange_rate": 1,
    "from_account_id": "460000000070003", /* Bank Account ID */
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize as Customer Payment

### Description
Categorize an uncategorized transaction as Customer Payment.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize/customerpayments`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **customer_id** (string): Customer ID.
*   **retainerinvoice_id** (long): Retainer Invoice ID (if applying to retainer).
*   **invoices** (array): Invoices being paid.
    *   **invoice_id** (string): Invoice ID.
    *   **amount_applied** (double): Amount applied.
    *   **tax_amount_withheld** (double): Tax withheld.
    *   **discount_amount** (double): Discount applied during payment.
*   **payment_mode** (string): Mode of payment.
*   **description** (string): Description.
*   **reference_number** (string): Reference number.
*   **exchange_rate** (integer): Exchange rate.
*   **amount** (double): Total payment amount (should match uncategorized amount).
*   **bank_charges** (double): Bank charges.
*   **account_id** (string): Bank/Credit Card account ID (where the uncategorized transaction exists).
*   **custom_fields** (array): Custom fields.
*   **documents** (array): Attachments.
*   **date** (string): Payment date.
*   **template_id** (long): Template ID *(Note: For thank you note?)*.
*   **contact_persons** (array): Contact persons for thank you note.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize/customerpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"customer_id": "...", "invoices": [...], "amount": 2000.00, ...}'
```

#### Body Parameters
```json
{
    "customer_id": "460000000000111",
    "retainerinvoice_id": 0,
    "invoices": [
        {
            /* "invoice_payment_id": "460000000134123", /* Not needed for create */
            "invoice_id": "460000000000481",
            "amount_applied": 150,
            "tax_amount_withheld": 0,
            "discount_amount": 20
        }
    ],
    "payment_mode": "Cash",
    "description": "string",
    "reference_number": "Ref-121",
    "exchange_rate": 1,
    "amount": 2000, /* Should match uncategorized amount */
    "bank_charges": 0,
    "account_id": "460000000048001", /* Bank account ID */
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "documents": [ { /* ... document details ... */ } ],
    "date": "2013-10-01",
    "template_id": 0,
    "contact_persons": [ "460000000870911", "460000000870915" ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize as Expense

### Description
Categorize an Uncategorized transaction as expense.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize/expenses`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **account_id** (string, Required): ID of the expense account to categorize into.
*   **paid_through_account_id** (string): ID of the bank/credit card account where the uncategorized transaction exists.
*   **date** (string): Transaction date.
*   **tax_id** (string): Not applicable 🇺🇸 - Tax ID.
*   **amount** (double): Amount of the expense.
*   **project_id** (string): Project ID.
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption code.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption ID.
*   **is_inclusive_tax** (boolean): Is amount tax inclusive.
*   **is_billable** (boolean): Is expense billable.
*   **reference_number** (string): Reference number.
*   **description** (string): Description.
*   **customer_id** (string): Customer ID (if billable).
*   **vendor_id** (string): Vendor ID.
*   **currency_id** (string): Currency ID.
*   **custom_fields** (array): Custom fields.
*   **tags** (array): Tags.
*   **documents** (array): Attachments.
*   **exchange_rate** (integer): Exchange rate.
*   **recurring_expense_id** (long): Link to a recurring expense profile.
*   **vat_treatment** (string): 🇬🇧 , Europe only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **acquisition_vat_id** (string): 🇬🇧 , Europe only - Acquisition VAT ID.
*   **reverse_charge_vat_id** (string): 🇬🇧 , Europe only - Reverse charge VAT ID.
*   **is_update_customer** (boolean): Update customer/vendor details.
*   **product_type** (string): 🇬🇧 , Europe , 🇿🇦 only - Type (goods, service, etc.).
*   **taxes** (array): Taxes applied.
*   **reason** (string): Reason.
*   **line_items** (array): For splitting the expense into multiple accounts/items.
*   **zcrm_potential_id** (long): CRM Potential ID.
*   Mileage specific fields also available (vehicle_id, mileage_unit, etc.)

### Query Parameters
*   **doc**: Document to attach (multipart).
*   **totalFiles**: Number of documents (multipart).
*   **document_ids**: IDs of existing documents to attach.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize/expenses?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_id": "EXPENSE_ACCOUNT_ID", "paid_through_account_id": "BANK_ACCOUNT_ID", "amount": 50.00, ...}'
```

#### Body Parameters
```json
{
    "account_id": "460000000048001", /* Expense account */
    "paid_through_account_id": "460000000000358", /* Bank account */
    "date": "2013-10-01",
    "amount": 2000
    /* ... other expense details ... */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize as Vendor Credit Refund

### Description
Categorize an uncategorized transaction as a refund from a vendor credit (money received from vendor). *(Note: Seems duplicate of "Categorize as Credit Note Refund", check API behavior)*.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize/vendorcreditrefunds`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **vendor_credit_id** (string, Required): ID of the vendor credit being refunded.
*   **date** (string, Required): Refund date.
*   **refund_mode** (string): Mode of refund.
*   **reference_number** (string): Reference number.
*   **amount** (double): Refund amount (should match uncategorized amount).
*   **exchange_rate** (integer): Exchange rate.
*   **account_id** (string, Required): The account ID to which the refund is received (the bank/card account with the uncategorized transaction).
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize/vendorcreditrefunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_credit_id": "460000000030049", "date": "2013-10-01", "amount": 2000, "account_id": "BANK_ACCOUNT_ID", ...}'
```

#### Body Parameters
```json
{
    "vendor_credit_id": "460000000030049",
    "date": "2013-10-01",
    "refund_mode": "Cash",
    "reference_number": "Ref-121",
    "amount": 2000,
    "exchange_rate": 1,
    "account_id": "460000000048001", /* Bank Account ID */
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Get Matching Transactions

### Description
Provide criteria to search for matching uncategorised transactions. Can include invoices/bills/credit-notes which result in new payment/refund records upon matching.

### Endpoint
`GET /banktransactions/uncategorized/{transaction_id}/match`

### OAuth Scope
`ZohoBooks.banking.READ`

### Query Parameters
*   **transaction_id** (string): *(Redundant - already in URL path)*.
*   **transaction_type** (string): Filter potential matches by type.
*   **date_after** (string): Filter matches after this date.
*   **date_before** (string): Filter matches before this date.
*   **amount_start** (double): Filter matches with amount greater than or equal to this.
*   **amount_end** (double): Filter matches with amount less than or equal to this.
*   **contact** (string): Filter matches by contact name.
*   **reference_number** (string): Filter matches by reference number.
*   **show_all_transactions** (boolean): Include potentially less relevant matches.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/match?organization_id=10234695&contact=Bowman' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "matching_transactions": [
        {
            "transaction_id": "460000000048017", /* ID of potential match */
            "date": "2013-10-01",
            "transaction_type": "deposit",
            "reference_number": "Ref-121",
            "amount": 2000,
            "debit_or_credit": "debit", /* Direction of the potential match */
            "transaction_number": "INV-000007", /* E.g., Invoice/Bill number */
            "is_paid_via_print_check": false,
            "contact_name": "Bowman and co",
            "is_best_match": true
        },
        {...},
        {...}
    ]
}
```

## Exclude a Transaction

### Description
Exclude a transaction from your bank or credit card account.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/exclude`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Query Parameters
*   **account_id** (string, Required): ID of the account where the transaction resides.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/exclude?organization_id=10234695&account_id=ACCOUNT_ID_HERE' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction has been excluded."
}
```

## Delete a Transaction

### Description
Delete a transaction from an account by specifying the transaction_id.

### Endpoint
`DELETE /banktransactions/{bank_transaction_id}`

### OAuth Scope
`ZohoBooks.banking.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/460000000048017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction has been deleted."
}
```

## Create a Transaction

### Description
Create a bank transaction based on the allowed transaction types.

### Endpoint
`POST /banktransactions`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **from_account_id** (string): Source account ID (Mandatory for specific types).
*   **to_account_id** (string): Destination account ID (Mandatory for specific types).
*   **transaction_type** (string, Required): Type of transaction (`deposit`, `refund`, `transfer_fund`, `card_payment`, `sales_without_invoices`, `expense_refund`, `owner_contribution`, `interest_income`, `other_income`, `owner_drawings`, `sales_return`). Module-specific types (Expense, Payments, Refunds) cannot be created here.
*   **amount** (double): Amount.
*   **payment_mode** (string): Mode of payment (Not applicable for some types).
*   **exchange_rate** (integer): Exchange rate.
*   **date** (string): Transaction date.
*   **customer_id** (string): Customer or Vendor ID.
*   **reference_number** (string): Reference number.
*   **description** (string): Description.
*   **currency_id** (string): Currency ID.
*   **tax_id** (string): Not applicable 🇺🇸 - Tax ID.
*   **is_inclusive_tax** (boolean): Is amount tax inclusive.
*   **tags** (array): Tags.
*   **from_account_tags** (array): Tags for source account.
*   **to_account_tags** (array): Tags for destination account.
*   **documents** (array): Attachments.
*   **bank_charges** (double): Bank charges.
*   **user_id** (long): User ID involved.
*   **tax_authority_id** (string): 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption ID.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"transaction_type": "deposit", "from_account_id": "...", "to_account_id": "...", "amount": 2000, ...}'
```

#### Body Parameters
```json
{
    "from_account_id": "460000000070003",
    "to_account_id": "460000000048001",
    "transaction_type": "deposit",
    "amount": 2000,
    "payment_mode": "Cash",
    "exchange_rate": 1,
    "date": "2013-10-01",
    "customer_id": "460000000000111",
    "reference_number": "Ref-121",
    "description": "string",
    "currency_id": "460000000000097",
    "tax_id": "string",
    "is_inclusive_tax": false,
    "tags": [ { /* ... tag details ... */ } ],
    "from_account_tags": [ { /* ... tag details ... */ } ],
    "to_account_tags": [ { /* ... tag details ... */ } ],
    "documents": [ { /* ... document details ... */ } ],
    "bank_charges": 0,
    "user_id": 0,
    "tax_authority_id": "string",
    "tax_exemption_id": "string",
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The bank transaction has been recorded.",
    "banktransaction": {
        "transaction_id": "460000000048017"
        /* ... full transaction details ... */
    }
}
```

## Categorize as Vendor Payment

### Description
Categorize an uncategorized transaction as Vendor Payment.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/categorize/vendorpayments`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **vendor_id** (string): Vendor ID.
*   **bills** (array): Bills being paid.
    *   **bill_id** (string): Bill ID.
    *   **amount_applied** (double): Amount applied to this bill.
    *   **tax_amount_withheld** (double): Tax withheld for this bill application.
*   **payment_mode** (string): Mode of payment.
*   **description** (string): Description.
*   **date** (string): Payment date.
*   **reference_number** (string): Reference number.
*   **exchange_rate** (integer): Exchange rate.
*   **paid_through_account_id** (string): Bank/Credit Card account ID (where the uncategorized transaction exists).
*   **amount** (double): Total payment amount (should match the uncategorized transaction amount).
*   **custom_fields** (array): Custom fields.
*   **is_paid_via_print_check** (boolean): 🇺🇸 , 🇨🇦 only - Paid via print check.
*   **check_details** (array): 🇺🇸 , 🇨🇦 only - Check details.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/categorize/vendorpayments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendor_id": "...", "bills": [...], "amount": 150.00, ...}'
```

#### Body Parameters
```json
{
    "vendor_id": "460000000026049",
    "bills": [
        {
            /* "bill_payment_id": "string", /* Not needed for create */
            "bill_id": "460000000053199",
            "amount_applied": 150,
            "tax_amount_withheld": 0
        }
    ],
    "payment_mode": "Cash",
    "description": "string",
    "date": "2013-10-01",
    "reference_number": "Ref-121",
    "exchange_rate": 1,
    "paid_through_account_id": "460000000000358", /* Bank account ID */
    "amount": 2000, /* Should match uncategorized transaction amount */
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "is_paid_via_print_check": false,
    "check_details": [ { /* ... check details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Categorize as Vendor Payment Refund

### Description
Categorizing bank transactions as Vendor Payment Refund (money received from vendor for an overpayment made to them).

### Endpoint
`POST /banktransactions/uncategorized/{statement_line_id}/categorize/vendorpaymentrefunds` *(Note: Uses `statement_line_id` in path)*

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **vendorpayment_id** (string): ID of the original Vendor Payment being refunded.
*   **date** (string, Required): Refund date.
*   **refund_mode** (string): Mode of refund.
*   **reference_number** (string): Reference number.
*   **amount** (double, Required): Refund amount (should match uncategorized amount).
*   **exchange_rate** (integer): Exchange rate.
*   **to_account_id** (string, Required): The account ID to which the refund is received (the bank/card account with the uncategorized transaction).
*   **description** (string): Description.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/STATEMENT_LINE_ID_HERE/categorize/vendorpaymentrefunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"vendorpayment_id": "...", "date": "2013-10-01", "amount": 2000, "to_account_id": "BANK_ACCOUNT_ID", ...}'
```

#### Body Parameters
```json
{
    "vendorpayment_id": "460000000012345",
    "date": "2013-10-01",
    "refund_mode": "Cash",
    "reference_number": "Ref-121",
    "amount": 2000,
    "exchange_rate": 1,
    "to_account_id": "460000000048001", /* Bank Account ID */
    "description": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction(s) have been categorized."
}
```

## Get Transaction

### Description
Fetch the details of a transaction by specifying the transaction_id.

### Endpoint
`GET /banktransactions/{bank_transaction_id}`

### OAuth Scope
`ZohoBooks.banking.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/460000000048017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "banktransaction": {
        "transaction_id": "460000000048017"
        /* ... full transaction details ... */
    }
}
```

## Get Transactions List

### Description
Get all the transaction details involved in an account.

### Endpoint
`GET /banktransactions`

### OAuth Scope
`ZohoBooks.banking.READ`

### Query Parameters
*   **account_id** (string): Filter by account ID.
*   **transaction_type** (string): Filter by transaction type.
*   **date** (string): Filter by date (variants: `_start`, `_end`).
*   **amount** (double): Filter by amount (variants: `_start`, `_end`).
*   **status** (string): Filter by categorization status (`All`, `uncategorized`, `manually_added`, `matched`, `excluded`, `categorized`).
*   **reference_number** (string): Search by reference number.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Uncategorized`, `Status.Categorized`, `Status.ManuallyAdded`, `Status.Excluded`, `Status.Matched`.
*   **sort_column** (string): Sort results. Allowed Values: `date`.
*   **transaction_status** (string): Filter by status *(Note: Potential duplicate of 'status' query param)*.
*   **search_text** (string): Search by contact name or description.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/banktransactions?organization_id=10234695&account_id=460000000048001&status=uncategorized' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "banktransactions": [
        {
            "transaction_id": "460000000048017",
            "date": "2013-10-01",
            "amount": 2000,
            "transaction_type": "deposit",
            "status": "categorized", /* Example status */
            "source": "manually_added", /* Or 'statement' */
            "account_id": "460000000048001",
            "account_name": "Petty Cash",
            "account_type": "cash",
            "price_precision": 2,
            "customer_id": "460000000000111",
            "payee": "Smith",
            "is_paid_via_print_check": false,
            "description": "string",
            "currency_id": "460000000000097",
            "currency_code": "USD",
            "currency_symbol": "$",
            "debit_or_credit": "debit",
            "offset_account_name": "Petty Cash",
            "is_offsetaccount_matched": false,
            "reference_number": "Ref-121",
            "imported_transaction_id": "460000000013297",
            "is_rule_exist": false,
            "rule_details": [ "string" ]
        },
        {...},
        {...}
    ]
    /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Match a Transaction

### Description
Match an uncategorized transaction with an existing transaction in the account.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/match`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **transactions_to_be_matched** (array): List of existing transactions to match against.
    *   **transaction_id** (string): ID of the existing transaction.
    *   **transaction_type** (string): Type of the existing transaction.

### Query Parameters
*   **account_id** (string, Required): ID of the account where the uncategorized transaction resides.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/match?organization_id=10234695&account_id=ACCOUNT_ID_HERE' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"transactions_to_be_matched": [{"transaction_id": "EXISTING_TXN_ID", "transaction_type": "deposit"}]}'
```

#### Body Parameters
```json
{
    "transactions_to_be_matched": [
        {
            "transaction_id": "460000000048017", /* ID of existing transaction to match */
            "transaction_type": "deposit"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction has been matched."
}
```

## Restore a Transaction

### Description
Restore an excluded transaction in your account.

### Endpoint
`POST /banktransactions/uncategorized/{transaction_id}/restore`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Query Parameters
*   **account_id** (string, Required): ID of the account where the transaction resides.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/uncategorized/460000000048017/restore?organization_id=10234695&account_id=ACCOUNT_ID_HERE' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The excluded transaction(s) have been restored."
}
```

## Uncategorize a Transaction

### Description
Revert a categorized transaction as uncategorized.

### Endpoint
`POST /banktransactions/{transaction_id}/uncategorize`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Query Parameters
*   **account_id** (string, Required): ID of the account where the categorized transaction resides.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/460000000048017/uncategorize?organization_id=10234695&account_id=ACCOUNT_ID_HERE' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Transaction(s) have been uncategorized."
}
```

## Update a Transaction

### Description
Make changes in the applicable fields of a transaction and update it.

### Endpoint
`PUT /banktransactions/{bank_transaction_id}`

### OAuth Scope
`ZohoBooks.banking.UPDATE`

### Arguments (Body Parameters)
*   **from_account_id** (string): Source account ID.
*   **to_account_id** (string): Destination account ID.
*   **transaction_type** (string, Required): Type of transaction.
*   **amount** (double): Amount.
*   **payment_mode** (string): Mode of payment.
*   **exchange_rate** (integer): Exchange rate.
*   **date** (string): Transaction date.
*   **customer_id** (string): Customer or Vendor ID.
*   **reference_number** (string): Reference number.
*   **description** (string): Description.
*   **currency_id** (string): Currency ID.
*   **tax_id** (string): Not applicable 🇺🇸 - Tax ID.
*   **is_inclusive_tax** (boolean): Is amount tax inclusive.
*   **tags** (array): Tags.
*   **from_account_tags** (array): Source account tags.
*   **to_account_tags** (array): Destination account tags.
*   **documents** (array): Attachments.
*   **bank_charges** (double): Bank charges.
*   **user_id** (long): User ID involved.
*   **tax_authority_id** (string): 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption ID.
*   **custom_fields** (array): Custom fields.
*   **line_items** (array): Line items (for split transactions).

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/460000000048017?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"transaction_type": "deposit", "amount": 2100, ...}'
```

#### Body Parameters
```json
{
    "from_account_id": "460000000070003",
    "to_account_id": "460000000048001",
    "transaction_type": "deposit",
    "amount": 2000,
    "payment_mode": "Cash",
    "exchange_rate": 1,
    "date": "2013-10-01",
    "customer_id": "460000000000111",
    "reference_number": "Ref-121",
    "description": "string",
    "currency_id": "460000000000097",
    "tax_id": "string",
    "is_inclusive_tax": false,
    "tags": [ { /* ... tag details ... */ } ],
    "from_account_tags": [ { /* ... tag details ... */ } ],
    "to_account_tags": [ { /* ... tag details ... */ } ],
    "documents": [ { /* ... document details ... */ } ],
    "bank_charges": 0,
    "user_id": 0,
    "tax_authority_id": "string",
    "tax_exemption_id": "string",
    "custom_fields": [ { /* ... custom field details ... */ } ],
    "line_items": [ { /* ... line item details with line_id ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The bank transaction has been updated.",
    "banktransaction": {
        "transaction_id": "460000000048017"
        /* ... updated transaction details ... */
    }
}
```

## Unmatch a Transaction

### Description
Unmatch a transaction that was previously matched and make it uncategorized.

### Endpoint
`POST /banktransactions/{transaction_id}/unmatch`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Query Parameters
*   **account_id** (string, Required): ID of the account where the matched transaction resides.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/banktransactions/460000000048017/unmatch?organization_id=10234695&account_id=ACCOUNT_ID_HERE' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction has been unmatched."
}
```

# Bank Rules

## Overview

### Bank Rules
In Zoho Books, you can automate the categorization of the bank feeds. The transaction rules feature in banking will help you in automatically identifying the bank transaction and categorizing it under the criteria provided by you.

### End Points
*   `POST /bankaccounts/rules`
*   `GET /bankaccounts/rules`
*   `PUT /bankaccounts/rules/{rule_id}`
*   `GET /bankaccounts/rules/{rule_id}`
*   `DELETE /bankaccounts/rules/{rule_id}`

### Attributes
*   **rule_id** (string): ID of the Rule
*   **rule_name** (string): Name of the Rule. Max-length [100]
*   **rule_order** (integer): Order of the rule
*   **apply_to** (string): Entities to which Rule must be applied (e.g., 'deposits', 'withdrawals')
*   **criteria_type** (string): Type of Criteria ('and' or 'or')
*   **criterion** (array): Criteria for the rule.
*   **record_as** (string): Entity type the transaction should be recorded as (e.g., 'deposit', 'expense').
*   **account_id** (string): Account ID of the Bank/Target account for the rule.
*   **account_name** (string): Name of the account (likely the target account).
*   **tax_id** (string): Tax ID involved in the transaction.
*   **customer_id** (string): ID of the Customer Associated with the Rule (if applicable).
*   **customer_name** (string): Name of the Customer Associated with the Rule.
*   **reference_number** (string): Specifies if Reference number is manual or generated from the statement ('manual', 'from_statement').
*   **payment_mode** (string): Payment Mode Associated with the Rule.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment (uk, eu_vat_registered, overseas).
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment (Allowed values vary by region).
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only - (Required if customer tax treatment is vat_registered).
*   **product_type** (string): 🇬🇧 , 🇿🇦 , Europe only - Product Type (Allowed values vary by region).
*   **tax_authority_id** (string): 🇺🇸 only - Tax Authority ID.
*   **tax_authority_name** (string): 🇺🇸 only - Tax Authority name.
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 only - Tax Exemption code.

### Example
```json
{
    "rule_id": "460000000048005",
    "rule_name": "Minimum Deposit Rule",
    "rule_order": 0,
    "apply_to": "deposits",
    "criteria_type": "and",
    "criterion": [
        {
            "criteria_id": "460000000048009",
            "field": "amount",
            "comparator": "greater_than_or_equals",
            "value": "500.00"
        }
    ],
    "record_as": "deposit",
    "account_id": "460000000000361",
    "account_name": "Petty Cash",
    "tax_id": "460000000048238",
    "customer_id": "46000000000111",
    "customer_name": "Trendz",
    "reference_number": "from_statement",
    "payment_mode": "Cash",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "product_type": "string",
    "tax_authority_id": "string",
    "tax_authority_name": "string",
    "tax_exemption_code": "string"
}
```

## Create a Rule

### Description
Create a rule and apply it on deposit/withdrawal for bank accounts and on refund/charges for credit card accounts.

### Endpoint
`POST /bankaccounts/rules`

### OAuth Scope
`ZohoBooks.banking.CREATE`

### Arguments (Body Parameters)
*   **rule_name** (string, Required): Name of the Rule. Max-length [100].
*   **target_account_id** (long, Required): The bank/credit card account ID on which the rule has to be applied.
*   **apply_to** (string, Required): Rule applies to deposits/withdrawals (bank) or refunds/charges (card). Allowed Values: `withdrawals`, `deposits`, `refunds`, `charges`.
*   **criteria_type** (string, Required): Specifies if all criteria must match ('and') or any ('or'). Allowed Values: `and`, `or`.
*   **criterion** (array, Required): List of criteria.
    *   **field** (string): Field to check (e.g., 'amount', 'description', 'payee').
    *   **comparator** (string): Comparison operator (e.g., 'equals', 'contains', 'greater_than').
    *   **value** (string): Value to compare against.
*   **record_as** (string, Required): Transaction type to create when rule matches. Allowed values depend on `apply_to` (see description). Allowed Values: `expense`, `deposit`, `refund`, `transfer_fund`, `card_payment`, `sales_without_invoices`, `expense_refund`, `interest_income`, `other_income`, `owner_drawings`.
*   **account_id** (long): The other account involved in the transaction (e.g., expense account for 'expense', bank account for 'transfer_fund').
*   **customer_id** (long): Customer ID (Applicable for sales_without_invoices, deposit, expense).
*   **tax_id** (string): Tax ID.
*   **reference_number** (string): How to set reference number. Allowed Values: `manual`, `from_statement`.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only.
*   **product_type** (string): 🇬🇧 , 🇿🇦 , Europe only - Product Type.
*   **tax_authority_id** (string): 🇺🇸 only - Tax Authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 only - Tax Exemption ID.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/rules?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"rule_name": "Minimum Deposit Rule", "target_account_id": 460000000048001, ...}'
```

#### Body Parameters
```json
{
    "rule_name": "Minimum Deposit Rule",
    "target_account_id": 460000000048001,
    "apply_to": "deposits",
    "criteria_type": "and",
    "criterion": [
        {
            "field": "amount",
            "comparator": "greater_than_or_equals",
            "value": "500.00"
        }
    ],
    "record_as": "deposit",
    "account_id": 460000000049001, /* e.g., Income Account ID */
    "customer_id": 46000000000111,
    "tax_id": "460000000048238",
    "reference_number": "manual",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "product_type": "string",
    "tax_authority_id": "string",
    "tax_exemption_id": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The bank rule has been created.",
    "rule": {
        "rule_id": "460000000048005"
        /* ... full rule details ... */
    }
}
```

## Delete a Rule

### Description
Delete a rule from your account and make it no longer applicable on the transactions.

### Endpoint
`DELETE /bankaccounts/rules/{rule_id}`

### OAuth Scope
`ZohoBooks.banking.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/rules/460000000048005?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The rule has been deleted."
}
```

## Get a Rule

### Description
Get details of a specific rule.

### Endpoint
`GET /bankaccounts/rules/{rule_id}`

### OAuth Scope
`ZohoBooks.banking.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/rules/460000000048005?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "rule_id": "460000000048005",
    "rule_name": "Minimum Deposit Rule",
    "rule_order": 0,
    "apply_to": "deposits",
    "criteria_type": "and",
    "criterion": [
        {
            "criteria_id": "460000000048009",
            "field": "amount",
            "comparator": "greater_than_or_equals",
            "value": "500.00"
        }
    ],
    "record_as": "deposit",
    "account_id": "460000000000361", /* Target Account ID */
    "account_name": "Petty Cash", /* Target Account Name */
    "tax_id": "460000000048238",
    "customer_id": "46000000000111",
    "customer_name": "Trendz",
    "reference_number": "from_statement",
    "payment_mode": "Cash",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "product_type": "string",
    "tax_authority_id": "string",
    "tax_authority_name": "string",
    "tax_exemption_code": "string"
}
```
*(Note: Example response structure differs slightly from Overview example, showing more detail)*

## Get Rules List

### Description
Fetch all the rules created for a specified bank or credit card account ID.

### Endpoint
`GET /bankaccounts/rules`

### OAuth Scope
`ZohoBooks.banking.READ`

### Query Parameters
*   **account_id** (string, Required): ID of the Bank Account for which to list rules.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/rules?organization_id=10234695&account_id=460000000000361' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "rules": [
        {
            "rule_id": "460000000048005",
            "rule_name": "Minimum Deposit Rule",
            "rule_order": 0,
            "apply_to": "deposits",
            "criteria_type": "and",
            "record_as": "deposit",
            "account_id": "460000000000361", /* Target Account ID */
            "account_name": "Petty Cash", /* Target Account Name */
            "criterion": [
                {
                    "criteria_id": "460000000048009",
                    "field": "amount",
                    "comparator": "greater_than_or_equals",
                    "value": "500.00"
                }
            ]
             /* Other rule details like customer_id, tax_id etc. might be included */
        }
        /* ... more rules ... */
    ]
}
```

## Update a Rule

### Description
Make changes to the rule, add or modify it and update.

### Endpoint
`PUT /bankaccounts/rules/{rule_id}`

### OAuth Scope
`ZohoBooks.banking.UPDATE`

### Arguments (Body Parameters)
*   **rule_name** (string, Required): Name of the Rule.
*   **target_account_id** (long, Required): The bank/credit card account ID.
*   **apply_to** (string, Required): `deposits`, `withdrawals`, `refunds`, `charges`.
*   **criteria_type** (string, Required): `and`, `or`.
*   **criterion** (array, Required): List of criteria.
    *   **criteria_id** (string): ID of existing criterion (needed for update).
    *   **field** (string): Field to check.
    *   **comparator** (string): Comparison operator.
    *   **value** (string): Value to compare against.
*   **record_as** (string, Required): Transaction type to create.
*   **account_id** (long): The other account involved.
*   **customer_id** (long): Customer ID.
*   **tax_id** (string): Tax ID.
*   **reference_number** (string): `manual` or `from_statement`.
*   **vat_treatment** (string): 🇬🇧 only - VAT treatment.
*   **tax_treatment** (string): GCC , 🇰🇪 , 🇿🇦 only - VAT treatment.
*   **is_reverse_charge_applied** (boolean): 🇿🇦 only.
*   **product_type** (string): 🇬🇧 , 🇿🇦 , Europe only - Product Type.
*   **tax_authority_id** (string): 🇺🇸 only - Tax Authority ID.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 only - Tax Exemption ID.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/bankaccounts/rules/460000000048005?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"rule_name": "Updated Rule Name", "target_account_id": 460000000048001, ...}'
```

#### Body Parameters
```json
{
    "rule_name": "Minimum Deposit Rule",
    "target_account_id": 460000000048001,
    "apply_to": "deposits",
    "criteria_type": "and",
    "criterion": [
        {
            "criteria_id": "460000000048009", /* Required to update existing criterion */
            "field": "amount",
            "comparator": "greater_than_or_equals",
            "value": "500.00"
        }
        /* Add new criterion objects without criteria_id */
        /* Omit criterion objects to delete them */
    ],
    "record_as": "deposit",
    "account_id": 460000000049001,
    "customer_id": 46000000000111,
    "tax_id": "460000000048238",
    "reference_number": "manual",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "product_type": "string",
    "tax_authority_id": "string",
    "tax_exemption_id": "string"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The bank rule has been updated.",
    "rule": {
        "rule_id": "460000000048005"
        /* ... updated rule details ... */
    }
}
```

# Chart of Accounts

## Overview

### Chart Of Accounts
The Chart of Accounts in Zoho Books consists of a wide range of accounts that are generally used with any type of business. The accounts are classified into different types such as Income, Expense, Equity, Liability & Assets.

### End Points
*   `POST /chartofaccounts`
*   `GET /chartofaccounts`
*   `PUT /chartofaccounts/{account_id}`
*   `GET /chartofaccounts/{account_id}`
*   `DELETE /chartofaccounts/{account_id}`
*   `POST /chartofaccounts/{account_id}/active`
*   `POST /chartofaccounts/{account_id}/inactive`
*   `GET /chartofaccounts/transactions`
*   `DELETE /chartofaccounts/transactions/{transaction_id}`

### Attributes
*   **account_id** (string): ID of the Account
*   **account_name** (string): Name of the account
*   **account_code** (string): Code Associated with the Account
*   **is_active** (boolean): Check if account is Active or Inactive
*   **account_type** (string): Type of the account. Allowed Values: `other_asset`, `other_current_asset`, `intangible_asset`, `right_to_use_asset`,`financial_asset`,`contingent_asset`, `cash`, `bank`, `fixed_asset`, `other_current_liability`, `credit_card`, `long_term_liability`, `loans_and_borrowing` ,`lease_liability` ,`employee_benefit_liability` ,`contingent_liability` ,`financial_liability` , `other_liability`, `equity`, `income`,`finance_income` ,`other_comprehensive_income` , `other_income`, `expense`, `manufacturing_expense` ,`impairment_expense` ,`depreciation_expense` ,`employee_benefit_expense` ,`lease_expense` ,`finance_expense` ,`tax_expense` , `cost_of_goods_sold`, `other_expense`, `accounts_receivable` and `accounts_payable`.
*   **currency_id** (string): ID of the account currency.
*   **currency_code** (string): Code of the Currency Associated with the Account
*   **description** (string): Description of the account
*   **is_system_account** (boolean): Check if it is an System Account
*   **is_involved_in_transaction** (boolean): Check if account is involved in transaction
*   **can_show_in_ze** (boolean): *(Purpose unclear)*
*   **include_in_vat_return** (boolean): 🇬🇧 only - Boolean to include an account in VAT returns.
*   **custom_fields** (array): Custom Fields associated with the account.
*   **parent_account_id** (string): ID of the Parent Account
*   **documents** (array): Documents associated with the account.
*   **created_time** (string): Created Time associated with the Entity
*   **last_modified_time** (string): Last Modified time associated with the entity

### Example
```json
{
    "account_id": "460000000038079",
    "account_name": "Notes Payable",
    "account_code": "string",
    "is_active": true,
    "account_type": "long_term_liability",
    "currency_id": "460000000000097",
    "currency_code": "INR",
    "description": "A Liability account which can be paid off in a time period longer than one year.",
    "is_system_account": true,
    "is_involved_in_transaction": false,
    "can_show_in_ze": false,
    "include_in_vat_return": true,
    "custom_fields": [
        {
            "customfield_id": "460000000080163",
            "value": "Normal"
        }
    ],
    "parent_account_id": "460000000009097",
    "documents": [
        "string"
    ],
    "created_time": "2013-01-17T15:27:23+0530",
    "last_modified_time": "2013-01-17T15:27:23+0530"
}
```

## Delete an Account

### Description
Deletes the given account. Accounts associated in any transaction/products could not be deleted.

### Endpoint
`DELETE /chartofaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.accountants.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/460000000038079?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been deleted."
}
```

## Delete a Transaction

### Description
Deletes the transaction listed in the account's transaction list. *(Note: This likely deletes the underlying transaction, e.g., the customer payment, not just the ledger entry).*

### Endpoint
`DELETE /chartofaccounts/transactions/{transaction_id}`

### OAuth Scope
`ZohoBooks.accountants.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/transactions/460000000050163?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The transaction has been deleted."
}
```

## Create an Account

### Description
Creates an account with the given account type.

### Endpoint
`POST /chartofaccounts`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Arguments (Body Parameters)
*   **account_name** (string, Required): Name of the account.
*   **account_code** (string): Code Associated with the Account.
*   **account_type** (string, Required): Type of the account (Allowed Values listed in Overview).
*   **currency_id** (string): ID of the account currency.
*   **description** (string): Description of the account.
*   **show_on_dashboard** (boolean): *(Purpose unclear)*.
*   **can_show_in_ze** (boolean): *(Purpose unclear)*.
*   **include_in_vat_return** (boolean): 🇬🇧 only - Include account in VAT returns.
*   **custom_fields** (array): Custom fields.
*   **parent_account_id** (string): ID of the Parent Account (for sub-accounts).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_name": "Notes Payable", "account_type": "long_term_liability", ...}'
```

#### Body Parameters
```json
{
    "account_name": "Notes Payable",
    "account_code": "string",
    "account_type": "long_term_liability",
    "currency_id": "460000000000097",
    "description": "A Liability account which can be paid off in a time period longer than one year.",
    "show_on_dashboard": false,
    "can_show_in_ze": false,
    "include_in_vat_return": true,
    "custom_fields": [
        {
            "customfield_id": "460000000080163",
            "value": "Normal"
        }
    ],
    "parent_account_id": "460000000009097"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been created.",
    "chart_of_account": {
        "account_id": "460000000038079",
        "account_name": "Notes Payable",
        /* ... full account details ... */
    }
}
```

## Get an Account

### Description
Gets the details of an account.

### Endpoint
`GET /chartofaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/460000000038079?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "account_id": "460000000038079",
    "account_name": "Notes Payable",
    "account_code": "string",
    "is_active": true,
    "account_type": "long_term_liability",
    "currency_id": "460000000000097",
    "currency_code": "INR",
    "description": "A Liability account which can be paid off in a time period longer than one year.",
    "is_system_account": true,
    "is_involved_in_transaction": false,
    "can_show_in_ze": false,
    "include_in_vat_return": true,
    "custom_fields": [
        {
            "customfield_id": "460000000080163",
            "value": "Normal"
        }
    ],
    "closing_balance": 0,
    "parent_account_id": "460000000009097",
    "documents": [
        "string"
    ],
    "created_time": "2013-01-17T15:27:23+0530",
    "last_modified_time": "2013-01-17T15:27:23+0530"
}
```
*(Note: Example response seems to be the account object directly, not nested under `chart_of_account` like Create/Update)*

## List Chart of Accounts

### Description
List all chart of accounts along with pagination.

### Endpoint
`GET /chartofaccounts`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **showbalance** (boolean): Get current balance of accounts.
*   **filter_by** (string): Filter accounts based on type and status. Allowed Values: `AccountType.All`, `AccountType.Active`, `AccountType.Inactive`, `AccountType.Asset`, `AccountType.Liability`, `AccountType.Equity`, `AccountType.Income`, `AccountType.Expense`.
*   **sort_column** (string): Sort accounts. Allowed Values: `account_name`, `account_type`.
*   **last_modified_time** (string): Filter by last modified time.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts?organization_id=10234695&filter_by=AccountType.Expense' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "chartofaccounts": [
        {
            "account_id": "460000000038079",
            "account_name": "Notes Payable",
            "account_code": "string",
            "account_type": "long_term_liability",
            "is_user_created": true,
            "is_system_account": true,
            "is_standalone_account": false,
            "is_active": true,
            "can_show_in_ze": false,
            "is_involved_in_transaction": false,
            "current_balance": null, /* Populated if showbalance=true */
            "parent_account_id": "460000000009097",
            "parent_account_name": " ",
            "depth": "string",
            "has_attachment": false,
            "is_child_present": "string",
            "child_count": "string",
            "documents": [ "string" ],
            "created_time": "2013-01-17T15:27:23+0530",
            "last_modified_time": "2013-01-17T15:27:23+0530"
        },
        {...},
        {...}
    ]
    /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## List Transactions for an Account

### Description
List all involved transactions for the given account.

### Endpoint
`GET /chartofaccounts/transactions`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **account_id** (string, Required): ID of the Account.
*   **date** (string): Search by date range (variants: `_start`, `_end`, `_before`, `_after`). Format yyyy-mm-dd.
*   **amount** (double): Search by amount range (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **filter_by** (string): Filter accounts based on its account type and status *(Note: Description seems incorrect, likely filters transactions)*. Allowed Values: `AccountType.All`, ... `AccountType.Expense`.
*   **transaction_type** (string): Search by transaction type. Allowed Values: `invoice`, `customer_payment`, `bills`, ..., `payment_to_initial_creditors`.
*   **sort_column** (string): Sort results. Allowed Values: `account_name`, `account_type` *(Note: Description seems incorrect, likely sorts by transaction fields like date, amount)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/transactions?organization_id=10234695&account_id=460000000038079' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "transactions": [
        {
            "categorized_transaction_id": "460000000052051", /* ID linking to bank transaction? */
            "transaction_type": "customer_payment",
            "transaction_status": "string",
            "transaction_source": "string",
            "transaction_id": "460000000050163", /* ID of the customer payment */
            "transaction_date": "2013-10-04",
            "account_id": "460000000038079",
            "customer_id": "460000000044001",
            "payee": "Richards Electric Company",
            "description": "A Liability account which can be paid off in a time period longer than one year.",
            "entry_number": "INV-00004", /* Related document number */
            "currency_id": "460000000000097",
            "currency_code": "INR",
            "debit_or_credit": "credit",
            "offset_account_name": "string",
            "reference_number": "string",
            "reconcile_status": "string",
            "debit_amount": "string",
            "credit_amount": 25
        },
        {...},
        {...}
    ]
     /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

## Update an Account

### Description
Updates the account information.

### Endpoint
`PUT /chartofaccounts/{account_id}`

### OAuth Scope
`ZohoBooks.accountants.UPDATE`

### Arguments (Body Parameters)
*   **account_name** (string, Required): Name of the account.
*   **account_code** (string): Code Associated with the Account.
*   **account_type** (string, Required): Type of the account (Allowed Values listed in Overview).
*   **currency_id** (string): ID of the account currency *(Note: Usually not updatable)*.
*   **description** (string): Description of the account.
*   **show_on_dashboard** (boolean): *(Purpose unclear)*.
*   **can_show_in_ze** (boolean): *(Purpose unclear)*.
*   **include_in_vat_return** (boolean): 🇬🇧 only - Include account in VAT returns.
*   **custom_fields** (array): Custom fields.
*   **parent_account_id** (string): ID of the Parent Account.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/460000000038079?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"account_name": "Updated Notes Payable", "description": "Updated desc.", ...}'
```

#### Body Parameters
```json
{
    "account_name": "Notes Payable",
    "account_code": "string",
    "account_type": "long_term_liability",
    "currency_id": "460000000000097",
    "description": "A Liability account which can be paid off in a time period longer than one year.",
    "show_on_dashboard": false,
    "can_show_in_ze": false,
    "include_in_vat_return": true,
    "custom_fields": [
        {
            "customfield_id": "460000000080163",
            "value": "Normal"
        }
    ],
    "parent_account_id": "460000000009097"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The details of the account have been updated.",
    "chart_of_account": {
        "account_id": "460000000038079",
        "account_name": "Notes Payable",
        /* ... updated account details ... */
    }
}
```

## Mark an Account as Inactive

### Description
Updates the account status as inactive.

### Endpoint
`POST /chartofaccounts/{account_id}/inactive`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/460000000038079/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been marked as inactive."
}
```

## Mark an Account as Active

### Description
Updates the account status as active.

### Endpoint
`POST /chartofaccounts/{account_id}/active`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/chartofaccounts/460000000038079/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The account has been marked as active."
}
```
# Journals

## Overview

### Journals
Journals are used by accountants to work directly with the general ledger to create both debit and credit entries for unique financial transactions.

### End Points
*   `POST /journals`
*   `GET /journals`
*   `PUT /journals/{journal_id}`
*   `GET /journals/{journal_id}`
*   `DELETE /journals/{journal_id}`
*   `POST /journals/{journal_id}/status/publish`
*   `POST /journals/{journal_id}/attachment`
*   `POST /journals/{journal_id}/comments` *(Note: Original docs typo jounral_id)*
*   `GET /journals/{journal_id}/comments` *(Implied/Missing from list)*
*   `PUT /journals/{journal_id}/comments/{comment_id}` *(Implied/Missing from list)*
*   `DELETE /journals/{journal_id}/comments/{comment_id}` *(Note: Original docs typo jounral_id)*
*   *(Note: GET/POST/DELETE for journal attachment endpoints are missing from this list but present in individual files)*

### Attributes
*   **journal_id** (string): ID of the Journal
*   **entry_number** (string): Entry Number of the Journal
*   **reference_number** (string): Reference number for the journal.
*   **notes** (string): Notes for the journal.
*   **currency_id** (string): ID of the Currency Associated with the Journal
*   **currency_code** (string): Code of the Currency Associated with the Journal
*   **currency_symbol** (string): Symbol of the Currency Associated with the Journal
*   **exchange_rate** (double): Exchange Rate between the Currencies
*   **journal_date** (string): Date on which the journal to be recorded. Format [yyyy-mm-dd].
*   **journal_type** (string): Type of the Journal. Allowed values: `Cash` and `Both` .
*   **vat_treatment** (string): 🇬🇧 , Europe only - VAT treatment (`uk`, `eu_vat_registered`, `overseas`).
*   **product_type** (string): 🇬🇧 only - Type (`digital_service`, `goods`, `service`).
*   **include_in_vat_return** (boolean): Europe , 🇬🇧 only - Include in VAT Return.
*   **is_bas_adjustment** (boolean): 🇦🇺 only - Check if Journal is created for BAS Adjustment.
*   **line_items** (array): Line items.
*   **location_id** (string): Location ID.
*   **location_name** (string): Name of the location.
*   **line_item_total** (double): Total of the Line Item *(Note: Likely sum of debits/credits, not a standard field)*.
*   **total** (double): Total of the Journal (debits or credits).
*   **bcy_total** (double): Total in Base Currency.
*   **price_precision** (integer): Price Precision for the Values.
*   **taxes** (array): Taxes associated.
*   **created_time** (string): Created Time.
*   **last_modified_time** (string): Last Modified Time.
*   **status** (string): Status (`draft`, `published`).
*   **custom_fields** (array): Custom fields.

### Example
```json
{
    "journal_id": "460000000038001",
    "entry_number": "1",
    "reference_number": "7355",
    "notes": "Loan repayment",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "currency_symbol": "$",
    "exchange_rate": 1,
    "journal_date": "2013-09-04",
    "journal_type": "both",
    "vat_treatment": "string",
    "product_type": "string",
    "include_in_vat_return": true,
    "is_bas_adjustment": true,
    "line_items": [
        {
            "line_id": "460000000038005",
            "account_id": "460000000000361",
            "customer_id": "string",
            "customer_name": "string",
            "account_name": "Petty Cash",
            "description": "string",
            "debit_or_credit": "credit",
            "tax_exemption_id": "string",
            "tax_exemption_type": "string",
            "tax_exemption_code": "string",
            "tax_authority_id": "string",
            "tax_authority_name": "string",
            "tax_id": "string",
            "tax_name": "string",
            "tax_type": "tax",
            "tax_percentage": "string",
            "amount": 5000,
            "bcy_amount": 100,
            "acquisition_vat_id": "string",
            "acquisition_vat_name": "string",
            "acquisition_vat_percentage": "string",
            "acquisition_vat_amount": "string",
            "reverse_charge_vat_id": "string",
            "reverse_charge_vat_name": "string",
            "reverse_charge_vat_percentage": "string",
            "reverse_charge_vat_amount": "string",
            "tags": [ { /* ... tag details ... */ } ],
            "location_id": "460000000038080",
            "location_name": "string",
            "project_id": "460000000898001",
            "project_name": "Network Distribution"
        }
    ],
    "location_id": "460000000038080",
    "location_name": "string",
    "line_item_total": 5000,
    "total": 5000,
    "bcy_total": 100,
    "price_precision": 2,
    "taxes": [ { /* ... tax details ... */ } ],
    "created_time": "2013-09-04T09:40:07+0530",
    "last_modified_time": "2013-09-05T17:13:31+0530",
    "status": "draft",
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

## Add Attachment to Journal

### Description
Attach a file to a journal.

### Endpoint
`POST /journals/{journal_id}/attachment`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Query Parameters
*   **attachment**: The file to attach (sent via multipart/form-data). Allowed Extensions likely similar to other modules (pdf, png, jpg, etc.).
*   **doc**: Alternative parameter name for the document (multipart).
*   **totalFiles**: Number of files being uploaded (multipart).
*   **document_ids**: IDs of existing documents to attach.

### Request Example

#### cURL
```curl
# Example for uploading a new file
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  -F "attachment=@/path/to/journal_support.pdf"
```

### Response Example
```json
{
    "code": 0,
    "message": "Your file has been successfully attached to the journal."
}
```

## Add Comment to Journal

### Description
Add a comment for a journal.

### Endpoint
`POST /journals/{journal_id}/comments` *(Note: Original docs had typo in URL)*

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Arguments (Body Parameters)
*   **description** (string, Required): Description of the comment.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Reviewed and approved."}'
```

#### Body Parameters
```json
{
    "description": "Journal Created"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Journal comment has been added successfully.",
    "comment": { /* Corrected: Original showed array */
        "comment_id": "460000000048023",
        "description": "string",
        "commented_by_id": "460000000017003",
        "commented_by": "John",
        "comment_type": "system", /* or user */
        "date": "string",
        "operation_type": "Added"
    }
}
```

## Create a Journal

### Description
Create a journal entry.

### Endpoint
`POST /journals`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Arguments (Body Parameters)
*   **journal_date** (string, Required): Date of the journal entry. Format [yyyy-mm-dd].
*   **reference_number** (string): Reference number.
*   **notes** (string): Notes.
*   **journal_type** (string): Type (`Cash` or `Both`).
*   **vat_treatment** (string): 🇬🇧 , Europe only - VAT treatment.
*   **include_in_vat_return** (boolean): Europe , 🇬🇧 only - Include in VAT Return.
*   **product_type** (string): 🇬🇧 only - Type (`digital_service`, `goods`, `service`).
*   **is_bas_adjustment** (boolean): 🇦🇺 only - Is BAS Adjustment.
*   **currency_id** (string): Currency ID.
*   **exchange_rate** (double): Exchange rate.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Journal line items. Must contain at least two lines, and debits must equal credits.
    *   **account_id** (string, Required): Account ID for the line.
    *   **debit_or_credit** (string, Required): 'debit' or 'credit'.
    *   **amount** (double, Required): Amount for the line.
    *   **description** (string): Line description.
    *   **customer_id** (string): Associated Customer ID (if applicable).
    *   **vendor_id** (string): Associated Vendor ID (if applicable).
    *   **tax_id** (string): Tax ID for the line (if applicable).
    *   ... other line-specific fields like project, tags, location etc.
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption code.
*   **tax_exemption_type** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 , 🇲🇽 only - Tax Exemption type (`customer` or `item`).
*   **status** (string): Status (`draft` or `published`). Default is `draft`.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/journals?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"journal_date": "2013-09-04", "notes": "Loan repayment", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "journal_date": "2013-09-04",
    "reference_number": "7355",
    "notes": "Loan repayment",
    "journal_type": "both",
    "vat_treatment": "string",
    "include_in_vat_return": true,
    "product_type": "string",
    "is_bas_adjustment": true,
    "currency_id": "460000000000097",
    "exchange_rate": 1,
    "location_id": "460000000038080",
    "line_items": [
        {
            "account_id": "460000000000361",
            "customer_id": "string",
            "description": "string",
            "tax_exemption_id": "string",
            "tax_authority_id": "string",
            "tax_exemption_type": "string",
            "tax_exemption_code": "string",
            "tax_authority_name": "string",
            "tax_id": "string",
            "amount": 5000,
            "debit_or_credit": "credit",
            "acquisition_vat_id": "string",
            "reverse_charge_vat_id": "string",
            "location_id": "460000000038080",
            "tags": [ { /* ... tag details ... */ } ],
            "project_id": "460000000898001"
        },
        { /* Need matching debit line */
            "account_id": "DEBIT_ACCOUNT_ID",
            "amount": 5000,
            "debit_or_credit": "debit"
            /* ... other details ... */
        }
    ],
    "tax_exemption_code": "string",
    "tax_exemption_type": "string",
    "status": "draft",
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The journal entry has been created.",
    "journal": {
        "journal_id": "460000000038001",
        /* ... full journal details ... */
    }
}
```

## Delete a Journal

### Description
Deletes the given journal.

### Endpoint
`DELETE /journals/{journal_id}`

### OAuth Scope
`ZohoBooks.accountants.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected journal entry has been deleted."
}
```

## Delete Journal Comment

### Description
Delete a journal comment.

### Endpoint
`DELETE /journals/{journal_id}/comments/{comment_id}` *(Note: Original docs had typo in URL)*

### OAuth Scope
`ZohoBooks.accountants.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/comments/460000000048023?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected journal comment entries have been deleted."
}
```

## Get Journal

### Description
Get the details of the journal.

### Endpoint
`GET /journals/{journal_id}`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "journal": {
        "journal_id": "460000000038001",
        /* ... full journal details ... */
    }
}
```

## Get Journal List

### Description
Get journal list.

### Endpoint
`GET /journals`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **entry_number** (string): Search by entry number (variants: `_startswith`, `_contains`).
*   **reference_number** (string): Search by reference number (variants: `_startswith`, `_contains`).
*   **date** (string): Search by date (variants: `_start`, `_end`, `_before`, `_after`).
*   **notes** (string): Search by notes (variants: `_startswith`, `_contains`).
*   **last_modified_time** (string): Filter by last modified time.
*   **total** (double): Search by total amount (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **customer_id** (string): Search by Customer ID.
*   **vendor_id** (string): Search by Vendor ID.
*   **filter_by** (string): Filter by date range. Allowed Values: `JournalDate.All`, `JournalDate.Today`, `JournalDate.ThisWeek`, `JournalDate.ThisMonth`, `JournalDate.ThisQuarter`, `JournalDate.ThisYear`.
*   **sort_column** (string): Sort results. Allowed Values: `journal_date`, `entry_number`, `reference_number`, `total`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/journals?organization_id=10234695&filter_by=JournalDate.ThisMonth' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "journals": [
        {
            "journal_id": "460000000038001",
            "journal_date": "2013-09-04",
            "entry_number": "1",
            "reference_number": "7355",
            "currency_id": "460000000000097",
            "notes": "Loan repayment",
            "journal_type": "both",
            "entity_type": "journal",
            "total": 5000,
            "bcy_total": 100,
            "custom_field": "string" /* Example seems simplified, should match custom_fields array format */
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "sort_column": "journal_date",
        "sort_order": "D",
        "applied_filter": "JournalDate.ThisMonth"
    }
}
```
*(Note: `page_context` was missing from the original example).*

## List Journal Comments and History

### Description
Get the complete history and comments of a journal.

### Endpoint
`GET /journals/{journal_id}/comments`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "460000000048023",
            "journal_id": "460000000038001",
            "description": "Comment text or history description",
            "commented_by_id": "460000000017003",
            "commented_by": "User Name or System",
            "comment_type": "system or user",
            "date": "YYYY-MM-DD",
            "date_description": "Relative time",
            "time": "HH:MM AM/PM",
            "operation_type": "Added/Updated/Published",
            "transaction_id": "...", // ID of related transaction if applicable
            "transaction_type": "journal"
        },
        {...}
    ]
}
```

## Mark Journal as Published

### Description
Mark a draft journal as published.

### Endpoint
`POST /journals/{journal_id}/status/publish`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/status/publish?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Journal has been published."
}
```

## Update a Journal

### Description
Updates the journal with given information.

### Endpoint
`PUT /journals/{journal_id}`

### OAuth Scope
`ZohoBooks.accountants.UPDATE`

### Arguments (Body Parameters)
*   **journal_date** (string, Required): Date of the journal entry.
*   **reference_number** (string): Reference number.
*   **notes** (string): Notes.
*   **journal_type** (string): Type (`Cash` or `Both`).
*   **vat_treatment** (string): 🇬🇧 , Europe only - VAT treatment.
*   **include_in_vat_return** (boolean): Europe , 🇬🇧 only - Include in VAT Return.
*   **product_type** (string): 🇬🇧 only - Type (`digital_service`, `goods`, `service`).
*   **is_bas_adjustment** (boolean): 🇦🇺 only - Is BAS Adjustment.
*   **currency_id** (string): Currency ID *(Note: Usually not updatable)*.
*   **exchange_rate** (double): Exchange rate.
*   **location_id** (string): Location ID.
*   **line_items** (array, Required): Journal line items. Debits must equal credits.
    *   **line_id** (string): Mandatory for updating existing lines. Omit for new. Remove from array to delete.
    *   **account_id** (string, Required): Account ID.
    *   **debit_or_credit** (string, Required): 'debit' or 'credit'.
    *   **amount** (double, Required): Amount.
    *   ... other line item fields ...
*   **tax_exemption_code** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 only - Tax Exemption code.
*   **tax_exemption_type** (string): 🇮🇳 , 🇺🇸 , 🇦🇺 , 🇨🇦 , 🇲🇽 only - Tax Exemption type.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"journal_date": "2013-09-05", "notes": "Updated note", "line_items": [...] ...}'
```

#### Body Parameters
```json
{
    "journal_date": "2013-09-04",
    "reference_number": "7355",
    "notes": "Loan repayment",
    "journal_type": "both",
    "vat_treatment": "string",
    "include_in_vat_return": true,
    "product_type": "string",
    "is_bas_adjustment": true,
    "currency_id": "460000000000097",
    "exchange_rate": 1,
    "location_id": "460000000038080",
    "line_items": [
        {
            "line_id": "460000000038005", /* Required for update */
            "account_id": "460000000000361",
            "customer_id": "string",
            "description": "string",
            "tax_exemption_id": "string",
            "tax_authority_id": "string",
            "tax_exemption_type": "string",
            "tax_exemption_code": "string",
            "tax_authority_name": "string",
            "tax_id": "string",
            "amount": 5000,
            "debit_or_credit": "credit",
            "acquisition_vat_id": "string",
            "reverse_charge_vat_id": "string",
            "tags": [ { /* ... tag details ... */ } ],
            "location_id": "460000000038080",
            "project_id": "460000000898001"
        },
        { /* Matching debit line, potentially with its line_id if updating */
            "account_id": "DEBIT_ACCOUNT_ID",
            "amount": 5000,
            "debit_or_credit": "debit"
            /* ... other details ... */
        }
    ],
    "tax_exemption_code": "string",
    "tax_exemption_type": "string",
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The journal entry has been updated.",
    "journal": {
        "journal_id": "460000000038001",
        /* ... updated journal details ... */
    }
}
```

## Update Journal Comment

### Description
Update an existing comment of a journal.

### Endpoint
`PUT /journals/{journal_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.accountants.UPDATE`

### Arguments (Body Parameters)
*   **description** (string, Required): The updated comment text.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/journals/460000000038001/comments/460000000048023?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Updated comment text."}'
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been updated.",
    "comment": {
        "comment_id": "460000000048023",
        "journal_id": "460000000038001",
        "description": "Updated comment text.",
        /* ... other comment fields ... */
    }
}
```

# Fixed Assets

## Overview

### Fixed Assets
Fixed assets are long-term tangible assets that a business owns and uses to produce goods and services. In Zoho Books, you can record fixed assets and automatically calculate depreciation for them. You can sell or write off the asset when it is likely to generate a profit, after it has completed its useful life, or when it has been fully depreciated.

### End Points
*   `POST /fixedassets`
*   `GET /fixedassets`
*   `PUT /fixedassets/{fixed_asset_id}`
*   `GET /fixedassets/{fixed_asset_id}`
*   `DELETE /fixedassets/{fixed_asset_id}`
*   `GET /fixedassets/{fixed_asset_id}/history`
*   `GET /fixedassets/{fixed_asset_id}/forecast`
*   `POST /fixedassets/{fixed_asset_id}/status/active`
*   `POST /fixedassets/{fixed_asset_id}/status/cancel`
*   `POST /fixedassets/{fixed_asset_id}/status/draft`
*   `POST /fixedassets/{fixed_asset_id}/writeoff`
*   `POST /fixedassets/{fixed_asset_id}/sell`
*   `POST /fixedassets/{fixed_asset_id}/comments`
*   `DELETE /fixedassets/{fixed_asset_id}/comments/{comment_id}`
*   `POST /fixedassettypes`
*   `GET /fixedassettypes`
*   `PUT /fixedassettypes/{fixed_asset_type_id}`
*   `DELETE /fixedassettypes/{fixed_asset_type_id}`

### Attributes
*   **fixed_asset_id** (string): ID of the fixed asset
*   **asset_name** (string): Name of the fixed asset.
*   **status** (string): Status (`draft`, `active`, `sold`, `written_off`, `cancelled`, `fully_depreciated`).
*   **asset_number** (string): Number of the fixed asset.
*   **asset_number_prefix** (string): Prefix of the asset number.
*   **asset_number_suffix** (integer): Suffix of the asset number.
*   **description** (string): Description.
*   **total_life** (number): Total life in months.
*   **fixed_asset_type_id** (string): Associated fixed asset type ID.
*   **fixed_asset_type_name** (string): Name of fixed asset type.
*   **depreciation_method** (string): Depreciation method (`declining_method`, `straight_line`, etc. varies by edition).
*   **depreciation_percentage** (double): Percentage for declining methods (0-100).
*   **depreciation_frequency** (string): Frequency (`yearly`, `monthly`).
*   **asset_cost** (double): Purchase cost.
*   **dep_start_value** (double): Value to start depreciation calculation from.
*   **salvage_value** (double): Residual value after depreciation.
*   **asset_purchase_date** (string): Purchase date. Format [yyyy-mm-dd].
*   **current_asset_value** (number): Current book value.
*   **accumulated_dep_value** (number): Accumulated depreciation.
*   **serial_no** (string): Serial number.
*   **depreciation_start_date** (string): Depreciation start date. Format [yyyy-mm-dd].
*   **last_depreciation_date** (string): Last depreciation run date. Format [yyyy-mm-dd].
*   **asset_account_id** (string): Asset tracking account ID.
*   **asset_account_name** (string): Asset tracking account name.
*   **expense_account_id** (string): Depreciation expense account ID (Expense or Other Expense type).
*   **expense_account_name** (string): Depreciation expense account name.
*   **depreciation_account_id** (string): Accumulated depreciation account ID.
*   **depreciation_account_name** (string): Accumulated depreciation account name.
*   **computation_type** (string): Computation type (`prorata_basis`, `no_prorata`).
*   **warranty_expiry_date** (string): Warranty expiration date. Format [yyyy-mm-dd].
*   **notes** (string): Notes.
*   **tags** (array): Tags applied.
*   **associated_transactions** (array): Linked transactions (e.g., purchase bill).
*   **comments** (array): Comments and history.
*   **custom_fields** (array): Custom fields.

### Example
```json
{
    "fixed_asset_id": "3640355000000319008",
    "asset_name": "Laptop",
    "status": "draft",
    "asset_number": "FA-00013",
    "asset_number_prefix": "FA-",
    "asset_number_suffix": 13,
    "description": "string",
    "total_life": 60,
    "fixed_asset_type_id": "3640355000000319008",
    "fixed_asset_type_name": "Machines",
    "depreciation_method": "declining_method",
    "depreciation_percentage": 12,
    "depreciation_frequency": "yearly",
    "asset_cost": 1000,
    "dep_start_value": 1000,
    "salvage_value": 100,
    "asset_purchase_date": "2024-12-17",
    "current_asset_value": 1000,
    "accumulated_dep_value": 0,
    "serial_no": "SN-0001",
    "depreciation_start_date": "2024-12-17",
    "last_depreciation_date": "",
    "asset_account_id": "3640355000000000367",
    "asset_account_name": "Furniture and Equipment",
    "expense_account_id": "3640355000000000421",
    "expense_account_name": "Telephone Expense",
    "depreciation_account_id": "3640355000000000367",
    "depreciation_account_name": "Furniture and Equipment",
    "computation_type": "prorata_basis",
    "warranty_expiry_date": "2027-12-17",
    "notes": "This is a laptop Model 2024",
    "tags": [
        {
            "tag_id": "460000000094001",
            "tag_option_id": "460000000048001",
            "tag_name": "Location",
            "tag_option_name": "USA"
        }
    ],
    "associated_transactions": [
        {}
    ],
    "comments": [
        {
            "comment_id": "3640355000000319013",
            "description": "string",
            "commented_by_id": "3640355000000075001",
            "commented_by": "Zoho Books",
            "comment_type": "system",
            "date": "2024-12-17",
            "date_description": "few seconds ago",
            "time": "11:34 AM",
            "operation_type": "Added"
        }
    ],
    "custom_fields": [
        {
            "customfield_id": "460000000098001",
            "value": "Normal"
        }
    ]
}
```

## Add Comment to Fixed Asset

### Description
Add a comment to the fixed asset.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/comments`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Arguments (Body Parameters)
*   **description** (string, Required): The comment text.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Asset inspected today."}'
```

#### Body Parameters
```json
{
    "description": "Fixed asset is in good condition"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comment has been added",
    "comment": {
        "comment_id": "3640355000000319013",
        "description": "string",
        "commented_by_id": "3640355000000075001",
        "commented_by": "Zoho Books",
        "comment_type": "system", /* or user */
        "date": "2024-12-17",
        "date_description": "few seconds ago",
        "time": "11:34 AM",
        "operation_type": "Added"
    }
}
```

## Cancel Fixed Asset

### Description
Cancel the fixed asset.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/status/cancel`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/status/cancel?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset's status changed"
}
```

## Create a Fixed Asset

### Description
Create a fixed asset.

### Endpoint
`POST /fixedassets`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Arguments (Body Parameters)
*   **asset_name** (string, Required): Name of the fixed asset.
*   **fixed_asset_type_id** (string, Required): ID of the associated fixed asset type.
*   **asset_account_id** (string, Required): Asset tracking account ID.
*   **expense_account_id** (string): Depreciation expense account ID.
*   **depreciation_account_id** (string): Accumulated depreciation account ID.
*   **depreciation_method** (string): Depreciation method (Allowed values vary by edition).
*   **depreciation_frequency** (string): Frequency (`yearly`, `monthly`).
*   **depreciation_percentage** (double): Percentage for declining methods (0-100). Required if method is declining.
*   **total_life** (number): Total life in months. Required if method is straight-line.
*   **salvage_value** (double): Salvage value.
*   **depreciation_start_date** (string): Depreciation start date. Format [yyyy-mm-dd].
*   **description** (string): Description.
*   **asset_cost** (double, Required): Purchase cost.
*   **computation_type** (string): Computation type (`prorata_basis`, `no_prorata`).
*   **warranty_expiry_date** (string): Warranty expiration date. Format [yyyy-mm-dd].
*   **asset_purchase_date** (string, Required): Purchase date. Format [yyyy-mm-dd].
*   **serial_no** (string): Serial number.
*   **dep_start_value** (double): Value to start depreciation from (defaults to `asset_cost` if omitted).
*   **notes** (string): Notes.
*   **tags** (array): Tags.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"asset_name": "Laptop", "fixed_asset_type_id": "...", "asset_account_id": "...", "asset_cost": 1000, ...}'
```

#### Body Parameters
```json
{
    "asset_name": "Laptop",
    "fixed_asset_type_id": "3640355000000319008",
    "asset_account_id": "3640355000000000367",
    "expense_account_id": "3640355000000000421",
    "depreciation_account_id": "3640355000000000367",
    "depreciation_method": "declining_method",
    "depreciation_frequency": "yearly",
    "depreciation_percentage": 12,
    "total_life": 60,
    "salvage_value": 100,
    "depreciation_start_date": "2024-12-17",
    "description": "string",
    "asset_cost": 1000,
    "computation_type": "prorata_basis",
    "warranty_expiry_date": "2027-12-17",
    "asset_purchase_date": "2024-12-17",
    "serial_no": "SN-0001",
    "dep_start_value": 1000,
    "notes": "This is a laptop Model 2024",
    "tags": [ { /* ... tag details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The fixed asset has been created.",
    "fixed_asset": {
        "fixed_asset_id": "3640355000000319008",
        "status": "draft", /* Initial status */
        /* ... full fixed asset details ... */
    }
}
```

## Create a Fixed Asset Type

### Description
Create a fixed asset type.

### Endpoint
`POST /fixedassettypes`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Arguments (Body Parameters)
*   **fixed_asset_type_name** (string, Required): Name of the fixed asset type.
*   **expense_account_id** (string, Required): Default depreciation expense account ID.
*   **depreciation_account_id** (string, Required): Default accumulated depreciation account ID.
*   **depreciation_method** (string, Required): Default depreciation method.
*   **depreciation_frequency** (string, Required): Default frequency (`yearly`, `monthly`).
*   **depreciation_percentage** (double, Required): Default percentage (Required if method is declining).
*   **total_life** (number, Required): Default total life in months (Required if method is straight-line).
*   **salvage_value** (double, Required): Default salvage value.
*   **computation_type** (string, Required): Default computation type (`prorata_basis`, `no_prorata`).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassettypes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"fixed_asset_type_name": "Machines", "expense_account_id": "...", ...}'
```

#### Body Parameters
```json
{
    "fixed_asset_type_name": "Machines",
    "expense_account_id": "3640355000000000421",
    "depreciation_account_id": "3640355000000000367",
    "depreciation_method": "declining_method",
    "depreciation_frequency": "yearly",
    "depreciation_percentage": 12,
    "total_life": 60,
    "salvage_value": 100,
    "computation_type": "prorata_basis"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The fixed asset type has been created.",
    "fixed_asset_type": {
        "fixed_asset_type_id": "3640355000000319008",
        "fixed_asset_type_name": "Machines",
        /* ... other type details ... */
    }
}
```

## Delete a Fixed Asset

### Description
Deletes the given fixed asset.

### Endpoint
`DELETE /fixedassets/{fixed_asset_id}`

### OAuth Scope
`ZohoBooks.fixedasset.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected fixed asset has been deleted."
}
```

## Delete a Fixed Asset Type

### Description
Deletes the given fixed asset type. *(Note: This likely fails if assets are currently assigned to this type).*

### Endpoint
`DELETE /fixedassettypes/{fixed_asset_type_id}`

### OAuth Scope
`ZohoBooks.fixedasset.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/fixedassettypes/3640355000000319008?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected fixed asset type has been deleted."
}
```

## Delete Fixed Asset Comment

### Description
Delete the comment of the fixed asset.

### Endpoint
`DELETE /fixedassets/{fixed_asset_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.fixedasset.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/comments/3640355000000319013?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset comment has been deleted"
}
```

## Get Fixed Asset

### Description
Get the details of the fixed asset.

### Endpoint
`GET /fixedassets/{fixed_asset_id}`

### OAuth Scope
`ZohoBooks.fixedasset.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "fixed_asset": { /* Corrected typo 'fissed-asset' from original */
        "fixed_asset_id": "3640355000000319008",
        /* ... full fixed asset details ... */
    }
}
```

## Get Fixed Asset History

### Description
It displays a detailed summary of the asset from acquisition till write off (includes depreciation entries).

### Endpoint
`GET /fixedassets/{fixed_asset_id}/history`

### OAuth Scope
`ZohoBooks.fixedasset.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/history?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "asset_history": [
        {
            "valuation_id": "3640355000000319008", /* ID of the valuation entry */
            "description": "string", /* Description of the event */
            "valuation_date": "2024-06-30", /* Date of the event */
            "depreciated_value": 91.65, /* Depreciation amount for this period */
            "current_value": 824.78, /* Book value after this event */
            "accumulated_value": 175.22, /* Accumulated depreciation after this event */
            "type": "depreciation", /* Type of event (depreciation, acquisition, writeoff, sale) */
            "is_journal_posted": true /* If depreciation journal was posted */
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```

## Get Fixed Asset List

### Description
Get fixed asset list.

### Endpoint
`GET /fixedassets`

### OAuth Scope
`ZohoBooks.fixedasset.READ`

### Query Parameters
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Cancel`, `Status.FullyDepreciated`, `Status.WriteOff`, `Status.Sold`, `Status.Draft`.
*   **sort_column** (string): Sort results. Allowed Values: `asset_name`, `asset_number`, `asset_cost`, `created_time`, `current_asset_value`.
*   **sort_order** (string): Sort order. Allowed Values: `A`, `D`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/fixedassets?organization_id=10234695&filter_by=Status.Active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "fixedassets": [
        {
            "fixed_asset_id": "3640355000000319008",
            "asset_number": "FA-00013",
            "asset_name": "Laptop",
            "status": "draft", /* Example status */
            "current_asset_value": 1000,
            "asset_cost": 1000,
            "fixed_asset_type_name": "Machines"
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "applied_filter": "Status.Active",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```
*(Note: `page_context` was missing from the original example).*

## Get Fixed Asset Type List

### Description
Get fixed asset type list.

### Endpoint
`GET /fixedassettypes`

### OAuth Scope
`ZohoBooks.fixedasset.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/fixedassettypes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "fixed_asset_types": [
        {
            "fixed_asset_type_id": "3640355000000319008",
            "fixed_asset_type_name": "Machines",
            /* ... other type details ... */
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: `page_context` was missing from the original example).*

## Get Fixed Asset's Forecast Depreciation

### Description
It displays a detailed summary of the asset’s future depreciation rates.

### Endpoint
`GET /fixedassets/{fixed_asset_id}/forecast`

### OAuth Scope
`ZohoBooks.fixedasset.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/forecast?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": [
        {
            "valuation_date": "2024-06-30", /* Future date of depreciation */
            "depreciated_value": 91.65, /* Forecasted depreciation amount */
            "current_value": 824.78, /* Forecasted book value */
            "accumulated_value": 175.22 /* Forecasted accumulated depreciation */
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: `page_context` was missing from the original example).*

## Mark Fixed Asset as Active

### Description
Mark the fixed asset as active to start calculating depreciation for the asset.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/status/active`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/status/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset's status changed"
}
```

## Mark Fixed Asset as Draft

### Description
Mark the fixed asset as draft.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/status/draft`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/status/draft?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset's status changed"
}
```

## Sell Fixed Asset

### Description
Sell the fixed asset. Records the disposal by linking it to an invoice line item representing the sale proceeds.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/sell`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Arguments (Body Parameters)
*   **expense_account_id** (string, Required): Account ID to record gain/loss on disposal.
*   **invoice_id** (string, Required): ID of the invoice recording the sale proceeds.
*   **line_item_id** (string, Required): ID of the line item on the invoice representing the fixed asset sale.
*   **reason** (string, Required): Reason for selling the fixed asset.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/sell?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"expense_account_id": "...", "invoice_id": "...", "line_item_id": "...", "reason": "..."}'
```

#### Body Parameters
```json
{
    "expense_account_id": "3640355000000000421", /* Gain/Loss on Sale Account */
    "invoice_id": "3640355000000319008", /* Invoice ID for the sale */
    "line_item_id": "3640355000000319008", /* Line item ID on the invoice */
    "reason": "Asset is no longer required"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset has been sold"
}
```

## Update a Fixed Asset

### Description
Updates the fixed asset with given information.

### Endpoint
`PUT /fixedassets/{fixed_asset_id}`

### OAuth Scope
`ZohoBooks.fixedasset.UPDATE`

### Arguments (Body Parameters)
*   **asset_name** (string, Required): Name of the fixed asset.
*   **fixed_asset_type_id** (string, Required): ID of the associated fixed asset type.
*   **asset_account_id** (string, Required): Asset tracking account ID.
*   **expense_account_id** (string): Depreciation expense account ID.
*   **depreciation_account_id** (string): Accumulated depreciation account ID.
*   **depreciation_method** (string): Depreciation method.
*   **depreciation_frequency** (string): Frequency (`yearly`, `monthly`).
*   **depreciation_percentage** (double): Percentage for declining methods (0-100).
*   **total_life** (number): Total life in months.
*   **salvage_value** (double): Salvage value.
*   **depreciation_start_date** (string): Depreciation start date. Format [yyyy-mm-dd].
*   **description** (string): Description.
*   **asset_cost** (double, Required): Purchase cost.
*   **computation_type** (string): Computation type (`prorata_basis`, `no_prorata`).
*   **warranty_expiry_date** (string): Warranty expiration date. Format [yyyy-mm-dd].
*   **asset_purchase_date** (string, Required): Purchase date. Format [yyyy-mm-dd].
*   **serial_no** (string): Serial number.
*   **dep_start_value** (double): Value to start depreciation from.
*   **notes** (string): Notes.
*   **tags** (array): Tags.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"asset_name": "Updated Laptop Name", "notes": "Updated notes.", ...}'
```

#### Body Parameters
```json
{
    "asset_name": "Laptop",
    "fixed_asset_type_id": "3640355000000319008",
    "asset_account_id": "3640355000000000367",
    "expense_account_id": "3640355000000000421",
    "depreciation_account_id": "3640355000000000367",
    "depreciation_method": "declining_method",
    "depreciation_frequency": "yearly",
    "depreciation_percentage": 12,
    "total_life": 60,
    "salvage_value": 100,
    "depreciation_start_date": "2024-12-17",
    "description": "string",
    "asset_cost": 1000,
    "computation_type": "prorata_basis",
    "warranty_expiry_date": "2027-12-17",
    "asset_purchase_date": "2024-12-17",
    "serial_no": "SN-0001",
    "dep_start_value": 1000,
    "notes": "This is a laptop Model 2024",
    "tags": [ { /* ... tag details ... */ } ],
    "custom_fields": [ { /* ... custom field details ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The fixed asset has been updated.",
    "fixed_asset": {
        "fixed_asset_id": "3640355000000319008",
        /* ... updated fixed asset details ... */
    }
}
```

## Update a Fixed Asset Type

### Description
Updates the fixed asset type with given information.

### Endpoint
`PUT /fixedassettypes/{fixed_asset_type_id}`

### OAuth Scope
`ZohoBooks.fixedasset.UPDATE`

### Arguments (Body Parameters)
*   **fixed_asset_type_name** (string, Required): Name of the fixed asset type.
*   **expense_account_id** (string, Required): Default depreciation expense account ID.
*   **depreciation_account_id** (string, Required): Default accumulated depreciation account ID.
*   **depreciation_method** (string, Required): Default depreciation method.
*   **depreciation_frequency** (string, Required): Default frequency.
*   **depreciation_percentage** (double, Required): Default percentage (Required if method is declining).
*   **total_life** (number, Required): Default total life in months (Required if method is straight-line).
*   **salvage_value** (double, Required): Default salvage value.
*   **computation_type** (string, Required): Default computation type.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/fixedassettypes/3640355000000319008?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"fixed_asset_type_name": "Updated Machines", ...}'
```

#### Body Parameters
```json
{
    "fixed_asset_type_name": "Machines",
    "expense_account_id": "3640355000000000421",
    "depreciation_account_id": "3640355000000000367",
    "depreciation_method": "declining_method",
    "depreciation_frequency": "yearly",
    "depreciation_percentage": 12,
    "total_life": 60,
    "salvage_value": 100,
    "computation_type": "prorata_basis"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The fixed asset type has been updated.", /* Corrected typo */
    "fixed_asset_type": {
        "fixed_asset_type_id": "3640355000000319008",
        /* ... updated type details ... */
    }
}
```

## Write Off Fixed Asset

### Description
Write off the fixed asset.

### Endpoint
`POST /fixedassets/{fixed_asset_id}/writeoff`

### OAuth Scope
`ZohoBooks.fixedasset.CREATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Date of write-off. Format [yyyy-mm-dd].
*   **expense_account_id** (string, Required): Account ID to record the write-off expense.
*   **reason** (string, Required): Reason for write-off.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/fixedassets/3640355000000319008/writeoff?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2024-12-17", "expense_account_id": "...", "reason": "..."}'
```

#### Body Parameters
```json
{
    "date": "2024-12-17",
    "expense_account_id": "3640355000000000421",
    "reason": "Asset is damaged"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Fixed asset has been written off"
}
```

# Base Currency Adjustment

## Overview

### Base Currency Adjustment
In Zoho Books you can have an insight on the profit or loss incurred due to the change in exchange rates and also can apply the changes to open transactions.

### End Points
*   `POST /basecurrencyadjustment`
*   `GET /basecurrencyadjustment`
*   `GET /basecurrencyadjustment/{base_currency_adjustment_id}`
*   `DELETE /basecurrencyadjustment/{base_currency_adjustment_id}`
*   `GET /basecurrencyadjustment/accounts`

### Attributes
*   **base_currency_adjustment_id** (string): ID of the Base Currency Adjustment
*   **adjustment_date** (string): Date of adjustment. Format [yyyy-mm-dd].
*   **exchange_rate** (double): Exchange rate of the currency.
*   **currency_id** (string): ID of currency for which adjustment is posted.
*   **accounts** (array): List of accounts affected by the adjustment.
    *   **account_id** (string): ID of the affected account.
    *   **account_name** (string): Name of the affected account.
    *   **bcy_balance** (double): Balance in base currency before adjustment.
    *   **fcy_balance** (double): Balance in foreign currency.
    *   **adjusted_balance** (double): Balance in base currency after adjustment.
    *   **gain_or_loss** (double): Gain or loss amount due to exchange rate change.
    *   **gl_specific_type** (integer): *(Internal type identifier)*.
*   **notes** (string): Notes for base currency adjustment.
*   **currency_code** (string): Currency Code involved in the Adjustment.

### Example
```json
{
    "base_currency_adjustment_id": "460000000039001",
    "adjustment_date": "2013-09-05",
    "exchange_rate": 1,
    "currency_id": "460000000000109",
    "accounts": [
        {
            "account_id": "460000000000364",
            "account_name": "Accounts Receivable",
            "bcy_balance": 171.47,
            "fcy_balance": 139.41,
            "adjusted_balance": 209.12,
            "gain_or_loss": 37.65,
            "gl_specific_type": 5
        }
    ],
    "notes": "Base Currency Adjustment against EUR",
    "currency_code": "EUR"
}
```

## Create Base Currency Adjustment

### Description
Creates a base currency adjustment for the given information.

### Endpoint
`POST /basecurrencyadjustment`

### OAuth Scope
`ZohoBooks.accountants.CREATE`

### Arguments (Body Parameters)
*   **currency_id** (string, Required): ID of currency for which adjustment needs to be posted.
*   **adjustment_date** (string, Required): Date of adjustment. Format [yyyy-mm-dd].
*   **exchange_rate** (double, Required): Exchange rate of the currency for the adjustment date.
*   **notes** (string, Required): Notes for base currency adjustment.

### Query Parameters
*   **account_ids** (string, Required): Comma-separated ID(s) of the accounts for which base currency adjustments need to be posted.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment?organization_id=10234695&account_ids=460000000000364' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"currency_id": "460000000000109", "adjustment_date": "2013-09-05", "exchange_rate": 1.2, "notes": "Adjustment for EUR"}'
```

#### Body Parameters
```json
{
    "currency_id": "460000000000109",
    "adjustment_date": "2013-09-05",
    "exchange_rate": 1, /* Use the actual rate for the date */
    "notes": "Base Currency Adjustment against EUR"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The adjustment has been made. The account balances will now reflect the adjustment.",
    "data": {
        "base_currency_adjustment_id": "460000000039001",
        "adjustment_date": "2013-09-05",
        "exchange_rate": 1,
        "currency_id": "460000000000109",
        "accounts": [
            {
                "account_id": "460000000000364",
                "account_name": "Accounts Receivable",
                "bcy_balance": 171.47,
                "fcy_balance": 139.41,
                "adjusted_balance": 209.12,
                "gain_or_loss": 37.65,
                "gl_specific_type": 5
            }
        ],
        "notes": "Base Currency Adjustment against EUR",
        "currency_code": "EUR"
    }
}
```

## Delete a Base Currency Adjustment

### Description
Deletes the base currency adjustment.

### Endpoint
`DELETE /basecurrencyadjustment/{base_currency_adjustment_id}`

### OAuth Scope
`ZohoBooks.accountants.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment/460000000039001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected base currency adjustment has been deleted."
}
```

## Get a Base Currency Adjustment

### Description
Get the base currency adjustment details.

### Endpoint
`GET /basecurrencyadjustment/{base_currency_adjustment_id}`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment/460000000039001?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "base_currency_adjustment_id": "460000000039001",
        "adjustment_date": "2013-09-05",
        "exchange_rate": 1,
        "currency_id": "460000000000109",
        "accounts": [
            {
                "account_id": "460000000000364",
                "account_name": "Accounts Receivable",
                "bcy_balance": 171.47,
                "fcy_balance": 139.41,
                "adjusted_balance": 209.12,
                "gain_or_loss": 37.65,
                "gl_specific_type": 5
            }
        ],
        "notes": "Base Currency Adjustment against EUR",
        "currency_code": "EUR"
    }
}
```

## List Account Details for Base Currency Adjustment

### Description
List of accounts having transaction with effect to the given exchange rate. (This endpoint essentially previews the effect of a potential adjustment).

### Endpoint
`GET /basecurrencyadjustment/accounts`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **currency_id** (string, Required): ID of currency for which adjustment effect needs to be previewed.
*   **adjustment_date** (string, Required): Date for the adjustment preview.
*   **exchange_rate** (double, Required): Exchange rate to use for preview.
*   **notes** (string, Required): Notes for the potential adjustment *(Note: Requiring notes for a GET preview seems unusual)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment/accounts?organization_id=10234695¤cy_id=460000000000109&adjustment_date=2013-09-05&exchange_rate=1¬es=Base%20Currency%20Adjustment%20against%20EUR' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "adjustment_date": "2013-09-05",
        "exchange_rate": 1,
        "currency_id": "460000000000109",
        "accounts": [
            {
                "account_id": "460000000000364",
                "account_name": "Accounts Receivable",
                "bcy_balance": 171.47, /* Current Base Currency Balance */
                "fcy_balance": 139.41, /* Foreign Currency Balance */
                "adjusted_balance": 209.12, /* Calculated Base Currency Balance at given rate */
                "gain_or_loss": 37.65, /* Calculated Gain/Loss */
                "gl_specific_type": 5
            }
        ],
        "notes": "Base Currency Adjustment against EUR",
        "currency_code": "EUR"
    }
}
```

## List Base Currency Adjustments

### Description
Lists base currency adjustments.

### Endpoint
`GET /basecurrencyadjustment`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **filter_by** (string): Filter list by date range. Allowed Values: `Date.All`, `Date.Today`, `Date.ThisWeek`, `Date.ThisMonth`, `Date.ThisQuarter`, `Date.ThisYear`.
*   **sort_column** (string): Sort list. Allowed Values: `adjustment_date`, `exchange_rate`, `currency_code`, `debit_or_credit`, `gain_or_loss`.
*   **last_modified_time** (string): Search using the Last Modified Time.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment?organization_id=10234695&filter_by=Date.ThisMonth' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "base_currency_adjustments": [
        {
            "base_currency_adjustment_id": "460000000039001",
            "adjustment_date": "2013-09-05",
            "exchange_rate": 1,
            "currency_id": "460000000000109",
            "currency_code": "EUR",
            "notes": "Base Currency Adjustment against EUR",
            "gain_or_loss": 37.65
        },
        {...},
        {...}
    ]
     /* Missing page_context object from example */
}
```
*Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example.*

# Projects

## Overview

### Projects
A project is a series of tasks performed over a period of time, to achieve certain targets. There can be many number of people working on a single project and a project may consist of single or multiple tasks. A project is billed and charged upon a customer whom the project was taken up for.

### End Points
*   `POST /projects`
*   `PUT /projects` *(Note: Likely for bulk/keyed updates)*
*   `GET /projects`
*   `PUT /projects/{project_id}`
*   `GET /projects/{project_id}`
*   `DELETE /projects/{project_id}`
*   `POST /projects/{project_id}/active`
*   `POST /projects/{project_id}/inactive`
*   `POST /projects/{project_id}/clone`
*   `POST /projects/{project_id}/users`
*   `GET /projects/{project_id}/users`
*   `POST /projects/{project_id}/users/invite`
*   `PUT /projects/{project_id}/users/{user_id}`
*   `GET /projects/{project_id}/users/{user_id}`
*   `DELETE /projects/{project_id}/users/{user_id}`
*   `POST /projects/{project_id}/comments`
*   `GET /projects/{project_id}/comments`
*   `DELETE /projects/{project_id}/comments/{comment_id}`
*   `GET /projects/{project_id}/invoices`
*   *(Note: PUT comment endpoint missing from list)*

### Attributes
*   **project_id** (string)
*   **project_name** (string): Name of the project. Max-length [100]
*   **customer_id** (string): Search projects by customer id.
*   **customer_name** (string)
*   **currency_code** (string)
*   **description** (string)
*   **status** (string): (e.g., `active`, `inactive`)
*   **billing_type** (string): The way you bill your customer. Allowed Values: `fixed_cost_for_project`, `based_on_project_hours`, `based_on_staff_hours`, `based_on_task_hours`
*   **rate** (float): Rate for fixed cost or project hours billing.
*   **budget_type** (string): Budgeting method.
*   **total_hours** (string): Total logged hours.
*   **total_amount** (double): Total project amount (calculated based on billing type).
*   **billed_hours** (string): Billed logged hours.
*   **billed_amount** (double): Billed amount.
*   **un_billed_hours** (string): Unbilled logged hours.
*   **un_billed_amount** (double): Unbilled amount.
*   **billable_hours** (string): Billable logged hours.
*   **billable_amount** (double): Billable amount.
*   **non_billable_hours** (string): Non-billable logged hours.
*   **non_billable_amount** (double): Non-billable amount.
*   **cost_budget_amount** (double): Budgeted Cost for the project.
*   **is_recurrence_associated** (boolean): Linked to recurring invoices.
*   **recurring_invoices** (array): Associated recurring invoice IDs/details.
*   **created_time** (string)
*   **show_in_dashboard** (boolean)
*   **tasks** (array): List of tasks in the project.
*   **users** (array): List of users assigned to the project.

### Example
```json
{
    "project_id": "460000000044019",
    "project_name": "REAL TIME TRAFFIC FLUX",
    "customer_id": "460000000044001",
    "customer_name": "SAF Instruments Inc",
    "currency_code": "USD",
    "description": "A simple algorithm is to be tested with vehicle detection application.",
    "status": "active",
    "billing_type": "fixed_cost_for_project",
    "rate": 5000,
    "budget_type": " ",
    "total_hours": "12:26",
    "total_amount": 500,
    "billed_hours": "12:27",
    "billed_amount": 500,
    "un_billed_hours": "00:00",
    "un_billed_amount": 0,
    "billable_hours": "12:26",
    "billable_amount": 500,
    "non_billable_hours": "0.00",
    "non_billable_amount": 0,
    "cost_budget_amount": "1000.00",
    "is_recurrence_associated": false,
    "recurring_invoices": [
        "string"
    ],
    "created_time": "2013-09-18T18:05:27+0530",
    "show_in_dashboard": true,
    "tasks": [
        {
            "task_id": "460000000044009",
            "task_name": "Distribution Analysis",
            "description": "A simple algorithm is to be tested with vehicle detection application.",
            "rate": 5000,
            "budget_hours": "0",
            "total_hours": "12:26",
            "billed_hours": "12:27",
            "un_billed_hours": "00:00",
            "non_billable_hours": "0.00",
            "status": "active",
            "is_billable": true,
            "task_custom_fields": ""
        }
    ],
    "users": [
        {
            "user_id": "460000000024003",
            "is_current_user": true,
            "user_name": "John David",
            "email": "johndavid@zilliuminc.com",
            "user_role": "admin",
            "status": "active",
            "rate": 5000,
            "budget_hours": "0",
            "total_hours": "12:26",
            "billed_hours": "12:27",
            "un_billed_hours": "00:00",
            "cost_rate": "10.00"
        }
    ]
}
```

## Activate Project

### Description
Mark project as active.

### Endpoint
`POST /projects/{project_id}/active`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected Projects have been marked as active."
}
```

## Assign Users

### Description
Assign users to a project.

### Endpoint
`POST /projects/{project_id}/users`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **users** (array, Required): List of users to assign.
    *   **user_id** (string, Required): ID of the user to assign.
    *   **rate** (string): Rate for this user (if billing type is staff hours).
    *   **budget_hours** (string): Budgeted hours for this user (if budget type is hours per staff).
    *   **cost_rate** (double): Cost rate for this user.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"users": [{"user_id": "USER_ID_TO_ASSIGN", "cost_rate": 15.00}]}'
```

#### Body Parameters
```json
{
    "users": [
        {
            "user_id": "460000000024003",
            "rate": "60.00", /* Example */
            "budget_hours": "50:00", /* Example */
            "cost_rate": "10.00"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Users added",
    "users": [
        {
            "user_id": "460000000024003",
            /* ... details of assigned user within the project context ... */
        },
        {...},
        {...}
    ]
}
```

## Clone Project

### Description
Cloning a project.

### Endpoint
`POST /projects/{project_id}/clone`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **project_name** (string, Required): Name for the new cloned project. Max-length [100].
*   **description** (string): Description for the new cloned project. Max-length [500].

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/clone?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"project_name": "Cloned Project Name", "description": "Cloned project desc."}'
```

#### Body Parameters
```json
{
    "project_name": "Network Distribution",
    "description": "Distribution for the system of intermediaries between the producer of goods and/or services and the final user"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Project has been cloned successfully.",
    "project": {
        "project_id": "NEW_PROJECT_ID",
        /* ... details of the newly cloned project ... */
    }
}
```

## Create a Project

### Description
Create a project.

### Endpoint
`POST /projects`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **project_name** (string, Required): Name of the project. Max-length [100].
*   **customer_id** (string, Required): ID of the customer.
*   **currency_id** (string): Currency ID.
*   **description** (string): Project description. Max-length [500].
*   **billing_type** (string, Required): Billing method. Allowed Values: `fixed_cost_for_project`, `based_on_project_hours`, `based_on_staff_hours`, `based_on_task_hours`.
*   **rate** (string): Hourly rate (for project/task/staff hours billing) or fixed cost.
*   **budget_type** (string): Budgeting method. Allowed Values: `total_project_cost`, `total_project_hours`, `hours_per_task`, `hours_per_staff`.
*   **budget_hours** (string): Budgeted hours (required for hour-based budgets).
*   **budget_amount** (string): Budgeted amount (required for cost-based budget).
*   **cost_budget_amount** (double): Budgeted cost for the project.
*   **user_id** (string, Required): ID of the user creating/assigned initially.
*   **tasks** (array): List of tasks to create with the project.
    *   **task_name** (string, Required): Name of the task.
    *   **description** (string): Task description.
    *   **rate** (string): Rate for this task (if billing is `based_on_task_hours`).
    *   **budget_hours** (string): Budgeted hours for this task (if budget is `hours_per_task`).
*   **users** (array): List of users to assign to the project.
    *   **user_id** (string, Required): ID of the user to assign.
    *   **rate** (string): Rate for this user (if billing is `based_on_staff_hours`).
    *   **budget_hours** (string): Budgeted hours for this user (if budget is `hours_per_staff`).
    *   **cost_rate** (double): Cost rate for this user.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"project_name": "Network Distribution", "customer_id": "460000000044001", ...}'
```

#### Body Parameters
```json
{
    "project_name": "Network Distribution",
    "customer_id": "460000000044001",
    "currency_id": "460000000098001",
    "description": "Distribution for the system of intermediaries between the producer of goods and/or services and the final user",
    "billing_type": "based_on_task_hours",
    "rate": " ", /* Or specific rate if based_on_project_hours */
    "budget_type": "hours_per_task", /* Example */
    "budget_hours": " ", /* Overall budget hours if needed */
    "budget_amount": " ", /* Overall budget amount if needed */
    "cost_budget_amount": "1000.00",
    "user_id": "USER_ID_HERE", /* ID of the user creating/initially assigned */
    "tasks": [
        {
            "task_name": "Task 1",
            "description": "First task",
            "rate": "50.00", /* Rate for this task */
            "budget_hours": "20:00" /* Budget for this task */
        }
    ],
    "users": [
        {
            "user_id": "USER_ID_1",
            "rate": "75.00", /* Rate for this staff member */
            "budget_hours": "40:00", /* Budget for this staff member */
            "cost_rate": "10.00"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The project has been created.",
    "project": {
        "project_id": "460000000044019",
        /* ... full project details ... */
    }
}
```

## Delete Comment

### Description
Deleting a comment.

### Endpoint
`DELETE /projects/{project_id}/comments/{comment_id}`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/comments/460000000044027?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The comment has been deleted."
}
```

## Delete Project

### Description
Deleting an existing project.

### Endpoint
`DELETE /projects/{project_id}`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The project has been deleted."
}
```

## Delete User Assignment

### Description
Remove user from a project.

### Endpoint
`DELETE /projects/{project_id}/users/{user_id}`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users/460000000024003?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The staff has been removed"
}
```

## Get a Project

### Description
Get the details of a project.

### Endpoint
`GET /projects/{project_id}`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "project": {
        "project_id": "460000000044019",
        /* ... full project details including tasks and users ... */
    }
}
```

## Get a User Assignment

### Description
Get details of a user's assignment within a project.

### Endpoint
`GET /projects/{project_id}/users/{user_id}`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users/460000000024003?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "user": {
        "user_id": "460000000024003",
        "is_current_user": true,
        "user_name": "John David",
        "email": "johndavid@zilliuminc.com",
        "user_role": "admin",
        "cost_rate": "10.00"
        /* Fields like rate, budget_hours specific to this project assignment would also be here */
    }
}
```

## Inactivate Project

### Description
Marking a project as inactive.

### Endpoint
`POST /projects/{project_id}/inactive`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected projects have been marked as inactive."
}
```

## Invite User

### Description
Invite a user to the project (and potentially to the organization if they are not already a user).

### Endpoint
`POST /projects/{project_id}/users/invite`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **user_name** (string, Required): Name of the user. Max-length [200].
*   **email** (string, Required): Email of the user. Max-length [100].
*   **user_role** (string): Role to assign (`staff`, `admin`, `timesheetstaff`).
*   **rate** (string): Rate for this user within the project.
*   **budget_hours** (string): Budgeted hours for this user within the project.
*   **cost_rate** (double): Cost rate for this user within the project.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users/invite?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"user_name": "New User", "email": "new.user@example.com", "user_role": "staff", ...}'
```

#### Body Parameters
```json
{
    "user_name": "John David",
    "email": "johndavid@zilliuminc.com",
    "user_role": "admin",
    "rate": " ", /* Or specific rate */
    "budget_hours": "0", /* Or specific budget */
    "cost_rate": "10.00"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The staff has been added.",
    "users": [
        {
            "user_id": "460000000024003", /* ID of the invited/added user */
            "user_name": "John David",
            "email": "johndavid@zilliuminc.com",
            "user_role": "admin",
            "is_current_user": true, /* If the inviting user is the same */
            "cost_rate": "10.00"
        },
        {...},
        {...}
    ]
}
```

## List Comments

### Description
Get comments for a project.

### Endpoint
`GET /projects/{project_id}/comments`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "comments": [
        {
            "comment_id": "460000000044027",
            "project_id": "460000000044019",
            "description": "A simple algorithm is to be tested with vehicle detection application.",
            "commented_by_id": "460000000024003",
            "commented_by": "John David",
            "is_current_user": true,
            "date": "YYYY-MM-DD", /* Corrected from original "6:52 PM" */
            "date_description": "19 days ago",
            "time": "6:52 PM"
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: `page_context` was missing from the original example).*

## List Invoices

### Description
Lists invoices created for this project.

### Endpoint
`GET /projects/{project_id}/invoices`

### OAuth Scope
`ZohoBooks.projects.READ`

### Query Parameters
*   **sort_column** (string): Sort invoices raised. Allowed Values: `invoice_number`, `date`, `total`, `balance`, `created_time`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "invoices": [
        {
            "invoice_id": "460000000044001",
            "customer_name": "SAF Instruments Inc",
            "status": "active", /* Status of the invoice */
            "invoice_number": "INV-00004",
            "reference_number": " ",
            "date": "YYYY-MM-DD", /* Corrected from original "6:52 PM" */
            "due_date": "YYYY-MM-DD", /* Corrected from original "6:52 PM" */
            "total": "310.75",
            "balance": "48.75",
            "created_time": "2013-09-18T18:05:27+0530"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 10, /* Example */
        "per_page": 450, /* Example */
        "report_name": "Project Invoices", /* Corrected from "Projects" */
        "has_more_page": false,
        "sort_order": "D",
        "sort_column": "created_time"
    }
}
```

## List Projects

### Description
List all projects with pagination.

### Endpoint
`GET /projects`

### OAuth Scope
`ZohoBooks.projects.READ`

### Query Parameters
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Inactive`.
*   **customer_id** (string): Filter by customer ID.
*   **sort_column** (string): Sort results. Allowed Values: `project_name`, `customer_name`, `rate`, `created_time`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects?organization_id=10234695&filter_by=Status.Active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "projects": [
        {
            "project_id": "460000000044019",
            "project_name": "REAL TIME TRAFFIC FLUX",
            "customer_id": "460000000044001",
            "customer_name": "SAF Instruments Inc",
            "description": "A simple algorithm...",
            "status": "active",
            "billing_type": "fixed_cost_for_project",
            "rate": 5000,
            "created_time": "2013-09-18T18:05:27+0530",
            "has_attachment": false,
            "total_hours": "12:26",
            "billable_hours": "12:26"
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected: original showed array */
        "page": 10, /* Example */
        "per_page": 450, /* Example */
        "report_name": "Projects",
        "has_more_page": false,
        "sort_order": "D",
        "sort_column": "created_time"
    }
}
```

## List Users

### Description
Get list of users associated with a project.

### Endpoint
`GET /projects/{project_id}/users`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "users": [
        {
            "user_id": "460000000024003",
            "is_current_user": true,
            "user_name": "John David",
            "email": "johndavid@zilliuminc.com",
            "user_role": "admin",
            "status": "active",
            "rate": 5000, /* Rate specific to this project assignment */
            "budget_hours": "0", /* Budget specific to this project assignment */
            "cost_rate": "10.00" /* Cost rate specific to this project assignment */
        },
        {...},
        {...}
    ]
}
```

## Post Comment

### Description
Post comment to a project.

### Endpoint
`POST /projects/{project_id}/comments`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **description** (string, Required): Comment text. Max-length [500].

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"description": "Client approved phase 1."}'
```

#### Body Parameters
```json
{
    "description": "Billing based on task hours"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Comments added.",
    "comment": { /* Corrected: original showed array */
        "project_id": "460000000044019",
        "comment_id": "460000000044027",
        "description": "A simple algorithm is to be tested with vehicle detection application.",
        "commented_by_id": "460000000024003",
        "commented_by": "John David",
        "date": "YYYY-MM-DD", /* Corrected from original "6:52 PM" */
        "date_description": "19 days ago",
        "time": "6:52 PM"
    }
}
```

## Update Project

### Description
Update details of a project.

### Endpoint
`PUT /projects/{project_id}`

### OAuth Scope
`ZohoBooks.projects.UPDATE`

### Arguments (Body Parameters)
*   **project_name** (string, Required): Name. Max-length [100].
*   **customer_id** (string, Required): Customer ID.
*   **currency_id** (string): Currency ID.
*   **description** (string): Description. Max-length [500].
*   **billing_type** (string, Required): Billing method.
*   **rate** (string): Rate.
*   **budget_type** (string): Budgeting method.
*   **budget_hours** (string): Budgeted hours.
*   **budget_amount** (string): Budgeted amount.
*   **cost_budget_amount** (double): Budgeted cost.
*   **user_id** (string, Required): User ID *(Note: Purpose unclear in update context unless changing owner)*.
*   **tasks** (array): List of tasks. Include `task_id` to update, omit for new, remove to delete.
*   **users** (array): List of users. Include `user_id` to update, omit for new, remove to delete assignment.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"project_name": "Updated Name", "description": "Updated desc.", ...}'
```

#### Body Parameters
```json
{
    "project_name": "Network Distribution",
    "customer_id": "460000000044001",
    "currency_id": "460000000098001",
    "description": "Distribution for the system...",
    "billing_type": "based_on_task_hours",
    "rate": " ",
    "budget_type": " ",
    "budget_hours": " ",
    "budget_amount": " ",
    "cost_budget_amount": "1000.00",
    "user_id": "USER_ID_HERE",
    "tasks": [ { /* ... task details with task_id for updates ... */ } ],
    "users": [ { /* ... user details with user_id for updates ... */ } ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The project information has been updated.",
    "project": {
        "project_id": "460000000044019",
        /* ... updated project details ... */
    }
}
```

## Update Project using Custom Field

### Description
Update a project using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /projects` *(Note: This endpoint is typically for bulk updates or upserts with unique keys)*

### OAuth Scope
`ZohoBooks.projects.UPDATE`

### Headers
*(Assumed based on description, not shown in example)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*(Same arguments as Create Project, ensure `task_id` and `user_id` are included in the arrays for updates)*

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/projects?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"project_name": "Updated Project Name", "customer_id": "...", ...}'
```

#### Body Parameters
```json
{
    "project_name": "Network Distribution",
    "customer_id": "460000000044001",
    "currency_id": "460000000098001",
    "description": "Distribution for the system of intermediaries...",
    "billing_type": "based_on_task_hours",
    "rate": " ",
    "budget_type": " ",
    "budget_hours": " ",
    "budget_amount": " ",
    "cost_budget_amount": "1000.00",
    "user_id": "USER_ID_HERE",
    "tasks": [
        {
            "task_id": "TASK_ID_TO_UPDATE", /* Required to update */
            "task_name": "Updated Task Name",
            /* ... other task fields ... */
        },
        { /* New Task Example */
            "task_name": "New Task",
            "rate": "60.00"
        }
    ],
    "users": [
        {
            "user_id": "USER_ID_TO_UPDATE", /* Required to update */
            "rate": "80.00",
            "cost_rate": "15.00"
        },
        { /* New User Assignment Example */
             "user_id": "NEW_USER_ID",
             "rate": "70.00",
             "cost_rate": "12.00"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The project information has been updated.",
    "project": {
        "project_id": "460000000044019",
        /* ... updated project details ... */
    }
}
```

## Update User Assignment

### Description
Update details of a user's assignment within a project (like rate, budget).

### Endpoint
`PUT /projects/{project_id}/users/{user_id}`

### OAuth Scope
`ZohoBooks.projects.UPDATE`

### Arguments (Body Parameters)
*   **user_name** (string): *(Likely read-only here, update via main user settings).*
*   **user_role** (string): Update role within project context? *(Unlikely, role is usually org-level)*. Allowed: `staff`, `admin`, `timesheetstaff`.
*   **rate** (float): Update hourly rate for this user on this project.
*   **budget_hours** (string): Update budgeted hours for this user on this project.
*   **cost_rate** (double): Update cost rate for this user on this project.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/projects/460000000044019/users/460000000024003?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"rate": 6000, "cost_rate": 12.00}'
```

#### Body Parameters
```json
{
    /* "user_name": "John David", /* Read-only likely */
    /* "user_role": "admin", /* Read-only likely */
    "rate": 5000,
    "budget_hours": "0",
    "cost_rate": "10.00"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The staff information has been updated.",
    "user": { /* Corrected: original showed array */
        "user_id": "460000000024003",
        "user_name": "John David",
        "email": "johndavid@zilliuminc.com",
        "user_role": "admin",
        "is_current_user": true,
        "cost_rate": "12.00", /* Updated value */
        "rate": 6000 /* Updated value */
        /* Updated budget_hours should also reflect here */
    }
}
```

# Tasks

## Overview

### Tasks
A project comprises of a single or multiple tasks that need to be completed. You need a task to the project before you log time.

### End Points
*   `POST /projects/{project_id}/tasks`
*   `GET /projects/{project_id}/tasks`
*   `PUT /projects/{project_id}/tasks/{task_id}`
*   `GET /projects/{project_id}/tasks/{task_id}`
*   `DELETE /projects/{project_id}/tasks/{task_id}`

### Attributes
*   **project_id** (string): Unique ID of the project generated by the server.
*   **task_id** (string): Unique ID of the task generated by the server.
*   **currency_id** (string): The currency id of the currency *(Note: Currency is usually project-level, may be contextual)*.
*   **customer_id** (string): Customer ID of the customer for whom the task is created.
*   **task_name** (string): The name of the task. Max-length [100].
*   **project_name** (string): The name of the project.
*   **customer_name** (string): Name of the customer to whom the task is created.
*   **billed_hours** (string): The total hours that are billed. Format "HH:MM" *(Note: Original doc listed type as double)*.
*   **log_time** (string): Total hours logged in the project. Format "HH:MM" *(Note: Original doc listed type as double)*.
*   **un_billed_hours** (string): Total hours that are unbilled. Format "HH:MM" *(Note: Original doc listed type as double)*.
*   **description** (string): The description of the task.
*   **rate** (integer): Hourly rate for the task.
*   **budget_hours** (integer): Budgeted hours for the task.
*   **status** (string): Status of the task (e.g., 'active', 'inactive').
*   **is_billable** (boolean): Whether the task is billable.

### Example
```json
{
    "project_id": "90300000072369",
    "task_id": "90300000072369",
    "currency_id": 982000000000190,
    "customer_id": "903000000000099",
    "task_name": "Painting",
    "description": "",
    "rate": 3,
    "budget_hours": 10,
    "status": "active",
    "is_billable": true,
    "project_name": "Furniture Manufacturing",
    "customer_name": "Sujin Kumar",
    "billed_hours": "12:06",
    "log_time": "13:06",
    "un_billed_hours": "01:00"
}
```

## Add a Task

### Description
Add a task to a project.

### Endpoint
`POST /projects/{project_id}/tasks`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **task_name** (string, Required): The name of the task. Max-length [100].
*   **description** (string): The description of the task.
*   **rate** (integer): Hourly rate for the task (applies if project billing is `based_on_task_hours`).
*   **budget_hours** (integer): Budgeted hours for the task (applies if project budget is `hours_per_task`).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/90300000072369/tasks?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"task_name": "Painting", "rate": 3}'
```

#### Body Parameters
```json
{
    "task_name": "Painting",
    "description": "",
    "rate": 3,
    "budget_hours": 10 /* Example budget */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Task has been added.", /* Corrected message */
    "task": {
        "project_id": "90300000072369",
        "task_id": "90300000072370", /* Example New Task ID */
        "currency_id": 982000000000190,
        "customer_id": "903000000000099",
        "task_name": "Painting",
        "description": "",
        "rate": 3,
        "budget_hours": 10,
        "status": "active",
        "is_billable": true, /* Assuming default */
        "project_name": "Furniture Manufacturing",
        "customer_name": "Sujin Kumar",
        "billed_hours": "00:00", /* Should be 0 for new task */
        "log_time": "00:00", /* Should be 0 for new task */
        "un_billed_hours": "00:00" /* Should be 0 for new task */
    }
}
```

## Delete Task

### Description
Delete a task added to a project.

### Endpoint
`DELETE /projects/{project_id}/tasks/{task_id}`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/90300000072369/tasks/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The task has been deleted successfully."
}
```

## Get a Task

### Description
Get the details of a task.

### Endpoint
`GET /projects/{project_id}/tasks/{task_id}`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/90300000072369/tasks/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "task": {
        "project_id": "90300000072369",
        "project_name": "Furniture Manufacturing",
        "task_id": "90300000072369",
        "task_name": "Painting",
        "description": "",
        "rate": 3,
        "budget_hours": 10,
        "status": "active",
        "is_billable": true,
        "customer_id": "903000000000099",
        "customer_name": "Sujin Kumar",
        "billed_hours": "12:06",
        "log_time": "13:06",
        "un_billed_hours": "01:00"
    }
}
```

## List Tasks

### Description
Get list of tasks added to a project.

### Endpoint
`GET /projects/{project_id}/tasks`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/90300000072369/tasks?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "tasks": [
        {
            "project_id": "90300000072369",
            "task_id": "90300000072369",
            "currency_id": 982000000000190,
            "customer_id": "903000000000099",
            "task_name": "Painting",
            "description": "",
            "rate": 3,
            "budget_hours": 10,
            "status": "active",
            "is_billable": true,
            "project_name": "Furniture Manufacturing",
            "customer_name": "Sujin Kumar",
            "billed_hours": "12:06",
            "log_time": "13:06",
            "un_billed_hours": "01:00"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Tasks",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Update a Task

### Description
Update the details of a task.

### Endpoint
`PUT /projects/{project_id}/tasks/{task_id}`

### OAuth Scope
`ZohoBooks.projects.UPDATE`

### Arguments (Body Parameters)
*   **task_name** (string, Required): The name of the task. Max-length [100].
*   **description** (string): The description of the task.
*   **rate** (integer): Hourly rate for the task.
*   **budget_hours** (integer): Budgeted hours for the task.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/projects/90300000072369/tasks/90300000072369?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"task_name": "Updated Painting Task", "rate": 4}'
```

#### Body Parameters
```json
{
    "task_name": "Updated Painting Task",
    "description": "Updated description",
    "rate": 4,
    "budget_hours": 12 /* Updated budget */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The task information has been updated.",
    "task": {
        "project_id": "90300000072369",
        "task_id": "90300000072369",
        "task_name": "Updated Painting Task",
        "description": "Updated description",
        "rate": 4,
        "budget_hours": 12,
        "status": "active",
        "is_billable": true,
        "project_name": "Furniture Manufacturing",
        "customer_name": "Sujin Kumar",
        "billed_hours": "12:06",
        "log_time": "13:06",
        "un_billed_hours": "01:00"
    }
}
```

# Time Entries

## Overview

### Time Entries
Time entries are various entries of time made by users in a project, based on the time they spent on a project, in a task.

### End Points
*   `POST /projects/timeentries`
*   `GET /projects/timeentries`
*   `DELETE /projects/timeentries` (Bulk Delete)
*   `PUT /projects/timeentries/{time_entry_id}`
*   `GET /projects/timeentries/{time_entry_id}`
*   `DELETE /projects/timeentries/{time_entry_id}` (Single Delete)
*   `POST /projects/timeentries/{time_entry_id}/timer/start`
*   `POST /projects/timeentries/timer/stop`
*   `GET /projects/timeentries/runningtimer/me`

### Attributes
*   **time_entry_id** (string)
*   **project_id** (string): Search time entries by project_id.
*   **project_name** (string)
*   **customer_id** (string): Search projects by customer id.
*   **customer_name** (string)
*   **task_id** (string): ID of the task.
*   **task_name** (string)
*   **user_id** (string): Search time entries by user_id.
*   **user_name** (string)
*   **is_current_user** (boolean)
*   **log_date** (string): Date time was logged. Format [yyyy-mm-dd].
*   **begin_time** (string): Start time. Format [HH:mm].
*   **end_time** (string): End time. Format [HH:mm].
*   **log_time** (string): Duration logged. Format [HH:mm].
*   **is_billable** (boolean)
*   **billed_status** (string): (e.g., `unbilled`, `invoiced`).
*   **invoice_id** (string): ID of the invoice this entry is billed on.
*   **notes** (string)
*   **timer_started_at** (string): Timestamp when timer started.
*   **timer_started_at_utc_time** (string): UTC timestamp when timer started.
*   **timer_duration_in_minutes** (string): Current running timer duration (minutes).
*   **timer_duration_in_seconds** (string): Current running timer duration (seconds).
*   **created_time** (string)
*   **timesheet_custom_fields** (array): Custom fields associated with the timesheet entry. *(Note: Original doc listed type as string)*.
*   **cost_rate** (double): Hourly cost rate for this specific time entry.
*   **cost_amount** (double): Calculated cost amount (cost_rate * hours).

### Example
```json
{
    "time_entry_id": "460000000044021",
    "project_id": "460000000044019",
    "project_name": "REAL TIME TRAFFIC FLUX",
    "customer_id": "460000000044001",
    "customer_name": "SAF Instruments Inc",
    "task_id": "460000000044009",
    "task_name": "Distribution Analysis",
    "user_id": "460000000024003",
    "user_name": "John David",
    "is_current_user": true,
    "log_date": "2013-09-17",
    "begin_time": "03:00",
    "end_time": "04:00",
    "log_time": "05:00",
    "is_billable": true,
    "billed_status": "unbilled",
    "invoice_id": null,
    "notes": null,
    "timer_started_at": null,
    "timer_started_at_utc_time": null,
    "timer_duration_in_minutes": null,
    "timer_duration_in_seconds": null,
    "created_time": "2013-09-18T18:05:27+0530",
    "timesheet_custom_fields": [], /* Example empty array */
    "cost_rate": 10.00, /* Example cost rate */
    "cost_amount": 50.00 /* Example calculated cost */
}
```

## Delete Time Entries (Bulk)

### Description
Deleting time entries.

### Endpoint
`DELETE /projects/timeentries`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Query Parameters
*   **timeentry_ids** (string, Required): Comma-separated list of time entry IDs to delete.

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries?organization_id=10234695&timeentry_ids=ID1,ID2,ID3' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The selected timesheet entries have been deleted"
}
```

## Delete Time Entry (Single)

### Description
Deleting a logged time entry.

### Endpoint
`DELETE /projects/timeentries/{time_entry_id}`

### OAuth Scope
`ZohoBooks.projects.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/460000000044021?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The time entry has been deleted."
}
```

## Get a Time Entry

### Description
Get details of a time entry.

### Endpoint
`GET /projects/timeentries/{time_entry_id}`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/460000000044021?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "time_entry": {
        "time_entry_id": "460000000044021",
        "project_id": "460000000044019",
        "project_name": "REAL TIME TRAFFIC FLUX",
        "customer_id": "460000000044001",
        "customer_name": "SAF Instruments Inc",
        "task_id": "460000000044009",
        "task_name": "Distribution Analysis",
        "user_id": "460000000024003",
        "user_name": "John David",
        "is_current_user": true,
        "log_date": "2013-09-17",
        "begin_time": "03:00",
        "end_time": "04:00",
        "log_time": "05:00",
        "is_billable": true,
        "billed_status": "unbilled",
        "invoice_id": null,
        "notes": null,
        "timer_started_at": null,
        "timer_started_at_utc_time": null,
        "timer_duration_in_minutes": null,
        "timer_duration_in_seconds": null,
        "created_time": "2013-09-18T18:05:27+0530",
        "cost_rate": 0.00,
        "cost_amount": 0.00
    }
}
```

## Get Running Timer

### Description
Get current running timer for the authenticated user.

### Endpoint
`GET /projects/timeentries/runningtimer/me`

### OAuth Scope
`ZohoBooks.projects.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/runningtimer/me?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "time_entry": {
        "time_entry_id": "460000000044021", /* ID of the running time entry */
        "project_id": "460000000044019",
        "project_name": "REAL TIME TRAFFIC FLUX",
        "task_id": "460000000044009",
        "task_name": "Distribution Analysis",
        "user_id": "460000000024003",
        "user_name": "John David",
        "is_billable": true,
        "notes": "Working on distribution analysis",
        "timer_started_at": "2023-10-27T10:00:00+0530",
        "timer_started_at_utc_time": "2023-10-27T04:30:00Z",
        "timer_duration_in_minutes": "125",
        "timer_duration_in_seconds": "7500"
        /* Other fields like log_date might be null/empty until stopped */
    }
}
```
*(Note: If no timer is running, the `time_entry` object might be null or empty)*

## List Time Entries

### Description
List all time entries with pagination.

### Endpoint
`GET /projects/timeentries`

### OAuth Scope
`ZohoBooks.projects.READ`

### Query Parameters
*   **from_date** (string): Fetch entries logged on or after this date. Format [yyyy-mm-dd].
*   **to_date** (string): Fetch entries logged on or before this date. Format [yyyy-mm-dd].
*   **filter_by** (string): Filter by date range or status. Allowed Values: `Date.All`, `Date.Today`, ..., `Date.CustomDate`, `Status.Unbilled`, `Status.Invoiced`.
*   **project_id** (string): Filter by Project ID.
*   **user_id** (string): Filter by User ID.
*   **sort_column** (string): Sort results. Allowed Values: `project_name`, `task_name`, `user_name`, `log_date`, `timer_started_at`, `customer_name`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries?organization_id=10234695&filter_by=Status.Unbilled' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "time_entries": [
        {
            "time_entry_id": "460000000044021",
            "project_id": "460000000044019",
            "project_name": "REAL TIME TRAFFIC FLUX",
            "customer_id": "460000000044001",
            "customer_name": "SAF Instruments Inc",
            "task_id": "460000000044009",
            "task_name": "Distribution Analysis",
            "user_id": "460000000024003",
            "is_current_user": true,
            "user_name": "John David",
            "log_date": "2013-09-17",
            "begin_time": "03:00",
            "end_time": "04:00",
            "log_time": "05:00",
            "is_billable": true,
            "billed_status": "unbilled",
            "invoice_id": null,
            "notes": null,
            "timer_started_at": null,
            "timer_duration_in_minutes": null,
            "created_time": "2013-09-18T18:05:27+0530",
            "cost_rate": 0.00,
            "cost_amount": 0.00
        },
        {...},
        {...}
    ],
    "page_context": { /* Corrected structure */
        "page": 1, /* Example */
        "per_page": 200, /* Example */
        "report_name": "TimeEntries", /* Corrected name */
        "has_more_page": false,
        "sort_order": "D",
        "sort_column": "customer_name"
    }
}
```

## Log Time Entries

### Description
Logging time entries.

### Endpoint
`POST /projects/timeentries`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Arguments (Body Parameters)
*   **project_id** (string, Required): ID of the project.
*   **task_id** (string, Required): ID of the task.
*   **user_id** (string, Required): ID of the user logging time.
*   **log_date** (string, Required): Date time was spent. Format [yyyy-mm-dd].
*   **log_time** (string): Duration spent. Either send this OR begin/end time. Format [HH:mm].
*   **begin_time** (string): Start time. Format [HH:mm].
*   **end_time** (string): End time. Format [HH:mm].
*   **is_billable** (boolean): Whether the time is billable.
*   **notes** (string): Description of work. Max-length [500].
*   **start_timer** (boolean): Set to `true` to start the timer immediately after logging this entry. *(Note: Original doc type was string)*.
*   **cost_rate** (double): Hourly cost rate for this entry.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"project_id": "PROJECT_ID", "task_id": "TASK_ID", "user_id": "USER_ID", "log_date": "2023-10-27", "log_time": "02:30", "is_billable": true}'
```

#### Body Parameters
```json
{
    "project_id": "460000000044019", /* Example Project ID */
    "task_id": "460000000044001",
    "user_id": "460000000024003",
    "log_date": "2013-09-17",
    /* Provide either log_time OR begin_time/end_time */
    /* "log_time": "05:00", */
    "begin_time": "10:00",
    "end_time": "15:00",
    "is_billable": true,
    "notes": "Analysis work completed.",
    "start_timer": false, /* Example: Do not start timer */
    "cost_rate": 10.00
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your timesheet entry has been added.",
    "time_entry": {
        "time_entry_id": "460000000044021",
        "project_id": "460000000044019",
        "task_id": "460000000044001",
        "user_id": "460000000024003",
        "log_date": "2013-09-17",
        "log_time": "05:00",
        "begin_time": "10:00",
        "end_time": "15:00",
        "is_billable": true,
        "notes": "Analysis work completed.",
        "cost_rate": 10.00,
        "cost_amount": 50.00,
        /* ... other time entry details ... */
    }
}
```

## Start Timer

### Description
Start tracking time spent for a specific task within a project. *(Note: Endpoint targets a time entry ID, which seems counter-intuitive. Starting a timer usually relates to a Project/Task combination and might create a new time entry or resume an existing one. Clarification needed on API behavior)*.

### Endpoint
`POST /projects/timeentries/{time_entry_id}/timer/start`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/460000000044021/timer/start?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The timer has been started.",
    "time_entry": {
        "time_entry_id": "460000000044021",
        /* ... time entry details, potentially with updated timer fields like timer_started_at ... */
    }
}
```

## Stop Timer

### Description
Stop tracking time for the currently running timer for the authenticated user.

### Endpoint
`POST /projects/timeentries/timer/stop`

### OAuth Scope
`ZohoBooks.projects.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/timer/stop?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Timer has been stopped successfully.",
    "time_entry": {
        "time_entry_id": "460000000044021", /* ID of the time entry that was stopped */
        "log_date": "2023-10-27",
        "log_time": "02:05", /* Example final logged time */
        "begin_time": null, /* Timer entries might not have begin/end */
        "end_time": null,
        /* ... final time entry details including log_time ... */
    }
}
```

## Update Time Entry

### Description
Update logged time entry.

### Endpoint
`PUT /projects/timeentries/{time_entry_id}`

### OAuth Scope
`ZohoBooks.projects.UPDATE`

### Arguments (Body Parameters)
*   **project_id** (string, Required): ID of the project.
*   **task_id** (string, Required): ID of the task.
*   **user_id** (string, Required): ID of the user.
*   **log_date** (string, Required): Date time was spent. Format [yyyy-mm-dd].
*   **log_time** (string): Duration spent. Either send this OR begin/end time. Format [HH:mm].
*   **begin_time** (string): Start time. Format [HH:mm].
*   **end_time** (string): End time. Format [HH:mm].
*   **is_billable** (boolean): Whether it is billable.
*   **notes** (string): Description of work. Max-length [500].
*   **cost_rate** (double): Hourly cost rate.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/projects/timeentries/460000000044021?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"project_id": "PROJECT_ID", "task_id": "TASK_ID", "user_id": "USER_ID", "log_date": "2013-09-17", "log_time": "05:30", ...}'
```

#### Body Parameters
```json
{
    "project_id": "460000000044019", /* Example Project ID */
    "task_id": "460000000044001",
    "user_id": "460000000024003",
    "log_date": "2013-09-17",
    "log_time": "05:30", /* Updated duration */
    /* begin_time and end_time might be cleared if log_time is provided */
    "is_billable": true,
    "notes": "Updated notes",
    "cost_rate": 12.50 /* Updated cost rate */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The timesheet's information has been updated.",
    "time_entry": {
        "time_entry_id": "460000000044021",
        "log_time": "05:30",
        "notes": "Updated notes",
        "cost_rate": 12.50,
        "cost_amount": 68.75, /* Example updated calculation */
        /* ... other updated time entry details ... */
    }
}
```

# Users

## Overview

### Users
Users are various individuals/entities that are a part of an organisation. Each user will have a different role to play, like admin, staff etc., .

### End Points
*   `POST /users`
*   `GET /users`
*   `PUT /users/{user_id}`
*   `GET /users/{user_id}`
*   `DELETE /users/{user_id}`
*   `GET /users/me`
*   `POST /users/{user_id}/invite`
*   `POST /users/{user_id}/active`
*   `POST /users/{user_id}/inactive`

### Attributes
*(Note: Attributes section was missing in the provided overview file. Attributes are typically found within the specific Get/List operation details.)*

## Create a User

### Description
Create a user for your organization.

### Endpoint
`POST /users`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **name** (string, Required): Name of the user.
*   **email** (string, Required): Email address of the user.
*   **role_id** (string): ID of the role to assign.
*   **cost_rate** (double): Hourly cost rate for the user.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/users?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"name": "Sujin Kumar", "email": "johndavid@zilliuminc.com", "role_id": "982000000006005"}'
```

#### Body Parameters
```json
{
    "name": "Sujin Kumar",
    "email": "johndavid@zilliuminc.com",
    "role_id": "982000000006005",
    "cost_rate": 0
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Your invitation has been sent."
}
```
*(Note: Creating a user sends an invitation. The user needs to accept it to become active).*

## Delete a User

### Description
Delete a user associated to the organization.

### Endpoint
`DELETE /users/{user_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The user has been removed from your organization."
}
```

## Get a User

### Description
Get the details of a user.

### Endpoint
`GET /users/{user_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "user": {
        "user_id": "982000000554041",
        "name": "Sujin Kumar",
        "email_ids": [
            {
                "email": "johndavid@zilliuminc.com",
                "is_selected": true
            }
        ],
        "status": "active",
        "user_role": "admin",
        "user_type": "zoho",
        "role_id": "982000000006005",
        "cost_rate": 0,
        "photo_url": "https://contacts.zoho.com/file?ID=...",
        "is_employee": true,
        "created_time": "2016-06-05T02:30:08-0700",
        "custom_fields": [] /* Corrected: Should be array */
    }
}
```

## Get Current User

### Description
Get the details of the current user (associated with the OAuth token).

### Endpoint
`GET /users/me`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/users/me?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "user": {
        "user_id": "982000000554041",
        "name": "Sujin Kumar",
        "email_ids": [
            {
                "email": "johndavid@zilliuminc.com",
                "is_selected": true
            }
        ],
        "status": "active",
        "user_role": "admin",
        "user_type": "zoho",
        "role_id": "982000000006005",
        "cost_rate": 0,
        "photo_url": "https://contacts.zoho.com/file?ID=...",
        "is_employee": true,
        "created_time": "2016-06-05T02:30:08-0700",
        "custom_fields": [] /* Corrected: Should be array */
    }
}
```

## Invite a User

### Description
Send invitation email to a user *(Note: This is likely for re-sending an invitation to an existing 'invited' user, use POST /users to create/invite initially)*.

### Endpoint
`POST /users/{user_id}/invite`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041/invite?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Your invitation has been sent."
}
```

## List Users

### Description
Get the list of all users in the organization.

### Endpoint
`GET /users`

### OAuth Scope
`ZohoBooks.settings.READ`

### Query Parameters
*   **filter_by** (string): Filter users by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Inactive`, `Status.Invited`, `Status.Deleted`.
*   **sort_column** (string): Sort users. Allowed Values: `name`, `email`, `user_role`, `status`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/users?organization_id=10234695&filter_by=Status.Active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "users": [
        {
            "user_id": "982000000554041",
            "role_id": "982000000006005",
            "name": "Sujin Kumar",
            "email": "johndavid@zilliuminc.com",
            "user_role": "admin",
            "status": "active",
            "is_current_user": true,
            "photo_url": "https://contacts.zoho.com/file?ID=...",
            "is_customer_segmented": false,
            "is_vendor_segmented": false,
            "user_type": "zoho"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 10,
        "has_more_page": false,
        "report_name": "Users",
        "sort_column": "name",
        "sort_order": "A"
    }
}
```

## Mark User as Active

### Description
Mark an inactive user as active.

### Endpoint
`POST /users/{user_id}/active`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The user has been marked as active."
}
```

## Mark User as Inactive

### Description
Mark an active user as inactive.

### Endpoint
`POST /users/{user_id}/inactive`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The user has been marked as inactive."
}
```

## Update a User

### Description
Update the details of a user.

### Endpoint
`PUT /users/{user_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **name** (string, Required): Name of the user.
*   **email** (string, Required): Email address of the user.
*   **role_id** (string): ID of the role to assign.
*   **cost_rate** (double): Hourly cost rate for the user.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/users/982000000554041?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"name": "Sujin K", "role_id": "NEW_ROLE_ID", "cost_rate": 15.0}'
```

#### Body Parameters
```json
{
    "name": "Sujin K", /* Updated name */
    "email": "johndavid@zilliuminc.com", /* Cannot typically update primary email */
    "role_id": "982000000006007", /* Updated role ID */
    "cost_rate": 15.0 /* Updated cost rate */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The user information has been updated."
    /* May optionally return the updated user object */
}
```

# Items

## Overview

### Items
Items are the products or services that you sell to your customers.

### End Points
*   `POST /items`
*   `PUT /items` *(Note: Likely for bulk/keyed updates, see Update Item using Custom Field)*
*   `GET /items`
*   `PUT /items/{item_id}`
*   `GET /items/{item_id}`
*   `DELETE /items/{item_id}`
*   `PUT /item/{item_id}/customfields`
*   `POST /items/{item_id}/active`
*   `POST /items/{item_id}/inactive`

### Attributes
*   **item_id** (string): ID of the item.
*   **name** (string): Name of the item. Max-length [100].
*   **status** (string): Status of the item (`active` or `inactive`).
*   **description** (string): Description for the item. Max-length [2000].
*   **rate** (double): Price of the item.
*   **unit** (string): Measurement unit for the item.
*   **tax_id** (string): Not applicable 🇺🇸 , 🇮🇳 - ID of the tax associated.
*   **purchase_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - ID of the purchase tax rule.
*   **sales_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - ID of the sales tax rule.
*   **tax_name** (string): Name of the associated tax.
*   **hsn_or_sac** (string): 🇮🇳 , 🇰🇪 , 🇿🇦 only - HSN/SAC Code.
*   **sat_item_key_code** (string): 🇲🇽 only - SAT Item Key Code.
*   **unitkey_code** (string): 🇲🇽 only - SAT Unit Key Code.
*   **tax_percentage** (string): Percent of the tax *(Note: Data type string, likely double/float)*.
*   **tax_type** (string): Type of the tax (e.g., `tax`, `tax_group`).
*   **sku** (string): SKU value, unique throughout the product.
*   **product_type** (string): Type of item (`goods`, `service`, `digital_service`, etc. - varies by edition).
*   **item_tax_preferences** (array): 🇮🇳 only - Tax preferences.
*   **custom_fields** (array): Custom fields.
*   **locations** (array): Location-specific stock details (for inventory items).

### Example
```json
{
    "item_id": 45667789900,
    "name": "Hard Drive",
    "status": "active",
    "description": "500GB",
    "rate": 120,
    "unit": "100GB",
    "tax_id": 982000000037049,
    "purchase_tax_rule_id": 127919000000106780,
    "sales_tax_rule_id": 127919000000106780,
    "tax_name": "Sales Tax",
    "hsn_or_sac": "string",
    "sat_item_key_code": "string",
    "unitkey_code": "string",
    "tax_percentage": "70%",
    "tax_type": "tax",
    "sku": "s12345",
    "product_type": "goods",
    "item_tax_preferences": [
        {
            "tax_id": 982000000037049,
            "tax_specification": "intra"
        }
    ],
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal"
        }
    ],
    "locations": [
        {
            "location_id": "460000000038080",
            "location_name": "",
            "status": "active",
            "is_primary": false,
            "location_stock_on_hand": "",
            "location_available_stock": "",
            "location_actual_available_stock": ""
        }
    ]
}
```

## Create an Item

### Description
Create a new item.

### Endpoint
`POST /items`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **name** (string, Required): Name of the item. Max-length [100].
*   **rate** (double, Required): Price of the item.
*   **description** (string): Description. Max-length [2000].
*   **tax_id** (string): Not applicable 🇺🇸 , 🇮🇳 - Tax ID to associate.
*   **locations** (array): Initial stock details per location (for inventory items).
    *   **location_id** (string, Required): ID of the location.
    *   **initial_stock** (string): Initial stock quantity at this location.
    *   **initial_stock_rate** (string): Initial stock rate at this location.
*   **purchase_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - Purchase tax rule ID.
*   **sales_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - Sales tax rule ID.
*   **tax_percentage** (string): Tax percentage *(Note: Data type string, likely double/float)*.
*   **sku** (string): SKU value (must be unique).
*   **product_type** (string): Type (`goods`, `service`, etc. - varies by edition).
*   **hsn_or_sac** (string): 🇮🇳 , 🇰🇪 , 🇿🇦 only - HSN/SAC Code.
*   **sat_item_key_code** (string): 🇲🇽 only - SAT Item Key Code.
*   **unitkey_code** (string): 🇲🇽 only - SAT Unit Key Code.
*   **is_taxable** (boolean): 🇮🇳 , 🇺🇸 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Is the item taxable.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Tax exemption ID (Mandatory if `is_taxable` is false).
*   **purchase_tax_exemption_id** (string): 🇰🇪 , 🇿🇦 only - Purchase tax exemption ID (Mandatory if `is_taxable` is false).
*   **account_id** (string): Sales/Income account ID.
*   **avatax_tax_code** (string): Avalara Integration only - Tax code. Max-length [25].
*   **avatax_use_code** (string): Avalara Integration only - Use code. Max-length [25].
*   **item_type** (string): Type (`sales`, `purchases`, `sales_and_purchases`, `inventory`). Default: `sales`.
*   **purchase_description** (string): Purchase description.
*   **purchase_rate** (string): Purchase price.
*   **purchase_account_id** (string): COGS account ID (Mandatory if `item_type` involves purchases/inventory).
*   **inventory_account_id** (string): Inventory asset account ID (Mandatory if `item_type` is inventory).
*   **vendor_id** (string): Preferred vendor ID.
*   **reorder_level** (string): Reorder level quantity.
*   **item_tax_preferences** (array): 🇮🇳 only - Tax preferences.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/items?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"name": "New Item", "rate": 50.00, ...}'
```

#### Body Parameters
```json
{
    "name": "Hard Drive",
    "rate": 120,
    "description": "500GB",
    "tax_id": 982000000037049,
    "locations": [
        {
            "location_id": "460000000038080",
            "initial_stock": "10", /* Example value */
            "initial_stock_rate": "100" /* Example value */
        }
    ],
    "purchase_tax_rule_id": 127919000000106780,
    "sales_tax_rule_id": 127919000000106780,
    "tax_percentage": "70%",
    "sku": "s12345",
    "product_type": "goods",
    "hsn_or_sac": "string",
    "sat_item_key_code": "string",
    "unitkey_code": "string",
    "is_taxable": true,
    "tax_exemption_id": "string",
    "purchase_tax_exemption_id": "string",
    "account_id": "SALES_ACCOUNT_ID", /* Example placeholder */
    "avatax_tax_code": "P0000000", /* Example string code */
    "avatax_use_code": "MEDICAL", /* Example string code */
    "item_type": "inventory", /* Example */
    "purchase_description": " ",
    "purchase_rate": "100", /* Example */
    "purchase_account_id": "COGS_ACCOUNT_ID", /* Example placeholder */
    "inventory_account_id": "INVENTORY_ASSET_ACCOUNT_ID", /* Example placeholder */
    "vendor_id": " ",
    "reorder_level": "5", /* Example */
    "item_tax_preferences": [
        {
            "tax_id": 982000000037049,
            "tax_specification": "intra"
        }
    ],
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Normal"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The item has been added.",
    "item": {
        "item_id": 45667789900,
        /* ... full item details ... */
    }
}
```

## Delete an Item

### Description
Delete the item created. Items that are part of transaction cannot be deleted.

### Endpoint
`DELETE /items/{item_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/items/45667789900?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The item has been deleted."
}
```

## Get an Item

### Description
Details of an existing item.

### Endpoint
`GET /items/{item_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/items/45667789900?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "item": {
        "item_id": 45667789900,
        "name": "Hard Drive",
        /* ... full item details ... */
    }
}
```

## List Items

### Description
Get the list of all active items with pagination.

### Endpoint
`GET /items`

### OAuth Scope
`ZohoBooks.settings.READ`

### Query Parameters
*   **name** (string): Search by name (variants: `_startswith`, `_contains`). Max-length [100].
*   **description** (string): Search by description (variants: `_startswith`, `_contains`). Max-length [100].
*   **rate** (double): Search by rate (variants: `_less_than`, `_less_equals`, `_greater_than`, `_greater_equals`).
*   **tax_id** (string): Search by tax ID.
*   **tax_name** (string): Search by tax name.
*   **is_taxable** (boolean): 🇮🇳 , 🇺🇸 , 🇲🇽 only - Filter by taxability.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇲🇽 only - Filter by tax exemption ID.
*   **account_id** (string): Filter by associated account ID.
*   **filter_by** (string): Filter by status. Allowed Values: `Status.All`, `Status.Active`, `Status.Inactive`.
*   **search_text** (string): Search by name or description. Max-length [100].
*   **sort_column** (string): Sort results. Allowed Values: `name`, `rate`, `tax_name`.
*   **sat_item_key_code** (string): 🇲🇽 only - Filter by SAT Item key code.
*   **unitkey_code** (string): 🇲🇽 only - Filter by SAT Unit code.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/items?organization_id=10234695&filter_by=Status.Active' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "items": [
        {
            "item_id": 45667789900,
            "name": "Hard Drive",
            "status": "active",
            "description": "500GB",
            "rate": 120,
            "unit": "100GB",
            "tax_id": 982000000037049,
            "purchase_tax_rule_id": 127919000000106780,
            "sales_tax_rule_id": 127919000000106780,
            "tax_name": "Sales Tax",
            "tax_percentage": "70%",
            "tax_type": "tax",
            "sku": "s12345",
            "product_type": "goods",
            "sat_item_key_code": "string",
            "unitkey_code": "string",
            "custom_fields": [ { /* ... custom field details ... */ } ]
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Items",
        "sort_column": "name", /* Example value */
        "sort_order": "A"
    }
}
```

## Mark as Active

### Description
Mark an inactive item as active.

### Endpoint
`POST /items/{item_id}/active`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/items/45667789900/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The item has been marked as active."
}
```

## Mark as Inactive

### Description
Mark an active item as inactive.

### Endpoint
`POST /items/{item_id}/inactive`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/items/45667789900/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The item has been marked as inactive."
}
```

## Update an Item

### Description
Update the details of an item.

### Endpoint
`PUT /items/{item_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **name** (string, Required): Name of the item. Max-length [100].
*   **rate** (double, Required): Price of the item.
*   **description** (string): Description. Max-length [2000].
*   **tax_id** (string): Not applicable 🇺🇸 , 🇮🇳 - Tax ID.
*   **purchase_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - Purchase tax rule ID.
*   **sales_tax_rule_id** (string): 🇲🇽 , 🇰🇪 , 🇿🇦 only - Sales tax rule ID.
*   **tax_percentage** (string): Tax percentage *(Note: Data type string, likely double/float)*.
*   **hsn_or_sac** (string): 🇮🇳 , 🇰🇪 , 🇿🇦 only - HSN/SAC Code.
*   **sat_item_key_code** (string): 🇲🇽 only - SAT Item Key Code.
*   **unitkey_code** (string): 🇲🇽 only - SAT Unit Key Code.
*   **sku** (string): SKU value (must be unique).
*   **product_type** (string): Type (`goods`, `service`, etc. - varies by edition).
*   **is_taxable** (boolean): 🇮🇳 , 🇺🇸 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Is the item taxable.
*   **tax_exemption_id** (string): 🇮🇳 , 🇺🇸 , 🇲🇽 , 🇰🇪 , 🇿🇦 only - Tax exemption ID.
*   **purchase_tax_exemption_id** (string): 🇰🇪 , 🇿🇦 only - Purchase tax exemption ID.
*   **account_id** (string): Sales/Income account ID *(Note: Changing account might have implications)*.
*   **avatax_tax_code** (string): Avalara Integration only - Tax code. Max-length [25].
*   **avatax_use_code** (string): Avalara Integration only - Use code. Max-length [25].
*   **item_type** (string): Item type *(Note: Usually cannot be changed after creation)*.
*   **purchase_description** (string): Purchase description.
*   **purchase_rate** (string): Purchase price.
*   **purchase_account_id** (string): COGS account ID *(Note: Changing account might have implications)*.
*   **inventory_account_id** (string): Inventory asset account ID *(Note: Changing account might have implications)*.
*   **vendor_id** (string): Preferred vendor ID.
*   **reorder_level** (string): Reorder level quantity.
*   **locations** (array): Update stock levels per location.
*   **item_tax_preferences** (array): 🇮🇳 only - Tax preferences.
*   **custom_fields** (array): Custom fields.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/items/45667789900?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"name": "Updated Hard Drive", "rate": 125.00, ...}'
```

#### Body Parameters
```json
{
    "name": "Hard Drive",
    "rate": 120,
    "description": "500GB",
    "tax_id": 982000000037049,
    /* ... other fields to update ... */
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "Urgent" /* Updated value */
        }
    ]
    /* Include locations array only if updating inventory details */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Item details have been saved.",
    "item": {
        "item_id": 45667789900,
        /* ... updated item details ... */
    }
}
```

## Update Custom Field in Item

### Description
Update the value of the custom field in existing items.

### Endpoint
`PUT /item/{item_id}/customfields`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   An array of custom field objects:
    *   **customfield_id** (long): ID of the custom field to update.
    *   **value** (string): The new value for the custom field.

### Query Parameters
*   **organization_id** (string, Required): ID of the organization.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/item/45667789900/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '[{"customfield_id": "46000000012845", "value": "UpdatedValue"}]'
```

#### Body Parameters
```json
[
    {
        "customfield_id": "46000000012845",
        "value": "Normal" /* New value */
    }
]
```

### Response Example
```json
{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}
```

## Update Item using Custom Field

### Description
Update an item using a custom field's unique value. Requires `X-Unique-Identifier-Key` and `X-Unique-Identifier-Value` headers. Optionally use `X-Upsert: true` to create if not found.

### Endpoint
`PUT /items` *(Note: This endpoint is typically for bulk updates or upserts with unique keys)*

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Headers
*(Assumed based on description, not shown in example)*
*   **X-Unique-Identifier-Key**: (Required) API name of the unique custom field.
*   **X-Unique-Identifier-Value**: (Required) Value of the unique custom field.
*   **X-Upsert**: (Optional, boolean) Set to `true` to create if not found.

### Arguments (Body Parameters)
*   *(Same arguments as Create an Item, excluding fields that cannot be changed after creation, like `item_type` or potentially account IDs depending on usage).*
*   **name** (string, Required): Name of the item.
*   **rate** (double, Required): Price of the item.
*   ... other updatable fields from Create Item ...

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/items?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"name": "Updated Item Name", "rate": 55.00, ...}'
```

#### Body Parameters
```json
{
    "name": "Hard Drive",
    "rate": 120,
    "description": "500GB",
    "tax_id": 982000000037049,
    /* ... other fields to update or required for upsert ... */
    "custom_fields": [
        {
            "customfield_id": "46000000012845",
            "value": "UpdatedValue"
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Item details have been saved.",
    "item": {
        "item_id": 45667789900,
        /* ... updated item details ... */
    }
}
```

# Locations

## Overview

### Locations
Create locations for each branch and warehouse in your organisation and manage them all in one place. In this document, you can learn how to create and manage locations in Zoho Books.

### End Points
*   `POST /settings/locations/enable`
*   `POST /locations`
*   `GET /locations`
*   `PUT /locations/{location_id}`
*   `DELETE /locations/{location_id}`
*   `POST /locations/{location_id}/active`
*   `POST /locations/{location_id}/inactive`
*   `POST /locations/{location_id}/markasprimary`

*(Note: Attributes are described within each specific endpoint section below, not listed globally here).*

## Create a Location

### Description
Create a location.

### Endpoint
`POST /locations`

### OAuth Scope
`ZohoBooks.locations.CREATE`

### Arguments (Body Parameters)
*   **location_name** (string, Required): Name of the location.
*   **type** (string): Type of the location (e.g., 'general', 'line_item_only').
*   **email** (string): Email id for the location.
*   **phone** (string): Mobile number for location.
*   **address** (object): Address details.
    *   **street_address1** (string): Street address line 1.
    *   **street_address2** (string): Street address line 2.
    *   **city** (string): City.
    *   **state** (string): State/Province.
    *   **state_code** (string): State code.
    *   **country** (string): Country.
    *   **attention** (string): Attention line.
*   **tax_settings_id** (string, Required for 🇮🇳 only): Tax Settings ID.
*   **parent_location_id** (string): Parent Location ID (for sub-locations).
*   **associated_series_ids** (array): Array of associated numbering series IDs.
*   **auto_number_generation_id** (string): Autonumber generation group ID.
*   **is_all_users_selected** (boolean): Whether all users are associated.
*   **user_ids** (string): Comma separated user IDs (if `is_all_users_selected` is false).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/locations?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"location_name": "Head Office", "type": "general", ...}'
```

#### Body Parameters
```json
{
    "type": "general", /* or line_item_only */
    "email": "willsmith@bowmanfurniture.com",
    "phone": "+1-925-921-9201",
    "address": {
        "city": "New York City",
        "state": "New York",
        "country": "U.S.A",
        "attention": "string",
        "state_code": "NY",
        "street_address1": "No:234,90 Church Street",
        "street_address2": "McMillan Avenue"
    },
    "location_name": "Head Office",
    "tax_settings_id": "460000000038080",
    "parent_location_id": "460000000041010",
    "associated_series_ids": [
        "982000000870911",
        "982000000870915"
    ],
    "auto_number_generation_id": "982000000870911",
    "is_all_users_selected": false,
    "user_ids": "460000000036868,460000000036869"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Location has been created.",
    "location": { /* Corrected: Original showed 'locations' */
        "location_id": "460000000038080",
        "location_name": "Head Office",
        "is_primary": true, /* Indicates if this is the primary location */
        "status": "active",
        "type": "general", /* or line_item_only */
        "email": "willsmith@bowmanfurniture.com",
        "phone": "+1-925-921-9201",
        "address": { /* ... address details ... */ },
        "parent_location_id": "460000000041010",
        "associated_series_ids": [ /* ... */ ],
        "auto_number_generation_id": "982000000870911",
        "associated_users": [ { "user_id": "...", "user_name": "..." } ],
        "tax_settings_id": "460000000038080"
    }
}
```

## Delete a Location

### Description
Delete a location. *(Note: Likely fails if location is used in transactions or has inventory).*

### Endpoint
`DELETE /locations/{location_id}`

### OAuth Scope
`ZohoBooks.locations.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/locations/130426000000664020?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The location has been deleted.."
}
```

## Enable Locations

### Description
Enable Locations for an organisation.

### Endpoint
`POST /settings/locations/enable`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/locations/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "We're enabling locations for your organization."
}
```

## List all Locations

### Description
List all the available locations in your zoho inventory *(Note: Description mentions Zoho Inventory, context is Zoho Books)*.

### Endpoint
`GET /locations`

### OAuth Scope
`ZohoBooks.locations.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/locations?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "locations": [
        {
            "location_id": "460000000038080",
            "location_name": "Head Office",
            "is_primary": true,
            "status": "active",
            "type": "general", /* or line_item_only */
            "email": "willsmith@bowmanfurniture.com",
            "phone": "+1-925-921-9201",
            "address": { /* ... address details ... */ },
            "tax_settings_id": "460000000038080",
            "parent_location_id": "460000000041010",
            "associated_series_ids": [ /* ... */ ],
            "auto_number_generation_id": "982000000870911",
            "is_all_users_selected": false,
            "associated_users": [ { /* ... user details ... */ } ]
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: `page_context` was missing from the original example).*

## Mark as Active

### Description
Mark location as Active.

### Endpoint
`POST /locations/{location_id}/active`

### OAuth Scope
`ZohoBooks.locations.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/locations/130426000000664020/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The location has been marked as active."
}
```

## Mark as Inactive

### Description
Mark location as Inactive.

### Endpoint
`POST /locations/{location_id}/inactive`

### OAuth Scope
`ZohoBooks.locations.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/locations/130426000000664020/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The location has been marked as inactive."
}
```

## Mark as Primary

### Description
Mark location as primary.

### Endpoint
`POST /locations/{location_id}/markasprimary`

### OAuth Scope
`ZohoBooks.locations.CREATE`

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/locations/130426000000664020/markasprimary?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The location has been marked as primary."
}
```

## Update Location

### Description
Update location details.

### Endpoint
`PUT /locations/{location_id}`

### OAuth Scope
`ZohoBooks.locations.UPDATE`

### Arguments (Body Parameters)
*   **location_name** (string, Required): Name of the location.
*   **type** (string): Type of the location.
*   **email** (string): Email id.
*   **phone** (string): Phone number.
*   **address** (object): Address details.
*   **tax_settings_id** (string, Required for 🇮🇳 only): Tax Settings ID.
*   **parent_location_id** (string): Parent Location ID.
*   **associated_series_ids** (array): Associated numbering series IDs.
*   **auto_number_generation_id** (string): Autonumber generation group ID.
*   **is_all_users_selected** (boolean): Whether all users are associated.
*   **user_ids** (string): Comma separated user IDs.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/locations/130426000000664020?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"location_name": "Updated Head Office", ...}'
```

#### Body Parameters
```json
{
    "type": "general", /* or line_item_only */
    "email": "willsmith@bowmanfurniture.com",
    "phone": "+1-925-921-9201",
    "address": { /* ... address details ... */ },
    "location_name": "Head Office",
    "tax_settings_id": "460000000038080",
    "parent_location_id": "460000000041010",
    "associated_series_ids": [ /* ... */ ],
    "auto_number_generation_id": "982000000870911",
    "is_all_users_selected": false,
    "user_ids": "460000000036868,460000000036869"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Location has been updated.",
    "location": { /* Corrected: Original showed 'locations' */
        "location_id": "460000000038080",
        "location_name": "Updated Head Office", /* Example update */
        "is_primary": true,
        "status": "active",
        /* ... other updated details ... */
    }
}
```

# Currency

## Overview

### Currency
In case your organization sells products or provides services to customer from different countries, you can add those currencies and exchange rates you deal with, to your Zoho Books account.

### End Points (Currency)
*   `POST /settings/currencies`
*   `GET /settings/currencies`
*   `PUT /settings/currencies/{currency_id}`
*   `GET /settings/currencies/{currency_id}`
*   `DELETE /settings/currencies/{currency_id}`

### End Points (Exchange Rates)
*   `POST /settings/currencies/{currency_id}/exchangerates`
*   `GET /settings/currencies/{currency_id}/exchangerates`
*   `PUT /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`
*   `GET /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`
*   `DELETE /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`

### Attributes (Currency)
*   **currency_id** (string): A unique ID for the currency.
*   **currency_code** (string): A unique standard code for the currency. Max-len [100].
*   **currency_name** (string): The name for the currency.
*   **currency_symbol** (string): A unique symbol for the currency. Max-len [4].
*   **price_precision** (integer): The precision for the price.
*   **currency_format** (string): The format for the currency to be displayed. Max-len [100].
*   **is_base_currency** (boolean): Is it the base currency of the organization.

### Example (Currency)
```json
{
    "currency_id": "982000000004012",
    "currency_code": "AUD",
    "currency_name": "AUD- Australian Dollar",
    "currency_symbol": "$",
    "price_precision": 2,
    "currency_format": "1,234,567.89",
    "is_base_currency": false
}
```

## Create a Currency

### Description
Create a currency for transaction.

### Endpoint
`POST /settings/currencies`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **currency_code** (string, Required): A unique standard code for the currency. Max-len [100].
*   **currency_symbol** (string): A unique symbol for the currency. Max-len [4].
*   **price_precision** (integer): The precision for the price.
*   **currency_format** (string, Required): The format for the currency to be displayed. Max-len [100].

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"currency_code": "AUD", "currency_symbol": "$", "price_precision": 2, "currency_format": "1,234,567.89"}'
```

#### Body Parameters
```json
{
    "currency_code": "AUD",
    "currency_symbol": "$",
    "price_precision": 2,
    "currency_format": "1,234,567.89"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The currency has been added.",
    "currency": {
        "currency_id": "982000000004012",
        "currency_code": "AUD",
        "currency_name": "AUD- Australian Dollar",
        "currency_symbol": "$",
        "price_precision": 2,
        "currency_format": "1,234,567.89",
        "is_base_currency": false
    }
}
```

## Create an Exchange Rate

### Description
Create an exchange rate for the specified currency.

### Endpoint
`POST /settings/currencies/{currency_id}/exchangerates`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **effective_date** (string, Required): Date the exchange rate is applicable. Format [yyyy-mm-dd].
*   **rate** (double, Required): Rate of exchange with respect to base currency.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012/exchangerates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"effective_date": "2013-09-04", "rate": 1.23}'
```

#### Body Parameters
```json
{
    "effective_date": "2013-09-04",
    "rate": 1.23
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The exchange rate has been added.",
    "exchange_rate": { /* Corrected structure, original showed just the rate */
        "exchange_rate_id": "GENERATED_ID_HERE",
        "currency_id": "982000000004012",
        "effective_date": "2013-09-04",
        "rate": 1.23
    }
}
```
*(Note: Original example response just showed `1.23`, which is unlikely. The full object is expected).*

## Delete a Currency

### Description
Delete a currency. Currency that is associated to transactions cannot be deleted.

### Endpoint
`DELETE /settings/currencies/{currency_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The currency has been deleted."
}
```

## Delete an Exchange Rate

### Description
Delete an exchange rate for the specified currency.

### Endpoint
`DELETE /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012/exchangerates/460000000038035?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "Exchange rate successfully deleted"
}
```

## Get a Currency

### Description
Get the details of a currency.

### Endpoint
`GET /settings/currencies/{currency_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "currency": {
        "currency_id": "982000000004012",
        "currency_code": "AUD",
        "currency_name": "AUD- Australian Dollar",
        "currency_symbol": "$",
        "price_precision": 2,
        "currency_format": "1,234,567.89",
        "is_base_currency": false
    }
}
```

## Get an Exchange Rate

### Description
Get the details of an exchange rate that has been associated to the currency.

### Endpoint
`GET /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012/exchangerates/460000000038035?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "exchange_rate": { /* Expected structure */
        "exchange_rate_id": "460000000038035",
        "currency_id": "982000000004012",
        "currency_code": "AUD",
        "effective_date": "2013-09-04",
        "rate": 1.23
    }
}
```
*(Note: Original example response just showed `1`, which is incorrect).*

## List Currencies

### Description
Get list of currencies configured.

### Endpoint
`GET /settings/currencies`

### OAuth Scope
`ZohoBooks.settings.READ`

### Query Parameters
*   **filter_by** (string): Filter currencies excluding base currency. Allowed Values: `Currencies.ExcludeBaseCurrency`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies?organization_id=10234695&filter_by=Currencies.ExcludeBaseCurrency' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "currencies": [
        {
            "currency_id": "982000000004012",
            "currency_code": "AUD",
            "currency_name": "AUD- Australian Dollar",
            "currency_symbol": "$",
            "price_precision": 2,
            "currency_format": "1,234,567.89",
            "is_base_currency": false,
            "exchange_rate": 1, /* Current or last known rate */
            "effective_date": "2013-09-04" /* Date of the exchange_rate shown */
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example).*

## List Exchange Rates

### Description
List of exchange rates configured for the currency.

### Endpoint
`GET /settings/currencies/{currency_id}/exchangerates`

### OAuth Scope
`ZohoBooks.settings.READ`

### Query Parameters
*   **from_date** (string): Returns the rate from this date or the previous closest match.
*   **is_current_date** (boolean): Return rate only if available for the current date.
*   **sort_column** (string): Sorts the list. Allowed Values: `effective_date`.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012/exchangerates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "exchange_rates": [
        {
            "exchange_rate_id": "460000000038035",
            "currency_id": "982000000004012",
            "currency_code": "AUD",
            "effective_date": "2013-09-04",
            "rate": 1.23
        },
        {...},
        {...}
    ],
    "page_context": { /* Added standard page_context */
        "page": 1,
        "per_page": 200,
        "has_more_page": false
    }
}
```
*(Note: List endpoints typically include a `page_context` object for pagination, which was missing from the original example).*

## Update a Currency

### Description
Update the details of a currency.

### Endpoint
`PUT /settings/currencies/{currency_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **currency_code** (string, Required): A unique standard code for the currency. Max-len [100].
*   **currency_symbol** (string): A unique symbol for the currency. Max-len [4].
*   **price_precision** (integer): The precision for the price.
*   **currency_format** (string, Required): The format for the currency to be displayed. Max-len [100].

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"currency_code": "AUD", "currency_symbol": "AU$", "price_precision": 2, "currency_format": "1 234 567,89"}'
```

#### Body Parameters
```json
{
    "currency_code": "AUD",
    "currency_symbol": "$",
    "price_precision": 2,
    "currency_format": "1,234,567.89"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Currency information has been saved.",
    "currency": {
        "currency_id": "982000000004012",
        "currency_code": "AUD",
        "currency_name": "AUD- Australian Dollar",
        "currency_symbol": "AU$", /* Example updated symbol */
        "price_precision": 2,
        "currency_format": "1 234 567,89", /* Example updated format */
        "is_base_currency": false
    }
}
```

## Update an Exchange Rate

### Description
Update the details of exchange rate for a currency.

### Endpoint
`PUT /settings/currencies/{currency_id}/exchangerates/{exchange_rate_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **effective_date** (string, Required): Date the exchange rate is applicable. Format [yyyy-mm-dd].
*   **rate** (double, Required): Rate of exchange.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/settings/currencies/982000000004012/exchangerates/460000000038035?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"effective_date": "2013-09-04", "rate": 1.25}'
```

#### Body Parameters
```json
{
    "effective_date": "2013-09-04",
    "rate": 1.23
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The exchange rate has been updated.",
    "exchange_rate": { /* Corrected structure, original didn't show updated object */
        "exchange_rate_id": "460000000038035",
        "currency_id": "982000000004012",
        "effective_date": "2013-09-04",
        "rate": 1.25 /* Example updated rate */
    }
}
```
*(Note: Original example response just showed the message. The updated object is expected).*

# Taxes

## Overview

### Taxes
Your business’ financials are affected by regulatory taxes and each organization has different country specific taxes to adhere to. This section covers individual taxes, tax groups, tax authorities, and tax exemptions.

### End Points (Taxes)
*   `POST /settings/taxes`
*   `GET /settings/taxes`
*   `PUT /settings/taxes/{tax_id}`
*   `GET /settings/taxes/{tax_id}`
*   `DELETE /settings/taxes/{tax_id}`

### End Points (Tax Groups)
*   `POST /settings/taxgroups`
*   `PUT /settings/taxgroups/{tax_group_id}`
*   `GET /settings/taxgroups/{tax_group_id}`
*   `DELETE /settings/taxgroups/{tax_group_id}`

### End Points (Tax Authorities)
*   `POST /settings/taxauthorities`
*   `GET /settings/taxauthorities`
*   `PUT /settings/taxauthorities/{tax_authority_id}`
*   `GET /settings/taxauthorities/{tax_authority_id}`
*   `DELETE /settings/taxauthorities/{tax_authority_id}`

### End Points (Tax Exemptions)
*   `POST /settings/taxexemptions`
*   `GET /settings/taxexemptions`
*   `PUT /settings/taxexemptions/{tax_exemption_id}`
*   `GET /settings/taxexemptions/{tax_exemption_id}`
*   `DELETE /settings/taxexemptions/{tax_exemption_id}`

### Attributes (Tax Object Example)
*   **tax_id** (string): ID of the Tax
*   **tax_name** (string): Name of the Tax
*   **tax_percentage** (double): Number of Percentage Taxable.
*   **tax_type** (string): Type (`tax` or `compound_tax`).
*   **tax_factor** (string): 🇲🇽 only - Type of Tax Factor (`rate`, `share`).
*   **tds_payable_account_id** (string): 🇲🇽 only - Input Tax ID. *(Note: Description seems confusing)*.
*   **tax_authority_id** (string): 🇺🇸 , 🇲🇽 only - ID of the tax authority.
*   **tax_authority_name** (string): Name of the Tax Authority.
*   **is_value_added** (boolean): Check if Tax is Value Added.
*   **tax_specific_type** (string): 🇮🇳 , 🇲🇽 , 🇿🇦 only - Type specific to region (e.g., `igst`, `iva`, `soa_less_than_28d`).
*   **country** (string): 🇬🇧 , Europe , 🌎 only - Country tax belongs to.
*   **country_code** (string): 🇬🇧 , Europe , GCC , 🌎 only - Two letter country code.
*   **purchase_tax_expense_account_id** (long): 🇦🇺 , 🇨🇦 only - Account ID for Purchase Tax computation.
*   **is_default_tax** (boolean): Is this the default tax for the organization.
*   **is_editable** (boolean): Can this tax be edited.
*   **output_tax_account_name** (string): Name of the liability account associated.
*   **purchase_tax_account_name** (string): 🇦🇺 , 🇨🇦 only - Name of the purchase tax expense account.
*   **tax_account_id** (string): ID of the liability account associated.

### Example (Tax Object)
```json
{ /* Corrected: Should be single object for overview example */
    "tax_id": "982000000566009",
    "tax_name": "Sales Group",
    "tax_percentage": 10.5,
    "tax_type": "tax",
    "tax_factor": "rate",
    "tds_payable_account_id": "132086000000107337", /* Check meaning */
    "tax_authority_id": "460000000066001",
    "tax_authority_name": "Illinois Department of Revenue",
    "is_value_added": false,
    "tax_specific_type": "string", /* Example: 'iva' or 'cgst' */
    "country": "United Kingdom", /* Example */
    "country_code": "GB", /* Corrected example */
    "purchase_tax_expense_account_id": null, /* Example */
    "is_default_tax": true,
    "is_editable": true,
    "output_tax_account_name": "Sales Tax Liability", /* Example */
    "purchase_tax_account_name": null, /* Example */
    "tax_account_id": "132086000000107333" /* Example */
}
```

## Create a Tax Group

### Description
Create a tax group associating multiple taxes.

### Endpoint
`POST /settings/taxgroups`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **tax_group_name** (string, Required): Name of the tax group.
*   **taxes** (string, Required): Comma Separated list of tax IDs to associate.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/taxgroups?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"tax_group_name": "State & Local Tax", "taxes": "TAX_ID_1,TAX_ID_2"}'
```

#### Body Parameters
```json
{
    "tax_group_name": "Sales Group",
    "taxes": "982000000566001,982000000566002" /* Example comma-separated IDs */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Tax group has been created.", /* Corrected message */
    "tax_group": {
        "tax_group_id": "982000000566010", /* Example New Tax Group ID */
        "tax_group_name": "Sales Group",
        "tax_group_percentage": 15.5, /* Example calculated total percentage */
        "taxes": [ /* List of associated taxes */
            {
                "tax_id": "982000000566001",
                /* ... tax details ... */
            },
             {
                "tax_id": "982000000566002",
                /* ... tax details ... */
            }
        ]
    }
}
```

## Create a Tax

### Description
Create a tax which can be associated with an item.

### Endpoint
`POST /settings/taxes`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **tax_name** (string, Required): Name of the Tax.
*   **tax_percentage** (double, Required): Tax percentage.
*   **tax_type** (string): Type (`tax` or `compound_tax`). Default is 'tax'.
*   **tax_factor** (string): 🇲🇽 only - Tax Factor (`rate`, `share`).
*   **tax_specific_type** (string): 🇮🇳 , 🇲🇽 , 🇿🇦 only - Region-specific tax type.
*   **tax_authority_name** (string): Name of the Tax Authority *(Note: Use `tax_authority_id` if possible)*.
*   **tax_authority_id** (string): 🇺🇸 , 🇲🇽 only - ID of the tax authority.
*   **country_code** (string): 🇬🇧 , Europe , GCC , 🌎 only - Two-letter country code.
*   **purchase_tax_expense_account_id** (long): 🇦🇺 , 🇨🇦 only - Account ID for Purchase Tax computation.
*   **is_value_added** (boolean): Is this a Value Added Tax.
*   **update_recurring_invoice** (boolean): Apply changes to recurring invoices.
*   **update_recurring_expense** (boolean): Apply changes to recurring expenses.
*   **update_draft_invoice** (boolean): Apply changes to draft invoices.
*   **update_recurring_bills** (boolean): Apply changes to recurring bills.
*   **update_draft_so** (boolean): Apply changes to draft sales orders.
*   **update_subscription** (boolean): Apply changes to subscriptions.
*   **update_project** (boolean): Apply changes to projects.
*   **is_editable** (boolean): Can this tax be edited later *(Note: Likely read-only based on system)*.

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/taxes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"tax_name": "Sales Group", "tax_percentage": 10.5, ...}'
```

#### Body Parameters
```json
{
    "tax_name": "Sales Group",
    "tax_percentage": 10.5,
    "tax_type": "tax",
    "tax_factor": "rate",
    "tax_specific_type": "string",
    "tax_authority_name": "Illinois Department of Revenue",
    "tax_authority_id": "460000000066001",
    "country_code": "GB", /* Corrected example */
    "purchase_tax_expense_account_id": 0,
    "is_value_added": false,
    "update_recurring_invoice": false,
    "update_recurring_expense": false,
    "update_draft_invoice": false,
    "update_recurring_bills": false,
    "update_draft_so": false,
    "update_subscription": false,
    "update_project": false
    /* is_editable is likely determined by system, not set on create */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The tax has been added.",
    "tax": { /* Corrected: Should return single object */
        "tax_id": "982000000566009",
        "tax_name": "Sales Group",
        "tax_percentage": 10.5,
        /* ... other tax details ... */
        "is_editable": true
    }
}
```

## Delete a Tax Group

### Description
Delete a tax group. Tax group that is associated to transactions cannot be deleted.

### Endpoint
`DELETE /settings/taxgroups/{tax_group_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/settings/taxgroups/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The tax group has been deleted."
}
```

## Delete a Tax

### Description
Delete a simple or compound tax.

### Endpoint
`DELETE /settings/taxes/{tax_id}`

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/settings/taxes/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The record has been deleted."
}
```

## Get a Tax Group

### Description
Get the details of a tax group.

### Endpoint
`GET /settings/taxgroups/{tax_group_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/taxgroups/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "tax_group": {
        "tax_group_id": "982000000566009",
        "tax_group_name": "Sales Group",
        "tax_group_percentage": 10.5,
        "taxes": [
            {
                "tax_id": "982000000566009", /* Example: Contains details of the single tax in this group */
                "tax_name": "Sales Group Tax Component",
                "tax_percentage": 10.5
                /* ... other tax details ... */
            }
        ]
    }
}
```

## Get a Tax

### Description
Get the details of a simple or compound tax.

### Endpoint
`GET /settings/taxes/{tax_id}`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/taxes/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "tax": { /* Corrected: Should return single object */
        "tax_id": "982000000566009",
        "tax_name": "Sales Group",
        "tax_percentage": 10.5,
        /* ... full tax details ... */
    }
}
```

## List Taxes

### Description
List of simple and compound taxes with pagination.

### Endpoint
`GET /settings/taxes`

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/taxes?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "taxes": [
        {
            "tax_id": "982000000566009",
            "tax_name": "Sales Group",
            "tax_percentage": 10.5,
            "tax_type": "tax",
            "tax_factor": "rate",
            "tax_specific_type": "string",
            "tax_authority_id": "460000000066001",
            "tax_authority_name": "Illinois Department of Revenue",
            "is_value_added": false,
            "is_default_tax": true,
            "is_editable": true,
            "output_tax_account_name": "string",
            "purchase_tax_account_name": "string",
            "tax_account_id": "132086000000107333",
            "purchase_tax_account_id": "132086000000107337"
        },
        {...},
        {...}
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Taxes",
        "applied_filter": "Status.All",
        "sort_column": "created_time",
        "sort_order": "D"
    }
}
```

## Update a Tax Group

### Description
Update the details of the tax group.

### Endpoint
`PUT /settings/taxgroups/{tax_group_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **tax_group_name** (string, Required): Name of the tax group.
*   **taxes** (string, Required): Comma Separated list of tax IDs to associate.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/settings/taxgroups/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"tax_group_name": "Updated Sales Group", "taxes": "TAX_ID_1,TAX_ID_3"}'
```

#### Body Parameters
```json
{
    "tax_group_name": "Updated Sales Group",
    "taxes": "982000000566001,982000000566003" /* Example updated list */
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Tax group has been updated.", /* Corrected message */
    "tax_group": {
        "tax_group_id": "982000000566009",
        "tax_group_name": "Updated Sales Group",
        /* ... updated tax group details ... */
    }
}
```

## Update a Tax

### Description
Update the details of a simple or compound tax.

### Endpoint
`PUT /settings/taxes/{tax_id}`

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **tax_name** (string, Required): Name of the Tax.
*   **tax_percentage** (double, Required): Tax percentage.
*   **tax_type** (string): Type (`tax` or `compound_tax`).
*   **tax_factor** (string): 🇲🇽 only - Tax Factor (`rate`, `share`).
*   **tax_specific_type** (string): 🇮🇳 , 🇲🇽 , 🇿🇦 only - Region-specific tax type.
*   **tax_authority_name** (string): Name of the Tax Authority.
*   **tax_authority_id** (string): 🇺🇸 , 🇲🇽 only - ID of the tax authority.
*   **country_code** (string): 🇬🇧 , Europe , GCC , 🌎 only - Two-letter country code.
*   **purchase_tax_expense_account_id** (long): 🇦🇺 , 🇨🇦 only - Account ID for Purchase Tax computation.
*   **is_value_added** (boolean): Is this a Value Added Tax.
*   **update_recurring_invoice** (boolean): Apply changes to recurring invoices.
*   **update_recurring_expense** (boolean): Apply changes to recurring expenses.
*   **update_draft_invoice** (boolean): Apply changes to draft invoices.
*   **update_recurring_bills** (boolean): Apply changes to recurring bills.
*   **update_draft_so** (boolean): Apply changes to draft sales orders.
*   **update_subscription** (boolean): Apply changes to subscriptions.
*   **update_project** (boolean): Apply changes to projects.
*   **tds_payable_account_id** (string): 🇲🇽 only - Input Tax ID *(Note: Description confusing)*.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/settings/taxes/982000000566009?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"tax_name": "Updated Sales Tax", "tax_percentage": 11.0, ...}'
```

#### Body Parameters
```json
{
    /* tax_id is in URL path */
    "tax_name": "Updated Sales Tax Name",
    "tax_percentage": 11.0,
    "tax_type": "tax",
    "tax_factor": "rate",
    "tax_specific_type": "string",
    "tax_authority_name": "Illinois Department of Revenue",
    "tax_authority_id": "460000000066001",
    "country_code": "GB", /* Corrected example */
    "purchase_tax_expense_account_id": 0,
    "is_value_added": false,
    "update_recurring_invoice": false,
    "update_recurring_expense": false,
    "update_draft_invoice": false,
    "update_recurring_bills": false,
    "update_draft_so": false,
    "update_subscription": false,
    "update_project": false,
    /* is_editable is likely read-only */
    "tds_payable_account_id": "132086000000107337"
}
```

### Response Example
```json
{
    "code": 0,
    "message": "Tax information has been saved.",
    "tax": { /* Corrected: Should return single object */
        "tax_id": "982000000566009",
        "tax_name": "Updated Sales Tax Name",
        "tax_percentage": 11.0,
        /* ... other updated tax details ... */
    }
}
```
# Opening Balance

## Overview

### Opening Balance
While migrating from existing accounting software to Zoho Books, you need to ensure that the transition is flawless, that all prevailing data such as journal entries, records, expense and income statements etc, has been recorded and continuity in financial statements is maintained. To ensure this, an opening balance needs to be calculated.

### End Points
*   `POST /settings/openingbalances`
*   `PUT /settings/openingbalances` *(Note: May require ID in body)*
*   `GET /settings/openingbalances` *(Note: Fetches the single OB record)*
*   `DELETE /settings/openingbalances` *(Note: Deletes the single OB record)*
*   *(Note: Endpoint `GET /basecurrencyadjustment/accounts` was included in the provided files for this section but belongs to Base Currency Adjustment)*

### Attributes
*   **opening_balance_id** (string): ID of opening balance.
*   **date** (string): Date on which the opening balance needs to be recorded. [yyyy-MM-dd].
*   **price_precision** (integer): Price Precision of the Values.
*   **accounts** (array): List of account balances.
    *   **acount_split_id** (string): ID for the specific account line within the opening balance.
    *   **account_id** (string): ID of the chart of account.
    *   **account_name** (string): Name of the account.
    *   **debit_or_credit** (string): 'debit' or 'credit'.
    *   **exchange_rate** (double): Exchange rate (if account currency differs from base).
    *   **currency_id** (string): ID of the account's currency.
    *   **currency_code** (string): Code of the account's currency.
    *   **bcy_amount** (double): Amount in base currency.
    *   **amount** (double): Amount in the account's currency.
    *   **location_id** (string): Location ID (if applicable).
    *   **location_name** (string): Name of the location.
*   **total** (integer): Total Amount from the Opening Balance *(Note: Represents the total debits or credits, which must match)*.

### Example
```json
{
    "opening_balance_id": "460000000050041",
    "date": "2013-10-01",
    "price_precision": 2,
    "accounts": [
        {
            "acount_split_id": "460000000050045",
            "account_id": "460000000000358",
            "account_name": "Undeposited Funds",
            "debit_or_credit": "debit",
            "exchange_rate": 1,
            "currency_id": "460000000000097",
            "currency_code": "USD",
            "bcy_amount": 2000,
            "amount": 2000,
            "location_id": "460000000038080",
            "location_name": "string"
        }
        /* ... more account entries ... */
    ],
    "total": 10000 /* Total Debits or Credits */
}
```

## Create Opening Balance

### Description
Creates opening balance with the given information. Debits must equal Credits.

### Endpoint
`POST /settings/openingbalances`

### OAuth Scope
`ZohoBooks.settings.CREATE`

### Arguments (Body Parameters)
*   **date** (string, Required): Date on which the opening balance needs to be recorded. [yyyy-MM-dd].
*   **accounts** (array, Required): List of account balances.
    *   **account_id** (string, Required): ID of the chart of account.
    *   **debit_or_credit** (string, Required): 'debit' or 'credit'.
    *   **exchange_rate** (double): Exchange rate (required if `currency_id` differs from base currency).
    *   **currency_id** (string): ID of the account's currency (required if account has foreign currency).
    *   **amount** (double, Required): Amount in the account's currency.
    *   **location_id** (string): Location ID (if applicable).

### Request Example

#### cURL
```curl
curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/settings/openingbalances?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"date": "2013-10-01", "accounts": [{"account_id": "...", "debit_or_credit": "debit", "amount": 2000}, {"account_id": "...", "debit_or_credit": "credit", "amount": 2000}]}'
```

#### Body Parameters
```json
{
    "date": "2013-10-01",
    "accounts": [
        {
            "account_id": "460000000000358",
            "debit_or_credit": "debit",
            "exchange_rate": 1, /* Only needed if currency_id is provided and differs from base */
            "currency_id": "460000000000097", /* Only needed for foreign currency accounts */
            "amount": 2000,
            "location_id": "460000000038080"
        },
        { /* Need balancing entry */
            "account_id": "ACCOUNT_ID_FOR_CREDIT",
            "debit_or_credit": "credit",
            "amount": 2000
             /* Other fields as needed */
        }
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The opening balances are saved!",
    "opening_balance": {
        "opening_balance_id": "460000000050041",
        "date": "2013-10-01",
        "price_precision": 2,
        "accounts": [
            {
                "acount_split_id": "460000000050045",
                "account_id": "460000000000358",
                "account_name": "Undeposited Funds",
                "debit_or_credit": "debit",
                "exchange_rate": 1,
                "currency_id": "460000000000097",
                "currency_code": "USD",
                "bcy_amount": 2000,
                "amount": 2000,
                "location_id": "460000000038080",
                "location_name": "string"
            }
             /* ... other account entries ... */
        ],
        "total": 10000
    }
}
```

## Delete Opening Balance

### Description
Delete the entered opening balance.

### Endpoint
`DELETE /settings/openingbalances` *(Note: Typically DELETE uses an ID like `/settings/openingbalances/{opening_balance_id}`. This might delete the *entire* OB record for the org).*

### OAuth Scope
`ZohoBooks.settings.DELETE`

### Request Example

#### cURL
```curl
curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/settings/openingbalances?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "The entered opening balance has been deleted."
}
```

## Get Opening Balance

### Description
Get opening balance details.

### Endpoint
`GET /settings/openingbalances` *(Note: Typically GET for a specific record uses an ID like `/settings/openingbalances/{opening_balance_id}`. This endpoint might fetch the single OB record for the org).*

### OAuth Scope
`ZohoBooks.settings.READ`

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/settings/openingbalances?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "opening_balance": {
        "opening_balance_id": "460000000050041",
        "date": "2013-10-01",
        "price_precision": 2,
        "accounts": [
            {
                "acount_split_id": "460000000050045",
                /* ... account details ... */
            }
             /* ... other account entries ... */
        ],
        "total": 10000
    }
}
```

## List Account Details for Base Currency Adjustment

*(Note: This section appears to be misplaced and belongs to the Base Currency Adjustment API, not Opening Balance.)*

### Description
List of accounts having transaction with effect to the given exchange rate.

### Endpoint
`GET /basecurrencyadjustment/accounts`

### OAuth Scope
`ZohoBooks.accountants.READ`

### Query Parameters
*   **currency_id** (string, Required): ID of currency for which adjustment effect needs to be previewed.
*   **adjustment_date** (string, Required): Date for the adjustment preview.
*   **exchange_rate** (double, Required): Exchange rate to use for preview.
*   **notes** (string, Required): Notes for the potential adjustment *(Note: Requiring notes for a GET preview seems unusual)*.

### Request Example

#### cURL
```curl
curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/basecurrencyadjustment/accounts?organization_id=10234695¤cy_id=460000000000109&adjustment_date=2013-09-05&exchange_rate=1¬es=Base%20Currency%20Adjustment%20against%20EUR' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
```

### Response Example
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "adjustment_date": "2013-09-05",
        "exchange_rate": 1,
        "currency_id": "460000000000109",
        "accounts": [
            {
                "account_id": "460000000000364",
                "account_name": "Accounts Receivable",
                "bcy_balance": 171.47,
                "fcy_balance": 139.41,
                "adjusted_balance": 209.12,
                "gain_or_loss": 37.65,
                "gl_specific_type": 5
            }
        ],
        "notes": "Base Currency Adjustment against EUR",
        "currency_code": "EUR"
    }
}
```

## Update Opening Balance

### Description
Updates the existing opening balance information. Debits must equal Credits.

### Endpoint
`PUT /settings/openingbalances` *(Note: Typically PUT uses an ID in the path, like `/settings/openingbalances/{opening_balance_id}`. This endpoint might require the ID in the body instead).*

### OAuth Scope
`ZohoBooks.settings.UPDATE`

### Arguments (Body Parameters)
*   **opening_balance_id** (string, Required): ID of the opening balance record to update.
*   **date** (string, Required): Date on which the opening balance needs to be recorded. [yyyy-MM-dd].
*   **accounts** (array, Required): List of account balances. Include `acount_split_id` for existing lines to update. Omit `acount_split_id` for new lines. Remove objects from array to delete lines.
    *   **acount_split_id** (string): ID for the specific account line (Required to update existing lines).
    *   **account_id** (string, Required): ID of the chart of account.
    *   **debit_or_credit** (string, Required): 'debit' or 'credit'.
    *   **exchange_rate** (double): Exchange rate.
    *   **currency_id** (string): Currency ID.
    *   **amount** (double, Required): Amount in the account's currency.
    *   **location_id** (string): Location ID.

### Request Example

#### cURL
```curl
curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/settings/openingbalances?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"opening_balance_id": "460000000050041", "date": "2013-10-01", "accounts": [...] ...}'
```

#### Body Parameters
```json
{
    "opening_balance_id": "460000000050041",
    "date": "2013-10-01",
    "accounts": [
        {
            "acount_split_id": "460000000050045", /* Required to update */
            "account_id": "460000000000358",
            /* "account_name": "Undeposited Funds", Read-only likely */
            "debit_or_credit": "debit",
            "exchange_rate": 1,
            "currency_id": "460000000000097",
            /* "currency_code": "USD", Read-only likely */
            /* "bcy_amount": 2000, Read-only likely */
            "amount": 2500, /* Updated amount */
            "location_id": "460000000038080"
            /* "location_name": "string" Read-only likely */
        },
        { /* Add new balancing entry if needed */
             "account_id": "NEW_ACCOUNT_ID",
             "debit_or_credit": "credit",
             "amount": 500
        }
        /* Omit an existing account object (by not including its acount_split_id) to delete it */
    ]
}
```

### Response Example
```json
{
    "code": 0,
    "message": "The opening balances are saved!",
    "opening_balance": {
        "opening_balance_id": "460000000050041",
        /* ... updated opening balance details ... */
    }
}
```