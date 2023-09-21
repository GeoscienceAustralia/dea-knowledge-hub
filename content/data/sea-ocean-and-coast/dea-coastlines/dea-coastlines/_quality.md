## Accuracy

## Quality Assurance

### Quality assurance

To allow problematic data to be accounted for or excluded from future analyses, DEA Coastlines data is automatically screened for several potential data quality issues. These issues are flagged in the "certainty" field and symbolised by dashed lines or white points on the [interactive DEA Coastlines map](https://maps.dea.ga.gov.au/story/DEACoastlines). These flags include:

##### Annual shorelines

-   *aerosol issues:* The accuracy of this shoreline may be affected by aerosol issues caused by the 1991 eruption of Mount Pinatubo.
-   *insufficient data:* The accuracy of this shoreline may be affected by limited good quality satellite observations at this location. This can lead to noisier and less reliable shorelines.
-   *unstable data:*The accuracy of this shoreline is affected by unstable data at this location. This may be caused by errors in the tidal model used to reduce the influence of tide, the presence of gently sloping intertidal mudflats or sandbars that can lead to inaccurate shoreline mapping, or noisy satellite imagery caused by high levels of cloud.

##### Rates of change points

-   *insufficient observations:* There are insufficient years of good quality annual shoreline data (< 25 years) to calculate reliable rates of coastal change at this location.
-   *likely rocky shoreline:* This coastline has been identified as a probable rocky or cliff shoreline. Rates of coastal change at this location may be less accurate due to noisy shoreline mapping caused by dark terrain shadows.
-   *extreme value (> 50 m):* This location has been identified as having an extreme rate of coastal change (> 50 metres per year) and should be interpreted with caution.
-   *high angular variability:* This rate of coastal change is unlikely to be accurate due to high levels of angular variability from this point to each annual shoreline. This can occur in complex coastal environments like river mouths, sandbars and mudflats that do not show linear patterns of coastal change over time.
-   *baseline outlier:* The baseline (i.e. most recent) annual shoreline is itself flagged as an outlier, potentially resulting in inaccurate rates of change at this location.

##### Coastal change hotspots

-   *insufficient points: *There are too few valid rates of change points in the 1 km/5 km/10 km radius around this location to calculate a reliable regional rate of change.

For more information, refer to **Caveats and limitations** above.

#### Caveats and limitations

##### Annual shorelines

-   Annual shorelines from DEA Coastlines summarise the median (i.e. "dominant") position of the shoreline throughout the entire year, corrected to a consistent tide height (0 m AMSL). Annual shorelines will therefore not reflect shorter-term coastal variability, for example changes in shoreline position between low and high tide, seasonal effects, or short-lived influences of individual storms. This means that these annual shorelines will show lower variability than the true range of coastal variability observed along the Australian coastline.

##### Rates of change points

-   Rates of change points do not assign a reason for change, and do not necessarily represent processes of coastal erosion or sea level rise. In locations undergoing rapid coastal development, the construction of new inlets or marinas may be represented as hotspots of coastline retreat, while the construction of ports or piers may be represented as hotspots of coastline growth. Rates of change points should therefore be evaluated with reference to the underlying annual coastlines and external data sources or imagery.
-   Rates of change points may be inaccurate or invalid within complex mouthbars, or other coastal environments undergoing rapid non-linear change through time. In these regions, it is advisable to visually assess the underlying annual shoreline data when interpreting rates of change to ensure these values are fit-for-purpose. Regions significantly affected by this issue include:
    -   Cambridge Gulf, Western Australia
    -   Joseph Bonaparte Gulf, Western Australia/Northern Territory

##### Data quality issues

-   Annual shorelines may be less accurate in regions with complex tidal dynamics or large tidal ranges, and low-lying intertidal flats where small tidal modelling errors can lead to large horizontal offsets in coastline positions (Figure 6). Annual shoreline accuracy in intertidal environments may also be reduced by the influence of wet muddy substrate or intertidal vegetation, which can make it difficult to extract a single unambiguous coastline (Bishop-Taylor et al. 2019a, 2019b, 2021). It is anticipated that future versions of this product will show improved results due to integrating more advanced methods for waterline detection in intertidal regions, and through improvements in tidal modelling methods. Regions significantly affected by intertidal issues include:
    -   The Pilbara coast, Western Australia from Onslow to Pardoo
    -   The Mackay region, Queensland from Proserpine to Broad Sound
    -   The upper Spencer Gulf, South Australia from Port Broughton to Port Augusta
    -   Western Port Bay, Victoria from Tooradin to Pioneer Bay
    -   Hunter Island Group, Tasmania from Woolnorth to Perkins Island
    -   Moreton Bay, Queensland from Sandstone Bay to Wellington Point
-   Annual shorelines may be noisier and more difficult to interpret in regions with low availability of satellite observations caused by persistent cloud cover. In these regions it can be difficult to obtain the minimum number of clear satellite observations required to generate clean, noise-free annual shorelines. Affected regions include:
    -   South-western Tasmania from Macquarie Heads to Southport
-   In some urban locations, the spectra of bright white buildings located near the coastline may be inadvertently confused with water, causing a land-ward offset from true shoreline positions. 
-   Some areas of extremely dark and persistent shadows (e.g. steep coastal cliffs across southern Australia) may be inadvertently mapped as water, resulting in a landward offset from true shoreline positions. 
-   1991 and 1992 shorelines are currently affected by aerosol-related issues caused by the 1991 Mount Pinatubo eruption. These shorelines should be interpreted with care, particularly across northern Australia. 

##### Validation approach

-   To compare annual shorelines to validation datasets, multiple validation observations in a year were combined into a single median measurement of coastline position. In the case where only a single validation observation was taken for a year, this single observation may not be reflective of typical shoreline conditions across the entire year period. Because of this, validation results are expected to be more reliable for validation datasets with multiple observations per year.
-   The current validation approach was biased towards Australia's south-western, southern and south-eastern coastlines due to the availability of historical coastal monitoring data. This bias prevented us from including more complex intertidal environments in our validation, which is likely to have inflated the accuracy of our results due to issues outlined above.

![Intertidal issues](https://cmi.ga.gov.au/sites/default/files/inline-images/Figure10_intertidal%20%281%29.png)

###### Figure 6: Potentially spurious shorelines in macrotidal coastal regions characterised by gently sloped tidal flat environments: a) Broad Sound and b) Shoalwater Bay, Queensland. Dashed shorelines indicate data that was flagged as affected by tidal modelling issues based on MNDWI standard deviation. In these locations, the TPXO 8 tidal model was unable to effectively sort satellite observations by tide heights, resulting in output shorelines that did not adequately suppress the influence of the tide.
