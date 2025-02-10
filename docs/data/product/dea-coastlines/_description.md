## Background

Australia has a highly dynamic coastline of over 30,000 km, with over 85% of its population living within 50 km of the coast. This coastline is subject to a wide range of pressures, including extreme weather and climate, sea level rise and human development. Understanding how the coastline responds to these pressures is crucial to managing this region, from social, environmental and economic perspectives.

## What this product offers

Digital Earth Australia Coastlines is a continental dataset that includes annual shorelines and rates of coastal change along the entire Australian coastline from 1988 to the present. 

The product combines satellite data from Geoscience Australia's Digital Earth Australia program with tidal modelling to map the most representative location of the shoreline at mean sea level for each year. The product enables trends of coastal retreat and growth to be examined annually at both a local and continental scale, and for patterns of coastal change to be mapped historically and updated regularly as data continues to be acquired. This allows current rates of coastal change to be compared with that observed in previous years or decades. 

The ability to map shoreline positions for each year provides valuable insights into whether changes to our coastline are the result of particular events or actions, or a process of more gradual change over time. This information can enable scientists, managers and policy makers to assess impacts from the range of drivers impacting our coastlines and potentially assist planning and forecasting for future scenarios.

% ## Data description

## Applications

* Monitoring and mapping rates of coastal erosion along the Australian coastline 
* Prioritise and evaluate the impacts of local and regional coastal management based on historical coastline change 
* Modelling how coastlines respond to drivers of change, including extreme weather events, sea level rise or human development 
* Supporting geomorphological studies of how and why coastlines have changed across time

## Technical information

This product contains five layers of data.

### Annual shorelines layer (shorelines_annual)

Annual shoreline vectors that represent the median or ‘most representative’ position of the shoreline at approximately 0 m Above Mean Sea Level for each year since 1988 (Figure 1).

Dashed shorelines have low certainty.

Learn more about this layer in the [Specifications tab](./?tab=specifications).

:::{figure} /_files/cmi/deacl_coastlines.*
:alt: DEA CoastLines coastline layer

Figure 1: Annual coastlines from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/story/DEACoastlines)
:::

### Rates of change points layer (rates_of_change)

A point dataset providing robust rates of coastal change for every 30 m along Australia’s non-rocky coastlines (Figure 2). The most recent annual shoreline is used as a baseline for measuring rates of change.

On the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/story/DEACoastlines), points are shown for locations with statistically significant rates of change (p-value &lt;= 0.01; see `sig_time` below) and good quality data (certainty = "good"; see `certainty` below) only. Each point shows annual rates of change (in metres per year; see `rate_time` below), and an estimate of uncertainty in brackets (95% confidence interval; see `se_time`). For example, there is a 95% chance that a point with a label **\-10.0 m (±1.0 m)** is retreating at a rate of between -9.0 and -11.0 metres per year.

Rates of change points contains the following attribute columns that can be accessed by clicking on labelled points in the web map:

Learn more about this layer in the [Specifications tab](./?tab=specifications).

:::{figure} /_files/cmi/deacl_statistics_2.*
:alt: DEA CoastLines rates of change statistics layer

Figure 2: Rates of change points from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/story/DEACoastlines)
:::

### Coastal change hotspots layers (hotspots_zoom_1, hotspots_zoom_2, and hotspots_zoom_3)

Three points layers summarising coastal change within moving 1 km, 5 km and 10 km windows along the coastline (Figure 3). These layers are useful for visualising regional or continental-scale patterns of coastal change. 

Learn more about this layer in the [Specifications tab](./?tab=specifications).

:::{figure} /_files/cmi/deacl_summary.*
:alt: DEA CoastLines summary layer

Figure 3: Coastal change hotspots from DEA Coastlines visualised on the [interactive DEA Coastlines web map](https://maps.dea.ga.gov.au/story/DEACoastlines)
:::

% ## Lineage

## Processing steps

1. Load stack of all available Landsat 5, 7, 8 and 9 satellite imagery for a location using Digital Earth Australia's Open Data Cube instance and virtual products.
2. Convert satellite observations to a remote sensing water index (MNDWI; Xu, 2006) 
3. For each satellite image, model ocean tides into a 5 x 5 km grid based on exact time of image acquisition using the `pixel_tides` function from [`dea_tools`](https://github.com/GeoscienceAustralia/dea-notebooks/blob/develop/Tools/dea_tools/coastal.py)
4. Interpolate tide heights into spatial extent of image stack. 
5. Mask out high and low tide pixels by removing all observations acquired outside of 50 percent of the observed tidal range centered over mean sea level. 
6. Combine tidally-masked data into annual median composites from 1988 to the present representing the coastline at approximately mean sea level. 
7. Apply morphological extraction algorithms to mask annual median composite rasters to a valid coastal region.
8. Extract waterline vectors using subpixel waterline extraction (Bishop et al., 2019). 
9. Compute rates of coastal change at every 30 m along Australia's non-rocky coastlines (extracted using the [Geoscience Australia Smartline product](http://pid.geoscience.gov.au/dataset/ga/104160)), and compute linear regression rates of change and derived statistics.

## Software

The following software was used to generate this product: 
* [DEA Coastlines GitHub code](https://github.com/GeoscienceAustralia/dea-coastlines)
* [Open Data Cube](https://github.com/opendatacube)
* [pyTMD Python-based tidal prediction software](https://github.com/tsutterley/pyTMD)
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

Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. International journal of remote sensing, 27(14), 3025-3033.
