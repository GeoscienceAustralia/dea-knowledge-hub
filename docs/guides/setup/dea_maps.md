# DEA Maps

[DEA Maps](https://maps.dea.ga.gov.au/) is an online platform where you can view Digital Earth Australia (DEA) datasets. It aims to make it easy for anyone to access our open-source data &mdash; whether you are a scientist, educator, journalist, or otherwise.

:::{admonition} Quick links
:class: note

* [Open DEA Maps](https://maps.dea.ga.gov.au/) to get started.
* [Filter by location](#filter-by-location) if you don't see any data or data doesn't cover a location.
:::

:::{contents} In this guide
:local:
:backlinks: none
:::

## Add data to the map

Let's add a dataset to the map so that we can view the data. Here's an example map of [DEA Surface Reflectance (Sentinel-2A MSI)](https://maps.dea.ga.gov.au/#share=s-bNYeackQuE5oILJe4O13j1HZjBQ)

1. Open [DEA Maps](https://maps.dea.ga.gov.au/).
1. Click **Explore map data** &gt; in the data catalogue, navigate through the folders to find the dataset that you want to access. (E.g. click 'Baseline satellite data' &gt; 'DEA Surface Reflectance (Sentinel-2)' &gt; 'DEA Surface Reflectance (Sentinel-2A MSI)'.)
1. Click the dataset's "**+**" icon to add it to the map (or click it's title then click **Add to the map**).
1. The dataset will be added to the left panel and you may now see data overlaid on the map. But **if you don't see any data or data doesn't cover a location** or , continue to the next section: **Filter by location**.

    ![Adding data](/_files/dea-maps/dea_maps_5.jpg)

<span id="filter-by-location"></span>

## Filter by location

After adding data to the map, if you don't see any data or the data doesn't cover a particular location, you can use the 'Filter by location' tool. This is especially useful for datasets that are provided as swaths (strips of data that the satellite captures as it travels), e.g. the 'Baseline satellite data' datasets. Zoom out on the map and you will often see that swaths of data are visible, but they are not covering the location you are interested in. Or you may find that no data exists at all for this particular time.

'Filter by location' will show the most recent data that is available for a given location.

1. In the left sidebar, click **Filter by location** for the dataset you have added the map.
1. Click a location on the map then wait for it to load.
1. Data should now be overlaid on that location. The left sidebar will indicate that the filter has been applied.
1. Next, you can either select **Remove filter** or **New location**.

    ![Adding data](/_files/dea-maps/dea_maps_6.jpg)

## Share a URL and save your map

Once you've created a map by adding layers, adjusting settings, and zooming in on a specific location, you will want to share this map with others, or save it so you can continue work on it later. You can do both of these using the **Share URL** feature.

1. Click **Share / Print** on the top right.
1. Click **Copy** to copy this custom URL to your clipboard.
1. Anyone who opens this URL will see your map, exactly as you configured it. You can send this URL to others, link to it from a public website, or bookmark it for later.

![Share](/_files/dea-maps/dea_maps_share_1.jpg)

## Switch bands and layers

Most datasets contain multiple 'bands' or 'layers' of data that reveal different features of the landscape. You can switch between these using the **Styles** dropdown in the left sidebar.

For example, the 'DEA Surface Reflectance (Sentinel-2)' dataset can be switched to the 'False colour - Green, SWIR, NIR' style. This style uses wavelengths of light beyond the visible spectrum ('near infrared' and 'short-wave infrared') to highlight waterbodies, vegetation, and other features more distinctly.

![False colour](/_files/dea-maps/dea_maps_styles_2.jpg)

## Compare side-by-side

There is a **Compare** feature that lets you view two different map configurations side-by-side. This allows you to compare two different datasets or the same dataset at two different times. Here's an example map of [DEA High Tide Imagery versus DEA Low Tide Imagery](https://maps.dea.ga.gov.au/#share=s-7YeWZKqWkF0Ctv5Av8RkHSWeNzQ).

1. In the left sidebar, click the three vertical dots ('Show more actions') on a dataset that you have added to the map &gt; click **Compare**.
1. A 'screen splitter' will now split the map into two halves. In the sidebar, the dataset's panel will be split into two copies: one labelled 'Left' and the other 'Right'.
1. You can configure each side of the map independently. E.g. you can change the 'Styles' value on the right side.
1. Each dataset can be assigned to either the **Left** or **Right** side or **Both** by selecting the relevant option in the left sidebar.
1. To compare two different datasets side-by-side: add an additional dataset to the map &gt; assign it to the right or left side &gt; remove the existing dataset that was assigned to that side.
1. To close this side-by-side view, click the "**&times;**" next to 'Split Screen Mode' in the left sidebar.

Note that you can share a URL of your comparison by using the **Share / Print** feature.

![Screen splitter](/_files/dea-maps/dea_maps_compare_2.jpg)

## Difference tool

The **Difference** tool allows you to visualise the changes in a dataset over time. Here is an example map showing [locations that have gotten wetter or dryer over time](https://maps.dea.ga.gov.au/#share=s-oAolm6NEW2vSCtXGJMUmPnIAUx2).

1. In the left sidebar, click the three vertical dots ('Show more actions') on a dataset that you have added to the map &gt; click **Difference**.
1. The difference tool will appear, replacing the left sidebar.
1. Select a location on the map to analyse by clicking anywhere on the map.
1. Under **Data Comparison A** and **Date Comparison B**, choose the two dates to compare. For best results, choose dates that don't have cloud cover.
1. Click **Choose a difference output** and select an option. For instance, the 'Modified Normalised Difference Water Index - Green, SWIR' is useful for comparing the distribution of water.
1. Click **Generate change detection**.
1. The difference will be shown on the map as a new dataset. For instance, the 'Modified Normalised Difference Water Index - Green, SWIR' shows locations that have gotten wetter over time in blue while locations that have gotten dryer are red.
1. To reopen the left sidebar, click **Show workbench**, and to close the difference tool, click **Exit**. You'll notice that in the left sidebar, the difference dataset has been added.

![Difference 2](/_files/dea-maps/dea_maps_diff_2.jpg)

## Export data as high-resolution TIFF

It's possible to export small areas of DEA data in the high-resolution TIFF image format. This exported data can used in QGIS and ArcGIS. (But for exporting larger volumes of data, you can use the [DEA Sandbox](/guides/setup/Sandbox/sandbox/) or [NCI](/guides/setup/NCI/README/) environments or download directly from the [DEA Public Data S3 Bucket](https://data.dea.ga.gov.au/).)

1. In the left sidebar, click the three vertical dots ('Show more actions') on a dataset that you have added to the map &gt; click **Export**.
1. Click two points on the map to draw a rectangle.
1. Click **Download extent** then wait for the TIFF file to be downloaded to your computer. (If the export fails, try zooming in and drawing a rectangle that covers a smaller land area.)

![Export](/_files/dea-maps/dea_maps_export_2.jpg)

## Navigate time and location

You can navigate through datasets across both location and time.

* Change to a different time by clicking the **Time** value in the left sidebar, or clicking on the timeline at the bottom.
* Zoom in and out of the map by scrolling the mouse, or use the "**+**" and "**-**" buttons.
* Move to a different location by dragging with the mouse, or type in the **Search for locations** bar. E.g. search for 'Lake Eyre', then click the option: 'Lake Eyre, SA'.

![Changing time](/_files/dea-maps/dea_maps_7.jpg)

## Additional features

* **Animate satellite imagery** &mdash; The time slider can also be used to animate satellite imagery. Click the arrow "Play" button to the left of the time slider, and control the speed of the animation using the "Play faster" and "Play slower" buttons.
* **Print your map** &mdash; Click **Share / Print** &gt; **Show Print View** &gt; a new page will open showing a printer-friendly view; click **Print** or press **Ctrl-p** on your keyboard.
* **Capture a high-quality image of your map** &mdash; Follow the steps above to print your map, except on the printer-friendly page, right-click on the image and select **Save image as ...**.
* **Help** &mdash; For more information about using DEA Maps, click **Help** on the top right, then you can take the tour, watch the videos, or read the guides.

***

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

