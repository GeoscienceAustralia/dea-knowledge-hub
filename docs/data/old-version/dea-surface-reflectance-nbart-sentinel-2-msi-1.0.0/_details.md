## Background

The light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.

## What this product offers

This product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, in different seasons and in different geographic locations.

These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

% ## Data description

## Applications

This product eliminates pre-processing requirements for a wide range of land and coastal monitoring applications and renders more accurate results from analyses, particularly those utilising time series data.

Such applications include various forms of change detection, including:

* monitoring of urban growth, coastal habitats, mining activities, and agricultural production
* compliance surveys
* scientific research emergency management

## Technical information

The standardised SR data products deliver calibrated optical surface reflectance data across land and coastal fringes. SR is a medium resolution (10/20/60 m) grid based on the Sentinel 2 MSI archive and presents surface reflectance data in 10, 20 and 60m pixels.

Radiance measurements from EO sensors do not directly quantify the surface reflectance of the Earth. Such measurements are modified by variations in atmospheric properties, sun position, sensor view angle, surface slope and surface aspect. To obtain consistent and comparable measures of Earth surface reflectance from EO, these variations need to be reduced or removed from the radiance measurements (Li et al., 2010). This is especially important when comparing imagery acquired in different seasons and geographic regions.

The SR product is created using a physics-based, coupled Bidirectional Reflectance Distribution Function (BRDF) and atmospheric correction model that can be applied to both flat and inclined surfaces (Li et al., 2012). The resulting surface reflectance values are comparable both within individual images and between images acquired at different times and/or with different sensors.

No data values and pixels that were determined as not view-able in NBART products are expressed as -999.

% ## Lineage

## Processing steps

1. Extract metadata from data sources

1. Calculate sun and sensor angles per pixel (Vincenty, 1975; Edberg and Oliver, 2013)

1. Determine values for six base atmospheric parameters across each image scene

1. Derive normalised surface reflectance for sun angle of 45°

% ## Software

## References

Li, F., Jupp, D. L. B., Reddy, S., Lymburner, L., Mueller, N., Tan, P., & Islam, A. (2010). An evaluation of the use of atmospheric and brdf correction to standardize landsat data. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, *3*(3), 257–270. [https://doi.org/10.1109/JSTARS.2010.2042281](https://doi.org/10.1109/JSTARS.2010.2042281)

Li, F., Jupp, D. L. B., Thankappan, M., Lymburner, L., Mueller, N., Lewis, A., & Held, A. (2012). A physics-based atmospheric and BRDF correction for Landsat data over mountainous terrain. Remote Sensing of Environment, 124, 756–770. [https://doi.org/10.1016/j.rse.2012.06.018](https://doi.org/10.1016/j.rse.2012.06.018)

