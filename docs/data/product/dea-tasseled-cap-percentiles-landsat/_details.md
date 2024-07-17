## Background

The Tasseled Cap (Kauth&ndash;Thomas) transformation takes satellite imagery and shows the degree of greeness, wetness and brightness across the observed area. These indexes help users understand the combinations of vegetation, water and bare areas respectively. As such the Tasseled Cap is a useful input into environmental analyses, especially where there are mixtures of all three features in the landscape, such as in wetlands.

## What this product offers

This product offers three percentiles per Tasseled Cap index per year. The percentiles are 10th, 50th, and 90th; the Tasseled Cap indexes are 'greeness', 'wetness', and 'brightness'; and the years are 1987 to 2023.

It is useful in broad environmental analyses where it is desirable to understand a mixed landscape including vegetation, water and bare areas, and as such is useful for wetlands analyses.

It includes cloud and shadow buffering with a size of 6 pixels. This buffering is applied to Landsat 5, Landsat 7, Landsat 8, and Landsat 9 data from 2022 onwards.

## Data description

Tasseled Cap percentiles are created by bringing together all individual satellite images for a year and generating the corresponding Tasseled Cap for each, before computing the 10th, 50th and 90th percentiles of their respective data ranges. The percentiles are chosen to represent minimum, middle and maximum (or general) conditions for each index per year, for every 30m x 30m pixel across Australia.

## Applications

This product provides valuable discrimination for characterising:

* Vegetated wetlands
* Salt flats
* Salt lakes
* Coastal land cover classes

## Technical information

The Tasseled Cap (Kauth&ndash;Thomas) transform translates the six spectral bands of Landsat into a three indexes describing greeness, wetness and brightness.  These indexes can be used to help understand complex ecosystems, such as wetlands or groundwater dependent ecosystems. The Tasseled Cap Percentiles capture how the greeness, wetness and brightness of the landscape behaves over time. 

The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing these indexes, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause false positives.

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

