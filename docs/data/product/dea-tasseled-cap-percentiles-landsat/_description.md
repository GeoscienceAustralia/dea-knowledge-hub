The DEA Tasseled Cap Percentiles product provides an annual summary of environmental conditions across the Australian landscape using Tasseled Cap indices, a method that transforms raw reflectance data into three components:

 - Brightness: Indicates the overall reflectivity of the land surface, often highlighting bare soil, urban areas or dry conditions.
 - Greenness: Reflects the presence and vigor of photosynthetic vegetation.
 - Wetness: Captures moisture content in soil and vegetation, helping to identify waterlogged or saturated areas.

To capture how these conditions vary throughout the year, the product includes percentile values for each tasseled cap index:

- The 10th percentile represents conditions that are lower than 90% of observations—typically the driest, least green, or least reflective states recorded during the year.
- The 50th percentile (or median) represents the middle value—a typical or average condition, where half the observations are higher and half are lower.
- The 90th percentile represents conditions that are higher than 90% of observations—typically the greenest, wettest, or brightest states observed.


These percentile summaries are useful for identifying and monitoring environmental features such as wetlands, groundwater-dependent ecosystems, salt lakes, clay pans, and coastal landforms. They are designed to support environmental classification, change detection, and long-term landscape monitoring.

## Background

The Tasseled Cap transformation (Kauth–Thomas) is a method used to simplify satellite imagery by converting raw spectral data into three key indices:

- Brightness – representing surface reflectance, often associated with bare soil or built environments.
- Greenness – indicating the presence and health of vegetation.
- Wetness – capturing moisture content in soil and vegetation.

These indices help describe the composition of the landscape in terms of vegetation, water, and bare ground. The transformation is particularly useful in complex environments where these features coexist—such as wetlands, floodplains, and coastal zones.

## What this product offers

This product provides annual summaries of the Tasseled Cap indices using percentile statistics. For each calendar year from 1987 to the most recent full year, the following are available:

- Three indices: Brightness, Greenness, and Wetness
- Three percentiles per index:
    - 10th percentile – representing lower-end conditions (e.g. driest, least green, or least reflective)
    - 50th percentile – the median or typical condition
    - 90th percentile – representing upper-end conditions (e.g. wettest, greenest, or most reflective)

These percentiles are calculated for every 30m x 30m pixel across Australia, using all available Landsat observations for the year. The product includes cloud and shadow masking, with a 6-pixel buffer applied to reduce contamination from atmospheric interference. It incorporates data from Landsat 5, 7, 8, and Landsat 9 (from 2022 onward).


## Data description

To generate the percentile layers, all valid satellite observations for a given year are processed to compute the Tasseled Cap indices (brightness, greenness, wetness). For each pixel, the distribution of values across the year is used to calculate the 10th, 50th, and 90th percentiles. 

These percentiles provide a robust summary of environmental variability, avoiding the sensitivity to outliers that can affect minimum, maximum, or mean values—especially in the presence of undetected cloud or shadow.

This approach enables users to assess the range and typical conditions of the landscape over time, supporting both temporal analysis and spatial comparison.


## Applications

The Tasseled Cap Percentiles are useful for:

- Wetland identification and monitoring
- Characterisation of salt lakes and salt flats
- Supporting classification of groundwater-dependant ecosystems
- Mapping coastal and estuarine land covers and environments


## Technical information

The Tasseled Cap (Kauth&ndash;Thomas) transform translates the six spectral bands of Landsat into a three indexes describing greenness, wetness and brightness.  These indexes can be used to help understand complex ecosystems, such as wetlands or groundwater dependent ecosystems. The Tasseled Cap Percentiles capture how the greenness, wetness and brightness of the landscape behaves over time. 

The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing these indexes, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause erroneous results.

The 10th, 50th and 90th percentiles of the Tasseled Cap are intended to capture the extreme (10th and 90th percentile) values and long-term average (50th percentile) values of each index.  Percentiles are used in preference to minimum, maximum and mean, as the min/max/mean statistical measures are more sensitive to undetected cloud/cloud shadow, and can be misleading for non-normally distributed data.

The Tasseled Cap Percentiles are intended to complement the DEA Water Observations (Water Observations from Space) and Fractional Cover algorithms. DEA WO is designed to discriminate open water, but the Tasseled Cap wetness index identifies areas of water and areas where water and vegetation are mixed together; i.e. mangroves and palustrine wetlands. Similarly Fractional Cover describes proportions of green, brown and bare areas in the landscape, and hence the Fractional Cover percentiles can be used in complement to the Tasseled Cap percentiles.

However if you are interested in terrestrial vegetation (where water in the pixel is not a factor), use the Fractional Cover product in preference to the Tasseled Cap, which provides a better biophysical characterisation of green vegetation fraction, dry vegetation fraction and bare soil vegetation fraction.

We used the Tasseled Cap transforms described in Crist et al. (1985).

## Lineage

The lineage of this product is inherited from its sole input, the terrain corrected surface reflectance product [Surface Reflectance NBART Collection 3 (Landsat)](https://knowledge.dea.ga.gov.au/data/category/dea-surface-reflectance/).

% ## Processing steps

% ## Software

## References

Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. *Remote Sensing of Environment*, *17*(3), 301–306. [https://doi.org/10.1016/0034-4257(85)90102-6](https://doi.org/10.1016/0034-4257(85)90102-6 )

