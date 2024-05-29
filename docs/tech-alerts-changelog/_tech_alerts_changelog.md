% See the DEA Tech Alerts and Changelog documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

% How to update the 'System status of DEA':
% Change the 'class' to either: tip / caution / danger
% Default content: All DEA systems are working as expected. There are no outstanding incidents or errors to report.

:::{admonition} System status of DEA
:class: caution

* Misclassification issue with Sentinel-2 's2cloudless' cloud masking from 2022. See below.
* Terra-derived DEA Hotspots are unavailable. See below.
* Performance issues with DEA Explorer and STAC API. See below.
:::

## Upcoming change: Shift in origin point of DEA Summary Product Grid

To accommodate an expanded area of coverage of Australia's external territories, the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/) will soon be shifted. The south-west origin point of the grid will be shifted from `-5472000.0, -2688000.0` to `-6912000.0, -4416000.0` (EPSG:3577).

Therefore, all tile grid references will shift 18 tiles west and 15 tiles south. For instance, a tile reference of `x10y10` will change to `x28y25`.

For a preview, see the [provisional version of the expanded DEA Summary Product Grid](https://maps.dea.ga.gov.au/#share=s-avXJqwjUtf55qGUmweYY5KYoVnI) on DEA Maps.

All new versions of our 'summary derivative products' will be affected by this change (but existing versions of the products will not be changed). These products are [DEA Geometric Median and Median Absolute Deviation (GeoMAD)](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/), [DEA Water Observations Statistics (Landsat)](/data/product/dea-water-observations-statistics-landsat/), [DEA Fractional Cover Percentiles](/data/product/dea-fractional-cover-percentiles-landsat/), [DEA Mangroves](/data/product/dea-mangrove-canopy-cover-landsat/), and [DEA Land Cover](/data/product/dea-land-cover-landsat/).

Learn more about the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/).

## 2024-05-24: Misclassification issue with Sentinel-2 's2cloudless' cloud masking from 2022

An issue has been identified that is causing widespread misclassification of clouds in DEA's Sentinel-2 `s2cloudless` cloud mask data generated since January 2022. 

We recommend that you avoid using `s2cloudless` cloud mask data from 2022 onwards until this issue is investigated. 

## 2024-05-13: Terra-derived DEA Hotspots are unavailable

