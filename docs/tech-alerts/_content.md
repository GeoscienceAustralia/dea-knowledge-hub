% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

## 3 Apr 2025: DEA Sandbox will be offline from 4pm Friday 4 April 2025 until further notice

Digital Earth Australia (DEA) is conducting a review of the DEA Sandbox to address ongoing technical issues. The DEA Sandbox will be offline from **4pm AEDT Friday 4 April 2025**. Users will not be able to access the DEA Sandbox environment while the review takes place.

Users will continue to have access to other DEA data and products, including DEA Maps and DEA Explorer, which will continue to update with Landsat and Sentinel data as normal. Users can also refer to [user guides](/guides/setup/dea_maps/) on how to download DEA data or access DEA web services. The 'Access' tab for each Product on the [DEA Knowledge Hub Data Product Catalogue](/data/) also contains targeted information on how to access and interact with each DEA product specifically. 

The DEA notebooks provided in the DEA Sandbox are still available to users via the [DEA Knowledge Hub - DEA Notebooks section](https://knowledge.dea.ga.gov.au/dea-notebooks/).

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz67edf098d41fd019Pzzzz6567c8b713b5b826/page.html)

## 1 Apr 2025: NOAA-21 Hotspots will be integrated with other VIIRS Sensors from 8 April

In [DEA Hotspots](/data/product/dea-hotspots/), the NOAA-21 feed can currently be selected through ‘AFIMG NOAA-21’, or ‘AFMOD NOAA-21’, but will be incorporated into the standard ‘AFMOD’ and ‘AFMIG’ filter from 8 April 2025.
 
NOAA-21 data can also be downloaded from the Sentinel S3 bucket with the Satellite ID ‘J02’. 

