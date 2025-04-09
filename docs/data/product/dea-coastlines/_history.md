## Changelog

### 2024 DEA Coastlines update

In April 2025, the DEA Coastlines product [was updated to version 3.0.0](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/3.0.0). The major improvement in this release is the application of new [Ensemble Tidal Modelling](https://knowledge.dea.ga.gov.au/data/product/dea-coastlines/?tab=description#ensemble-tidal-modelling) to the calculation of all shorelines from 1988 to 2024.

### 2023 DEA Coastlines update

In August 2024, the DEA Coastlines product [was updated to version 2.2.0](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/2.2.0). This update adds additional interim annual shoreline data for 2023. The 2023 shoreline is subject to change, and will be updated to a final version in the following DEA Coastlines update (March 2025). 

**Improvements and additions:** 
* This update adds new functionality to easily switch between annual shorelines and rates of change on DEA Maps using a "Style" selector. 

### 2022 DEA Coastlines update

In August 2023, the DEA Coastlines product [was updated to version 2.1.0](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/2.1.0). This update consists of the addition of interim annual shoreline data for 2022. The 2022 shoreline is interim data that is subject to change, and will be updated to a final version in the following 2023 DEA Coastlines update (in August 2024).

### 2021 DEA Coastlines update

In March 2023, the DEA Coastlines product [was updated to version 2.0.0](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/2.0.0). This includes the following key changes to the data and web services: 

**Improvements and additions:** 
* Added annual shoreline data for 2021. The 2021 shoreline is interim data that is subject to change, and will be updated to a final version in the following 2022 DEA Coastlines update (in July 2023).
* Improved data coverage over offshore islands and reefs. This includes new shorelines and rates of coastal change over the Indian Ocean, Great Barrier Reef and Coral Sea.
* DEA Coastlines now uses data from the FES2014 global tidal model. This model produces accurate tide modelling across Australia ([Seifi et al. 2019](https://www.mdpi.com/2072-4292/11/10/1211)) and globally ([Lyard et al. 2021](https://os.copernicus.org/articles/17/615/2021)) and is more flexible and easier to install than the older TPXO8 tidal model.
* Inclusion of Landsat 9 data to provide additional satellite data from late 2021 onwards.
* Improved shoreline mapping certainty attributes to provide information about the quality of each individual annual shoreline (compared to the previous approach of identifying all annual shorelines in an area as low or good quality; see **Quality assurance** below for more detail).
* New rates of change points certainty attributes to provide information about the quality of each point (see **Quality assurance** below for more detail).
* Three coastal change hotspot layers are now included in the product, summarising coastal change within 1 km, 5 km and 10 km windows around each hotspot point. These layers now include attributes providing the median position of all annual shorelines around each hotspot point, which can be used to plot and identify regional trends of coastal change.
* Rates of change points now contain a new "uid" ID field containing a unique [geohash](https://en.wikipedia.org/wiki/Geohash) ID that can be used to more easily track rates of change points as they are updated in future DEA Coastlines updates.
* Rates of change points include a new "id\_primary" field containing the ID of their Primary sediment compartment from the [Australian Coastal Sediment Compartments](https://ecat.ga.gov.au/geonetwork/srv/api/records/21a23d9a-00dd-ab19-e053-10a3070a2746) framework. This enables points to be easily queried and summarised by coastal sediment compartment.

**Backwards incompatible changes:**
* The annual shorelines WFS layer "dea:coastlines" has been renamed to "dea:annual\_shorelines".
* The rates of change points WFS layer "dea:coastlines\_statistics" has been renamed to "dea:rates\_of\_change".

### Previous updates

For a full summary of changes made in previous versions, [refer to GitHub](https://github.com/GeoscienceAustralia/dea-coastlines/releases/tag/v1.1.0). 
