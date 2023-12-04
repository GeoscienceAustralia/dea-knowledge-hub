## Background

This product has been deprecated and is superseded by this product: [DEA Surface Reflectance (Landsat 8 OLI-TIRS)](https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs)

We need to be able to exclude cloud and cloud shadow affected observations from analyses of optical Earth observation data.

Historically this has been done via the user selecting 'cloud free' images as input for their analysis. However, manual selection of cloud free scenes is neither timely nor practical for large scale automated analysis at continental or 'whole of archive' scale. This necessitates the use of per pixel information about whether the observation is 'clear'; i.e. free of cloud, cloud shadow and sensor saturation, and contains information for all bands.

## What this product offers

This product facilitates interpretation and processing of Surface Reflectance NBAR/NBART, Fractional Cover and all derivative products.

It provides an assessment of the quality of observations at a pixel level and includes information about:

* spectral contiguity (lack of signal in any band)
* saturation in any band
* presence of cloud
* presence of cloud shadow
* land or sea

% ## Data description

## Applications

By removing the need for cloud screening and specific scene selection the PQ25 will significantly reduce pre-processing requirements for a wide range of land and coastal monitoring applications and render more accurate results from these analyses, particularly for those utilising time series data.

Such applications include various forms of change detection, including the monitoring of:

* urban growth
* coastal habitats
* mining activities
* agricultural production

It can also be used in compliance surveys, scientific research and emergency management.

## Technical information

As Landsat Imagery becomes more readily available, there has been a rapid increase in the amount of analyses undertaken by researchers around the globe.

Most researchers use some form of quality masking schema in order to remove undesirable pixels from analysis, whether that be cloud, cloud shadow, observations over the ocean, or saturated pixels.

In the past, researchers would reject partly cloud-affected scenes in favour of cloud-free scenes. However, Landsat time series analysis using all cloud-free pixels has become a valuable technique and has increased the demand for automation of cloud, cloud shadow and saturation detection.

This product assesses each image pixel to determine if it is an unobscured, unsaturated observation of the Earth's surface and also whether the pixel is represented in each spectral band.

It allows users to produce masks which can be used to exclude pixels which do not meet their quality criteria from analysis. The capacity to automatically exclude such pixels is essential for emerging multi-temporal analysis techniques that make use of every quality assured pixel within a time series of observations.

You can choose to process only land pixels, or only sea pixels depending on their analytical requirements.

The PQ25 product combines established algorithms that detect clouds including the Automated Cloud Cover Assessment (ACCA) (Irish et al. 2006) and Function of mask (Fmask) (Zhu and Woodcock 2012) .

ACCA is already widely used within the remote sensing community; it is fast and relatively accurate. Fmask on the other hand is newer, but is rapidly becoming more established, and can provide a more accurate cloud mask than ACCA in certain cloud environments.

Emergency response applications such as flood mapping typically have to contend with individual cloud affected scenes and therefore rely on effective cloud and cloud shadow removal techniques.

## Lineage

The sensor saturation flagging protocols developed for the Web Enabled Landsat Data (WELD) product as described in Roy et al. (2011) are used to flag sensor saturation.

The PQ25 product has similarities to the QAB layer packaged with OLI data, however it uses additional algorithms to detect cloud and cloud shadow, and is available for Landsats 5, 7 and 8.

% ## Processing steps

% ## Software

## References

Irish, R. R., Barker, J. L., Goward, S. N., & Arvidson, T. (2006). Characterization of the Landsat-7 ETM+ automated cloud-cover assessment (ACCA) algorithm. *Photogrammetric Engineering & Remote Sensing*, *72*(10), 1179–1188. [https://doi.org/10.14358/PERS.72.10.1179](https://doi.org/10.14358/PERS.72.10.1179)

Zhu, Z., & Woodcock, C. E. (2012). Object-based cloud and cloud shadow detection in Landsat imagery. Remote Sensing of Environment, 118, 83–94. [https://doi.org/10.1016/j.rse.2011.10.028](https://doi.org/10.1016/j.rse.2011.10.028)

