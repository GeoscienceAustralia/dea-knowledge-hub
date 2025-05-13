:::{admonition} Streaming data from AWS is strongly recommended
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

**Stream continental COG mosaics in QGIS**
    
1. Open the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Right click one of the `.tif` files representing a particular band e.g. `ga_s2_tidal_composites_cyear_3_2018_low-blue.tif` &gt; click **Copy link address**.
1. Open QGIS on your computer.
1. In QGIS, click **Layer** &gt; **Add Layer** &gt; **Add Raster Layer**.
    1. For **Source Type** protocol, select **HTTP(S)** or **cloud** or otherwise.
    1. For **Type**, select **HTTP/HTTPS/FTP**.
    1. In the **URI** field, paste the link to the band that you copied to the clipboard.
1. Click **Add** to start streaming the layer. Data should appear on the map after a few seconds (or after several minutes on slow internet connections).

Learn more about streaming cloud datasets: [How to read a Cloud Optimized GeoTIFF with QGIS](https://cogeo.org/qgis-tutorial.html).

**Stream multi-band continental COG mosaics in QGIS**

To make it easier to visualise DEA Tidal Composite bands in true and false colour, we provide several Virtual Raster files (`.vrt`) that can be loaded into QGIS.
These Virtual Rasters stream data from the cloud automatically, avoiding the need to download multiple files. They also provide instructions for combining, streaming, and viewing multiple COG files simultaneously. 

1. Open the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Click to download the `.vrt` file of interest, e.g. `ga_s2_tidal_composites_cyear_3_2018_vrt-low-truecolour.vrt`
1. On your computer, drag the downloaded `.vrt` file into your GIS project.
1. The multi-band dataset will stream seamlessly into your QGIS project.

**Stream continental COG mosaics in Esri ArcPro**

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

**Download data from individual tiles (Not recommended)**

Note: Downloading individual tiles is not recommended, but can be useful for accessing small amounts of data. 

1. Open the DEA Tidal Composites [ga_s2ls_intertidal_cyear_3](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Click on `ga_summary_grid_c3_32km_coastal.geojson` to download the file to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. (Alternatively, you can access this file via DEA Maps to identify the required tiles: **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal 32 km tile grid**.)
1. Open the [DEA Tidal Composites](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/) directory in DEA's Amazon S3 bucket and navigate into the folder of the tile that you require. The folder names are based on the 'x' and 'y' coordinate references. E.g. first enter the `x079` folder, then the `y123`.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Click to download the product layer of interest, e.g. `ga_s2_tidal_composites_cyear_3_x079y123_2018--P1Y_final_low-red.tif`. Learn more about file naming and product layers: [Technical Information](./?tab=description#product-layers).

If you encounter difficulty with any of these instructions, or with the COG files themselves, please contact us at earth.observation@ga.gov.au
:::

