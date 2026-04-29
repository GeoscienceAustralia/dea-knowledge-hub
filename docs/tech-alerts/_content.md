% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

## 30 April 2026: DEA coastal products &mdash; annual update now available

![]()

<figure>
    <figcaption>DEA Coastlines showing Cervantes, WA with annual coastline data of 37 years of coastal change (1988-2025).</figcaption>
</figure>

The latest annual product update is now available for the following DEA coastal products:

* [DEA Coastlines](/data/product/dea-coastlines/) &mdash; 2025 annual data
* [DEA Intertidal](/data/product/dea-intertidal/) &mdash; 2024 annual data
* [DEA Tidal Composites](/data/product/dea-tidal-composites/) &mdash; 2024 annual data

These annual updates support year-to-year comparison of shoreline and coastal change, including in areas with rapid or significant coastal dynamics.

![]()

<figure>
    <figcaption>DEA Intertidal shows Arnhem Land, Northern Territory in 2024 using Intertidal Elevation layer.</figcaption>
</figure>

DEA users now have access to the latest annual coastal data, with 2025 Coastlines and 2024 Intertidal and Tidal Composites available for analysis and comparison.

The Intertidal and Tidal Composites products continue to be generated using a three-year rolling window (this release draws on 2023–2025 observations) to provide the best view of the median year, 2024. This supports robust year-to-year assessment of Australia’s dynamic coastal environments.

![]()

<figure>
    <figcaption>DEA Tidal Composites false colour view of the Cambridge Gulf, Western Australia in 2024 showing high tide flooding.</figcaption>
</figure>

Together, these updates provide a nationally consistent view of Australia’s coastlines and align coastal datasets with DEA’s annual terrestrial data cycle, helping users confidently monitor and compare change across land, water and coastal zones.

[View the Tech Alert]()

## 15 April 2026: Upcoming updates to DEA Water Observations Multi-Year, Mangroves and Land Cover summary products

As part of Digital Earth Australia’s (DEA) planned 2025 annual product update in the coming weeks, [DEA Water Observations Multi-Year Summary data](/data/product/dea-water-observations-statistics-landsat/) will be made available to include an additional two years of data. The existing version will be replaced with the expanded time series.

Additionally, the [DEA Mangroves](/data/product/dea-mangroves/) and [Land Cover](/data/product/dea-land-cover-landsat/) products will have an update to **Tile x28y46** on the West Australian coast as a classification error was identified. Some areas of ocean in this tile were misclassified as mangroves and will be corrected in the historical records.

These updates are expected to take place during the **week of 27 April 2026**, alongside DEA’s 2025 annual product update.

No action is required; temporary disruptions could be experienced to the DEA Water Observations Multi-Year Summary, DEA Land Cover and Mangroves products during the data transition period.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz69deeb5f9e03e642Pzzzz6567c8b713b5b826/page.html)

## 2 Apr 2026: Interim Processing Approach to Digital Earth ARD Dataset

**What’s happening?**

Digital Earth Australia (DEA)’s Landsat and Sentinel 2 [Analysis Ready Data (ARD) products](/data/category/dea-surface-reflectance/) currently use third party datasets to correct the data for Australian conditions. A dataset used in this correction - the National Oceanic and Atmospheric Administration’s NCEP/NCAR Reanalysis 1 water vapour dataset has been discontinued.

To address this the Digital Earth team will be incorporating the European Centre for Medium Weather Forecast (ECMWF) data source into its ARD corrections, which has been assessed and found suitable as an alternative source of water vapour data. This action will provide Digital Earth the time to undertake an assessment of other data sources to identify the long-term solution.

DEA derivative data products will experience an interruption in service while ECMWF is incorporated into our processing pipelines. The products that will be affected include:

* [DEA Water Observations (Landsat)](/data/product/dea-water-observations-landsat/)
* [DEA Fractional Cover (Landsat)](/data/product/dea-fractional-cover-landsat/)
* [DEA Waterbodies (Landsat)](/data/product/dea-waterbodies-landsat/)
* [DEA Fuel Moisture Content (Sentinel 2)](/data/product/dea-fuel-moisture-content/)

**DEA ARD dataset maturity**

