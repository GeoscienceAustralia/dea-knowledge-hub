# DEA Maps

[DEA Maps](https://maps.dea.ga.gov.au/) is an online platform where you can view Digital Earth Australia (DEA) data products. It aims to make it easy for anyone to access our open-source data &mdash; scientists and non-scientists alike.

:::{admonition} Start exploring
:class: note

Open [DEA Maps](https://maps.dea.ga.gov.au/)
:::

:::{contents} In this guide
:local:
:backlinks: none
:::

## Getting started with DEA Maps

1. Launch DEA Maps: <https://maps.dea.ga.gov.au/>. A pop-up window will appear:

    ![Starting with DEA Maps](/_files/dea-maps/dea_maps_1.jpg)

1. Click `Take the tour`. A series of pop-up tips will appear explaining how to use the main features of DEA Maps. Click `Next` to proceed to the next tip, then finally `Finish` to complete the tour.

    ![Guide to DEA Maps](/_files/dea-maps/dea_maps_2.jpg)

1. Once the tour is complete, experiment with scrolling and zooming in and out of the map (use your mouse wheel, double click, or click the `+` or `-` buttons on the top right). For this example, zoom in to Lake Menindee in western New South Wales.

    Note: You can also zoom to a location by typing into the `Search for locations` box on the top-left, then clicking on your location in the drop-down menu. Try this with \"Lake Menindee\".

    ![Menindee](/_files/dea-maps/dea_maps_3.jpg)

1. Click `Explore map data` on the top-left to start adding data to the map. This will bring up a view of the DEA data catalogue.

    ![Data catalogue](/_files/dea-maps/dea_maps_4.jpg)

1. We can now add data to the map. In this example, we will load 10 m resolution satellite imagery from the Copernicus Sentinel-2 satellites. First, click on `Satellite data` to open this folder, then click on the `DEA Surface Reflectance (Sentinel-2)` product. This will show you a preview of the data we are about to load. When you are ready, click `Add to the map`.

    ![Adding data](/_files/dea-maps/dea_maps_5.jpg)

1. The `DEA Surface Reflectance (Sentinel-2)` product will now be added to the \"workbench\" on the left of the screen. At this point, satellite data may not display on the map - this may be because there were no Sentinel-2 images captured over this location on the select day. To filter our satellite data to all images captured at this location, click `Filter by location`, then click on the map. You will see the filter applied in blue in the workbench on the left.

    ![Adding data](/_files/dea-maps/dea_maps_6.jpg)

1. Sentinel-2 satellite data will now appear on the map. To view imagery for a different date, select a new time by clicking on the date in the workbench, or drag the time slider along the bottom of the map window.

    ![Changing time](/_files/dea-maps/dea_maps_7.jpg)

Note: The time slider can also be used to animate satellite imagery. Click the arrow "Play" button to the left of the time slider, and control the speed of the animation using the "Play faster" and "Play slower" buttons.

## Changing styles

Data on DEA Maps often contains multiple layers for each product that can be visualised to reveal important information about the Australian landscape. To view these layers:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above). Click the white box below `Styles` to bring up a list of available styles for the dataset.

    ![Styles](/_files/dea-maps/dea_maps_styles_1.jpg)

1. From this menu, click `False colour - Green, SWIR, NIR`. This will display a false colour view of the satellite imagery that uses wavelengths of light that are invisible to the human eye (near and short-wave infrared) to highlight the presence of water (blue) and growing vegetation (bright green).

    ![False colour](/_files/dea-maps/dea_maps_styles_2.jpg)

1. Experiment with selecting other styles. The list includes several specialised remote sensing indices developed to emphasise different features in the landscape:

* Vegetation (`Normalised Difference Vegetation Index - Red, NIR`)
* Water (`Normalised Difference Water Index - Green, NIR`, `Modified Normalised Difference Water Index - Green, SWIR`)
* Algal blooms (`Normalised Difference Chlorophyll Index - Red Edge, Red`)
* Burnt areas (`Normalised Burn Ratio - NIR, SWIR`)

    ![Other styles](/_files/dea-maps/dea_maps_styles_3.jpg)

## Sharing and printing

DEA Maps allows you to easily create print-friendly views of satellite data for sharing outside the interactive website. It also allows you to create custom "share links" which preserve the exact layers you have loaded into the map. 

**Creating a share link**

1. Load one or more satellite datasets into your workbench and filter it them your location (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above). Click `Share / Print` at the top-right of the map.
1. Click `Copy` to copy a customised share link to your clipboard. When opened, this link will contain an identical view of the map containing all the layers you have loaded into the map.

    ![Share 1](/_files/dea-maps/dea_maps_share_1.jpg)

**Showing a print view**

1. After clicking `Share / Print` at the top-right of the map, click `Print` or `Show Print View` to bring up a print-friendly view of your map window.

    ![Share 2](/_files/dea-maps/dea_maps_share_2.jpg)

Hint: To obtain a high quality image of your map, right click on the image at the top of the print view and select `Save image as ...`.

## Exporting data

Note: This method is suitable for exporting small areas of DEA data at high resolution. To download large areas of data or multiple timesteps, please use the [DEA Sandbox](/guides/setup/Sandbox/sandbox/) or [NCI](/guides/setup/NCI/README/) analysis environments, or download directly from DEA\'s Amazon S3 bucket: <https://data.dea.ga.gov.au/>
   
To export data directly from DEA Maps for use in GIS software:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above). Click the three vertical dots on the dataset ("Show more actions"), then click `Export`.

    ![Export](/_files/dea-maps/dea_maps_export_1.jpg)

