## Background

This product has been deprecated and is superseded by this product:  [DEA Surface Reflectance (Landsat 5 TM)](https://cmi.ga.gov.au/data-products/dea/358/dea-surface-reflectance-landsat-5-tm)

The light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.

## What this product offers

This Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Landsat archive since 1987. This is undertaken to allow comparison of imagery acquired at different times, by different sensors, in different seasons and in different geographic locations. These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways.

The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

% ## Data description

## Applications

This product eliminates pre-processing requirements for a wide range of land and coastal monitoring applications and renders more accurate results from analyses, particularly those utilising time series data.

Such applications include various forms of change detection, including:

* monitoring of urban growth, coastal habitats, mining activities, and agricultural production
* compliance surveys
* scientific research emergency management

## Technical information

Surface Reflectance (SR) is a suite of Earth Observation (EO) products from GA. The SR product suite provides standardised optical surface reflectance datasets using robust physical models to correct for variations in image radiance values due to atmospheric properties, and sun and sensor geometry. The resulting stack of surface reflectance grids are consistent over space and time which is instrumental in identifying and quantifying environmental change. SR is based on radiance data from the Landsat TM/ETM+ and OLI sensors. 

The standardised SR data products deliver calibrated optical surface reflectance data across land and coastal fringes. SR is a medium resolution (~25 m) grid based on the Landsat TM/ETM+/OLI archive and presents surface reflectance data in 25 m² grid cells.

Radiance measurements from EO sensors do not directly quantify the surface reflectance of the Earth. Such measurements are modified by variations in atmospheric properties, sun position, sensor view angle, surface slope and surface aspect. To obtain consistent and comparable measures of Earth surface reflectance from EO, these variations need to be reduced or removed from the radiance measurements (Li et al., 2010). This is especially important when comparing imagery acquired in different seasons and geographic regions.

The SR product is created using a physics-based, coupled BRDF and atmospheric correction model that can be applied to both flat and inclined surfaces (Li et al., 2012). The resulting surface reflectance values are comparable both within individual images and between images acquired at different times and/or with different sensors.

This product does not include terrain illumination reflectance correction (see Surface Reflectance NBART 2 (Landsat)).

## Lineage

#### Landsat archive

GA has acquired Landsat imagery over Australia since 1979, including TM, ETM+ and OLI imagery. While this data has been used extensively for numerous land and coastal mapping studies, its utility for accurate monitoring of environmental resources has been limited by the processing methods that have been traditionally used to correct for inherent geometric and radiometric distortions in EO imagery. To improve access to Australia’s archive of Landsat TM/ETM+/OLI data, several collaborative projects have been undertaken in conjunction with industry, government and academic partners. These projects have enabled implementation of a more integrated approach to image data correction that incorporates normalising models to account for atmospheric effects, BRDF and topographic shading (Li et al., 2012). The approach has been applied to Landsat TM/ETM+ and OLI imagery to create the SR products. The advanced supercomputing facilities provided by the National Computational Infrastructure (NCI) at the Australian National University (ANU) have been instrumental in handling the considerable data volumes and processing complexities involved with production of this product.

#### Surface Reflectance correction models

Image radiance values recorded by passive EO sensors are a composite of:  
• surface reflectance;  
• atmospheric condition;  
• interaction between surface land cover, solar radiation and sensor view angle; and  
• land surface orientation relative to the imaging sensor.  
It has been traditionally assumed that Landsat imagery display negligible variation in sun and sensor view angles, however these can vary significantly both within and between scenes, especially in different seasons and geographic regions (Li et al., 2012). The SR product delivers modeled surface reflectance from Landsat TM/ETM+/OLI/ data using physical rather than empirical models. Accordingly, this product will ensure that reflective value differences between imagery acquired at different times by different sensors will be primarily due to on-ground changes in biophysical parameters rather than artifacts of the imaging environment.

#### Integrated time series data

Once consistent and comparable measures of surface reflectance have been retrieved from EO data, it is possible to quantify changes in Earth surface features through time.  
Given the growing time series of EO imagery, this landmark facility will streamline the process of reliably monitoring long-term changes in land and water resources.

## Processing steps

1. Extract metadata from data sources

1. Calculate sun and sensor angles per pixel (Vincenty, 1975; Edberg and Oliver, 2013)

1. Determine values for six base atmospheric parameters across each image scene

1. Derive normalised surface reflectance for sun angle of 45°

1. Ortho-processing using DSM

% ## Software

## References

Li, F., Jupp, D. L. B., Reddy, S., Lymburner, L., Mueller, N., Tan, P., & Islam, A. (2010). An evaluation of the use of atmospheric and brdf correction to standardize landsat data. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, *3*(3), 257–270. [https://doi.org/10.1109/JSTARS.2010.2042281](https://doi.org/10.1109/JSTARS.2010.2042281)

Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. Remote Sensing of Environment, 124, 756–770. [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