Direct Broadcast satellite downloads from the Terra satellite have again become unavailable. This means that Terra-derived [DEA Hotspots](https://hotspots.dea.ga.gov.au/) are unavailable until further notice.

This is due to the TERRA MODIS satellite experiencing power problems. The satellite continues to collect data but its direct broadcast has stopped.

## 2024-05-06: Performance issues with DEA Explorer and STAC API

You may notice slow load times or outages with the [DEA Explorer](https://explorer.dea.ga.gov.au/) and [DEA Explorer STAC API](https://explorer.dea.ga.gov.au/stac/). We apologise for any inconvenience that this may cause and we are working to solve this issue.

## 2024-05-01: Six of Australia’s offshore territories now covered by Digital Earth Australia baseline satellite data

In support of Indigenous Communities in the Torres Strait, in addition to government agencies reporting on Ocean Ecosystem Accounts and Marine Parks management, DEA is making baseline satellite data available for 6 offshore territories and islands in the Torres Strait.

Learn more about the [DEA ARD expanded processing extent](/guides/reference/ard-expanded-processing-extent/).

## 2024-04-23: It's now easier to cite DEA products

A new 'Cite this product' section has been added to each product page to make it
easier to cite the product in your academic paper, article, or presentation.
A citation may been provided for the data itself, and where relevant, to the
published methods paper. 

See this feature on the [DEA Waterbodies product page](/data/product/dea-waterbodies-landsat/?tab=overview#citations). 

## 2024-04-18: New Validation reports section

The Knowledge Hub contains a new [Validation reports](/validation/) section. This is where you will find reports of Geoscience Australia’s validation data, published periodically. This data can be used to validate Geoscience Australia’s other datasets.

See the latest Daily Validation Summary Report: [2023-11-27: Transect NSW Site 1, Sentinel-2B overpass](/validation/daily-report/2023-11-27/)

## 2024-04-10: DEA Intertidal 1.0.0 released

The [DEA Intertidal](/data/product/dea-intertidal/) product suite maps the changing elevation, exposure and tidal characteristics of Australia’s exposed intertidal zone, the complex zone that defines the interface between land and sea.

This new product suite expands upon the [DEA Intertidal Elevation (Landsat)](/data/old-version/dea-intertidal-elevation-landsat-1.0.0/) product which has now been deprecated.

See [DEA Intertidal](/data/product/dea-intertidal/) for more information.

## 2024-04-03: Terra-derived DEA Hotspots have been restored

Direct Broadcast satellite downloads from the Terra satellite have been restored and have been successfully processed into [DEA Hotspots](/data/product/dea-hotspots/).

## 2024-03-28: DEA Sandbox outage (Resolved)

Users may have encountered an unplanned outage on the [Digital Earth Australia Sandbox](https://app.sandbox.dea.ga.gov.au/).

DEA has implemented a solution as we continue to investigate the cause of the problem.

DEA Sandbox users are warned to expect intermittent issues over the next 12 hours.

Users may be unable to log in to or access their DEA Sandbox account while the incident is being investigated. Users may also notice reduced performance on other DEA systems during this outage.

You can monitor the status of DEA’s systems on the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/). If you would like to contact DEA, please email [earth.observation@ga.gov.au](mailto:earth.observation@ga.gov.au)

## 2024-03-25: DEA Waterbodies version 3.0.0 released

Improvements include additional supporting data for the most recent observations made available through web mapping services (WMS) and DEA Maps, more metadata, Landsat 9 data, and pipeline upgrades. Version 3.0.0 of DEA Waterbodies uses the same underlying polygon set as DEA Waterbodies version 2.0.0. [Learn more](/data/product/dea-waterbodies-landsat/?tab=history)

## 2024-03-21: Terra-derived DEA Hotspots are unavailable (Resolved)

We have received notice from NASA that Direct Broadcast satellite downloads from the Terra satellite are currently unavailable. This means that Terra-derived [DEA Hotspots](https://hotspots.dea.ga.gov.au/) are unavailable until further notice.

## 2024-03-21: DEA OWS services restored

Outages affecting DEA Open Web Services (OWS) have been resolved. Work will be continuing over the coming months to further improve performance and reliability of these services. 

See the [DEA monitoring dashboard](https://monitoring.dea.ga.gov.au/) to check the current status of DEA's services.

## 2024-02-26: Sentinel-2 contiguity fix reprocessing complete

Learn more in the [Sentinel-2A Surface Reflectance NBART](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2a-msi/?tab=history#changelog) and [Sentinel-2B Surface Reflectance NBART](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2b-msi/?tab=history#changelog) changelogs.

## 2024-02-20: DEA Notebooks update

A minor update to the DEA Tools package that includes updates to tide modelling and parallel processing functions. It also adds a new `load_reproject` function to the `datahandling` module which allows reading and reprojecting external raster data. For more detail, see the [dea-notebooks 0.3.1 release notes](https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/0.3.1).

## 2024-02-20: New external land use and bathymetry datasets added to DEA Sandbox

Two new external datasets have been added to the DEA Sandbox: the [2020 ABARES Catchment Scale Land Use of Australia 50m](https://explorer.dea.ga.gov.au/products/abares_clum_2020/datasets/225c3043-6e3f-5cc4-95d0-fa64d79b7d38) 
dataset, and the recently released [2023 Geoscience Australia AusBathyTopo 250m](https://explorer.dea.ga.gov.au/products/ga_ausbathytopo250m_2023/datasets/0b636500-ec81-5bb0-a81d-35c1aed00aaa)
high-resolution depth model for Australia. These datasets provide valuable insights into land use patterns and the physical
shape of Australia's mainland, our coasts and deep ocean regions.

These datasets can be loaded on the DEA Sandbox using the product names `abares_clum_2020` and `ga_ausbathytopo250m_2023`.

## 2024-02-15: Upcoming changes to DEA Geomedian, Median Absolute Deviation and other derivative products

The Geoscience Australia [Landsat Geometric Median and Median Absolute Deviation](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat) Collection 3 products v3.1.0 are undergoing a major upgrade which will be released shortly as v4.0.0.

Find out the details [here](https://communication.ga.gov.au/link/id/zzzz65cd75b153a33890Pzzzz61de67bd94bfe861/page.html).

## 2024-01-24: Water Observations and Fractional Cover Percentiles 2023 annual summaries released

See [DEA Water Observations Statistics (Landsat)](/data/product/dea-water-observations-statistics-landsat/?tab=history) 
and [DEA Fractional Cover Percentiles (Landsat)](/data/product/dea-fractional-cover-percentiles-landsat/) for more information. 

## 2024-01-10: Sentinel-2 contiguity fix - Reprocessing commenced

Reprocessing to fix the Sentinel-2 contiguity issue has commenced with expected completion in early 2024. The issue 
was caused by anomalies in ESA Level 1 source data.

A [known Sentinel-2 contiguity issue](https://communication.ga.gov.au/link/id/zzzz659dea46b27d5565Pzzzz61de67bd94bfe861/page.html) 
created by ESA Level 1 anomalies (“[Striping due to lost source packets](https://communication.ga.gov.au/link/id/zzzz659dea46b3858302Pzzzz61de67bd94bfe861/page.html)”) 
is impacting approximately 0.5% of our Sentinel-2 Analysis Ready Data (S2 ARD) between 2015 and 2023. 

Affected products: 

* ARD Sentinel-2 products (ga_s2am_ard_3, ga_s2bm_ard_3)

See [DEA Tech alert email](https://communication.ga.gov.au/link/id/zzzz659df9f7f306b556Pzzzz61de67bd94bfe861/page.html) for more information. 
Click [here](https://communication.ga.gov.au/link/id/zzzz659de7f165049054Pzzzz61de67bd94bfe861/page.html) to subscribe to DEA Tech alert emails.

