:::{dropdown} How to view the data on DEA Maps

To add DEA Tidal Composites to DEA Maps manually:

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Select **Explore map data** on the top-left.
1. Select **Sea, ocean and coast** &gt; **DEA Tidal Composites** &gt; **DEA Tidal Composites (Sentinel-2)**.
1. Click the blue **Add to the map** button on top-right.

Now you can explore using the **Time** and **Styles** options in the left-hand workbench.
:::

:::{dropdown} How to access the data on AWS

To stream continental data mosaics of the individual annual bands:

1) Navigate into the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) AWS S3 bucket
2) Select the year of interest e.g. `2018--P1Y/`
3) Right click the `.tif` file (band) of interest e.g. `ga_s2_tidal_composites_cyear_3_2018_low-blue.tif`
4) Select `Copy link address`
5) Open your GIS program
6) Select `Add Raster layer` (or equivalent)
7) Select `Source Type` protocol as `HTTP(S)` or `cloud` etc
8) Paste the link into the dialogue box
9) Select `ok` to stream the layer 
10) For more on streaming cloud datasets, see:
    * [QGIS: tutorial](https://cogeo.org/qgis-tutorial.html)
    * :::{dropdown} [ESRI: tutorial](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm) 
    
    Create a cloud storage connection using the following settings, leaving all others blank:

        |  Parameter  |  Setting  |
        |  ---------  |  -------  |
        |  Connection File Name |  DEA data  |
        |  Service Provider  |  AMAZON  |
        |  Bucket (Container) Name  |  dea-public-data  |
        |  Folder  |  derivative  |
        |  Region (Environment)  |  Asia Pacific (Sydney)  |
        |  Service Endpoint  |  s3.ap-southeast-2.amazonaws.com  |
        |  Provider Options -->  Name  |  ARC_DEEP_CRAWL  |
        |  Provider Options --> Value  |  NO  |
        |  ---------  |  -------  |
        :::


To *stream* annual continental multi-band imagery mosaics:

1) Navigate into the DEA Tidal Composites [continental_mosaics](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/continental_mosaics/) AWS S3 bucket
2) Select the year of interest e.g. `2018--P1Y/`
3) Left click to download the `.vrt` file of interest e.g. `ga_s2_tidal_composites_cyear_3_2018_vrt-low-truecolour.vrt`
4) From your `downloads` folder, drag the `.vrt` file into your GIS project
5) The multi-band dataset will stream in your project as the `.vrt` file contains the instructions for combining, streaming and viewing multiple COG files simultaneously.

To *download* data, either:

1) [Not recommended]: Follow steps `1-2` above and left-click any `.tif` to download. **Beware** the continental mosaic files are huge in volume.

    or

2) Navigate to this [AWS S3 bucket](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2ls_intertidal_cyear_3/).

3) Left-click on the `ga_summary_grid_c3_32km_coastal.geojson` file to download to your computer. This file can be used in a GIS package to identify the product tiles that you require for a given location. Alternatively, you can access this file via DEA Maps to identify required tiles (Sea, ocean and coast > DEA Intertidal > DEA Intertidal 32 km tile grid).

4) Navigate to the [DEA Tidal Composites](https://data.dea.ga.gov.au/?prefix=derivative/ga_s2_tidal_composites_cyear_3/1-0-0/) bucket and select the required tile folder, first using the tile ‘x’ reference (e.g. x079) and then the tile ‘y’ reference (e.g. y123). Then select your year of interest.

5) Click on the required product layer to download. See [Technical Information](./?tab=description#product-layers) for details on file naming and product layer details.
:::
