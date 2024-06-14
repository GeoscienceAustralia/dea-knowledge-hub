# DEA Published Product Currency Report


The [DEA Published Product Currency Report][CurrencyReport] tracks the percentage of DEA published data products that are current. Note that products that don't periodically publish new data and provisional products are excluded from this report.

(Internal staff can view the full history of data in the [Currency History report][HistoryReport] which will also be explained in this guide. Internal staff can also [contribute to the Currency logbook][CurrencyLogbook].)

:::{contents} In this guide
:depth: 1
:local:
:backlinks: none
:::

## Definition of Currency

Currency is a reporting metric used by DEA that is defined as "the percentage of DEA published data products that are current". It measures how often a product's data is published on time within the financial year (1 July to 30 June) or financial quarter. It is a percentage value where 100% means 'always on time' and 0% means 'never on time'. Currency is tracked for individual products and these are aggregated into an average value for DEA as a whole.

We also measure whether a product 'is current'. This indicates whether the product currently has the expected data, or if there is currently a delay in publishing. This value is either 'Yes' or 'No'.

## Audience and purpose

The [Currency Report][CurrencyReport] is provided for both external and internal stakeholders. External auditors can use it to verify that DEA is meeting their performance targets. Internally, we may use it to gain insight on which products have high performance versus which products have encountered difficulties.

## Financial year reporting cycle

The reporting cycle is the Financial Year ('fin. year') which starts in 1 July and ends in 30 June each year. Furthermore, the report uses Financial Quarters &mdash; these are Q1 (1 Jul &ndash; 30 Sep), Q2 (1 Oct &ndash; 31 Dec), Q3 (1 Jan &ndash; 31 Mar), and Q4 (1 Apr &ndash; 30 Jun).

## Fields of the report

Here are explanations of the fields used in this report.

* **Update frequency** &mdash; How often the product data is published.
* **Last updated** &mdash; The date of the last time that the product data was published.
* **Is current?** &mdash; Whether the product currently has the expected data (versus, whether it is currently delayed).
* **Currency this fin. year** &mdash; The Currency of the product during this financial year, up to the current date. The aggregate of this statistic across all products is included at the top of the report.
* **Currency previous fin. year** &mdash; The Currency of the product during the previous financial year.
* **Currency this fin. quarter** &mdash; The Currency of the product during this financial quarter, up to the current date.
* **Currency previous fin. quarter** &mdash; The Currency of the product during the previous financial quarter.

## Which products are not included?

Currency can only be meaningfully tracked for certain types of products and that is why not all products are included in this report. If you cannot find a product in this report, it is due to one of the following reasons.

* It is a **provisional product** &mdash; Provisional products have not yet passed quality control and/or been finalised for release.
* It is **not the latest version** of the product &mdash; Only the latest version of the product contains the latest processing algorithm and latest features.
* It is **not updated periodically** &mdash; Only products that are updated on a periodic basis (e.g. Daily or Yearly) are included in this report.
* It does **not have any updates planned** &mdash; Products for which we don't plan to publish any more data are not included in this report.

## Products vs Yearly products

The report contains two tables: **Products** and **Yearly products**. The Products table contains the Daily products and other products that can be tracked automatically by our system. Alternately, the Yearly products table contains the Yearly products and any other products that cannot be tracked manually by our system. The Yearly products table is partially automatic, but requires some manual data entry from our staff.

## Calculating Currency for Daily products

The Currency values for Daily products are automatically tracked by our system based on the date that the data was last published. Internal staff can learn the [technical details of how DEA Currency is tracked][CurrencyInternalDoc]. In summary, the Currency is tracked using either of the following methods: it can use the Open Data Cube (ODC) data, an SQS queue subscribed to certain events, or is calculated from another statistic called Completeness.

## Calculating Currency for Yearly products






NOTE yearly products are published yearly not on strict date.






## Algorithm for Timeliness

In the **Products** table, Timeliness is calculated by an algorithm that works as follows.

1. Find the age of the latest published data (in hours). This is calculated from the difference between the latest scene's acquisition date and the calendar time.

    $age = acquisition\_date - calendar\_time$

1. Each product has a 'business rule' that defines the maximum threshold for this age that we calculated. For instance, a product may have a business rule of $\leq 16\ days$. This means that if the age is more than 16 days, then the data is overdue. We run this check every day and if the age is within the threshold, we assign 100% Timeliness for that day; whereas, if the age is above the threshold, we assign 0% for that day.
1. The Timeliness values of a span of multiple days are averaged to find the Timeliness for each financial year and the Timeliness for each financial quarter.

In the **Additional products** table, Timeliness is calculated based on the number of days that the product has been overdue throughout the entire financial year. Our staff manually record the number of days  that it has been overdue. It uses the following algorithm.

$100 - (\frac{d}{365.25} \times 100)$

Where $d$ is the number of days overdue this financial year.

For example, if the product has been overdue for 5 days, the Timeliness will be 98.63%.

## History report

The [DEA Published Product Currency Report - History][CurrencyReport] report provides a history of the data from the Currency report since 1 July 2024 (which is the time when we began tracking this statistic). It is password-protected and can only be accessed by some Geoscience Australia internal stakeholders. This report uses the same data as the Currency report but it includes the history of previous years. However, note that it doesn't include the data from the Yearly products table of this report, due to technical limitations. The Yearly products historical data is stored in a 'log table' in the database.

[CurrencyReport]: https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1
[HistoryReport]: https://mgmt.sandbox.dea.ga.gov.au/d/c1674b20-8c8a-4d90-aef2-02796275cf2b/4e57919d-fc9d-59d7-9bd1-aa61d41bcb92?orgId=1
[CurrencyInternalDoc]: https://docs.dev.dea.ga.gov.au/internal_services/reporting-systems/etls/currency.html
