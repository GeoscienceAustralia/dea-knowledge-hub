## Accuracy

The accuracy of the tide height data is limited by the accuracy of the OTPS model. Tidal modelling on self-similar coastal polygons was performed to minimise regional uncertainty.

Accuracies and limitations related to geomedian compositing of observations are discussed in Roberts et al (2017).

Users should beware of seasonal and diurnal effects in the imagery, especially in the north east of Australia where the footprint of the highest and lowest astronomical tides are large. Consequently, where image acquisition misses the highest astronomical tide, for example, pooling effects of water are still visible in the landscape in lowest observed tidal composite imagery.

This product has been rendered in both true colour and false colour. Validation and interpretation of surface features has not been attempted here. Interpretation of surface features is at the users own discretion.

## Quality assurance

E-cognition was used to distribute the Australian coastline into 306 self similar polygons in terms of tidal characteristics, from which OTPS tidal modelling of the centroid was used to tide tag all Landsat observations occurring within that polygon. This process was identical to that used in the generation of ITEM v 2.0.0

A geomedian compositing process (Roberts et al., 2017) was used to ensure a valid surface reflectance spectra was generated for nominated subsets of the observed tidal range.

Climate based testing was undertaken to determine the best percentage of high and low tide tagged observations to include into a continental composite image. Seventeen Koppen climate zones (Rubel and Kottek, 2010) across Australia were tested to account for variability in features including cloud cover and glint. Seasonal signatures were identified in some northern parts of Australia due to the sun synchronous nature of Landsat image acquisition. Southern parts of the Australian coastline, including western Tasmania, Victoria and south Western Australia, were affected by low sun-angle and consequently, produce darker composites compared to the north. Considering this, the highest and lowest 20 % of observed tides were selected as the values to best represent the end-members of the Australian inter-tidal zone.

To minimise the smoothing of coastal features due to large data sets, the time range for inclusion of observations into the composite products was likewise minimised. Typically, the optimal time-range for a polygon composite ranged from 2000 to 2017. In polygons with a high count of valid observations, the time-range was reduced to 2010 to 2017. Where the polygon had a low count of valid observations, the time range was extended to 1995 - 2017. The decision to lengthen or shorten the time range for data inclusion in a polygon was made by visual observation of the quality of the geomedian composite and reference to the pixel count of valid observations for each polygon. Images affected by cloud, cloud shadow or an absence of data were associated with low or zero pixel counts. In these situations, the time range was extended. Where pixel counts indicated a high number of valid observations, the time range was lowered. Typically, this occurred in areas including north west Western Australia.