[View the Tech Alert](https://communication.ga.gov.au/NOAA-21-Hotspots-Integrated-with-other-VIIRS-Sensors)

## 20 Mar 2025: DEA Sentinel-2C data now operational  

Sentinel-2C data are now operational and supplying DEA products. DEA’s [ga_s2cm_ard_3](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2c-msi/) product is receiving data for both our NRT and definitive offerings, which should now be fed into user workflows. [DEA Maps](http://maps.dea.ga.gov.au/#share=s-oeiMObC1NOBrld9OlCY9hcjdzNB), the [DEA Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login), and [DEA Notebooks](https://knowledge.dea.ga.gov.au/notebooks/DEA_products/DEA_Sentinel2_Surface_Reflectance/) have all been updated to include Sentinel-2C data.

Users of our Sentinel-2A products ([ga_s2am_ard_3](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2a-msi/)) should switch to our Sentinel-2C data products. Please note Sentinel-2B continued to provide data throughout and hence our Sentinel-2B product ([ga_s2bm_ard_3](https://knowledge.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2b-msi/)) is not affected by this switch-over process.

In February, the [European Commission](https://communication.ga.gov.au/link/id/zzzz67db6439c4d9b829Pzzzz61de67bd94bfe861/page.html) announced an “exceptional and temporary extension” to the life and availability of data from the Sentinel-2A satellite mission for one year. We plan to evaluate the quality of data coming out of this mission, and if satisfactory, will add them to DEA data holdings in addition to Sentinel-2C. 

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz67db8854cd6cd573Pzzzz6567c8b713b5b826/page.html)

## 20 Mar 2025: s2cloudless cloud mask data reprocessed

DEA has implemented a fix to the Sentinel-2 s2cloudless cloud mask correction. Due to this issue, Sentinel-2 observations between 25 January 2022 and 7 June 2024 using the cloud mask data were previously unusable. [The error arose](https://sentiwiki.copernicus.eu/web/s2-processing) with the addition of an offset factor introduced in ESA's Sentinel-2 L1C Processing Baseline 4.0.0 on 25 January 2022. This resulted in widespread over-classification of cloud after this date, particularly over bare regions and agricultural regions. DEA has reprocessed the affected data with new offset factors to produce correct cloud classifications.

Reprocessing of affected Sentinel-2 data has been ongoing since October 2024 and is now complete. Users can again use s2cloudless to cloud mask Sentinel-2 data, particularly for the now-corrected observations between the period of 25 January 2022 and 7 June 2024.  

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz67db8854cd6cd573Pzzzz6567c8b713b5b826/page.html)

## 13 Mar 2025: Landsat near-real-time (NRT) data outage (Resolved)

Landsat near-real-time (NRT) data is now being published on its normal cadence, as the issue in our (DEA's) data systems has been resolved. The data gap caused by the downtime from 9 March onwards has now been backfilled and the data is available. (Note that there is still a data gap from 6 March to 9 March (UTC) due to the planned USGS maintenance.)

## 12 Mar 2025: Landsat near-real-time (NRT) data outage (6 March to the present) due to planned USGS maintenance and a subsequent issue

Planned USGS maintenance caused DEA's Landsat near-real-time (NRT) data to experience downtime. This planned maintenance occurred from 6 March to 9 March (UTC); however, a subsequent issue in our (DEA's) own data systems has caused the outage to continue to the present time. We are currently working on the issue and expect it to be resolved by the end of the day.

## 5 Mar 2025: Shift in origin point of DEA Summary Product Grid

To accommodate an expanded area of coverage of Australia's external territories, the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/) has being shifted. The south-west origin point of the grid has been being shifted from `-5472000.0, -2688000.0` to `-6912000.0, -4416000.0` (EPSG:3577). Therefore, all tile grid references have shifted 18 tiles west and 15 tiles south. For instance, a tile reference of `x10y10` has changed to `x28y25`. For a preview, see the [provisional version of the expanded DEA Summary Product Grid](https://maps.dea.ga.gov.au/#share=s-avXJqwjUtf55qGUmweYY5KYoVnI) on DEA Maps. [Download the new grid from AWS S3](https://dea-public-data.s3.ap-southeast-2.amazonaws.com/derivative/ga_summary_grid_c3_expanded.geojson)

The latest versions of all of our 'summary derivative products' have now been updated to the new origin point (but existing versions of the products were not be changed). The last product to be updated was [DEA Land Cover](/data/product/dea-land-cover-landsat/) in its version 2.0.0 release on 5 March 2025.

Learn more about the [DEA Summary Product Grid](/guides/reference/collection_3_summary_grid/).

## 5 Mar 2025: Version 2.0.0 of DEA Land Cover released

We are excited to announce the release of [DEA Land Cover 2.0.0](/data/product/dea-land-cover-landsat/). This latest version introduces improvements to the DEA Land Cover product, enhancing the translation of over three decades of satellite imagery into evidence of how Australia’s land, vegetation, and waterbodies have changed over time.

* **Breaking change:** Shift in grid origin point
* **Breaking change:** Data structure changes
* Improved cloud masking to reduce noise
* Landsat 9 included
* Machine Learning Upgrade
* Pixel resolution
* Product ID Update
* 'No data' value changed
* Level 4 classification update
* Collection Upgrade

DEA Land Cover 1.0.0 will be decommissioned in June 2025.

See the [Version 2.0.0 Changelog](/data/product/dea-land-cover-landsat/?tab=history) for more information.

The product page also includes [known issues and limitations](/data/product/dea-land-cover-landsat/?tab=quality), some of which are being actively worked on.

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz67c92c7428d1a912Pzzzz6567c8b713b5b826/page.html)

## 20 Feb 2025: DEA near-real-time data not up-to-date

DEA near-real-time ARD datasets are currently not up-to-date. We are investigating the cause of this issue. 

## 20 Feb 2025: DEA Sandbox unplanned outage (Resolved)

The DEA Sandbox is currently unavailable. We are currently working to restore the service. 

## 21 Jan 2025: Sentinel-2A data switching over to Sentinel-2C

Digital Earth Australia’s Sentinel-2A data products will stop publishing data updates on 21 January 2025. They will be replaced with equivalent Sentinel-2C data products, which will begin publishing data shortly after. For further information on the precise timing of the transfer, please see [Sentinel Online](https://sentinel.esa.int/web/sentinel/-/precise-timing-of-transfer-of-duty-from-sentinel-2a-to-sentinel-2c-on-21-january). The historical Sentinel-2A data will still be provided as public data. A new ga_s2cm_ard_3 product will begin receiving data for both our NRT and definitive offerings within the coming weeks. 

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz678f06dcdfdd9113Pzzzz6567c8b713b5b826/page.html)

## 8 Jan 2025: DEA Maps data not up-to-date (Resolved)

[DEA Maps](/guides/setup/dea_maps/) and [OWS layers](/guides/setup/gis/README/) are not currently up-to-date with the data available on [DEA AWS](/guides/setup/AWS/data_and_metadata/). We are investigating the cause of this issue. 

The affected services will be updated once the issue is resolved. 

## 2 Sep 2024: Expanded extents data processing is currently paused, with data available to May 2024 <!-- NOTE Remember to remove the banner on the page: https://pr-302-preview.khpreview.dea.ga.gov.au/guides/reference/ard-expanded-processing-extent/ -->

This year, we [expanded the processing extents](/guides/reference/ard-expanded-processing-extent/) for our [Surface Reflectance products](/data/category/dea-surface-reflectance/) and derivative products.

Unfortunately, due to unanticipated issues with an external network connection, we have needed to pause the back-processing of this expanded extent data since May 2024. You may have noticed this issue, for example, if you attempted to access ARD from the Heard Island and McDonald Islands and found that there are no images more recent than May 2024.
