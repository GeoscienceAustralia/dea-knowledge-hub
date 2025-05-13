:::{admonition} Streaming is strongly recommended
:class: note

DEA Tidal Composite data is extremely large with files up to 15 GB in size. We strongly recommend streaming rather than downloading the data. Please see the instructions below: **How to stream data from AWS**
:::

(access-guides)=

:::{dropdown} How to view the data on DEA Maps

To add DEA Tidal Composites to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Tidal Composites** &gt; **DEA Tidal Composites (Sentinel-2)**.
1. Click the blue **Add to the map** button on top-right.

Now you can explore using the **Time** and **Styles** options in the left-hand workbench.
:::

:::{dropdown} How to stream data from AWS

The easiest way to access DEA Tidal Composite data is via our continental-scale Cloud Optimised GeoTIFF mosaics (COGs).
The COG file format is a type of GeoTIFF raster file (`.tif`) that allows you to quickly and efficiently 'stream' data directly from the Amazon S3 cloud without having to download files to your computer.
This allows you to rapidly access data from the entire Australian continent without having to download large files.

See the following guides for how to access the data depending on your use case.

**Streaming continental COG mosaics in QGIS**
    
1. Open the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Enter a directory of a particular year, e.g. `2018--P1Y/`
1. Right click one of the `.tif` files representing a particular band e.g. `ga_s2_tidal_composites_cyear_3_2018_low-blue.tif` &gt; click **Copy link address**.
1. Open QGIS on your computer.
1. In QGIS, click **Layer** &gt; **Add Layer** &gt; **Add Raster Layer**.
    1. For **Source Type** protocol, select **HTTP(S)** or **cloud** or otherwise.
    1. For **Type**, select **HTTP/HTTPS/FTP**.
    1. In the **URI** field, paste the link to the band that you copied to the clipboard.
1. Click **Add** to start streaming the layer. Data should appear on the map after a few seconds (or after several minutes on slow internet connections).

Learn more about streaming cloud datasets: [How to read a Cloud Optimized GeoTIFF with QGIS](https://cogeo.org/qgis-tutorial.html).

**Streaming multi-band continental COG mosaics in QGIS**

To make it easier to visualise DEA Tidal Composite bands in true and false colour, we provide several Virtual Raster files (`.vrt`) that can be loaded into QGIS.
These Virtual Rasters stream data from the cloud automatically, avoiding the need to download multiple files. They also provide instructions for combining, streaming, and viewing multiple COG files simultaneously. 

1. Open the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Enter a directory of a particular year, e.g. `2018--P1Y/`
1. Click to download the `.vrt` file of interest, e.g. `ga_s2_tidal_composites_cyear_3_2018_vrt-low-truecolour.vrt`
1. On your computer, drag the downloaded `.vrt` file into your GIS project.
1. The multi-band dataset will stream seamlessly into your QGIS project.

**Streaming continental COG mosaics in Esri ArcPro**

1. To connect Esri ArcPro to DEA's Amazon S3 bucket, follow Esri's tutorial: [Connect to a cloud store](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm). Use the following configurations for your cloud storage connection and leave the other fields blank:
    * **Connection File Name** &mdash; `DEA data`
    * **Service Provider** &mdash; `AMAZON`
    * **Bucket Name (Container)** &mdash; `dea-public-data`
    * **Folder** &mdash; `derivative`
    * **Region (Environment)** &mdash; `Asia Pacific (Sydney)`
    * **Service Endpoint** &mdash; `s3.ap-southeast-2.amazonaws.com`
    * **Provider Options**
        * `ARC_DEEP_CRAWL=NO`
        * `AWS_NO_SIGN_REQUEST=TRUE`

**Downloading data from individual tiles**

:::{note}
Downloading individual tiles is not recommended, but can be useful for accessing small amounts of data. 
:::

1. Navigate into the [ga_s2ls_intertidal_cyear_3](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory on Amazon S3
1. Left-click on the `ga_summary_grid_c3_32km_coastal.geojson` file to download to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. Alternatively, you can access this file via DEA Maps to identify required tiles (Sea, ocean and coast > DEA Intertidal > DEA Intertidal 32 km tile grid).
1. Navigate to the [DEA Tidal Composites](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/) directory and select the required tile folder, first using the tile ‘x’ reference (e.g. x079) and then the tile ‘y’ reference (e.g. y123). Then select your year of interest.
1. Left-click on the required product layer to download. See [Technical Information](./?tab=description#product-layers) for details on file naming and product layer details.

:::




If you encounter difficulty with the instructions below or the COG files themselves, please reach out to earth.observation@ga.gov.au for assistance.
