## Background

Areas that are partially covered in water, or where water is mixed with vegetation when viewed from above, provide habitat for a wide range of aquatic organisms.  

The ability to map partial inundation is also crucial to understand patterns of human water use. We need to be able to identify potential wetlands and groundwater dependent ecosystems on the Australian continent so that they can be monitored and managed.

## What this product offers

The Tasseled Cap Wetness Percentiles provide a multi-decadal summary of landscape wetness that can be used to identify wetlands and groundwater ecosystems. 

They provide statistical summaries (10th, 50th and 90th percentiles) of the Tasseled Cap wetness index from 1987 to 2017. 

They are intended for use as inputs into classification algorithms to identify potential wetlands and groundwater dependent ecosystems, and characterise salt flats, clay pans, salt lakes and coastal land forms.

% ## Data description

## Applications

This product provides valuable discrimination for characterising: 

* vegetated wetlands 
 
* salt flats 
 

* salt lakes 
 
* coastal land cover classes

## Technical information

The Tasseled Cap wetness transform translates the six spectral bands of Landsat into a single wetness index.  The wetness index can be used to identify areas in the landscape that are potentially wetlands or groundwater dependent ecosystems. The Tasseled Cap Wetness Percentiles capture how the wetness index behaves over time.  The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing the wetness index, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause false positives (a falsely high wetness index). 

The 10th, 50th and 90th percentiles of the Tasseled Cap wetness index are intended to capture the extreme (10th and 90th percentile) values and long-term average (50th percentile) values of the wetness index.  Percentiles are used in preference to minimum, maximum and mean, as the min/max/mean statistical measures are more sensitive to undetected cloud/cloud shadow, and can be misleading for non-normally distributed data. 

The Tasseled Cap Wetness Percentiles are intended to complement the Water Observations from Space (WOfS) algorithm. WOfS is designed to discriminate open water, but the Tasseled Cap wetness index identifies areas of water and areas where water and vegetation are mixed together; i.e. mangroves and palustrine wetlands. 

If you are interested in terrestrial vegetation (where water in the pixel is not a factor), use the Fractional Cover product, which provides a better biophysical characterisation of green vegetation fraction, dry vegetation fraction and bare soil vegetation fraction. 

We used the Tasseled Cap transforms described in Crist et al. (1985).

## Lineage

The lineage of this product is inherited from its sole input, the terrain corrected surface reflectance product Surface Reflectance NBART 2 (Landsat).

% ## Processing steps

% ## Software

## References

Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. *Remote Sensing of Environment*, *17*(3), 301–306. [https://doi.org/10.1016/0034-4257(85)90102-6](https://doi.org/10.1016/0034-4257(85)90102-6 )

