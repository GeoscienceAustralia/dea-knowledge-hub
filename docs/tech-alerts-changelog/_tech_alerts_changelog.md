% See the DEA Tech Alerts and Changelog documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

% How to update the 'System status of DEA':
% Change the 'class' to either: tip / caution / danger
% Default content: All DEA systems are working as expected. There are no outstanding incidents or errors to report.

:::{admonition} System status of DEA
:class: caution

* Expanded extents data processing is currently paused, with data available to May 2024. See below. <!-- NOTE Remember to remove the banner on the page: https://pr-302-preview.khpreview.dea.ga.gov.au/guides/reference/ard-expanded-processing-extent/ -->
* Misclassification issue with Sentinel-2 's2cloudless' cloud masking from 2022. See below.
* Terra-derived DEA Hotspots are unavailable. See below.
* NCI Explorer may experience instability. See below.
:::

## In progress: GeoMAD Processing Bug

A bug in our processing code related to multithreading using numexpr (a fast numerical expression evaluator for Numpy) has been identified which may cause a 400x400 pixel data block to be misplaced within a tile. For the full GeoMAD archive, it is possible that there are around 8-12 tiles with incorrect data (misplaced blocks). It is unknown at this stage which tiles are affected. We are investigating the bug and will provide more information in late 2024 to early 2025.

## In progress: Shift in origin point of DEA Summary Product Grid

:::{include} ../_components/shift-in-summary-product-grid-tech-alert.md
:::

Learn more about the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/).

## 13 Sep 2024: Outage affecting multiple web services (Resolved)

