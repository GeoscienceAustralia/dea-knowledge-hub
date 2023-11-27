## Accuracy

The accuracy of the stacked line plots is dependent on the accuracy of the underlying algorithms: Water Observations from Space (Mueller et al. 2016) and the Joint Remote Sensing Research Program's Fractional Cover algorithm (Scarth et al. 2010). 

The Tasseled Cap Wetness threshold used in the Wetlands Insight Tool has been compared with independent inundation data for one major wetland complex, however the Tasseled Cap Wetness index may under or overestimate the actual extent of inundation for individual wetlands.  The use of a consistent threshold means that the 'precision' is high, insofar as you're measuring the same aspect of the wetland at each point in time, however the accuracy with which Tasseled Cap Wetness measures free water underneath/within wetland vegetation is not quantified.

The interpretability of the results for each polygon is dependent on the accuracy of the linework that has been used to create that polygon. The line work used in the Wetlands Insight Tool (Ramsar Wetlands) comes from the 19/03/2020 revision of the [Ramsar Wetlands of Australia Dataset](http://www.environment.gov.au/fed/catalog/search/resource/details.page?uuid=%7BF49BFC55-4306-4185-85A9-A5F8CD2380CF%7D) (available under a [Creative Commons Attribution 3.0 Australia Licence](https://creativecommons.org/licenses/by/3.0/au/)) and has been processed by exploding large polygons into smaller polygons in QGIS. This means that sites where multiple boundaries exist have a separate plot for separate subsites, allowing users to understand the dynamics of the subsites separately. Users are able to manually combine Wetlands Insight Tool outputs accessed through DEA Maps as csvs to gain an understanding of combined sites.  The 6 Australian Ramsar Sites in external territories are excluded as they are outside of Australia’s satellite data footprint.

The 30 metre resolution of Landsat imposes an intrinsic limitation on the Wetlands Insight Tool.  Wetland areas that are small, or long and narrow in nature are likely to be inaccurate (due to inclusion of neighbouring non-wetland pixels) or difficult to interpret (stack line plots for areas with a small number of pixels have sharp steps in them).

The period of time between when Landsat 5 ceased operations (November 2011) and Landsat 8 data became routinely available (May 2013) is likely to be inaccurate.  There will be some wetlands, close to the centre of Landsat paths where Landsat 7 continued to capture suitable (gap free) data, however it is safer, as a general rule, to consider this period as 'low data quality'. Other periods where less than four observations occur in a calendar year are also considered 'low data quality'. Regions of low data quality are hashed with a pale rectangular overlay in the Wetlands Insight Tool plots. 

![Wetlands Insight Tool plot for Narran Lakes Nature Reserve, New South Wales, showing variations in open water, wet, green vegetation, dry vegetation and bare soil from 1987 to 2021](/_files/cmi/NarranLakesNatureReserveNSWWIT.png)

## Quality assurance

Quality assurance was undertaken to ensure that a Wetlands Insight Tool stacked line plot was generated for every exploded polygon in the Ramsar Wetlands polygon set, where satellite data was available through Digital Earth Australia. Sites outside continental Australia may not be available in the dataset.

