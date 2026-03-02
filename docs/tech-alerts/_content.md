% See the DEA Tech Alerts documentation:
% https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/tech_alerts_changelog.html

## 2 Mar 2026: New Sentinel-2A ARD made available after mission continuation

DEA has reenabled Sentinel-2A data following the European Space Agency (ESA) announcing in early 2025 the satellite mission will continue in a modified orbit adjacent to Sentinel-2B.

This tandem acquisition is expected to allow the two satellites to capture scenes in nearly identical conditions, further enhancing radiometric performance and consistency. You can read more at the [Copernicus Data Space Ecosystem website](https://dataspace.copernicus.eu/news/2025-12-19-sentinel-2a-and-sentinel-2b-tandem-acquisitions) and [here](https://sentiwiki.copernicus.eu/web/s2-mission).

The current estimate of the S2A datasets to be added to the collection as of 09/02/2026 is around 28,000. For comparison, the numbers of Sentinel-2B and Sentinel-2C datasets for the same period are 66,011 and 63,449 respectively. 

Even though Sentinel-2A is now on the modified orbit closely following Sentinel-2B, the orbital parameters of the satellite remain largely unchanged. See the S2A and S2B swaths on [**DEA Maps**](https://communication.ga.gov.au/link/id/zzzz699fea2597249988Pzzzz61de67bd94bfe861/page.html).

DEA users with existing workflows consuming Sentinel-2B and Sentinel-2C data should not see any impact, and no further action should be required. However, users running automatic workflows that are not filtering out Sentinel-2A data may see an uptick in data volume as we process and publish our Sentinel-2A data backlog. 

If you do not want to process these S2A data in your workflows, please make sure to exclude them.

Sentinel-2A has been collecting data for nearly 12 months. This data will now be added to our ARD collection. 

The additional S2A datasets are now available. 

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz699fea3b3ab52484Pzzzz61de67bd94bfe861/page.html)

## 2 Mar 2026: Redundant Sentinel-2 Near Real Time data removed

Digital Earth Australia (DEA) has removed more than 87,000 redundant Near-Real Time (NRT) data tiles from our Surface Reflectance data to ensure consistency within the definitive DEA tile set.

NRT is the [rapid dataset maturity level](/guides/reference/dataset_maturity_guide/) produced within 48 hours of image capture, but it is considered of lower quality than our final Anaysis Ready Data (ARD) products. These NRT data are later converted to the definitive or ‘final’ maturity level when high quality ancillary data is available.

To better manage our data and improve system processing we have begun cleaning up these redundant packets that have been superseded by the final definitive data.

During this process we have identified NRT that are not available in the final datasets, as well as tiles in the definitive datasets that are not available in NRT.

To address this we have removed redundant Sentinel-2 tiles in the NRT processing only, leaving the definitive tile set in place. 

We have also updated the processing tile sets for Landsat and Sentinel-2 and synchronised the [NCI](https://explorer.nci.dea.ga.gov.au/products) and [AWS](https://explorer.dea.ga.gov.au/products) processing so both services now work off the same core tile set.

For the Landsat tile set there will be additional tiles processed to AWS while for Sentinel-2 some tiles will be removed as well as some tiles added. This will result in a net reduction in the number of tiles processed to AWS, and a minor net-gain for NCI. The majority of the NRT tiles are over the ocean and deemed unlikely to include relevant EO data.  

By removing the old NRT data and synchronising NCI and AWS tile processing we will provide better overall data management and consistency across these DEA services.  

This process has been completed and we will continue to monitor the changes into the near future.  

![](/_files/tech-alerts/2026-03-02-nrt-data-removed.jpeg)

<figure>
    <figcaption>The DEA Landsat and Sentinel tile grids showing redundant tiles that have been removed circled in red.</figcaption>
</figure>

[View the Tech Alert](https://communication.ga.gov.au/link/id/zzzz699fea3b3ab52484Pzzzz61de67bd94bfe861/page.html)

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

