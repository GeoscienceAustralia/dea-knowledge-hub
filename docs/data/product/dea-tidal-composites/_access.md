(access-guides)=

:::{admonition} Streaming data from AWS is strongly recommended
:class: note

DEA Tidal Composite data is extremely large with files up to 15 GB in size. We strongly recommend streaming data directly from the cloud rather than downloading the data. Please see the instructions below: **How to stream data from AWS**
:::

:::{dropdown} How to view the data on DEA Maps

Take a Storymap walk-through of the dataset to see some of its features and applications.

- Open DEA Maps [Tidal Composites Storymap](https://maps.dea.ga.gov.au/story/DEATidalComposites)

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
