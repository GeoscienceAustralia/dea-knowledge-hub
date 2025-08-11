## Background

Australia’s hot, dry climate and expansive bushland make it one of the most fire-prone regions in the world and hence understanding vegetation dryness is critical for managing bushfire risk.

One key measure used for this purpose is Fuel Moisture Content (FMC) which refers to the amount of water contained in vegetation, expressed as a percentage of its dry weight. FMC plays a vital role in fire management because it indicates how easily vegetation can ignite and sustain fire; lower FMC levels mean drier and more flammable fuel.

## Use constraints

This product is not meant to replace field measurements of fuel moisture. It is intended to be used in conjunction with that information and interpreted by people with expert knowledge.

## What this product offers

The DEA Fuel Moisture Content (FMC) product is a remotely sensed proxy for the moisture content of vegetation. It estimates the percentage of water mass relative to dry mass in living vegetation based on its spectral signature. Vegetation moisture is a critical variable for understanding vegetation flammability and fire potential.

Values range from 0 – 300%. A value of 300% would mean there is approximately three times as much water (by weight) as dry plant material. A value of 100% means that water weight to dry plant material is roughly equal. A value of 0% means that there is almost no measured water content.
Values in the range of 0 – 150% are particularly relevant to fire behaviour analysis, as this range is strongly associated with changes in vegetation flammability and the likelihood of ignition.

FMC is derived from Sentinel 2A, 2B, and 2C satellite imagery at a 20 m resolution for all of Australia from 12 July 2015 to the present. This product shows FMC values calculated for each pixel in the corresponding Sentinel-2 scene with masking applied for cloud, cloud shadow, water, and terrain shadow.

## Applications

* Monitoring and mapping the dryness of vegetation across different landscapes.
* Predicting and assessing vegetation flammability and fire risk, including fire spread and intensity.
* Modelling fire risk over time and across different ecosystems with changing climate conditions.
* Prioritising and evaluating fire, forestry, and utility agency management based on the dryness and the assessed fire risk of vegetation.

Please note that this product should not be used to make safety of life decisions.

## Technical information

DEA Fuel Moisture Content (FMC) is a gridded dataset indicating the moisture content of vegetation. This product includes measurements taken between 12 July 2015 and the present (inclusive) from the Sentinel 2A, 2B, and 2C satellites. FMC covers all of mainland Australia and Tasmania but excludes offshore Territories. The dataset is updated automatically as each new Sentinel-2 scene is acquired and processed as Analysis Ready Data (ARD).

The calculation of FMC is done using a random forest machine learning model which is an emulator of the model used in the MODIS-based Australian flammability monitoring system (Yebra et al, 2018). The inputs to the model are the Sentinel 2 bands (blue, green, red, red edge 1, 2, and 3, NIR 1 and 2, and SWIR 2 and 3). In addition, two normalised difference indices are used (NDVI Rouse (1973) and NDVII Hunt and Rock (1989)). All input bands are loaded at 20 x 20 m resolution. The visible light bands that have a resolution of 10 m are resampled using Bilinear sampling. Masking for cloud, cloud shadow, water, and terrain shadow are also applied.

## Lineage

This product is based on the work of Dr. Marta Yebra and the team at the Bushfire Research Centre of Excellence at the Australian National University (ANU). Remotely sensed FMC was developed and delivered as the Australian flammability monitoring system with the support of the former Bushfire and Natural Hazards Cooperative Research Centre (now Natural Hazards Research Australia).

DEA Fuel Moisture Content replaces the MODIS-based Australian flammability monitoring system, improving the spatial resolution from 500 m to 20 m.

## References

Yebra, M., Quan, X., Riaño, D., Rozas Larraondo, P., van Dijk, A. I. J. M., & Cary, G. J., 2018. A fuel moisture content and flammability monitoring methodology for continental Australia based on optical remote sensing. Remote Sensing of Environment, 212, 260–272. https://doi.org/10.1016/j.rse.2018.04.053

