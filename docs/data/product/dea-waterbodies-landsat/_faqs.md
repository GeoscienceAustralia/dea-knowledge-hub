## Frequently asked questions

Here you will find answers to the most frequently asked questions about this product.
If you need more help, please contact <a href="mailto:earth.observation@ga.gov.au">earth.observation@ga.gov.au</a>.


### About the waterbody graphs

:::{dropdown} Is this product showing waterbody volume?
No. DEA Waterbodies does not measure the volume of water in any waterbody.

The tool detects the wet surface area of a waterbody. The wet surface area does not correlate to the volume of water in a storage. For example, a waterbody can be observed as wet with just a shallow covering of water.
:::

:::{dropdown} What does ‘100%’ wet surface area refer to?
The outline of each waterbody corresponds to the maximum observed wet surface area of the waterbody between 1987 and 2020. In the time series, this maximum area is considered as 100% wet surface area. The 100% wet surface area does not correlate to the volume of water in a storage. For example, a waterbody can be observed as wet with just a shallow covering of water. The maximum observed wet area is available as ‘area_m2’ in the [data](./?tab=details#data-specification-tables).
:::

:::{dropdown} Do the time series provide information on the source of water observed?
No. This tool does not differentiate between water sources.
:::

:::{dropdown} How often are the DEA Waterbodies time series updated?
The DEA Waterbodies time series are updated as soon as data from the satellites are available. An individual time series could be updated fortnightly or less frequently if it was cloudy on the days the satellite was overhead.  

Landsat satellites do not observe all of Australia at the same time. The dates of satellite observations are dependent on the date that the satellite observed a particular waterbody. Landsat satellites take 16 days to collect data across all of Australia, with different locations being collected on different days within that 16-day interval. Landsat data is available approximately two weeks from the satellite overpass before the Water Observations feature layers used to process Waterbodies are created. Waterbodies are then processed as Water Observations feature layer scenes become available in the DEA datacube. It takes approximately ten minutes to process Waterbodies per scene, once the data is available.
:::

:::{dropdown} Why are some time series shorter than others?
All useable observations for each waterbody have been included in the individual waterbody time series. Short or missing time series can result from frequent cloud cover, misclassification, or other processing issues.

If less than 90% of the total waterbody is observed on any one day, due to cloud cover or missing data, then that observation is marked as a missing value within the CSV file.

Cloud cover leading to invalid data can be a particular problem in coastal regions, northern Australia during summer, and in Tasmania.

Some larger salt lakes in Australia have very few records currently available. For larger waterbodies, which may cross multiple swath boundaries or suffer from misclassifications (salt lakes can be misclassified as cloud due to their brightness) this can be problematic. 
:::

:::{dropdown} How does DEA Waterbodies deal with clouds?
Data used within DEA Waterbodies is cloud masked. If less than 90% of the total waterbody is observed on any one day, due to cloud cover or missing data, then that observation is marked as a missing value.

Cloud cover leading to invalid data can be a particular problem in coastal regions, northern Australia during summer, and in Tasmania.
:::

:::{dropdown} Why are the time series irregularly spaced in time?
Landsat satellites do not observe all of Australia at the same time. The dates of satellite observations are dependent on the date that the satellite observed that particular waterbody. Landsat satellites take 16 days to collect data across all of Australia, with different locations being collected on different days within that 16-day interval. This means that the date stamps of each time series are not common across all waterbodies. DEA Waterbodies contains data from all available Landsat satellites.
:::

:::{dropdown} What are the two different time series provided for each waterbody?
Within the DEA Waterbodies web service, there are two time series provided for each waterbody, which can be seen in the legend panel on the left side once a waterbody has been selected, and the time series expanded:

* **Pc Wet** &mdash; The 'Percentage of total surface area observed as wet'. This is the percentage of the total surface area of the waterbody that has been classified as 'wet' for each time step. (Note: this is not a volume)
* **Px Wet** &mdash; The 'Wet Pixel Count'. This is the total number of pixels that have been classified as 'wet' for each time step. This value is useful if you need to calculate an area of wet pixels. Each pixel is 30 m by 30 m.
:::

### About the mapped waterbodies

:::{dropdown} What satellite imagery does DEA Waterbodies use?
DEA Waterbodies is based on Landsat satellite data provided by the United States Geological Survey. The Digital Earth Australia (DEA) program within Geoscience Australia calibrates this data and makes it available publicly.

The tool uses data from the Landsat 5 TM (1987--2011), Landsat 7 ETM+ (1999--present), Landsat 8 OLI (2013--present), and Landsat 9 OLI-2 (2021--present) missions.

To find out more about the Landsat missions, see the [USGS Landsat Missions webpages](https://www.usgs.gov/land-resources/nli/landsat/landsat-satellite-missions?qt-science_support_page_related_con=2#qt-science_support_page_related_con).
:::

:::{dropdown} How do you classify water from satellite imagery?
The water classifier that is used by DEA Waterbodies is the **DEA Water Observations** algorithm. It is a decision tree algorithm that classifies each pixel as 'wet', 'dry' or 'invalid'.

For details on how the Water Observations from Space algorithm classifies water, see the paper: [Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia](https://doi.org/10.1016/j.rse.2015.11.003).
:::

:::{dropdown} How big does a waterbody have to be to be included?
DEA Waterbodies only maps waterbodies larger than 2,700 m<sup>2</sup> (the size of 3 Landsat pixels). This size was chosen to minimise noise caused by large numbers of small wet areas in the landscape.
:::

:::{dropdown} What does the outline of individual waterbodies represent?
The outline of each waterbody corresponds to the maximum observed wet surface area of the waterbody between 1987 and 2020, except for two cases. Long, thin waterbodies were separated into multiple polygons as described in Krause et al. 2021, and the following waterbodies were replaced by the extents from the [Surface Hydrology Polygons (Regional)](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/83134) dataset: 

* Kati Thanda-Lake Eyre (North) 
* Kati Thanda-Lake Eyre (South) 
* Lake Torrens 
* Lake Frome / Munda 
* Lake Gairdner 
* Lake Blanche 
* Lake Everard 

Waterbody outlines may not directly match up with the edges of a waterbody, as the edges themselves are not inundated, and so will not be captured within the wet extent. The waterbodies may also not match up with the previously mapped extent of any waterbody found in other map products. 
:::

:::{dropdown} Why do some waterbodies look pixelated?
The pixelated outlines show which satellite pixels have been included inside each waterbody. We chose not to smooth the outlines of the waterbodies to make it clear that this mapping has been done using satellite data and to make it clear which pixels have been included in each waterbodies’ time series.
:::

:::{dropdown} Why is there is a waterbody missing from your map?
There are a few reasons why a waterbody might be missing:

* It may be too small: DEA Waterbodies only maps waterbodies larger than 2,700m<sup>2</sup> (3 whole Landsat pixels).
* It may not have been wet enough: DEA Waterbodies only maps waterbodies that have been observed as wet at least 10% of the time between 1987 and 2020. If a waterbody fills very infrequently, it may not meet this threshold.
* The waterbody may have too much vegetation surrounding it: the **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river or a wetland), the classifier will not see this as water and the waterbody may not be mapped.
* The water in the waterbody does not look like water: very sediment-filled water, particularly in northern Australia, is often misclassified as land.
* It may be new: newly constructed waterbodies will not be included in this product as they will not have been observed as wet at least 10% of the time between 1987 and 2020. Waterbodies that have been constructed or modified after 2016 may not be captured within this tool. Future updates of this product should capture newer waterbodies.

If there is a waterbody missing from DEA Waterbodies that you would like to report, please contact us at <a href="earth.observation@ga.gov.au">dea@ga.gov.au</a>

Reports of missing waterbodies may assist us during quality checking of future product releases.
:::

:::{dropdown} Why are there whole/parts of rivers missing?
The **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river), the classifier will not see this as water, and the waterbody will be cut short, even though the river continues along underneath the vegetation.

Additionally, the Landsat satellite data on which this dataset is based has a pixel resolution of 30 m x 30 m. A pixel will only be classified as water where the pixel is almost entirely made up of water. For example, where rivers narrow or contain large sandbanks the pixel will incorporate these other signatures, and not be classified as water.

Both of these factors mean that rivers are not seen as continuous features throughout DEA Waterbodies. Some rivers have also been split into shorter sections for ease of analysis.
:::

::::{dropdown} Why are some of the waterbody polygons patchy?
Some of the waterbody polygons contain holes or are quite irregularly shaped. This is caused by the DEA Water Observations classifier not seeing these ‘missing bits’ as water frequently enough, and so they are excluded.

The **DEA Water Observations** classifier that determines where water is observed does not work well where water is combined with vegetation. If there is vegetation obscuring the water (like a tree leaning across a river or a wetland), the classifier will not see this as water and the resulting mapped waterbody may be patchy. For example, water under mangroves. 

:::{figure} /_files/dea-waterbodies/DEA_Waterbodies_v3.0_mangroves_faq.jpg
:alt: Screenshot of DEA Waterbodies showing marked line boundaries of blue water shape

Mangroves at the mouth of Fitzroy River near Rockhampton as mapped within DEA Waterbodies.
:::
::::

:::{dropdown} Why are some waterbodies fused together instead of being separate?
DEA Waterbodies are mapped using water-classified pixels. If a pixel is predominantly water, it will be mapped as water. Small levees or roads between adjacent waterbodies will not necessarily separate the mapped waterbodies if they are not large enough to influence the total make up of their pixel. This means that some separate waterbodies are mapped as a single waterbody within DEA Waterbodies.
:::

:::{dropdown} Does DEA Waterbodies show flooded areas?
By design, we have excluded locations where water is seen only during extreme flood events. A wetness threshold of 10% was applied to the data, meaning that only waterbodies observed as being wet at least 10% of the time between 1987 and 2020 are included. This threshold was determined to be sensitive enough to capture the locations of persistent waterbodies, but not so sensitive as to pick up too many false positives like flood irrigation, flood events, or soggy areas in the landscape.
:::

### Other information about DEA Waterbodies

:::{dropdown} How do I download the data?
Individual waterbody time series can be downloaded within the [National Map](https://nationalmap.gov.au/) and [DEA Maps](http://maps.dea.ga.gov.au/) platforms. 

The underlying polygon dataset containing the map of over 300,000 waterbodies across Australia can be downloaded from the [Access tab](./?tab=access).
:::

:::{dropdown} Can I load DEA Waterbodies into my GIS software?
DEA Waterbodies has been provided as a [web mapping service](https://geoserver.dea.ga.gov.au/geoserver/dea/wms) (WMS). You can load this service into your GIS software by connecting to the service endpoint (see the metadata provided with the layer in [National Map](https://nationalmap.gov.au/) or [DEA Maps](http://maps.dea.ga.gov.au/) for details). Data available through this service can be viewed on the [data specification](./?tab=details#data-specification-tables) tables.
:::

:::{dropdown} How was DEA Waterbodies produced?
The code used to produce DEA Waterbodies polygons is available [here](https://github.com/GeoscienceAustralia/dea-waterbodies). DEA Waterbodies time series generation code is also available on [GitHub](https://github.com/GeoscienceAustralia/dea-conflux). There is a [peer-reviewed journal article](https://doi.org/10.3390/rs13081437) that explains in detail the methods used to produce DEA Waterbodies.
:::

:::{dropdown} How do I cite DEA Waterbodies?
DEA Waterbodies is published by Geoscience  Australia under the [Creative Commons Attribution 4.0 International Licence](https://creativecommons.org/licenses/by/4.0/). You can attribute the data and derivative works using the following two citations: 

Dataset citation: 

Dunn, B., Krause, C., Newey, V., Lymburner, L., Alger, M.J., Adams, C., Yuan, F., Ma, S., Barzinpour, A., Ayers, D., McKenna, C., Schenk, L. 2024. Digital Earth Australia Waterbodies v3.0. Geoscience Australia, Canberra. [https://dx.doi.org/10.26186/148920](https://dx.doi.org/10.26186/148920) 

Research paper citation: 

Krause, C.E., Newey, V., Alger, M.J. and Lymburner, L., (2021). Mapping and Monitoring the Multi-Decadal Dynamics of Australia’s Open Waterbodies using Landsat. *Remote Sensing*, *13*, 1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437) 
:::

:::{dropdown} Who did you collaborate with to produce DEA Waterbodies?
DEA Waterbodies version 1 was the result of a collaboration between Geoscience Australia, the NSW Department of Planning, Industry and Environment, and the Murray Darling Basin Authority to determine the potential of satellite imagery to provide useful insights about water in the landscape. 

The update from version 2 to version 3.0 of the DEA Waterbodies product and service was created through a collaboration between Geoscience Australia, the National Aerial Firefighting Centre, Natural Hazards Research Australia, and FrontierSI to make the product more useful in hazard applications. 
:::

:::{dropdown} How do I get more information or provide feedback on DEA Waterbodies?
Contact us at <a href="mailto:earth.observation@ga.gov.au">earth.observation@ga.gov.au</a>
:::