1. Follow the instructions in the pop-up by clicking twice on the map to draw a rectangle. When done, press `Download extent`.

    ![Export 2](/_files/dea-maps/dea_maps_export_2.jpg)

1. Satellite data for this extent will be downloaded to your PC. This data can now be loaded into GIS software like QGIS or ArcGIS.

## Compare tool

It can be useful to compare different satellite datasets, or imagery from different dates to investigate change over time. To do this, we can use the "Compare" tool:

1. Load a satellite dataset into your workbench and filter it to your location (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above). Click the three vertical dots on the dataset ("Show more actions"), then click `Compare`.

    ![Compare](/_files/dea-maps/dea_maps_compare_1.jpg)

1. A screen splitter will appear at the centre of the map, and a new copy of our dataset will be added to the workbench. The workbench has also updated with orange labels to show that this new copy will be shown on the `Left` of the screen, and our original data shown on the `Right`. 

    ![Screen splitter](/_files/dea-maps/dea_maps_compare_2.jpg)

1. Filter this new copy of our dataset to the same location (e.g. `Filter by location` then click on the map), then select a new date from the "Time" dropdown. The left-hand side of the map will update with Sentinel-2 imagery from this date. Using your mouse, you can now grab the screen splitter in the centre of the screen, and swipe from side to side to compare imagery from these two time periods side-by-side.

    ![Screen splitter 2](/_files/dea-maps/dea_maps_compare_3.jpg)

1. To deactive the "Compare" tool, click the orange "Compare" icon on the top right of the map.

    ![Deactiveate screen splitter](/_files/dea-maps/dea_maps_compare_4.jpg)

## Difference tool

The "Compare" tool above allowed us to visually compare different satellite data. However, it can also be useful to quantitatively compare differences between different satellite images to reveal parts of the landscape that have changed significantly over time. To do this, we can use the more advanced "Difference" tool:

1. Load a satellite dataset into your workbench (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above). Click the three vertical dots on the dataset ("Show more actions"), then click `Difference`.

    ![Difference](/_files/dea-maps/dea_maps_diff_1.jpg)

1. The "Difference" tool will replace the workbench on the left of the map. This tool allows us to choose satellite images from two different dates, and analyse them to calculate changes across time. As a first step, tell the tool the location we want to analyse by clicking once in the middle of the map.

    ![Difference 2](/_files/dea-maps/dea_maps_diff_2.jpg)

1. Once the data is filtered, click on the date below `Date Comparison A` and `Date Comparison B`, and use the date picker (i.e. click on the dates) to change the dates that are displayed on the left and right of the map. Try and choose two dates without clouds, as these will be used to identify parts of the landscape that have changed through time.

   Note: If using the Lake Menindee example, try setting `Date Comparison A` to `18/04/2021` and `Date Comparison B` to `18/05/2021` for a example of a dry and wet landscape.

    ![Difference 3](/_files/dea-maps/dea_maps_diff_3.jpg)

