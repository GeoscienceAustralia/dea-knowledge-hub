(access-guides)=

:::{admonition} Streaming data from AWS is strongly recommended
:class: note

DEA Tidal Composite data is extremely large with files up to 15 GB in size. We strongly recommend streaming data directly from the cloud rather than downloading the data. Please see the instructions below: **How to stream data from AWS**
:::

:::{dropdown} How to view the data on DEA Maps

To add DEA Tidal Composites to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Tidal Composites** &gt; **DEA Tidal Composites (Sentinel-2)**.
1. Click the blue **Add to the map** button on top-right.

Now you can explore using the **Time** and **Styles** options in the left-hand workbench.
:::

:::{dropdown} How to stream data from AWS (Recommended)

The easiest way to access DEA Tidal Composite data is via our continental-scale cloud-optimised GeoTIFF mosaics (COGs).
The COG file format is a type of GeoTIFF raster file (`.tif`) that allows you to quickly and efficiently 'stream' data directly from the Amazon S3 cloud without having to download files to your computer.
This allows you to rapidly access data from the entire Australian continent without having to download large files.

VRT (Virtual Raster) files are also provided alongside the .tif mosaics. These files serve as lightweight wrappers around the main data and can be used to open data in GIS software with visual settings already applied.

For detailed instructions, please visit the [Continental Cloud-Optimised GeoTIFF Mosaics page](/guides/continental-cogs-geotiff-mosaics/)

:::

:::{dropdown} How to download data from individual tiles (Not recommended)

```{warning}
Downloading individual tiles is **not recommended**, but can be useful for accessing small amounts of data.
```

1. Open the [DEA Intertidal](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/) directory in DEA's Amazon S3 bucket.
1. Click on `ga_summary_grid_c3_32km_coastal.geojson` to download the file to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. (Alternatively, you can access this file via DEA Maps to identify the required tiles: **Sea, ocean and coast** &gt; **DEA Intertidal** &gt; **DEA Intertidal 32 km tile grid**.)
1. Open the [DEA Tidal Composites](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/) directory in DEA's Amazon S3 bucket and navigate into the folder of the tile that you require. The folder names are based on the 'x' and 'y' coordinate references. E.g. first enter the `x079` folder, then the `y123`.
1. Enter a directory of a particular year, e.g. `2018--P1Y`
1. Click to download the product layer of interest, e.g. `ga_s2_tidal_composites_cyear_3_x079y123_2018--P1Y_final_low-red.tif`. Learn more about file naming and product layers: [Technical Information](./?tab=description#product-layers).
:::
