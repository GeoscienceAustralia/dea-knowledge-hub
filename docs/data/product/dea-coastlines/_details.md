## Background

Australia has a highly dynamic coastline of over 30,000 km, with over 85% of its population living within 50 km of the coast. This coastline is subject to a wide range of pressures, including extreme weather and climate, sea level rise and human development. Understanding how the coastline responds to these pressures is crucial to managing this region, from social, environmental and economic perspectives.

## What this product offers

[**Digital Earth Australia Coastlines**](https://maps.dea.ga.gov.au/story/DEACoastlines) is a continental dataset that includes annual shorelines and rates of coastal change along the entire Australian coastline from 1988 to the present. 

The product combines satellite data from Geoscience Australia's Digital Earth Australia program with tidal modelling to map the most representative location of the shoreline at mean sea level for each year. The product enables trends of coastal retreat and growth to be examined annually at both a local and continental scale, and for patterns of coastal change to be mapped historically and updated regularly as data continues to be acquired. This allows current rates of coastal change to be compared with that observed in previous years or decades. 

The ability to map shoreline positions for each year provides valuable insights into whether changes to our coastline are the result of particular events or actions, or a process of more gradual change over time. This information can enable scientists, managers and policy makers to assess impacts from the range of drivers impacting our coastlines and potentially assist planning and forecasting for future scenarios.

% ## Data description

## Applications

* Monitoring and mapping rates of coastal erosion along the Australian coastline 
* Prioritise and evaluate the impacts of local and regional coastal management based on historical coastline change 
* Modelling how coastlines respond to drivers of change, including extreme weather events, sea level rise or human development 
* Supporting geomorphological studies of how and why coastlines have changed across time

## Technical information

### 2022 DEA Coastlines update

In August 2023, the DEA Coastlines product was updated to version 2.1.0.

This update consists of the addition of annual shoreline data for 2022. The 2022 shoreline is interim data that is subject to change, and will be updated to a final version in the following 2023 DEA Coastlines update (in July 2024).

### 2021 DEA Coastlines update

In March 2023, the DEA Coastlines product [was updated to version 2.0.0](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/2.0.0). This includes the following key changes to the data and web services: 

#### Improvements and additions: 

* Added annual shoreline data for 2021. The 2021 shoreline is interim data that is subject to change, and will be updated to a final version in the following 2022 DEA Coastlines update (in July 2023).
 
* Improved data coverage over offshore islands and reefs. This includes new shorelines and rates of coastal change over the Indian Ocean, Great Barrier Reef and Coral Sea.
 
* DEA Coastlines now uses data from the FES2014 global tidal model. This model produces accurate tide modelling across Australia ([Seifi et al. 2019](https://www.mdpi.com/2072-4292/11/10/1211)) and globally ([Lyard et al. 2021](https://os.copernicus.org/articles/17/615/2021)) and is more flexible and easier to install than the older TPXO8 tidal model.
 
* Inclusion of Landsat 9 data to provide additional satellite data from late 2021 onwards.
 
* Improved shoreline mapping certainty attributes to provide information about the quality of each individual annual shoreline (compared to the previous approach of identifying all annual shorelines in an area as low or good quality; see **Quality assurance** below for more detail).
 
* New rates of change points certainty attributes to provide information about the quality of each point (see **Quality assurance** below for more detail).
 
* Three coastal change hotspot layers are now included in the product, summarising coastal change within 1 km, 5 km and 10 km windows around each hotspot point. These layers now include attributes providing the median position of all annual shorelines around each hotspot point, which can be used to plot and identify regional trends of coastal change.
 
* Rates of change points now contain a new "uid" ID field containing a unique [geohash](https://en.wikipedia.org/wiki/Geohash) ID that can be used to more easily track rates of change points as they are updated in future DEA Coastlines updates.
 
* Rates of change points include a new "id\_primary" field containing the ID of their Primary sediment compartment from the [Australian Coastal Sediment Compartments](https://ecat.ga.gov.au/geonetwork/srv/api/records/21a23d9a-00dd-ab19-e053-10a3070a2746) framework. This enables points to be easily queried and summarised by coastal sediment compartment.
 

#### Backwards incompatible changes:

* The annual shorelines WFS layer "dea:coastlines" has been renamed to "dea:annual\_shorelines".
 
* The rates of change points WFS layer "dea:coastlines\_statistics" has been renamed to "dea:rates\_of\_change".  
  
 

#### Previous updates

For a full summary of changes made in previous versions, [refer to Github](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/v1.1.0). 

###   
DEA Coastlines dataset

The DEA Coastlines product contains five layers:

* Annual shorelines
* Rates of change points
* Coastal change hotspots (1 km)
* Coastal change hotspots (5 km)
* Coastal change hotspots (10 km)

#### Annual shorelines

Annual shoreline vectors that represent the median or ‘most representative’ position of the shoreline at approximately 0 m Above Mean Sea Level for each year since 1988 (Figure 1).

Dashed shorelines have low certainty (see **Caveats and limitations** below).

Annual shorelines include the following attribute fields:

* *year:* The year of each annual shoreline.
* *certainty:* A column providing important data quality flags for each annual shoreline (see **Quality assurance** below for more detail about each data quality flag).
* *tide\_datum:* The tide datum of each annual shoreline (e.g. "0 m AMSL").
* *id\_primary:* The name of the annual shoreline's Primary sediment compartment from the [Australian Coastal Sediment Compartments](https://ecat.ga.gov.au/geonetwork/srv/api/records/21a23d9a-00dd-ab19-e053-10a3070a2746) framework

###### ![DEA CoastLines coastline layer](/_files/cmi/deacl_coastlines.JPG)  
  
Figure 1: Annual coastlines from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/#share=s-DEACoastlines&playStory=1)

#### Rates of change points

A point dataset providing robust rates of coastal change for every 30 m along Australia’s non-rocky coastlines (Figure 2). The most recent annual shoreline is used as a baseline for measuring rates of change.

###### ![DEA CoastLines rates of change statistics layer](/_files/cmi/deacl_statistics_2.JPG)  
  
Figure 2: Rates of change points from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/#share=s-DEACoastlines&playStory=1)

On the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/#share=s-DEACoastlines&playStory=1), points are shown for locations with statistically significant rates of change (p-value <= 0.01; see *sig\_time* below) and good quality data (certainty = "good"; see *certainty* below) only. Each point shows annual rates of change (in metres per year; see *rate\_time* below), and an estimate of uncertainty in brackets (95% confidence interval; see *se\_time*). For example, there is a 95% chance that a point with a label **\-10.0 m (±1.0 m)** is retreating at a rate of between -9.0 and -11.0 metres per year.

Rates of change points contains the following attribute columns that can be accessed by clicking on labelled points in the web map: 

##### Annual shoreline distances

* *dist\_1990, dist\_1991 etc*: Annual shoreline distances (in metres) relative to the most recent baseline shoreline. Negative values indicate that an annual shoreline was located inland of the baseline shoreline. By definition, the most recent baseline column will always have a distance of 0 m.

##### Rates of change statistics

* *rate\_time*: Annual rates of change (in metres per year) calculated by linearly regressing annual shoreline distances against time (excluding outliers). Negative values indicate retreat and positive values indicate growth. 
* *sig\_time*: Significance (p-value) of the linear relationship between annual shoreline distances and time. Small values (e.g. p-value < 0.01 or 0.05) may indicate a coastline is undergoing consistent coastal change through time. 
* *se\_time*: Standard error (in metres) of the linear relationship between annual shoreline distances and time. This can be used to generate confidence intervals around the rate of change given by *rate\_time* (e.g. 95% confidence interval = *se\_time \* 1.96*)
* *outl\_time*: Individual annual shoreline are noisy estimators of coastline position that can be influenced by environmental conditions (e.g. clouds, breaking waves, sea spray) or modelling issues (e.g. poor tidal modelling results or limited clear satellite observations). To obtain reliable rates of change, outlier shorelines are excluded using a robust Median Absolute Deviation outlier detection algorithm, and recorded in this column. 

##### Other fields

* *uid:* A unique [geohash](https://en.wikipedia.org/wiki/Geohash) identifier for each point.
* *id\_primary:* The name of the point's Primary sediment compartment from the [Australian Coastal Sediment Compartments](https://ecat.ga.gov.au/geonetwork/srv/api/records/21a23d9a-00dd-ab19-e053-10a3070a2746) framework. 
* *certainty:* A column providing important data quality flags for each point in the dataset (see **Quality assurance** below for more detail about each data quality flag).
* *sce*: Shoreline Change Envelope (SCE). A measure of the maximum change or variability across all annual shorelines, calculated by computing the maximum distance between any two annual shorelines (excluding outliers). This statistic excludes sub-annual shoreline variability.
* *nsm*: Net Shoreline Movement (NSM). The distance between the oldest (1988) and most recent annual shoreline (excluding outliers). Negative values indicate the coastline retreated between the oldest and most recent shoreline; positive values indicate growth. This statistic does not reflect sub-annual shoreline variability, so will underestimate the full extent of variability at any given location.
* *max\_year, min\_year*: The year that annual shorelines were at their maximum (i.e. located furthest towards the ocean) and their minimum (i.e. located furthest inland) respectively (excluding outliers). This statistic excludes sub-annual shoreline variability.
* *angle\_mean, angle\_std*: The mean angle and standard deviation between the baseline point to all annual shorelines. This data is used to calculate how well shorelines fall along a consistent line; high angular standard deviation indicates that derived rates of change are unlikely to be correct.
* *valid\_obs, valid\_span:* The total number of valid (i.e. non-outliers, non-missing) annual shoreline observations, and the maximum number of years between the first and last valid annual shoreline.

#### Coastal change hotspots (1 km, 5 km, 10 km)

Three points layers summarising coastal change within moving 1 km, 5 km and 10km windows along the coastline (Figure 3). These layers are useful for visualising regional or continental-scale patterns of coastal change. 

###### ![DEA CoastLines summary layer](/_files/cmi/deacl_summary.JPG)  
  
Figure 3: Coastal change hotspots from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/story/DEACoastlines)

% ## Lineage

## Processing steps

1. Load stack of all available Landsat 5, 7, 8 and 9 satellite imagery for a location 

1. Convert satellite observations to a remote sensing water index (MNDWI) 

1. For each satellite image, model ocean tides into a 5 x 5 km grid based on exact time of image acquisition 

1. Interpolate tide heights into spatial extent of image stack 

1. Mask out high and low tide pixels by removing all observations acquired outside of 50 percent of the observed tidal range centered over mean sea level 

1. Combine tidally-masked data into annual median composites from 1988 to the present representing the coastline at approximately mean sea level 

1. Apply morphological extraction algorithms to mask annual median composite rasters to a valid coastal region

1. Extract waterline vectors using subpixel waterline extraction 

1. Compute rates of coastal change at every 30 m along Australia's non-rocky coastlines using linear regression

## Software

The following software was used to generate this product: 

* [DEA Coastlines Github code](https://github.com/GeoscienceAustralia/dea-coastlines)
* [OpenDataCube](https://github.com/opendatacube)
* [FES2014 global tide model](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/description-fes2014.html)

## References

Bishop-Taylor, R., Nanson, R., Sagar, S., Lymburner, L. (2021). Mapping Australia's dynamic coastline at mean sea level using three decades of Landsat imagery. *Remote Sensing of Environment*, 267, 112734. Available: [https://doi.org/10.1016/j.rse.2021.112734](https://doi.org/10.1016/j.rse.2021.112734)

Nanson, R., Bishop-Taylor, R., Sagar, S., Lymburner, L., (2022). Geomorphic insights into Australia's coastal change using a national dataset derived from the multi-decadal Landsat archive. *Estuarine, Coastal and Shelf Science*, 265, p.107712. Available: [https://doi.org/10.1016/j.ecss.2021.107712](https://doi.org/10.1016/j.ecss.2021.107712)

Bishop-Taylor, R., Sagar, S., Lymburner, L., & Beaman, R. J. (2019a). Between the tides: Modelling the elevation of Australia's exposed intertidal zone at continental scale. *Estuarine, Coastal and Shelf Science*, 223, 115-128. Available: [https://doi.org/10.1016/j.ecss.2019.03.006](https://doi.org/10.1016/j.ecss.2019.03.006)

Bishop-Taylor, R., Sagar, S., Lymburner, L., Alam, I., & Sixsmith, J. (2019b). Sub-pixel waterline extraction: Characterising accuracy and sensitivity to indices and spectra. *Remote Sensing*, 11(24), 2984. Available: [https://doi.org/10.3390/rs11242984](https://doi.org/10.3390/rs11242984)

DoT, (2018). Capturing the Coastline: Mapping Coastlines in WA over 75 Years. Department of Transport, Western Australia (2018). Available: [https://www.transport.wa.gov.au/mediaFiles/marine/MAC\_P\_CapturingtheCoastline.pdf](https://www.transport.wa.gov.au/mediaFiles/marine/MAC_P_CapturingtheCoastline.pdf)

Griffith Centre for Coastal Management, 2016. Sunshine Coast Beach Profile Database: Description of BPA Historical Database and Recommendations for Ongoing Monitoring Programs (No. 188), Griffith Centre for Coastal Management Research Report. 

Harrison, A.J., Miller, B.M., Carley, J.T., Turner, I.L., Clout, R., Coates, B., 2017. NSW beach photogrammetry: A new online database and toolbox. Australasian Coasts & Ports 2017: Working with Nature 565.

Lyard, F.H., Allain, D.J., Cancet, M., Carrère, L. and Picot, N., 2021. FES2014 global ocean tide atlas: design and performance. Ocean Science, 17(3), pp.615-649.

Pucino, N., Kennedy, D.M., Carvalho, R.C., Allan, B., Ierodiaconou, D., 2021. Citizen science for monitoring seasonal-scale beach erosion and behaviour with aerial drones. Scientific Reports 11, 3935. https://doi.org/10.1038/s41598-021-83477-6 

Sagar, S., Roberts, D., Bala, B., & Lymburner, L. (2017). Extracting the intertidal extent and topography of the Australian coastline from a 28 year time series of Landsat observations. *Remote Sensing of Environment*, 195, 153-169. Available: [https://doi.org/10.1016/j.rse.2017.04.009](https://doi.org/10.1016/j.rse.2017.04.009)

Seifi, F., Deng, X. and Baltazar Andersen, O., 2019. Assessment of the accuracy of recent empirical and assimilated tidal models for the Great Barrier Reef, Australia, using satellite and coastal data. Remote Sensing, 11(10), p.1211.

Short, A.D., Bracs, M.A., Turner, I.L., 2014. Beach oscillation and rotation: local and regional response at three beaches in southeast Australia. Journal of Coastal Research 712–717. https://doi.org/10.2112/SI-120.1 

South Australian Coast Protection Board, 2000. Monitoring Sand Movements along the Adelaide Coastline. Department for Environment and Heritage, South Australia. 

Strauss, D., Murray, T., Harry, M., Todd, D., 2017. Coastal data collection and profile surveys on the Gold Coast: 50 years on. Australasian Coasts & Ports 2017: Working with Nature 1030. 

TASMARC, 2021. TASMARC (The Tasmanian Shoreline Monitoring and Archiving Project) (2019) TASMARC database. Available: h[ttp://www.tasmarc.info/](http://www.tasmarc.info/)

Turner, I. L., Harley, M. D., Short, A. D., Simmons, J. A., Bracs, M. A., Phillips, M. S., & Splinter, K. D. (2016). A multi-decade dataset of monthly beach profile surveys and inshore wave forcing at Narrabeen, Australia. *Scientific data*, *3*(1), 1-13. Available: [http://narrabeen.wrl.unsw.edu.au/](http://narrabeen.wrl.unsw.edu.au/)

