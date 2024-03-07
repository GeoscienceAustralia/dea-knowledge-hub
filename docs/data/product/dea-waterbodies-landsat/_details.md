## Background

DEA Waterbodies provides up-to-date information about the extent and location of surface water in Australia to enable us to understand of this valuable and increasingly scarce resource.

It uses Geoscience Australia’s archive of over 30 years of Landsat satellite imagery to identify the locations of over 300,000 waterbodies on the Australian landscape and it estimates the wet surface area of these waterbodies.

The tool applies a [water classification scheme](/data/product/dea-water-observations-landsat/) to each available Landsat satellite image and maps the locations of waterbodies across Australia. It provides a time series of wet surface areas for all waterbodies that are present for over 10% of the time between 1987 and 2020, and are larger than 2,700 m<sup>2</sup> (the size of three Landsat pixels).

The tool allows you to see changes in the wet surface area of waterbodies over time. This can be used to identify when waterbodies are increasing or decreasing in wet surface area.

% ## Data description

## Applications

* Understand local through to national-scale surface water dynamics over time and geography
* Provide supporting information to better manage water across Australia
* Gain insights into the severity and spatial distribution of drought
* Identify potential water sources for aerial firefighting
* Get deeper insight into [DEA Water Observations](/data/product/dea-water-observations-landsat/) data

## Technical information

The DEA Waterbodies product is comprised of two key components:
* a polygon dataset of automatically mapped waterbody outlines, and
* a csv time series for each polygon capturing the surface area of water within each polygon at every available, clear Landsat observation. 

### Data Specification Tables

The DEA Waterbodies v3.0 Shapefile and CSV contain the following data, as specified in these tables.

```{eval-rst}
:download:`Download the Data Specification Tables as a PDF </_files/dea-waterbodies/DEA_Waterbodies_v3.0_Data_Spec_Table.pdf>`

```

#### Data specification table for DEA Waterbodies 3.0 Shapefile

|Field name |Description |Update Frequency |Data Availability*** |Status^ |Type |
|:----|:----|:----|:----|:----|:----|
|uid |A unique identifier determined from waterbody location and data version |Once per version |Shapefile, DEA Maps, WMS, csv |Existing |String |
|perimetr_m |Perimeter of the defined waterbody (m) |Once per version |Shapefile, DEA Maps, WMS |Existing |Real |
|area_m2 |Area of the defined waterbody (m2) |Once per version |Shapefile, DEA Maps, WMS |Existing |Real |
|dt_wetobs |The last date any water was observed. This is subject to the satellite having clear visibility of the waterbody. The satellite must view 80% of a waterbody to have a valid wet observation recorded.   |As scene input data is available* |DEA Maps, WMS |New |DateTime (UTC) |
|wet_sa_m2 |The total estimated wet surface area calculated from the last clear satellite observation of the waterbody. Calculated as the wet percentage (pc_wet, see timeseries) multiplied by the waterbody area (area_m2) divided by 100.** Any area estimates should be compared to additional data for verification. |As scene input data is available* |DEA Maps, WMS |New |Real |
|dt_satpass |The most recent date that the satellite passed over the waterbody. |As scene input data is available* |DEA Maps, WMS |New |DateTime (UTC) |
|dt_updated |The date that the dt_wetobs, wet_sa_m2 and dt_satpass attributes were last updated. |As scene input data is available* |DEA Maps, WMS |New |DateTime (UTC) |
|dt_created |The date the polygons were created |Once per version |Shapefile, DEA Maps, WMS |New |DateTime (UTC) |
|meta_url |The metadata url for this dataset |Once per version |Shapefile, DEA Maps, WMS |New |String |
|timeseries |The Amazon S3 location of the wet percentage time series for this waterbody. The timeseries data is stored in a CSV file with the following columns: </br></br> (DateTime UTC) – date of observation </br></br> pc_wet (Float) – percentage of the waterbody recorded as wet (0-100) </br></br> px_wet (Integer) – number of 30m Landsat pixels recorded as wet  |Value is static, but the csv contents are updated as scene input data becomes available* |Shapefile, DEA Maps, WMS |Existing |String |


#### Data specification table for DEA Waterbodies 3.0 Timeseries CSV

|Field name |Description |Update Frequency |Data Availability |Status |Type |
|:----|:----|:----|:----|:----|:----|
|date |date of observation (UTC) |Value is static, but the csv contents are updated as scene input data becomes available* |DEA Maps, csv |Existing |DateTime (UTC) |
|pc_wet |percentage of the waterbody recorded as wet (0-100) |Value is static, but the csv contents are updated as scene input data becomes available* |DEA Maps, csv |Existing |Float |
|px_wet |number of 30m Landsat pixels recorded as wet |Value is static, but the csv contents are updated as scene input data becomes available* |DEA Maps, csv |Existing |Integer |

</p><p><small>* Scene data is available approximately two weeks from the satellite overpass for the Water Observations feature layers used to process Waterbodies. Waterbodies scenes are processed as Water Observations feature layer scenes become available in the DEA datacube. It takes approximately ten minutes to process Waterbodies per scene.  One Landsat scene measures approximately 190 x 180 km https://www.nasa.gov/wp-content/uploads/2015/04/landsat_9_fast_facts.pdf  

** Larger waterbodies are easier to detect and smaller or narrower waterbodies are harder to detect. Area estimates should be compared to additional data for verification. 

*** Data fields empty in shapefile (dt_wetobs, wet_sa_m2, dt_satpass, dt_updated) are available for the latest relevant observations only via DEA Maps and WMS 

^Data fields introduced in v3.0 are ‘New’ </small></p>

### Producing DEA Waterbodies

DEA Waterbodies is a polygon-based view of DEA Water Observations (DEA WO), derived through the automatic processing of DEA WO to identify the outlines of persistent waterbodies across Australia (Figure 1). 

:::{figure} /_files/cmi/V2Workflow.JPG
:alt: DEA Waterbodies workflow

Figure 1: Flow diagram outlining the steps taken to produce DEA Waterbodies polygons
:::

For a detailed discussion of the methods used to produce DEA Waterbodies v1, refer to [Krause et al. 2021](https://doi.org/10.3390/rs13081437). For the differences between DEA Waterbodies v1, v2 and v3.0, refer to the [Changelog](./?tab=history#changelog). DEA Waterbodies v3.0 uses the same polygon/vector outlines as DEA Waterbodies v2, with additional metadata.

## Lineage

This product builds upon [DEA Water Observations](/data/product/dea-water-observations-landsat/).

The code used in the development of this product is available on [GitHub](https://github.com/GeoscienceAustralia/dea-conflux).

% ## Processing steps

% ## Software

## References

Krause, C.E., Newey, V., Alger, M.J. and Lymburner, L., (2021). Mapping and monitoring the multi-decadal dynamics of Australia’s open waterbodies using Landsat. Remote Sensing, 13(8), p.1437. [https://doi.org/10.3390/rs13081437](https://doi.org/10.3390/rs13081437)

Mueller, N., Lewis, A., Roberts, D., Ring, S., Melrose, R., Sixsmith, J., Lymburner, L., McIntyre, A., Tan, P., Curnow, S., & Ip, A. (2016). Water observations from space: Mapping surface water from 25 years of Landsat imagery across Australia. *Remote Sensing of Environment*, *174*, 341–352. [https://doi.org/10.1016/j.rse.2015.11.003](https://doi.org/10.1016/j.rse.2015.11.003)

