(access-guides)=

:::{admonition} Streaming data from AWS is strongly recommended
:class: note

DEA Intertidal data is extremely large with files up to 6 GB in size. We strongly recommend streaming data directly from the cloud rather than downloading the data. Please see the instructions below: **How to stream data from AWS**
:::

:::{dropdown} How to explore DEA Maps

Start exploring [DEA Intertidal on DEA Maps](https://maps.dea.ga.gov.au/story/DEAIntertidal).

To add DEA Intertidal to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal (Sentinel-2, Landsat)**
1. Click the **Add to the map** button on top-right.

View the product layer required by selecting the layer from the **Styles** dropdown menu, and use the **Time** selector to view the annual time-series of each product layer.

Note that the colour ramp for the **Elevation** and **Elevation Uncertainty** product layers is scaled dynamically from 'low' to 'high' to account for the wide variation of tidal ranges and elevations found across Australia, and provide the best contrast on the DEA Maps platform. 

To query an absolute value for any of the product layers, click on a location to see a plain text summary of all the DEA Intertidal product suite data values at that pixel location.
:::

:::{dropdown} How to stream data from AWS (Recommended)

The easiest way to access DEA Intertidal data is via our continental-scale cloud-optimised GeoTIFF mosaics (COGs).
The COG file format is a type of GeoTIFF raster file (`.tif`) that allows you to quickly and efficiently 'stream' data directly from the Amazon S3 cloud without having to download files to your computer.
This allows you to rapidly access data from the entire Australian continent without having to download large files.

See the following guides for how to access the data depending on your use case.

**Stream continental COG mosaics in QGIS**
    
1. Open the DEA Intertidal [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/2-0-0/continental_mosaics/) directory in DEA's Amazon S3 bucket.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Right click one of the `.tif` files representing a particular band e.g. `ga_s2ls_intertidal_cyear_3_2018_elevation.tif` &gt; click **Copy link address**.
1. Open QGIS on your computer.
1. In QGIS, click **Layer** &gt; **Add Layer** &gt; **Add Raster Layer**.
    1. For **Source Type**, select **Protocol: HTTP(S), cloud, etc.**.
    1. For **Protocol Type**, select **HTTP/HTTPS/FTP**.
    1. In the **URI** field, paste the link to the band that you copied to the clipboard.
1. Click **Add** to start streaming the layer. Data should appear on the map after a few seconds (or after several minutes on slow internet connections).

Learn more about streaming cloud datasets: [How to read a Cloud Optimized GeoTIFF with QGIS](https://cogeo.org/qgis-tutorial.html).

```{figure} /_files/dea-tidal-composites/streaming-cogs.*
:alt: Streaming COGs in QGIS
```

**Stream continental COG mosaics in Esri ArcGIS Pro**

To connect Esri ArcGIS Pro to DEA's Amazon S3 bucket, follow Esri's tutorial: [Connect to a cloud store](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm). 

1. Use the following configurations for your **cloud storage connection**:

```{figure} /_files/dea-tidal-composites/arcpro_cog_settings.*
:alt: Streaming COGs in ArcPro
```

1. In the **Catalog** pane:
    1. Expand **Cloud Stores**.
    1. Expand the **DEA derivative data** cloud store.
    1. Navigate to `ga_s2ls_intertidal_cyear_3/2-0-0/continental_mosaics/`.
    1. Enter a directory of a particular year, e.g. `2018--P1Y`.
    1. Drag and drop the `.tif` COG file representing a particular band e.g. `ga_s2ls_intertidal_cyear_3_2018_elevation.tif` onto the map.

1. **Important:** When adding COG files to ArcGIS Pro, select `No` when asked whether to build statistics for the layer.

If you encounter difficulty with any of these instructions, or with the COG files themselves, please contact us at [earth.observation@ga.gov.au](mailto:earth.observation@ga.gov.au)
:::

:::{dropdown} How to download data from ELVIS

To download the data from the ELVIS (Elevation Information System) platform, follow these steps.

1. Open the [ELVIS platform](https://elevation.fsdf.org.au/).
1. Zoom in to your coastal area of interest on the ELVIS map.
1. Click **Order data** on the top-right of the page.
1. Select your desired selection method, then click **Draw**.
1. Select your area of interest on the map, then click **Search**.
1. In the **Search Results** menu (on the right side), locate the **10 Metre Intertidal DEM** results and select the years of data you wish to order.
1. Enter your industry and email address, then click **Order dataset**.
1. Your data will be emailed to you as a zipped folder containing DEA Intertidal Elevation and Elevation Uncertainty GeoTIFF rasters.

![Accessing DEA Intertidal on ELVIS](/_files/dea-intertidal/DEAIntertidal_ELVIS_access.jpg)
:::

:::{dropdown} How to download data from individual tiles (Not recommended)

Downloading individual tiles is **not recommended**, but can be useful for accessing small amounts of data. 

1. Open the [DEA Intertidal](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/) directory in DEA's Amazon S3 bucket.
1. Click on `ga_summary_grid_c3_32km_coastal.geojson` to download the file to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. (Alternatively, you can access this file via DEA Maps to identify the required tiles: **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal 32 km tile grid**.)
1. Open the [DEA Intertidal](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/2-0-0/) directory in DEA's Amazon S3 bucket and navigate into the folder of the tile that you require. The folder names are based on the 'x' and 'y' coordinate references. E.g. first enter the `x082` folder, then the `y122`.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Click to download the product layer of interest, e.g. `ga_s2ls_intertidal_cyear_3_x082y122_2021--P1Y_final_extents.tif`. Learn more about file naming and product layers: [Technical Information](./?tab=description#product-layers).
:::

