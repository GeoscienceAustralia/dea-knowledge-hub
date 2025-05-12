:::{dropdown} How to view the data on DEA Maps

To add DEA Tidal Composites to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Tidal Composites** &gt; **DEA Tidal Composites (Sentinel-2)**.
1. Click the blue **Add to the map** button on top-right.

Now you can explore using the **Time** and **Styles** options in the left-hand workbench.
:::

:::{dropdown} How to access the data on AWS

The easiest way to access DEA Tidal Composite data is via our provided continental-scale Cloud Optimised GeoTIFF mosaics (COGs).
The COG file format is a type of GeoTIFF (i.e. `.tif`) raster file that allows you to quickly and efficiently "stream" data directly from the cloud (e.g. Amazon S3), without having to download them to your computer.
This allows you to rapidly access data from the entire Australian continent, without having to wait for data to download.

:::{important}

DEA Tidal Composite data is extremely large (e.g. up to 15 gb per file). We **strongly recommend streaming data** rather than downloading individual raster files. If you encounter difficulty with the instructions below or the COG files themselves, please reach out to earth.observation@ga.gov.au for assistance.
:::

:::{dropdown}   * **Streaming continental COG mosaics in QGIS**
    
1. Navigate into the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory on Amazon S3
1. Select your year of interest e.g. `2018--P1Y/`
1. Right click the `.tif` file (band) of interest e.g. `ga_s2_tidal_composites_cyear_3_2018_low-blue.tif`
1. Select `Copy link address`
1. Open QGIS
1. Select `Layer` > `Add Layer` > `Add Raster Layer`
1. Select `Source Type` protocol as `HTTP(S)` or `cloud` etc, and ensure `Type` is set to `HTTP/HTTPS/FTP`
1. Paste the link into the `URI` dialogue box
1. Select `Add` to stream the layer. Data should appear on the map after a few seconds delay (or several minutes on slow internet connections)

:::{tip}

For more on streaming cloud datasets, see: [QGIS Tutorial: How to read a Cloud Optimized GeoTIFF with QGIS](https://cogeo.org/qgis-tutorial.html)
:::
:::

:::{dropdown}   * **Streaming multi-band continental COG mosaics in QGIS**

:::{note}

To make it easier to visualise DEA Tidal Composite bands in true and false colour, we provide several Virtual Raster (`.vrt`) files that can be loaded into QGIS.
These Virtual Rasters stream data from the cloud by default, avoiding you to have to download multiple files.
:::

1) Navigate into the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory on Amazon S3
2) Select the year of interest e.g. `2018--P1Y/`
3) Left click to download the `.vrt` file of interest e.g. `ga_s2_tidal_composites_cyear_3_2018_vrt-low-truecolour.vrt`
4) From your `Downloads` folder, drag the `.vrt` file into your GIS project
5) The multi-band dataset will stream seamlessly into your QGIS project via the `.vrt` file which contains instructions for combining, streaming and viewing multiple COG files simultaneously. 
:::

:::{dropdown}   * **Streaming continental COG mosaics in Esri ArcPro**

1) Follow the Esri [connect to a cloud store tutorial](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm) to connect Esri ArcPro to DEA's Amazon S3 bucket

2) Create a cloud storage connection using the following settings, leaving all others blank:

    |  Parameter  |  Setting  |
    |  ---------  |  -------  |
    |  Connection File Name |  DEA data  |
    |  Service Provider  |  AMAZON  |
    |  Bucket (Container) Name  |  dea-public-data  |
    |  Folder  |  derivative  |
    |  Region (Environment)  |  Asia Pacific (Sydney)  |
    |  Service Endpoint  |  s3.ap-southeast-2.amazonaws.com  |
    |  Provider Options  |  ARC_DEEP_CRAWL=NO  |
    |  Provider Options  |  AWS_NO_SIGN_REQUEST=TRUE  |

:::

:::{dropdown}   * **Downloading data from individual tiles**

:::{note}

Downloading individual tiles is not recommended, but can be useful for accessing small amounts of data. :::

1) Navigate into the [ga_s2ls_intertidal_cyear_3](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) directory on Amazon S3

2) Left-click on the `ga_summary_grid_c3_32km_coastal.geojson` file to download to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. Alternatively, you can access this file via DEA Maps to identify required tiles (Sea, ocean and coast > DEA Intertidal > DEA Intertidal 32 km tile grid).

3) Navigate to the [DEA Tidal Composites](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/) directory and select the required tile folder, first using the tile ‘x’ reference (e.g. x079) and then the tile ‘y’ reference (e.g. y123). Then select your year of interest.

4) Left-click on the required product layer to download. See [Technical Information](./?tab=description#product-layers) for details on file naming and product layer details.

:::
:::
 