1. We can now run the change detection computation. Click `Choose a difference output` on the "Difference" tool. This gives us several options that can be used to compare differences in specific landscape characteristics over time (e.g. water, vegetation, fire scars). For this example, select `Modified Normalised Difference Water Index - Green, SWIR` which is useful for comparing the distribution of water in the landscape. When ready, click `Generate change detection`.

    ![Difference 4](/_files/dea-maps/dea_maps_diff_4.jpg)

1. A new layer will appear on the map. Locations that have grown wetter over time are shown in blue, while locations that have have become drier are shown in red. Scroll around the map to explore patterns of change. To close the "Difference" tool, click "Exit" at the top of the window. 

    ![Difference 5](/_files/dea-maps/dea_maps_diff_5.jpg)

1. Your workbench will reappear, with the difference output layer added as a new dataset on the map.

    ![Difference 6](/_files/dea-maps/dea_maps_diff_6.jpg)

## Watercourse Discharge tool 

The Bureau of Meteorology provides current and historic water discharge data for 3,500 hydrological measurement stations across Australia. The Digital Earth Australia “Watercourse Discharge" tool can be used to match satellite imagery to watercourse discharge information over time at each measuring station. The tool enables the user to plot watercourse discharge and then easily search the related satellite images for the date of measurement.

1. Load a satellite dataset into your workbench (e.g. follow the `DEA Surface Reflectance (Sentinel-2)` example above).
1. Load watercourse discharge data (e.g. the Hydrologic Reference Stations dataset) to your workbench by clicking on `Explore map data`. Scroll down and click `Other` > `Water Regulations Data (BoM)` > `Hydrological Reference Stations` > `Water Discharge`. Then click `Add to the map`.  

    ![Watercourse Discharge Tool 1](/_files/dea-maps/dea_maps_wdt_1.jpg)
   
1. The Hydrological Reference Stations watercourse measuring locations located across the country are shown below. Zoom into the map and click on a station of interest. A pop up with the stations name, location and other details will appear. Click `Show DEA Surface Reflectance (Sentinel-2) at this location`. Then click `Expand` and then close the pop up.

    ![Watercourse Discharge Tool 2](/_files/dea-maps/dea_maps_wdt_2.jpg)

    ![Watercourse Discharge Tool 3](/dea-maps/dea_maps_wdt_3.jpg)
   
1. A hydrograph of your chosen station will now be at the bottom of the screen. To link the Sentinel-2 data to the hydrograph, click on the `Show available times` chart symbol in the DEA Surface Reflectance (Sentinel-2) card on your workbench.

    ![Watercourse Discharge Tool 4](/_files/dea-maps/dea_maps_wdt_4.jpg)
   
1. Sentinel-2 captures will now appear as dots on the hydrograph. Clicking on a dot will load imagery from that date onto the map. Hovering over a dot will show the date and time of capture and the average watercourse discharge rate. Note: Sentinel-2 data is only available for 2015 onwards. To clearly see the dots on the hydrograph, you may need to zoom in using your mouse wheel. 

    ![Watercourse Discharge Tool 5](/_files/dea-maps/dea_maps_wdt_5.jpg)
   
1. You can change the style of the Sentinel-2 data by clicking on the `Styles` dropdown menu in the DEA Surface Reflectance (Sentinel-2) card on your workbench. The example below shows Modified Normalised Difference Water Index – Green, SWIR.

    ![Watercourse Discharge Tool 6](/_files/dea-maps/dea_maps_wdt_6.jpg)

## For more assistance

DEA Maps contains additional helpful guides for assisting with exploring our datasets. To access this help at any point, click the `Help` button on the bottom-right:

![Help 1](/_files/dea-maps/dea_maps_help_1.jpg)

This will bring up a menu containing detailed guides to performing useful tasks with DEA Maps:

![Help 2](/_files/dea-maps/dea_maps_help_2.jpg)

