# DEA Published Product Timeliness and Currency Report

This report tracks the Timeliness and Currency of DEA's published products. **Timeliness** measures how often a product's data is published on time (where 100% means 'always on time'). **Currency** indicates whether the product currently has the expected data. In this guide, you will learn how to understand and analyse this report.

[View the DEA Published Product Timeliness and Currency Report][TimelinessReport]

:::{admonition} The data isn't loading
:class: note

If the report data doesn't load, please refresh the page and then you should see the data. This seems to be a Grafana bug. If you encounter this bug, you may see the error: "Public dashboard panel not found" or the text: "No data".
:::

:::{contents} In this guide
:depth: 1
:local:
:backlinks: none
:::

## View the reports

The primary report is the [DEA Published Product Timeliness and Currency Report][TimelinessReport]. Internal staff can also view a secondary report containing the history of this data over several years and quarters: [DEA Published Product Timeliness and Currency Report - History][HistoryReport].

## Audience and purpose

The report is designed to be used by both external and internal stakeholders. External auditors may use it to check that our product data is being published on time. Internally, we may use it to define targets that we aim to achieve each financial year. We also use it to gain valuable insights, such as to assess which products are being published reliably versus which products have had difficulties.

## Financial year

This report is based on the Financial Year rather than the Calendar Year. The Financial Year ('fin. year') is from 1 July to 30 June. The report also uses Financial Quarters. These are Q1 (1 Jul &ndash; 30 Sep), Q2 (1 Oct &ndash; 31 Dec), Q3 (1 Jan &ndash; 31 Mar), and Q4 (1 Apr &ndash; 30 Jun).

## Fields of the report

In the [Timeliness and Currency report][TimelinessReport], the following fields contain useful information.

* **Update frequency** &mdash; How often the product data is expected to be published.
* **Last updated** &mdash; The date of the last time that the product data was published.
* **Is current?** &mdash; Whether the product currently has the expected data. (This represents 'Currency'.)
* **Timeliness this fin. year** &mdash; The Timeliness of the product during this financial year, to date. Note that the average of these values for all products in the report is displayed at the top of the report.
* **Timeliness previous fin. year** &mdash; The Timeliness of the product during the previous financial year.
* **Timeliness this fin. quarter** &mdash; The Timeliness of the product during this financial quarter, to date.
* **Timeliness previous fin. quarter** &mdash; The Timeliness of the product during the previous financial quarter.

## Which products are included?

Only products that meet the following criteria are included in this report. This is so that the Timeliness and Currency statistics are meaningful for all the products in this report.

* **Published product** &mdash; Not a 'provisional product'.
* **Latest version** &mdash; Not an old version.
* **Regularly updated** &mdash; Not a product with 'No updates planned'.

Therefore, if you can't find a certain product in the report, it is likely that it doesn't meet one of those criteria.

## The Products and Additional products tables

This report includes two tables: **Products** and **Additional products**. The Products table is for products that are tracked automatically by our system and this table contains the most comprehensive data. The Additional products table is for products that we track manually and this table contains only the essential data.

## How Timeliness is calculated

Timeliness is a value that ranges from 0% (meaning 'never on time') to 100% (meaning 'always on time').

In the **Products** table, it is calculated by ...................... TODO

In the **Additional products** table, it is calculated from the number of days that the product has been overdue throughout the entire financial year. It uses the following formula.

$100 - (\frac{d}{365.25} \times 100)$

Where $d$ is the number of days overdue this financial year.

## How Currency is calculated

In the **Products** table, it is calculated automatically by our system based on the age of the latest 'scene' in the product. Internal staff can learn the [technical details of DEA Currency][CurrencyInternalDoc].

The 'Is current' data is not available in the **Additional products** table.

[TimelinessReport]: https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1
[HistoryReport]: https://mgmt.sandbox.dea.ga.gov.au/d/c1674b20-8c8a-4d90-aef2-02796275cf2b/4e57919d-fc9d-59d7-9bd1-aa61d41bcb92?orgId=1
[CurrencyInternalDoc]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html#sqs-currency
