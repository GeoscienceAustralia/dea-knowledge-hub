## Frequently asked questions

### About the waterbody graphs

:::{dropdown} Is this product showing waterbody volume?
No. DEA Waterbodies does not measure the volume of water in any waterbody.

The tool detects the wet surface area of a waterbody. The wet surface area does not correlate to the volume of water in a storage. For example a waterbody can be observed as wet with just a shallow covering of water.
:::

:::{dropdown} What does ‘100%’ wet surface area refer to?
The outline of each waterbody corresponds to the maximum observed wet surface area of the waterbody between 1987 and 2020. In the time series, this maximum area is considered as 100% wet surface area. The 100% wet surface area does not correlate to the volume of water in a storage. For example a waterbody can be observed as wet with just a shallow covering of water.
:::

:::{dropdown} Do the time series provide information on the source of water observed?
No. This tool does not differentiate between water sources.
:::

:::{dropdown} How often are the DEA Waterbodies time series updated?
The DEA Waterbodies time series are updated at least monthly. An individual time series may not be updated as frequently if it was cloudy on the days the satellite was overhead.

Landsat satellites do not observe all of Australia at the same time. The dates of satellite observations are dependent on the date that the satellite observed that waterbody. Landsat satellites take 16 days to collect data across all of Australia, with different locations being collected on different days within that 16 days.
:::

:::{dropdown} Why are some time series shorter than others?
All useable observations for each waterbody have been included in the individual waterbody time series. Short or missing time series can result from frequent cloud cover, misclassification, or other processing issues.

If less than 90% of the total waterbody is observed on any one day, due to cloud cover or missing data, then that observation is marked as a missing value within the csv file.

Cloud cover leading to invalid data can be a particular problem in coastal regions, northern Australia during summer, and in Tasmania.
:::

:::{dropdown} How does DEA Waterbodies deal with clouds?
Data used within DEA Waterbodies is cloud masked. If less than 90% of the total waterbody is observed on any one day, due to cloud cover or missing data, then that observation is marked as a missing value.

Cloud cover leading to invalid data can be a particular problem in coastal regions, northern Australia during summer, and in Tasmania.
:::

:::{dropdown} Why are the time series irregularly spaced in time?
Landsat satellites do not observe all of Australia at the same time. The dates of satellite observations are dependent on the date that the satellite observed that waterbody. Landsat satellites take 16 days to collect data across all of Australia, with different locations being collected on different days within that 16 days. This means that the date stamps of each time series are not common across all waterbodies.
:::

:::{dropdown} What are the two different time series provided for each waterbody?
Within the DEA Waterbodies web service, there are two time series provided for each waterbody, which can be seen in the legend panel on the left hand side once a waterbody has been selected, and the time series expanded:

* 'Percentage of total surface area observed as wet': the percentage of the total surface area of the waterbody that has been classified as 'wet' for each time step. (Note: this is not a volume)
* 'Wet Pixel Count': the total number of pixels that have been classified as 'wet' for each time step. This value is useful if you need to calculate an area of wet pixels. Each pixel is 30 metres by 30 metres.
:::

### About the mapped waterbodies

:::{dropdown} What satellite imagery does DEA Waterbodies use?
DEA Waterbodies is based on Landsat satellite data provided by the United States Geological Service. The Digital Earth Australia (DEA) program within Geoscience Australia corrects this data and makes it available publicly.

The tool uses data from the Landsat 5 TM (1987--2011), Landsat 7 ETM+ (1999--present), and Landsat 8 OLI (2013--present) missions.

To find out more about the Landsat missions, check out the [USGS Landsat Missions webpages](https://www.usgs.gov/land-resources/nli/landsat/landsat-satellite-missions?qt-science_support_page_related_con=2#qt-science_support_page_related_con)
:::

:::{dropdown} How do you classify water from satellite imagery?
The water classifier that is used by DEA Waterbodies is the **DEA Water Observations** algorithm. It is a decision tree algorithm that classifies each pixel as 'wet', 'dry' or 'invalid'.

For details on how the Water Observations from Space algorithm classifies water, [see this paper](https://doi.org/10.1016/j.rse.2015.11.003)
:::

:::{dropdown} How big does a waterbody have to be to be included?
DEA Waterbodies only maps waterbodies larger than 2,700 m<sup>2</sup> (3 whole Landsat pixels). This size was chosen to minimise noise caused by large numbers of small wet areas in the landscape.
:::

:::{dropdown} What does the outline of individual waterbodies represent?
The outline of each waterbody corresponds to the maximum observed wet surface area of the waterbody between 1987 and 2020. DEA Waterbodies is derived completely from satellite data, which means that the outline of each waterbody is based entirely on the extent of water mapped by satellite observations.

It may not directly match up with the edges of a waterbody, as the edges themselves are not inundated, and so will not be captured within the wet extent. The waterbodies also may not match up with the previously mapped extent of any waterbody found in other map products.
:::

:::{dropdown} Why do the waterbodies look pixelated?
DEA Waterbodies is derived completely from satellite data, which means that the outline of each waterbody is based entirely on the extent of water mapped by satellite observations. The pixelated outlines show which satellite pixels have been included inside each waterbody. We chose not to smooth the outlines of the waterbodies to make it clear that this mapping has been done using satellite data, and to make it clear which pixels have been included in each waterbodies’ time series.
:::

:::{dropdown} There is a waterbody missing from your map. Why?
There are a few reasons why a waterbody might be missing:

It might be too small: DEA Waterbodies only maps waterbodies larger than 2,700m<sup>2</sup> (3 whole Landsat pixels).

* It might not have been wet enough: DEA Waterbodies only maps waterbodies that have been observed as wet at least 10% of the time between 1987 and 2020. If a waterbody fills very infrequently, it may not meet this threshold.
* The waterbody might have too much vegetation surrounding it: the **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river or a wetland), the classifier will not see this as water and the waterbody may not be mapped.
* The water in the waterbody does not look like water: very sediment-filled water, particularly in northern Australia, is often misclassified as land.
* It might be new: newly constructed waterbodies will not be included in this product as they will not have been observed as wet at least 10% of the time between 1987 and 2020. Waterbodies that have been constructed or modified after 2016 may not be captured within this tool. Future updates of this product should capture newer waterbodies.

If there is a waterbody missing from DEA Waterbodies that you would like to report, please contact us at <a href="mailto:dea@ga.gov.au">dea@ga.gov.au</a>

Reports of missing waterbodies may assist us during quality checking of future product releases.
:::

:::{dropdown} Why are there whole/parts of rivers missing?
The **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river), the classifier will not see this as water, and the waterbody will be cut short, even though the river continues along underneath the vegetation.