DEA ARD data will continue to be produced until a suitable alternative water vapour dataset is available. The ARD correction will continue to be applied to DEA data using a pre-calculated climatology, which is currently used in the “near-real time” (NRT) ARD products.

Data produced using this climatology will be flagged with the “interim” maturity flag to make it easy to identify in metadata. More information about DEA dataset maturity [can be found here](/guides/reference/dataset_maturity_guide/).

Once the ECMWF data is incorporated into our processes, the interim flagged data will be reprocessed, and a “final” maturity product will be produced using this data source.

DEA’s downstream data products will only be processed from “final” quality data and will experience a disruption in production while this activity is underway.

**When’s it happening?**

DEA Landsat and Sentinel 2 ARD products will begin to see production of “interim” data from 9 April 2026.

Once this occurs, the impacted DEA derivative products listed will stop updating.

At this stage, we anticipate that ARD corrections using ECMWF will resume by early May 2026. We will notify DEA users with a Tech Alert when available.

Once a suitable long-term replacement water vapour dataset is available, we will advise DEA users of how we intend to incorporate it into our data collection.

**What action do you need to take?**

No action by users is required.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz69cdf18461773486Pzzzz6567c8b713b5b826/page.html)

## 3 Mar 2026: Redundant Sentinel-2 Near Real Time data removed

![](/_files/tech-alerts/2026-03-03-nrt-data-removed.jpeg)

<figure>
    <figcaption>The DEA Landsat and Sentinel tile grids showing redundant tiles that have been removed circled in red.</figcaption>
</figure>

Digital Earth Australia (DEA) has removed more than 87,000 redundant Near-Real Time (NRT) data tiles from our Surface Reflectance data to ensure consistency within the definitive DEA tile set.

NRT is the [rapid dataset maturity level](/guides/reference/dataset_maturity_guide/) produced within 48 hours of image capture, but it is considered of lower quality than our final Anaysis Ready Data (ARD) products. These NRT data are later converted to the definitive or ‘final’ maturity level when high quality ancillary data is available.

To better manage our data and improve system processing we have begun cleaning up these redundant packets that have been superseded by the final definitive data.

During this process we have identified NRT that are not available in the final datasets, as well as tiles in the definitive datasets that are not available in NRT.

To address this we have removed redundant Sentinel-2 tiles in the NRT processing only, leaving the definitive tile set in place.

We have also updated the processing tile sets for Landsat and Sentinel-2 and synchronised the [NCI](https://explorer.nci.dea.ga.gov.au/products) and [AWS](https://explorer.dea.ga.gov.au/products) processing so both services now work off the same core tile set.

For the Landsat tile set there will be additional tiles processed to AWS while for Sentinel-2 some tiles will be removed as well as some tiles added. This will result in a net reduction in the number of tiles processed to AWS, and a minor net-gain for NCI. The majority of the NRT tiles are over the ocean and deemed unlikely to include relevant EO data.

By removing the old NRT data and synchronising NCI and AWS tile processing we will provide better overall data management and consistency across these DEA services.

This process has been completed and we will continue to monitor the changes into the near future.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz69a66543ec0f4562Pzzzz6567c8b713b5b826/page.html)

(s2a-re-enabled-tech-alert)=

## 3 Mar 2026: New Sentinel-2A ARD made available after mission continuation