Multiple web services are experiencing an outage: DEA Explorer (Prod), DEA WCS (PROD - EKS), DEA WMS (PROD - EKS), and DEA WMTS (PROD - EKS). We are currently working on resolving the issue. See the [real-time status](https://status.dea.ga.gov.au/) of these services.

<span id="2024-09-02-expanded-extent-paused"></span>

## 2 Sep 2024: Expanded extents data processing is currently paused, with data available to May 2024 <!-- NOTE Remember to remove the banner on the page: https://pr-302-preview.khpreview.dea.ga.gov.au/guides/reference/ard-expanded-processing-extent/ -->

This year, we [expanded the processing extents](/guides/reference/ard-expanded-processing-extent/) for our [Surface Reflectance products](/data/category/dea-surface-reflectance/) and derivative products.

Unfortunately, due to unanticipated issues with an external network connection, we have needed to pause the back-processing of this expanded extent data since May 2024. You may have noticed this issue, for example, if you attempted to access ARD from the Heard Island and McDonald Islands and found that there are no images more recent than May 2024.

## 16 Aug 2024: Hotspots MODIS SRSS missing data (Resolved)

On 21 Aug, we detected that the DEA Hotspots MODIS SRSS sub-product was missing `*hotspots.txt` and `*metadata.txt` files in its daily data folders since 16 Aug. This was caused by a software bug. After detecting the issue, we fixed the bug on the same day and uploaded all the missing data files.

## 8 Aug 2024: NCI Explorer may experience instability

The [NCI Explorer](https://explorer.nci.dea.ga.gov.au/) has experienced some intermittent outages recently. We are currently investigating the cause of the issue. If the NCI Explorer fails to load, please try again later.

## 2 Aug 2024: Version 4.0.0 of DEA Geometric Median and Median Absolute Deviation released

The newly released version 4.0.0 of [DEA Geometric Median and Median Absolute Deviation](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/) contains new features and changes such as the following.

* **Breaking change:** Shift in grid origin point.
* Enhanced cloud masking to reduce noise.
* Combined Landsat 8 and 9 product.
* Prefixed band measurement names.

See the [Version 4.0.0 Changelog](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/?tab=history) for more information.

## 1 Aug 2024: Resolved outage of Hotspots S-NPP VIIRS data

The Suomi-NPP VIIRS Hotspots sub-product has resumed publishing data because the satellite's issue has been resolved.

## 25 Jul 2024: Outage of Hotspots S-NPP VIIRS data (Resolved)

This issue concerns [DEA Hotspots](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/). The Suomi-NPP satellite has experienced a data outage that has resulted in data unavailability until further notice. Therefore, Suomi-NPP VIIRS Hotspots cannot be published until this issue is resolved. Other DEA Hotspots sub-products are unaffected by this outage.

## 1 Jul 2024: External data products now featured on the Knowledge Hub

External data products are produced by external providers such as a different program of Geoscience Australia or a different organisation entirely. These external data products may assist with the analysis of DEA data. DEA even provides services relating to some of these external products. Therefore, we have begun to include some external products on our Knowledge Hub so that you can easily find and access this data. So far, we have added three external data products to the Knowledge Hub. But watch this space, as there are more to come!

View the [External data products in the Knowledge Hub](/data/theme/external-data/).

## 1 Jul 2024: DEA Sandbox new user signups restored

An issue was preventing new users from signing up to the [DEA Sandbox](https://app.sandbox.dea.ga.gov.au/) for the past 5 days. We have now fixed the issue and you should now be able to sign up for the DEA Sandbox.

## 28 Jun 2024: DEA Published Product Currency Report released

We have released a report that tracks the Currency of our data products and if they are on time. Currency is a measure of how consistently DEA’s data products have been published through DEA in line with the stated update frequency on or before the scheduled publish date. External auditors can use this report to verify that DEA is meeting its performance targets, and internally, we use it for our annual reporting practices.

View the [DEA Published Product Currency Report](https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1).

Learn more about how to [understand and analyse this report](/guides/setup/operational-reports/product-currency-report/).

Internal staff can also [view the full history of data](https://mgmt.sandbox.dea.ga.gov.au/d/c1674b20-8c8a-4d90-aef2-02796275cf2b/4e57919d-fc9d-59d7-9bd1-aa61d41bcb92?orgId=1).

## 24 Jun 2024: Performance issues with DEA Explorer and STAC API (Resolved)

The recent performance issues with the [DEA Explorer](https://explorer.dea.ga.gov.au/) and [DEA Explorer STAC API](https://explorer.dea.ga.gov.au/stac/) have now been resolved. You will notice that the performance and stability of these services has returned to normal. We hope you continue to enjoy using these services.

## 14 Jun 2024: DEA Sandbox service has been restored

The unplanned outage that affected the [DEA Sandbox](https://app.sandbox.dea.ga.gov.au/) today has been resolved. The DEA Sandbox is now back online.

## 14 Jun 2024: DEA Sandbox unplanned outage (Resolved)

The [DEA Sandbox](https://app.sandbox.dea.ga.gov.au/) is currently experiencing an unplanned outage. We are investigating the issue and hope to have the service back up and running soon. We will post an update when the service is restored.

## 12 Jun 2024: DEA Intertidal data now available on ELVIS

[DEA Intertidal](/data/product/dea-intertidal/) elevation and uncertainty data can now be ordered and downloaded from the ELVIS platform.

For instructions on how to access this data from ELVIS, visit the [DEA Intertidal page (Access tab)](/data/product/dea-intertidal/?tab=access).

## 30 May 2024: NCI THREDDS data access links updated to point to the new THREDDS server

NCI has released an upgrade to the THREDDS Data Service and will [decommission the existing THREDDS server after 30th June 2024](https://opus.nci.org.au/display/NDP/THREDDS+Upgrade).

To prepare for this change, all THREDDS data access links in the Knowledge Hub have been updated to point to the new THREDDS server: all `https://dapds00.nci.org.au/thredds/...` links have been changed to `https://thredds.nci.org.au/thredds/...`.

## 24 May 2024: Misclassification issue with Sentinel-2 's2cloudless' cloud masking from 2022

An issue has been identified that is causing widespread misclassification of clouds in DEA's Sentinel-2 `s2cloudless` cloud mask data generated since January 2022. 

We recommend that you avoid using `s2cloudless` cloud mask data from 2022 onwards until this issue is investigated. 

## 13 May 2024: Terra-derived DEA Hotspots are unavailable

Direct Broadcast satellite downloads from the Terra satellite have again become unavailable. This means that Terra-derived [DEA Hotspots](https://hotspots.dea.ga.gov.au/) are unavailable until further notice.

This is due to the TERRA MODIS satellite experiencing power problems. The satellite continues to collect data but its direct broadcast has stopped.

## 6 May 2024: Performance issues with DEA Explorer and STAC API

You may notice slow load times or outages with the [DEA Explorer](https://explorer.dea.ga.gov.au/) and [DEA Explorer STAC API](https://explorer.dea.ga.gov.au/stac/). We apologise for any inconvenience that this may cause and we are working to solve this issue.

## 1 May 2024: Six of Australia’s offshore territories now covered by Digital Earth Australia baseline satellite data

In support of Indigenous Communities in the Torres Strait, in addition to government agencies reporting on Ocean Ecosystem Accounts and Marine Parks management, DEA is making baseline satellite data available for 6 offshore territories and islands in the Torres Strait.

Learn more about the [DEA ARD expanded processing extent](/guides/reference/ard-expanded-processing-extent/).

## 23 Apr 2024: It's now easier to cite DEA products

A new 'Cite this product' section has been added to each product page to make it
easier to cite the product in your academic paper, article, or presentation.
A citation may been provided for the data itself, and where relevant, to the
published methods paper. 

See this feature on the [DEA Waterbodies product page](/data/product/dea-waterbodies-landsat/?tab=overview#citations). 

## 18 Apr 2024: New Validation reports section

The Knowledge Hub contains a new [Validation reports](/validation/) section. This is where you will find reports of Geoscience Australia’s validation data, published periodically. This data can be used to validate Geoscience Australia’s other datasets.

See the latest Daily Validation Summary Report: [2023-11-27: Transect NSW Site 1, Sentinel-2B overpass](/validation/daily-report/2023-11-27/)

## 10 Apr 2024: DEA Intertidal 1.0.0 released

The [DEA Intertidal](/data/product/dea-intertidal/) product suite maps the changing elevation, exposure and tidal characteristics of Australia’s exposed intertidal zone, the complex zone that defines the interface between land and sea.

This new product suite expands upon the [DEA Intertidal Elevation (Landsat)](/data/old-version/dea-intertidal-elevation-landsat-1.0.0/) product which has now been deprecated.

See [DEA Intertidal](/data/product/dea-intertidal/) for more information.

## 3 Apr 2024: Terra-derived DEA Hotspots have been restored

Direct Broadcast satellite downloads from the Terra satellite have been restored and have been successfully processed into [DEA Hotspots](/data/product/dea-hotspots/).

## 28 Mar 2024: DEA Sandbox outage (Resolved)

Users may have encountered an unplanned outage on the [Digital Earth Australia Sandbox](https://app.sandbox.dea.ga.gov.au/).

DEA has implemented a solution as we continue to investigate the cause of the problem.

DEA Sandbox users are warned to expect intermittent issues over the next 12 hours.

Users may be unable to log in to or access their DEA Sandbox account while the incident is being investigated. Users may also notice reduced performance on other DEA systems during this outage.

You can monitor the status of DEA’s systems on the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/). If you would like to contact DEA, please email [earth.observation@ga.gov.au](mailto:earth.observation@ga.gov.au)

## 25 Mar 2024: DEA Waterbodies version 3.0.0 released

Improvements include additional supporting data for the most recent observations made available through web mapping services (WMS) and DEA Maps, more metadata, Landsat 9 data, and pipeline upgrades. Version 3.0.0 of DEA Waterbodies uses the same underlying polygon set as DEA Waterbodies version 2.0.0. [Learn more](/data/product/dea-waterbodies-landsat/?tab=history)

## 21 Mar 2024: Terra-derived DEA Hotspots are unavailable (Resolved)

We have received notice from NASA that Direct Broadcast satellite downloads from the Terra satellite are currently unavailable. This means that Terra-derived [DEA Hotspots](https://hotspots.dea.ga.gov.au/) are unavailable until further notice.

## 21 Mar 2024: DEA OWS services restored

Outages affecting DEA Open Web Services (OWS) have been resolved. Work will be continuing over the coming months to further improve performance and reliability of these services. 

See the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/) to check the current status of DEA's services.

## 26 Feb 2024: Sentinel-2 contiguity fix reprocessing complete

Learn more in the [Sentinel-2A Surface Reflectance NBART](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2a-msi/?tab=history#changelog) and [Sentinel-2B Surface Reflectance NBART](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2b-msi/?tab=history#changelog) changelogs.

## 20 Feb 2024: DEA Notebooks update

A minor update to the DEA Tools package that includes updates to tide modelling and parallel processing functions. It also adds a new `load_reproject` function to the `datahandling` module which allows reading and reprojecting external raster data. For more detail, see the [dea-notebooks 0.3.1 release notes](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/0.3.1).

## 20 Feb 2024: New external land use and bathymetry datasets added to DEA Sandbox

Two new external datasets have been added to the DEA Sandbox: the [2020 ABARES Catchment Scale Land Use of Australia 50m](https://explorer.dea.ga.gov.au/products/abares_clum_2020/datasets/225c3043-6e3f-5cc4-95d0-fa64d79b7d38) 
dataset, and the recently released [2023 Geoscience Australia AusBathyTopo 250m](https://explorer.dea.ga.gov.au/products/ga_ausbathytopo250m_2023/datasets/0b636500-ec81-5bb0-a81d-35c1aed00aaa)
high-resolution depth model for Australia. These datasets provide valuable insights into land use patterns and the physical
shape of Australia's mainland, our coasts and deep ocean regions.

These datasets can be loaded on the DEA Sandbox using the product names `abares_clum_2020` and `ga_ausbathytopo250m_2023`.

## 15 Feb 2024: Upcoming changes to DEA Geomedian, Median Absolute Deviation and other derivative products

The Geoscience Australia [Landsat Geometric Median and Median Absolute Deviation](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat) Collection 3 products v3.1.0 are undergoing a major upgrade which will be released shortly as v4.0.0.

Find out the details [here](https://communication.ga.gov.au/link/id/zzzz65cd75b153a33890Pzzzz61de67bd94bfe861/page.html).

## 24 Jan 2024: Water Observations and Fractional Cover Percentiles 2023 annual summaries released

See [DEA Water Observations Statistics (Landsat)](/data/product/dea-water-observations-statistics-landsat/?tab=history) 
and [DEA Fractional Cover Percentiles (Landsat)](/data/product/dea-fractional-cover-percentiles-landsat/) for more information. 

## 10 Jan 2024: Sentinel-2 contiguity fix - Reprocessing commenced

Reprocessing to fix the Sentinel-2 contiguity issue has commenced with expected completion in early 2024. The issue 
was caused by anomalies in ESA Level 1 source data.

A [known Sentinel-2 contiguity issue](https://communication.ga.gov.au/link/id/zzzz659dea46b27d5565Pzzzz61de67bd94bfe861/page.html) 
created by ESA Level 1 anomalies (“[Striping due to lost source packets](https://communication.ga.gov.au/link/id/zzzz659dea46b3858302Pzzzz61de67bd94bfe861/page.html)”) 
is impacting approximately 0.5% of our Sentinel-2 Analysis Ready Data (S2 ARD) between 2015 and 2023. 

Affected products: 

* ARD Sentinel-2 products (ga_s2am_ard_3, ga_s2bm_ard_3)

See [DEA Tech alert email](https://communication.ga.gov.au/link/id/zzzz659df9f7f306b556Pzzzz61de67bd94bfe861/page.html) for more information. 
Click [here](https://communication.ga.gov.au/link/id/zzzz659de7f165049054Pzzzz61de67bd94bfe861/page.html) to subscribe to DEA Tech alert emails.

