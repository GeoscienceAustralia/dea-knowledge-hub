# DEA Maps

[DEA Maps](https://maps.dea.ga.gov.au/) is an online platform where you can view Digital Earth Australia (DEA) data products. It aims to make it easy for anyone to access our open-source data &mdash; whether you are a scientist, educator, journalist, or otherwise.

**Quick links**

* **Start exploring:** [Open DEA Maps](https://maps.dea.ga.gov.au/)
* **If you don't see any data or data doesn't cover a location:** [Filter by location](#filter-by-location)

:::{contents} In this guide
:local:
:backlinks: none
:::

## Add data to the map

Let's add a data product to the map so that we can view the data.

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Click **Explore map data** &gt; in the data catalogue, navigate through the folders to find the data product that you want to access. (E.g. click 'Baseline satellite data' &gt; 'DEA Surface Reflectance (Sentinel-2)' &gt; 'DEA Surface Reflectance (Sentinel-2A MSI)'.)
1. Click the product's "**+**" icon to add it to the map (or click it's title then click **Add to the map**).
1. The data product will be added to the left panel and you may now see data overlaid on the map. But **if you don't see any data or data doesn't cover a location** or , continue to the next section: **Filter by location**.

    ![Data catalogue](/_files/dea-maps/dea_maps_4.jpg)

    ![Adding data](/_files/dea-maps/dea_maps_5.jpg)

<span id="filter-by-location"></span>

## Filter by location

After adding data to the map, if you don't see any data or the data doesn't cover a particular location, you can use the 'Filter by location' tool. This is especially useful for products that are provided as swaths (strips of data that the satellite captures as it travels), e.g. the Baseline satellite data products. Zoom out on the map and you will often see that swaths of data are visible, but they are not covering the location you are interested in. Or you may find that no data exists at all for this particular time.

'Filter by location' will show the most recent data that is available for a given location.

1. In the left sidebar, click **Filter by location** for the product you have added the map.
1. Click a location on the map then wait for it to load.
1. Data should now be overlaid on that location. The left sidebar will indicate that the filter has been applied.
1. Next, you can either select **Remove filter** or **New location**.

    ![Adding data](/_files/dea-maps/dea_maps_6.jpg)

## Share a URL and save your map

Once you've created a map by adding layers, adjusting settings, and zooming in on a specific location, you will want to share this map with others, or save it so you can continue work on it later. You can do both of these using the **Share URL** feature.

1. Click **Share / Print** on the top right.
1. Click **Copy** to copy this custom URL to your clipboard.
1. Anyone who opens this URL will see your map, exactly as you configured it. You can send this URL to others, link to it from a public website, or bookmark it for later.

## Switch bands and layers

Most data products contain multiple 'bands' or 'layers' of data that reveal different features of the landscape. You can switch between these using the **Styles** dropdown in the left sidebar.

For example, the 'DEA Surface Reflectance (Sentinel-2)' product can be switched to the 'False colour - Green, SWIR, NIR' style. This style uses wavelengths of light beyond the visible spectrum ('near infrared' and 'short-wave infrared') to highlight waterbodies, vegetation, and other features more distinctly.

![False colour](/_files/dea-maps/dea_maps_styles_2.jpg)

## Navigate time and location

You can navigate through data products across both location and time.

* Change to a different time by clicking the **Time** value in the left sidebar, or clicking on the timeline at the bottom.
* Zoom in and out of the map by scrolling the mouse, or use the "**+**" and "**-**" buttons.
* Move to a different location by dragging with the mouse, or type in the **Search for locations** bar. E.g. search for 'Lake Eyre', then click the option: 'Lake Eyre, SA'.

![Changing time](/_files/dea-maps/dea_maps_7.jpg)

## Additional features

* **Animate satellite imagery** &mdash; The time slider can also be used to animate satellite imagery. Click the arrow "Play" button to the left of the time slider, and control the speed of the animation using the "Play faster" and "Play slower" buttons.

***

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

