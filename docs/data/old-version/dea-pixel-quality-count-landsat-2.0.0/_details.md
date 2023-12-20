## Background

This product has been deprecated and is superseded by these products:

* [DEA Surface Reflectance OA (Landsat 5 TM)](/data/product/dea-surface-reflectance-oa-landsat-5-tm/)
* [DEA Surface Reflectance OA (Landsat 7 ETM+)](/data/product/dea-surface-reflectance-oa-landsat-7-etm/)
* [DEA Surface Reflectance OA (Landsat 8 OLI-TIRS)](/data/product/dea-surface-reflectance-oa-landsat-8-oli-tirs/)

We need to be able to exclude cloud and cloud shadow affected observations from analyses of optical Earth observation data.

Historically this has been done via the user selecting 'cloud free' images as input for their analysis. However, manual selection of cloud free scenes is neither timely nor practical for large scale automated analysis at continental or 'whole of archive' scale. This necessitates the use of per pixel information about whether the observation is 'clear'; i.e. free of cloud, cloud shadow and sensor saturation, and contains information for all bands.

## What this product offers

This product is a count of how many times a pixel contains a clear observation of the earth's surface (land or sea) at a particular location for a particular period of time.

It is available for the following epochs:

:::{list-table}

* - **PQ-COUNT-SUMMARY**
  - Contains a count of all observations contained within the DEA (from 1987 to the most up to date imagery available).
* - **PQ-COUNT-ANNUAL-SUMMARY**
  - Contains a count of the number of observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
* - **PQ-COUNT-SEASONAL-SUMMARY**
  - Contains a count of the number of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons.
:::

% ## Data description

## Applications

This product is designed to provide users of the DEA data cube with information about the number of observations available at a particular location/epoch.

This information can also be used to normalise observation counts of particular phenomena (e.g. what percentage of time a pixel meets a particular criterion during a given year).

## Technical information

As Landsat Imagery becomes more readily available, there has been a rapid increase in the amount of analyses undertaken by researchers around the globe.

Most researchers use some form of quality masking schema in order to remove undesirable pixels from analysis, whether that be cloud, cloud shadow, observations over the ocean, or saturated pixels.

In the past, researchers would reject partly cloud-affected scenes in favour of cloud-free scenes. However, Landsat time series analysis using all cloud-free pixels has become a valuable technique and has increased the demand for automation of cloud, cloud shadow and saturation detection. This information can be captured from the Landsat Product Generation System (LPGS) and through the application of well recognised cloud/cloud shadow screening algorithms, such as the automated cloud cover assessment (ACCA) and function of mask (Fmask) algorithms.

This information is captured per image via the Pixel Quality 2 (Landsat) product, and summarised with respect to time via this Pixel Quality Count 2 (Landsat) product.

The observation density of the Landsat archive is impacted by a range of factors including mission factors (cloud avoidance, scan line corrector errors, sensor saturation, number of sensors in operation at a particular point in time and the long term acquisition plan).

The number of 'clear' surface observations is further impacted by biophysical factors (cloud, cloud shadow). For users performing multi-temporal analysis such as time series analysis, best available pixel compositing or multi-temporal statistics, analyses are all constrained by the number of cloud free surface observations available for a particular epoch/location of interest.

### Features

This product is designed to inform users about the number of cloud/cloud shadow free observations of the Earth's surface that are available for their particular location/epoch of interest.

This product shows the influence on observation density of the following:
* the 'side lap' between adjacent paths of Landsat imagery, where the observation density in the 'side lap' is approximately double that for the middle of the path
* the impact of regional cloud patterns - with lower observation densities occurring in the wet tropics and temperate zones
* the impact of errors of omission and commission in the cloud/cloud shadow screening algorithms (where certain surface targets are erroneously flagged as clouds, or where clouds and shadows have not been flagged)
* the impacts of sensor saturation in Landsat 5 TM and Landsat 7 ETM+ (particularly noticeable over coastal sand dunes and salt flats)

This product is available per year and for the entire depth of the Landsat archive. This allows users who are interested in analysis of a particular year to assess how many observations were available that year, and allows users who are conducting 'full depth of archive' analysis to assess how many observations are available as input.

This product will allow users to evaluate how mission factors (such as scan-line corrector-off gaps and sensor saturation) and biophysical factors (such as cloud detection algorithm errors of commission) will affect the number of clear observations available at a particular location.

The darkest blue tones indicate the lowest observation counts, whereas the darkest red tones indicate the highest observation counts.  Roebuck Bay in Western Australia (shown below) falls within the sidelap between adjacent paths, and is therefore observed twice as frequently.  However errors of commission with the cloud masks and sensor saturation over bright targets reduce the number of 'clear' observations over some coastal cover types.  The 'venetian' blinds artefacts exist because the Landsat 7 scan-line-corrector (SLC) errors are not randomly distributed, so there are areas with higher and lower frequency of SLC gaps.

![Clear observation count for Roebuck Bay in Western Australia](/_files/cmi/Observation_density.png)

% ## Lineage

% ## Processing steps

% ## Software

% ## References

