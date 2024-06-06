# DEA Published Product Timeliness and Currency Report

In this guide, you will learn how to understand and analyse the [DEA Published Product Timeliness and Currency Report][TimelinessReport]. You will also learn about the report containing the historical data (however this report is only available to internal stakeholders): [DEA Published Product Timeliness and Currency Report - History][HistoryReport].

:::{admonition} Bug: The report data doesn't load when opened via link
:class: note

When you open a report by clicking a link from another report, the data may fail to load due to a Grafana bug. To load the data, you will need to refresh the page. If you encounter this bug, you may see the "Public dashboard panel not found" error or the "No data" text.
:::

:::{contents} In this guide
:depth: 1
:local:
:backlinks: none
:::

## Audience and purpose

The [Timeliness and Currency Report][TimelinessReport] is designed to be used by both external and internal stakeholders. External auditors can use it to check that our product data is being published on time. Internally, we may use it to define targets that we aim to achieve each financial year. We can also use it to gain insight on which products are being published reliably versus which products have encountered difficulties.

## Key terms

The key terms used in this report are defined as follows.

* **Timeliness** &mdash; A measure of how often a product's data is published on time. It is a value that ranges from 0% (meaning 'never on time') to 100% (meaning 'always on time').
* **Currency** &mdash; A measure of whether the product currently has the expected data. This is indicated by the 'Is current' metric which can be either 'Yes' or 'No'.

## Financial year

This report is based on the Financial Year ('fin. year') which starts in 1 July and ends in 30 June. (It doesn't use the Calendar Year which is from 1 Jan to 31 Dec.) Furthermore, the report uses Financial Quarters &mdash; these are Q1 (1 Jul &ndash; 30 Sep), Q2 (1 Oct &ndash; 31 Dec), Q3 (1 Jan &ndash; 31 Mar), and Q4 (1 Apr &ndash; 30 Jun).

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

In the **Products** table, Timeliness is calculated by an algorithm that works as follows.

1. Calculate the age of the latest published data by finding the difference between the latest scene's acquisition date and the calendar time.
1. If the age is within the threshold of a specified business rule, then the timeliness is 100% for this day. If not, then it is 0%.
1. The Timeliness of multiple days are averaged across a financial year and across a financial quarter.

In the **Additional products** table, Timeliness is calculated from the number of days that the product has been overdue throughout the entire financial year. It uses the following formula.

$100 - (\frac{d}{365.25} \times 100)$

Where $d$ is the number of days overdue this financial year.

So if the product has been overdue for 5 days throughout the entire financial year so far, the Timeliness will be 98.63%.

## How Currency is calculated

In the **Products** table, the 'Is current' data is calculated automatically by our system based on the date that the data was last published. Internal staff can learn the [technical details of DEA Currency][CurrencyInternalDoc].

The 'Is current' data is not available in the **Additional products** table.

[TimelinessReport]: https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1
[HistoryReport]: https://mgmt.sandbox.dea.ga.gov.au/d/c1674b20-8c8a-4d90-aef2-02796275cf2b/4e57919d-fc9d-59d7-9bd1-aa61d41bcb92?orgId=1
[CurrencyInternalDoc]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html#sqs-currency
