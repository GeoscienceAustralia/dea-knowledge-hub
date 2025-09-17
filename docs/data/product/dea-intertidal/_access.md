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

VRT (Virtual Raster) files are also provided alongside the .tif mosaics. These files serve as lightweight wrappers around the main data and can be used to open data in GIS software with visual settings already applied.

For detailed instructions, please visit the [Continental Cloud-Optimised GeoTIFF Mosaics page](/guides/continental-cogs-geotiff-mosaics/)

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

```{warning}
Downloading individual tiles is **not recommended**, but can be useful for accessing small amounts of data.
```

1. Open the [DEA Intertidal](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/) directory in DEA's Amazon S3 bucket.
1. Click on `ga_summary_grid_c3_32km_coastal.geojson` to download the file to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. (Alternatively, you can access this file via DEA Maps to identify the required tiles: **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal 32 km tile grid**.)
1. Open the [DEA Intertidal](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/2-0-0/) directory in DEA's Amazon S3 bucket and navigate into the folder of the tile that you require. The folder names are based on the 'x' and 'y' coordinate references. E.g. first enter the `x082` folder, then the `y122`.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Click to download the product layer of interest, e.g. `ga_s2ls_intertidal_cyear_3_x082y122_2021--P1Y_final_extents.tif`. Learn more about file naming and product layers: [Technical Information](./?tab=description#product-layers).
:::

