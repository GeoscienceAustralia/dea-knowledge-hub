## Background

This product has been deprecated and is superseded by this product: [DEA Geometric Median and Median Absolute Deviation (Landsat)](https://cmi.ga.gov.au/data-products/dea/645/dea-geometric-median-and-median-absolute-deviation-landsat).

It is important to see how dynamic or variable the Australian landscape is over any given year, especially to help with understanding how the landscape changes, or to discriminate parts of the landscape that stay the same throughout the year (like forests) from those areas that go through big changes in cover (such as cropping areas).

By understanding different patterns of variation, we can characterise various types of land cover and land use, and detect changes of significance in the landscape.

## What this product offers

This product provides tools to exploit the time series of Earth Observation data available in Digital Earth Australia.

It uses a Triple Median Absolute Deviation (TMAD), which provides three 'second order' high dimensional statistic composites per time period, which measure how much an area varies from the average in terms of 'distance' based on factors such as brightness and spectra:

* Euclidean distance (EMAD)
* Cosine (spectral) distance (SMAD)
* Bray Curtis dissimilarity (BCMAD)

Together, they provide information on variance in the source data and are useful for change detection applications.

% ## Data description

## Applications

This product gives information about:

* variance and change, so it can be used in machine learning for change detection
 
* land cover mapping
 
* environmental monitoring

## Technical information

The 'first order' statistics include the mean and the median.

The 'second order' statistics produced here are the equivalent statistic to the standard deviation for medians, being the Median Absolute Deviation (MAD).

This product is designed to provide measures of variance of the time series from which it is calculated. As such, it provides measures of change in the landscape over the time period of the input data. The various distance measures used in the TMAD provide information on variance in the following ways:

* Euclidean distance (EMAD) is more sensitive to changes in target brightness.
* Cosine (spectral) distance (SMAD) is more sensitive to change in target spectral response.
* Bray Curtis dissimilarity (BCMAD) is more sensitive to the distribution of the observation values through time.

Each MAD provides information on different land cover change features and is useful in classification.

The mathematical derivation of the three MADs can be found in Roberts et al (2018).

## Lineage

The three layers of the TMAD are calculated by computing the multidimensional distance between each observation in a time series of multispectral (or higher dimensionality such as hyperspectral) satellite imagery with the multidimensional median of the time series. The median used for this calculation is the geometric median corresponding to the time series. 

The TMAD is calculated over annual time periods on Earth observations from a single sensor by default (such as the annual time series of Landsat 8 observations); however, it is applicable to multi-sensor time series of any length that computing resources can support.

For the purposes of the default Digital Earth Australia product, TMADs are computed per calendar year, per sensor (Landsat 5, Landsat 7 and Landsat 8) from terrain-illumination-corrected surface reflectance data (Analysis Ready Data), compared to the annual geometric median of that data.

## Processing steps

1. Surface Reflectance Calculation (NBAR + Terrain Illumination Correction)

1. Geometric Median

1. Median Absolute Deviation

% ## Software

## References

Roberts, D., Dunn, B., & Mueller, N. (2018). Open data cube products using high-dimensional statistics of time series. *IGARSS 2018 - 2018 IEEE International Geoscience and Remote Sensing Symposium*, 8647–8650. [https://doi.org/10.1109/IGARSS.2018.8518312](https://doi.org/10.1109/IGARSS.2018.8518312)

