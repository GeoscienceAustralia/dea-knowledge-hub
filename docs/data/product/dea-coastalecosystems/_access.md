% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/services/dea-knowledge-hub/operating-procedures/product-metadata-fields/#kh-product-metadata-fields

:::{admonition} Streaming data from AWS is strongly recommended
:class: note

DEA Coastal Ecosytems data is large with files up to 2-3 GB in size. We strongly recommend streaming data directly from the cloud rather than downloading the data. Please see the instructions below: **How to stream data from AWS**
:::

:::{dropdown} How to explore DEA Maps (To be completed with StoryMap)

Start exploring [DEA Coastal Ecosystems on DEA Maps](https://maps.dea.ga.gov.au/story/DEACoastalEcosystems).

To add DEA Coastal Ecosystems to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Coastal Ecosystems** &gt; **DEA Coastal Ecosystems (Sentinel-2)**
1. Click the **Add to the map** button on top-right.

View the product layer required by selecting the layer from the **Styles** dropdown menu, and use the **Time** selector to view the annual time-series of each product layer.

% TODO To query an absolute value for any of the product layers, click on a location to see a plain text summary of all the DEA Intertidal product suite data values at that pixel location.
:::

:::{dropdown} How to stream data from AWS (Recommended)

The easiest way to access DEA Coastal Ecosystems data is via our continental-scale cloud-optimised GeoTIFF mosaics (COGs).
The COG file format is a type of GeoTIFF raster file (`.tif`) that allows you to quickly and efficiently 'stream' data directly from the Amazon S3 cloud without having to download files to your computer.
This allows you to rapidly access data from the entire Australian continent without having to download large files.

VRT (Virtual Raster) files are also provided alongside the .tif mosaics. These files serve as lightweight wrappers around the main data and can be used to open data in GIS software with visual settings already applied.

For detailed instructions, please visit the [Continental Cloud-Optimised GeoTIFF Mosaics page](/guides/continental-cogs-geotiff-mosaics/)

:::


:::{dropdown} How to download Continental Mosaic data 



1. Open the [DEA Coastal Ecosystems](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_coastalecosystems_cyear_3_v1/AU/) directory in DEA's Amazon S3 bucket: 
1. Enter a directory of a particular year, e.g. `2021--P1Y`
1. Click to download the product layer of interest, e.g. `ga_s2_coastalecosystems_cyear_3_v1-0-0_AU_2021—P1Y_final_classification.tif`. Learn more about file naming and product layers: [Technical Information](./?tab=description#core-product-layers).
:::