Additionally, the Landsat satellite data on which this dataset is based has a pixel resolution of 30 metres by 30 metres. A pixel will only be classified as water where the pixel is almost entirely made up of water. For example, where rivers narrow or contain large sandbanks the pixel will incorporate these other signatures, and not be classified as water.

Both of these factors mean that rivers are not seen as continuous features throughout DEA Waterbodies.
:::

::::{dropdown} Why are some of the waterbody polygons patchy?
Some of the waterbody polygons contain holes, or are quite irregularly shaped. This is caused by the DEA Water Observations classifier not seeing these ‘missing bits’ as water frequently enough, and so they are excluded. This is particularly evident in the very large waterbodies in central Australia, like Kati Thanda–Lake Eyre, where the inflow points to the north of the lake are infrequently inundated when compared to the southern end of the lake, where water pools in the landscape.

Additionally the **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river or a wetland), the classifier will not see this as water and the resulting mapped waterbody may be patchy.

:::{figure} /_files/dea-waterbodies/dea-waterbodies-kati-thanda-lake-eyre.png
:alt: Screenshot of DEA Waterbodies website showing marked line boundaries of blue water shape

Kati Thanda–Lake Eyre as mapped within DEA Waterbodies
:::
::::

:::{dropdown} Why are some waterbodies fused together instead of being separate?
DEA Waterbodies are mapped using water classified pixels. If a pixel is predominantly water, it will be mapped as water. Small levees or roads between adjacent waterbodies will not necessarily separate the mapped waterbodies if they are not large enough to influence the total make up of their pixel. This means that some separate waterbodies are mapped as a single waterbody within DEA Waterbodies.
:::

:::{dropdown} Does DEA Waterbodies show flooded areas?
By design, we have excluded locations where water is seen only during extreme flood events. A wetness threshold of 10% was applied to the data, meaning that only waterbodies observed as wet at least 10% of the time between 1987 and 2020 have been included. This threshold was determined to be sensitive enough to capture the locations of persistent waterbodies, but not so sensitive as to pick up too many false positives like flood irrigation, flood events or soggy areas in the landscape.
:::

### Other information about DEA Waterbodies

:::{dropdown} How do I download the data?
Individual waterbody time series can be downloaded within [National Map](https://nationalmap.gov.au/) and [DEA Maps](http://maps.dea.ga.gov.au/). Instructions on how to download individual time series can be found in the User Guide.

The underlying polygon dataset containing the map of over 300,000 waterbodies across Australia can be downloaded from the [Access tab](./?tab=access).
:::

:::{dropdown} Can I load DEA Waterbodies into my GIS software?
DEA Waterbodies has been provided as a web mapping service. You can consume this service by connecting to the service endpoint (see the metadata provided with the layer in [National Map](https://nationalmap.gov.au/) or [DEA Maps](http://maps.dea.ga.gov.au/) for details). Please note that for now, this service will only allow you to access the underlying waterbody map, not the individual time series associated with each waterbody.
:::

:::{dropdown} How was DEA Waterbodies produced?
The code used to produce DEA Waterbodies has been uploaded to Geoscience Australia's [GitHub page](https://github.com/GeoscienceAustralia/dea-waterbodies). There is also a [peer reviewed journal article](https://doi.org/10.3390/rs13081437) that explains in detail the methods used to produce DEA Waterbodies.
:::

:::{dropdown} How do I cite DEA Waterbodies?
Krause, Claire E.; Newey, Vanessa; Alger, Matthew J.; Lymburner, Leo. 2021. "Mapping and Monitoring the Multi-Decadal Dynamics of Australia's Open Waterbodies Using Landsat" Remote Sens. 13, no. 8: 1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437)
:::

:::{dropdown} Who did you collaborate with to produce DEA Waterbodies?
DEA Waterbodies was the result of a collaboration between Geoscience Australia, the NSW Department of Planning, Industry and Environment, and the Murray Darling Basin Authority to determine the potential of satellite imagery to provide useful insights about water in the landscape.
:::

:::{dropdown} How do I get more information or provide feedback on DEA Waterbodies?
Contact us at <a href="mailto:Earth.Observation@ga.gov.au">Earth.Observation@ga.gov.au</a>
:::

