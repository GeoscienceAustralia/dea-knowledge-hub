## Background

The Tasseled Cap transformation (Kauth and Thomas, 1976) is a method used to simplify satellite imagery by converting raw spectral data into three key indices:

- Brightness – representing surface reflectance, often associated with bare soil or built environments.
- Greenness – indicating the presence and health of vegetation.
- Wetness – capturing moisture content in soil and vegetation.

These indices help describe the composition of the landscape in terms of vegetation, water, and bare ground. The transformation is particularly useful in complex environments where these features coexist such as wetlands, floodplains, and coastal zones.

## What this product offers

This product provides annual summaries of the Tasseled Cap indices using percentile statistics. For each calendar year from 1987 to the most recent full year, the following are available:

- Three indices: Brightness, Greenness, and Wetness
- Three percentiles per index:
    - 10th percentile – representing lower-end conditions
    - 50th percentile – the median or typical condition
    - 90th percentile – representing upper-end conditions

Percentiles are calculated for every 30m x 30m pixel across Australia, using all available Landsat observations for the year. The product includes cloud and shadow masking and incorporates data from Landsat 5, 7, 8, and 9.


## Data description

To generate the percentile layers, all valid satellite observations for a given year are processed to compute the Tasseled Cap indices (brightness, greenness, wetness). For each pixel, the distribution of values across the year is used to calculate the 10th, 50th, and 90th percentiles. 

These percentiles provide a robust summary of environmental variability, avoiding the sensitivity to outliers that can affect minimum, maximum, or mean values—especially in the presence of undetected cloud or shadow. This approach enables users to assess the range and typical conditions of the landscape over time, supporting both temporal analysis and spatial comparison.


## Applications

The Tasseled Cap Percentiles are useful for:

- Wetland identification and monitoring
- Characterisation of salt lakes and salt flats
- Supporting classification of groundwater-dependant ecosystems
- Mapping coastal and estuarine land covers and environments


## Technical information

The Tasseled Cap transformation used to generate this product implements the coefficients described by Crist et al. (1985), adapted for Landsat surface reflectance data. The Tasseled Cap Transformation (TCT) is a linear transformation that projects multispectral data into a new coordinate system defined by three components: Brightness, Greenness, and Wetness. 

In other words, the transformation reduces a larger number of spectral bands into three composite indices that are easier to interpret and apply in analyses. These indices are designed to capture the dominant modes avenues spectral variation in terrestrial landscapes:

- Brightness is a weighted sum of all bands and reflects overall surface albedo.
- Greenness contrasts the visible and near-infrared bands to highlight photosynthetically active vegetation.
- Wetness contrasts shortwave infrared bands with visible and near-infrared bands to detect moisture in soil and vegetation.


The transformation coefficients used in this product are based on those developed by Crist et al. (1985) for Landsat Thematic Mapper (TM) data and adapted for subsequent Landsat sensors (ETM+, OLI, and OLI-2) to ensure spectral consistency across the Landsat archive

### Annual summarisation using percentiles

For each calendar year, all valid observations are processed to calculate the Tasseled Cap indices. The 10th, 50th (median), and 90th percentiles are then calculated for each Tasseled Cap index for every 30m x 30m pixel across Australia. 

These percentiles summarise the distribution of index values over the calendar year and characterise the lower-bound, central tendency and upper-bound of the measures of Brightness, Greenness and Wetness.

Percentiles are used instead of minimum, maximum, or mean values because they are less sensitive to outliers and better suited to non-normally distributed data. This makes them more reliable for detecting subtle or seasonal changes in complex environments.


### Interpretation and use

- The 10th percentile typically reflects the driest, least vegetated, or least reflective conditions observed during the year.
- The 50th percentile represents the median state of the landscape, offering a stable reference point for long-term monitoring.
- The 90th percentile captures peak greenness, wetness, or brightness, useful for identifying maximum vegetation productivity or episodic inundation.

These percentile layers are particularly valuable for land cover classification, wetland mapping, coastal zone monitoring, and ecosystem condition assessment, especially in environments where vegetation, water, and bare ground co-occur or fluctuate seasonally.

The percentile-based approach used in this dataset aligns with best practices in time-series analysis of Earth observation data, as seen in related products such as [DEA Geometric Median and Median Absolute Deviation](/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/), [DEA Fractional Cover Percentiles](/data/product/dea-fractional-cover-percentiles-landsat/), and [DEA Water Observations from Space (WOFS)](/data/product/dea-water-observations-statistics-landsat/). Together, these products form a complementary suite of tools for understanding landscape dynamics across Australia.

## Lineage

The Tasseled Cap Percentiles are derived from Landsat surface reflectance data from the [Surface Reflectance NBART Collection 3 (Landsat)](/data/category/dea-surface-reflectance/). This input dataset includes terrain-corrected, analysis-ready data (ARD) from Landsat 5, Landsat 7, Landsat 8, and Landsat 9.

To ensure data quality, all input imagery is masked for cloud and shadow contamination, with a 6-pixel buffer applied around detected cloud and shadow areas. This step reduces the influence of atmospheric interference and improves the reliability of the percentile calculations.

For each calendar year, all valid observations are processed to compute the Tasseled Cap indices using the transformation coefficients described by Crist et al. (1985). These indices are calculated for every 30m x 30m pixel across Australia.

The 10th, 50th, and 90th percentiles are then computed from the full time series of index values for each pixel. These percentiles are statistical summaries, not direct satellite observations. They represent synthetic values that describe the distribution of environmental conditions over the year.

The resulting dataset is a synthetic summary of observed conditions, designed to support environmental monitoring, classification, and change detection across a wide range of Australian ecosystems.


% ## Processing steps

% ## Software

## References

Kauth R. J. & G. S. Thomas (1976). The Tasselled Cap - A Graphic Description of the Spectral-Temporal Development of Agricultural Crops as Seen by LANDSAT. *Proceedings of the Symposium on Machine Processing of Remotely Sensed Data*


Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. *Remote Sensing of Environment*, *17*(3), 301–306. [https://doi.org/10.1016/0034-4257(85)90102-6](https://doi.org/10.1016/0034-4257(85)90102-6 )