DEA has reenabled Sentinel-2A (S2A) data following the European Space Agency (ESA) announcing in early 2025 the satellite mission [will continue in a modified orbit adjacent to Sentinel-2B (S2B)](https://dataspace.copernicus.eu/news/2025-1-27-sentinel-2a-exceptional-temporary-extension-campaign-starting-march-2025).

This extended campaign includes a unique tandem acquisition period between January and March 2026. This will allow the two satellites to capture scenes in nearly identical conditions, further enhancing radiometric performance and consistency. You can read more at the [Copernicus Data Space Ecosystem website](https://dataspace.copernicus.eu/news/2025-12-19-sentinel-2a-and-sentinel-2b-tandem-acquisitions) and [here](https://sentiwiki.copernicus.eu/web/s2-mission).

The current estimate of the S2A datasets to be added to the collection as of 09/02/2026 is around 28,000. For comparison, the numbers of Sentinel-2B and Sentinel-2C datasets for the same period are 66,011 and 63,449 respectively.

Sentinel-2A has been collecting data for nearly 12 months. This data will now be added to our ARD collection.

The additional S2A datasets are now available. You can now see the temporary tandem acquisitions of S2A and S2B swaths on [DEA Maps](https://maps.dea.ga.gov.au/#share=s-t7l2lP0FPHEW2eWsC9a6ez4AupT).

Even though Sentinel-2A is now on the modified orbit following Sentinel-2B, the orbital parameters of the satellite remain largely unchanged.

DEA users with existing workflows consuming Sentinel-2B and Sentinel-2C data should not see any impact, and no further action should be required. However, users running automatic workflows that are not filtering out Sentinel-2A data may see an uptick in data volume as we process and publish our Sentinel-2A data backlog.

If you do not want to process these S2A data in your workflows, please make sure to exclude them.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz69a66543ec0f4562Pzzzz6567c8b713b5b826/page.html)

## Summary of DEA Tech Alerts 2025

The following Tech Alerts were posted to this page in the previous year. To read these, [view DEA Tech Alerts 2025](/tech-alerts/2025/).

| Date&nbsp;posted | Title of Tech Alert |
|---|---|
| 18 Dec 2025 | Shutdown period (Resumed) |
| 17 Dec 2025 | New release &mdash; Digital Earth Australia Coastal Ecosystems |
| 19 Nov 2025 | The Landsat 9 satellite outage 17&ndash;23 October 2025 (Resolved) |
| 18 Nov 2025 | Digital Earth access to Landsat 8 and 9 data restored |
| 20 Oct 2025 | Landsat production currently impacted by outage (Resolved) |
| 14 Oct 2025 | New release &mdash; DEA Fuel Moisture Content |
| 14 Oct 2025 | DEA Sandbox access update |
| 2 Oct 2025 | US Government Shutdown Impact: Geoscience Australia’s Digital Earth not currently experiencing any disruption to services |
| 10 Sep 2025 | DEA Land Cover continental mosaics |
| 10 Sep 2025 | Old product versions being deprecated soon |
| 10 Sep 2025 | DEA data in the Digital Atlas of Australia |
| 26 Jun 2025 | Tech Alert |
| 23 May 2025 | NOAA-19-derived DEA Hotspots discontinued from 16 June 2025 |
| 21 May 2025 | DEA Waterbodies 3.0 |
| 15 May 2025 | DEA Intertidal 2.0.0 released incorporating 2023 data |
| 15 May 2025 | DEA Tidal Composites released |
| 1 May 2025 | Missing Sentinel-2C data on AWS datacube is being restored |
| 30 Apr 2025 | DEA Coastlines 3.0 and 2024 data are now available |
| 30 Apr 2025 | DEA Terrestrial products 2024 calendar year updates now available |
| 22 Apr 2025 | DEA Sandbox technical review update |
| 22 Apr 2025 | STAC API/Explorer |
| 4 Apr 2025 | URGENT: The DEA Sandbox is offline until further notice (Resolved) |
| 3 Apr 2025 | URGENT: DEA Sandbox will be offline from 4pm Friday 4 April 2025 until further notice (Resolved) |
| 1 Apr 2025 | NOAA-21 Hotspots will be integrated with other VIIRS Sensors from 8 April |
| 20 Mar 2025 | DEA Sentinel-2C data now operational   |
| 20 Mar 2025 | s2cloudless cloud mask data reprocessed |
| 13 Mar 2025 | Landsat near-real-time (NRT) data outage (Resolved) |
| 12 Mar 2025 | Landsat near-real-time (NRT) data outage (6 March to the present) due to planned USGS maintenance and a subsequent issue |
| 5 Mar 2025 | Shift in origin point of DEA Summary Product Grid |
| 5 Mar 2025 | Version 2.0.0 of DEA Land Cover released |
| 20 Feb 2025 | DEA near-real-time data not up-to-date |
| 20 Feb 2025 | DEA Sandbox unplanned outage (Resolved) |
| 21 Jan 2025 | Sentinel-2A data switching over to Sentinel-2C |
| 8 Jan 2025 | DEA Maps data not up-to-date (Resolved) |

