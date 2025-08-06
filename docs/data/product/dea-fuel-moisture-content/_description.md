## Background

Australia’s hot, dry climate and expansive bushland make it one of the most fire-prone regions in the world, where understanding vegetation dryness is critical for managing bushfire risk. 
One key measure used in this context is Fuel Moisture Content (FMC), which refers to the amount of water contained in vegetation, expressed as a percentage of its dry weight. FMC plays a vital role in fire management because it indicates how easily vegetation can ignite and sustain fire, as lower FMC levels mean drier, more flammable fuel.

## Use constraints

This product is not meant to replace field measurements of fuel moisture. It is intended to be used in conjunction with that information and interpreted with expert knowledge by fire managers.

## What this product offers

The Fuel Moisture Content (FMC) product communicates the moisture content of vegetation. It measures the percentage of water mass relative to dry mass in living vegetation. Values range from 0–300%, where 300 would mean there is three times as much water (by weight) than dry plant material. Vegetation moisture is a critical variable for understanding vegetation flammability and fire potential. Values between 0–150% are particularly relevant for fire behaviour analysis, as variations within this range are most strongly associated with changes in vegetation flammability and the likelihood of ignition.

FMC is derived from Sentinel 2A, 2B & 2C satellite imagery at a 20m resolution for all of Australia from 12 July 2015 to present. This product shows FMC values calculated for each pixel in the corresponding Sentinel-2 scene with applied masking cloud, cloud shadow, water and terrain shadow.

## Applications

* Monitoring and mapping the dryness of vegetation across different landscapes
* Predict and assess vegetation flammability and fire risk, spread and intensity
* Modelling fire risk over time and across different ecosystems with changing climate conditions
* Prioritise and evaluate fire, forestry and utility agency management based on the dryness and fire risk of vegetation

Please note that this product should not be used to make safety of life decisions.

## Technical information

Digital Earth Australia (DEA) Fuel Moisture Content (FMC) is a gridded dataset indicating the moisture content of vegetation. The current product (version 1.0.0) includes measurements taken between 12 July 2015 and the present (inclusive) from the Sentinel 2A, 2B & 2C satellites. FMC covers all of mainland Australia and Tasmania but exclude off-shore Territories. The dataset is updated automatically as each new Sentinel-2 scene is acquired and processed to Analysis Ready Data (ARD) state.

The calculation of FMC is done using a random forest machine learning model which is an emulator of the model used in the MODIS-based Australian flammability monitoring system (Yebra et al, 2018). The inputs to the model are the Sentinel 2 bands (blue, green, red, red edge 1, 2 &3, NIR 1 & 2, and SWIR 2 & 3). In addition, two normalised difference indices are used (NDVI Rouse (1973) and NDVII Hunt and Rock (1989)). All input bands are loaded at 20x20 m resolution. The visible light bands that have a resolution of 10m are resampled using Bilinear sampling. Masking for cloud, cloud shadow, water and terrain shadow is also applied.

## Lineage

This product is based on the work of Dr. Marta Yebra and the team at the Bushfire Research Centre of Excellence at ANU. Remotely sensed FMC was developed and delivered as the Australian flammability monitoring system with the support of the former Bushfire and Natural Hazards Cooperative Research Centre (now Natural Hazards Research Australia).

DEA Fuel Moisture Content replaces the MODIS based Australian flammability monitoring system, improving the spatial resolution from 500m to 20m.

## References

Yebra, M., Quan, X., Riaño, D., Rozas Larraondo, P., van Dijk, A. I. J. M., & Cary, G. J., 2018. A fuel moisture content and flammability monitoring methodology for continental Australia based on optical remote sensing. Remote Sensing of Environment, 212, 260–272. https://doi.org/10.1016/j.rse.2018.04.053

