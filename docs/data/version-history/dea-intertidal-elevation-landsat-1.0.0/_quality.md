## Accuracy

To assess the accuracy of NIDEM, we compared modelled elevations against three independent elevation and bathymetry validation datasets: 
the DEM of Australia derived from LiDAR 5 Metre Grid (Geoscience Australia, 2015), 
elevation data collected from Real Time Kinematic (RTK) GPS surveys (Danaher & Collett, 2006; HydroSurvey Australia, 2009), 
and 1.0 m resolution multibeam bathymetry surveys (Solihuddin et al., 2016). 

We assessed overall accuracy across three distinct intertidal environments: sandy beaches and shores, tidal flats, and rocky shores and reefs

| Intertidal environment   | Number of sites | Pearson's correlation | Spearman's correlation | RMSE +/- |
|--------------------------|-----------------|-----------------------|------------------------|----------|
| Sandy beaches and shores | 5               | 0.92                  | 0.93                   | 0.41 m   |
| Tidal flats              | 9               | 0.78                  | 0.81                   | 0.39 m   |
| Rocky shores and reefs   | 7               | 0.46                  | 0.79                   | 2.98 m   |

## Limitations

NIDEM covers the exposed intertidal zone which includes sandy beaches and shores, tidal flats and rocky shores and reefs. The model excludes intertidal vegetation communities such as mangroves.

Areas with comparatively steep coastlines and small tidal ranges are poorly captured in the 25 m spatial resolution input Landsat data and resulting NIDEM model. This includes much of the south eastern and southern Australian coast (e.g. New South Wales, Victoria, Tasmania).

Poor validation results for rocky shore and reef sites within the southern Kimberly region highlighted limitations in the NIDEM model that occur when the global OTPS TPX08 Atlas Tidal Model was unable to predict complex and asynchronous local tidal patterns. This is likely to also reduce model accuracy in complex estuaries and coastal wetlands where river flow or vegetative resistance causes hydrodynamic attenuation in tidal flow.

The complex temporal behaviour of tides mean that a sun synchronous sensor like Landsat does not observe the full range of the tidal cycle at all locations. This causes spatial bias in the proportion of the tidal range observed in different regions, which can prevent NIDEM from providing elevation data for areas of the intertidal zone exposed or inundated at the extremes of the tidal range. Accordingly, NIDEM provides elevation data for the portion of the tidal range observed by Landsat, rather than the full tidal range.

While image compositing and masking methods have been applied to remove the majority of noise and non-tidal artefacts from NIDEM, issues remain in several locations. It is recommended that the data be used with caution in the following areas: 
* The Recherche Archipelago in southern Western Australia
* Port Phillip Bay in Victoria
* The eastern coast of Tasmania and King Island
* Saunders Reef and surrounds in the northern Coral Sea