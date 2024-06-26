# DEA Published Product Currency Report


The [DEA Published Product Currency Report][CurrencyReport] tracks the percentage of DEA published data products that are current. Note that products that don't periodically publish new data and provisional products are excluded from this report.

(Internal staff can view the full history of data in the [Currency History Report][HistoryReport] which will also be explained in this guide. Internal staff can also [contribute to the Currency logbook][CurrencyLogbook].)

:::{admonition} Get started
:class: note

Open the [DEA Published Product Currency Report][CurrencyReport]
:::

:::{contents} In this guide
:depth: 1
:local:
:backlinks: none
:::

## Definition of Currency

Currency is a reporting metric that we define as follows.

> **Currency:** A measure of how consistently Digital Earth Australia's data products have been published through Digital Earth Australia in line with the stated update frequency (e.g. daily or yearly) on or before the scheduled publish date (as recorded on the Digital Earth Australia Knowledge Hub).

Essentially, Currency measures how often DEA's data products publish their data on time, according to their scheduled publish dates. It ranges from 100% meaning 'always on time' to 0% meaning 'never on time'.

Currency can be measured on a daily, quarterly, and yearly basis (Daily Currency, Quarterly Currency, and Yearly Currency). Furthermore, Currency can be measured for a single product or it can be aggregated across all products.

We also measure whether a product 'is current'. This refers to whether the product's data is currently up-to-date according to its publishing schedule, or whether a delay is being experienced. The value of 'is current' is either 'Yes' or 'No'.

## Audience and purpose

The [Currency Report][CurrencyReport] is provided for the public and also for internal stakeholders. External auditors can use it to verify that DEA is meeting their performance targets. Internally, we use it for our annual reporting practices.

## Financial year reporting cycle

This report is based on the Financial Year (FY) which starts in 1 July and ends in 30 June each year. Furthermore, the report uses Financial Quarters &mdash; these are Q1 (1 Jul &ndash; 30 Sep), Q2 (1 Oct &ndash; 31 Dec), Q3 (1 Jan &ndash; 31 Mar), and Q4 (1 Apr &ndash; 30 Jun).

## Fields of the report

Here are explanations of the fields used in this report.

* **Update frequency** &mdash; How often the product data is published.
* **Last updated** &mdash; The date of the last time that the product data was published.
* **Is current?** &mdash; Whether the product currently has the expected data (versus, whether it is currently delayed). For example, if data was scheduled to be published on 1 Jan, but it is now 1 Feb and the data hasn't been published, then this value will be 'No'. When the data is eventually published, this value will change to 'Yes'.
* **Currency this FY** &mdash; The Currency of the product during this financial year, up to the current date. The aggregate of this statistic across all products is included at the top of the report.
* **Currency previous FY** &mdash; The Currency of the product during the previous financial year.
* **Currency this quarter** &mdash; The Currency of the product during this financial quarter, up to the current date.
* **Currency previous quarter** &mdash; The Currency of the product during the previous financial quarter.

## Which products are not included?

Currency can only be meaningfully tracked for certain types of products and that is why not all products are included in this report. If you cannot find a product in this report, it is due to one of the following reasons.

* It is a **provisional product** &mdash; Provisional products have not yet passed quality control and/or been finalised for release.
* It is **not the latest version** of the product &mdash; Only the latest version of the product contains the latest processing algorithm and latest features.
* It is **not updated periodically** &mdash; Only products that are updated on a periodic basis (e.g. Daily or Yearly) are included in this report.
* It does **not have any updates planned** &mdash; Products for which we don't plan to publish any more data are not included in this report.

For example, the [DEA Wetlands Insight Tool][WetlandsInsight] products are only published 'as needed' &mdash; they are not updated on a periodic basis and therefore they aren't included in this report. And, the [DEA Land Cover (Landsat)][LandCover] tool has 'no updates planned', so it is also excluded from the report.

[WetlandsInsight]: https://knowledge.dea.ga.gov.au/data/category/dea-wetlands-insight-tool/
[LandCover]: https://knowledge.dea.ga.gov.au/data/product/dea-land-cover-landsat/

## Table A vs Table B

The report contains two tables: **Products (Table A)** and **Products (Table B)**. Table A contains the Daily products and any other products that can be tracked automatically by our system. In contrast, Table B contains the Yearly products and any other products that cannot be tracked automatically by our system. Table B is partially automatic but requires a small amount of data entry from our staff once per year.

One thing to note about Yearly products is that we may schedule to publish them on a different date each year. Hence, if a yearly product was published on 1 August last year, you cannot assume that it will be published on 1 August this year.

## How Currency is calculated

The way that Currency is calculated differs between Table A and Table B.

### Table A calculations

For products in **Table A**, the following calculations are made. This is an automatic process.

1. Find out the age of the latest 'scene' of a product. To find out this age, we use one of multiple methods. Internal staff can learn the [technical details of these Currency methods][CurrencyInternalDoc]. The latest scene is compared to the current calendar date to find the age.
    $\text{Age} = \text{Acquisition date} - \text{Calendar date}$
1. Check the 'business rule' for the product. This rule defines the maximum threshold for this age value that we calculated. For instance, a product may have a business rule of $\leq 16\ days$. This means that if the age is more than 16 days, then the data is overdue. We run this check every day and if the age is within the threshold, we assign 100% Currency for that day; whereas, if the age is above the threshold, we assign 0% Currency for that day.
1. The Currency values over a span of multiple days are averaged to find the Currency for each financial year and the Currency for each financial quarter.

<span id="table-b"></span>

### Table B calculations

For products in **Table B**, the following calculations are made. This is a partially automatic and partially manual process.

1. An automated script runs every day to calculate the Currency of the products in this table based on their **Latest release** date and **Next update due** dates. Internal staff can learn about the [technical details of this script and other details of Table B][CurrencyInternalDocTableB].
1. The Currency value is then calculated as follows.
    * If the product is overdue ($\text{Days overdue} > 0$), then the formula is used:

        $\text{Currency} = 100 - (\frac{\text{Days overdue}}{365.25} \times 100)$

        This formula calculates the number of days overdue as a percentage of the entire year (365.25 days). Therefore, if the product is 5 days overdue, the Currency will be 98.63%.

        Note that the Currency is always a value between 0% and 100%. It cannot be a negative value.

    * Otherwise, if the product is not overdue ($\text{Days overdue} = 0$), then the Currency will be 100%.
1. Each financial year, a few manual steps are required. Internal staff will need to [complete the manual steps][CurrencyInternalDocManualSteps].

## History report

The [Currency History Report][CurrencyReport] report provides a history of the data from the Currency report since the beginning of when we started tracking this statistic: 1 July 2024. It can only be accessed by internal stakeholders. This report uses the same data as the Currency report but it includes the history of previous years.

Note that it doesn't include the data from 'Products (Table B)' of this report due to technical limitations. Instead, the historical data of 'Products (Table B)' is stored in a log table in the database.

[CurrencyReport]: https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1
[HistoryReport]: https://mgmt.sandbox.dea.ga.gov.au/d/c1674b20-8c8a-4d90-aef2-02796275cf2b/4e57919d-fc9d-59d7-9bd1-aa61d41bcb92?orgId=1
[CurrencyInternalDoc]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html
[CurrencyInternalDocTableB]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html#table-b
[CurrencyInternalDocManualSteps]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html#manual-steps
[CurrencyLogbook]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency_logbook.html#currency-report-logbook
