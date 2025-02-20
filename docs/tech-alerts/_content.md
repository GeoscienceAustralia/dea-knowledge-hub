% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

::::{dropdown} In progress: Shift in origin point of DEA Summary Product Grid
:::{include} ../_components/shift-in-summary-product-grid-tech-alert.md
:::

Learn more about the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/).
::::

## 20 Feb 2025: DEA data not up-to-date

DEA ARD datasets are currently not up-to-date. We are investigating the cause of this issue. 

## 20 Feb 2025: DEA Sandbox unplanned outage (Resolved)

The DEA Sandbox is currently unavailable. We are currently working to restore the service. 

## 21 Jan 2025: Sentinel-2A data switching over to Sentinel-2C

Digital Earth Australia’s Sentinel-2A data products will stop publishing data updates on 21 January 2025. They will be replaced with equivalent Sentinel-2C data products, which will begin publishing data shortly after. For further information on the precise timing of the transfer, please see [Sentinel Online](https://sentinel.esa.int/web/sentinel/-/precise-timing-of-transfer-of-duty-from-sentinel-2a-to-sentinel-2c-on-21-january). The historical Sentinel-2A data will still be provided as public data. A new ga_s2cm_ard_3 product will begin receiving data for both our NRT and definitive offerings within the coming weeks. 

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz678f06dcdfdd9113Pzzzz6567c8b713b5b826/page.html)

## 08 Jan 2025: DEA Maps data not up-to-date (Resolved)

[DEA Maps](/guides/setup/dea_maps/) and [OWS layers](/guides/setup/gis/README/) are not currently up-to-date with the data available on [DEA AWS](/guides/setup/AWS/data_and_metadata/). We are investigating the cause of this issue. 

The affected services will be updated once the issue is resolved. 

## 2 Sep 2024: Expanded extents data processing is currently paused, with data available to May 2024 <!-- NOTE Remember to remove the banner on the page: https://pr-302-preview.khpreview.dea.ga.gov.au/guides/reference/ard-expanded-processing-extent/ -->

This year, we [expanded the processing extents](/guides/reference/ard-expanded-processing-extent/) for our [Surface Reflectance products](/data/category/dea-surface-reflectance/) and derivative products.

Unfortunately, due to unanticipated issues with an external network connection, we have needed to pause the back-processing of this expanded extent data since May 2024. You may have noticed this issue, for example, if you attempted to access ARD from the Heard Island and McDonald Islands and found that there are no images more recent than May 2024.