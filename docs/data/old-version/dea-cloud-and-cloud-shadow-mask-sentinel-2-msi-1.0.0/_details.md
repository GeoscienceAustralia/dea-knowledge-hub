## Background

Remote sensing images play more and more important roles in a lot of applications. Such applications and other remote sensing activities depends on noise free remote sensing data. Beside sensor abnormality, clouds and clouds shadow pose significant challenges to obtaining desire results. Detecting cloud and cloud shadow pixels and removing them from inputs for remote sensing data is essential for all remote sensing data modelling algorithms.

## What this product offers

This product is a time series cloud and cloud shadow detection algorithm for Sentinel-2 surface reflectance data.

It models time series of surface reflectance derived indices and calculates time series abnormality coefficients for pixels in the time series. It does not rely on predefined training data to generate complex models with many rule sets, which often work well for data similar to the training data while return poor results for data contrasting to the training data. Instead, it identifies cloud and cloud shadows by detecting local abnormalities in temporal and spatial contexts from abnormality coefficients.

% ## Data description

## Applications

This product can be applied to filter out noisy data in any application using Sentinel-2 data as inputs.

A remote sensing application loads Sentinel-2 data in conjunction with the Sentinel-2 cloud and cloud masks. Then any data which is not in the clear category can be identify and excluded from the inputs for the application.

## Technical information

This product uses time series analysis to identify clouds and cloud shadows so that they can be excluded from automated analysis. 

Many cloud and cloud shadow mask algorithms have been proposed and implemented to filter cloud and cloud shadows pixels for satellite images. Some cloud mask algorithms are pixel or object based, i.e. cloud detection algorithm only uses spectral data in a single scene, while some cloud mask algorithms relies multiple scenes from same areas to detect clouds.

Fmask (function of mask) (Zhu & Woodcock, 2012) was originally developed for cloud and cloud shadow detection in Landsat imagery. Fmask algorithm consists of two passes. In the first pass, several spectral tests are combined to identify potential cloud pixels. In the second pass, clear pixels (i.e., non-potential cloud pixels) from the first pass are used for computing cloud probability for all pixels in the image. For water pixels, the cloud probability is calculated as the product of temperature probability and brightness probability while the probability of land pixels is calculated as product of temperature probability and variability probability. Each probability is either as a cut-point function or normalised band ratio. Subsequent iterations of the algorithms (Qiu, Zhu, & He, 2019; Zhu, Wang, & Woodcock, 2015) extended the Fmask algorithm to accommodate Landsat 8 and Sentinel-2 data.   

Hagolle et al proposed a multi-temporal method for cloud detection (MTCD), applied to FORMOSAT-2, VENµS, LANDSAT and SENTINEL-2 images. (Hagolle, Huc, Pascual, & Dedieu, 2010). The main criterion to detect clouds is a threshold on the reflectance increase in the blue spectral band, and is complemented by a few criteria to avoid false detections. The main limitation of the algorithm is that a clear scene is required to be identified for each pixel before the cloud detection procedure can be run.

#### Input data

Among 12 Sentinel-2A and Sentinel-2B spectral bands, 6 bands are selected for the time series cloud and cloud shadow detection algorithm. They are Blue, Green, Red, Near Infra-Red and two Short-Wave Infra-Red bands. The following table shows some of the properties of the  Sentinel-2 spectral data used in the TSmask algorithm.

**Sentinel 2 bands**

**DEA band name**

**Central wavelength (nm)**

**Resolution (m)**   

**Bandwidth (nm)**

Blue

nbart\_blue

496.6/492.1

10

98/98

Green

nbart\_green

560.0/558.0

10

45/46

Red

nbart\_red

664.5/665.0

10

38/39

Narrow NIR

nbart\_nir\_2

864.8/864.0

20

33/32

SWIR

nbart\_swir\_2

1613.7/1610.4

20

143/141

SWIR

nbart\_swir\_3

2202.4/2185.7

20

242/238

#### Output data

This product classifies a Sentinel-2 pixel into one of four distinctive categories:

0 = No observation

1 = Clear

2 = Cloud

3 = Cloud shadow

#### TSmask algorithm

The above mentioned cloud and cloud shadow mask algorithm did not work very well on Sentinel-2 data. There are several reasons for that. First of all, most of cloud mask algorithms were developed for the Landsat TM/ETM+ data. With parameters of rule sets were trained with the Landsat data, models with such parameters may not work on the Sentinel-2 data which has different spectral characters. Also complexity of some cloud mask algorithms, which often consists of 10s or even hundreds rule sets, means that they cannot be easily adapted to accommodate new data.  

Therefore, there are demands for a cloud and cloud shadow mask algorithm for Sentinel-2A and Sentinel-2B surface reflectance data. The algorithm should be accurate, robust and efficient. It should be able to apply to data from wide range of climate regions and ground cover types, able to adapt to landcover changes over and require minimum prerequisite user defined training data and auxiliary data.

The design of the time series cloud and cloud shadow mask algorithm (TSmask) adopted an unsupervised learning approach. TSmask does not rely on predefined training data to generate complex models with many rule sets, which often work well for data similar to the training data while return poor results for data contrasting to the training data. Instead, TSmask identifies cloud and cloud shadows by detecting local abnormalities in temporal and spatial contexts. Details of TSmask are described in the following paragraphs.

Three indices are derived from surface reflectance of the selected 6 bands. They are band average (BA), which is the mean of surface reflectance of 6 selected bands, modified normalised difference water index (MNDWI) (Xu, 2006) and modified soil adjusted vegetation index (MSAVI) (Qi et al., 1994).  

Combining Sentinel-2A data and Sentinel-2B data, the number of points in an annual time series ranges from 50 to 100. It can be estimated that the average time gap between 2 consecutive observations is about 3 to 7 days. Therefore for any location in a series of images, fluctuations of surface reflectance should not exceed a certain range for a series of clear observations within a short time frame. The TSmask defines a moving window over time series of band average (BA). The TSmask detects abnormal fluctuations within a short time frame by defining a small local moving window containing 3N data points in the time series. Fluctuation is estimated by calculating the difference between the mean of the second N points and the mean of the first and the third N points in the moving window. Fluctuation Coefficient (FC) for the second N points in a moving window is then defined as the ratio between the difference and the mean of the first and the third N points in the moving window. If FC is higher than a predefined threshold, then the second N points in a moving windows are declared as cloud pixels. If FC is lower than a predefined threshold, then the second N points in a moving window are declared as cloud shadow pixels. By moving a local window from the start to the end of a time series, cloud and cloud shadow pixels in the whole time series are identified.

The process can be repeated multiple times with identified cloud points and cloud shadow points removed from the subsequent processes. So that in each step, the time series becomes less noisy. Starting at 1, the value of N should also be gradually increased to detect single cloud or cloud shadow pixel, 2 consecutive cloud or cloud shadow pixels, 3 consecutive cloud or cloud shadow pixels in the time series.  

When the time series cloud and cloud shadow detection procedure completed. The data is run through a series of spectral and spatial filters. These filters target confusions between certain ground objects and clouds or cloud shadows, such as bright ground objects and clouds, water body/wet lands and cloud shadows, etc. Using BA, MSAVI and MNDWI as inputs, the spectral filters are able to detect ground objects which are wrongly classified as clouds or cloud shadows, further reducing false positive rate in detection. A spatial filter is also applied to eliminate cloud or cloud shadow objects with spatial size smaller than a threshold.

#### STEPS

**Step 1: Identify extreme and invalid data**

In this step, pixels in the time series with BA>0.45 is labelled as cloud (with mask value = 3), while BA<=-0.0999 is labelled as invalid (with mask value = 1). The procedure is shown in Figure 1.

![identify extreme data](/_files/dea-cloud-and-cloud-shadow-mask/cloud_1.png)

*Figure 1\. Identify extreme and invalid data.*

**Step 2: Remove data labelled in the previous step from the time series**

The updated time series is shown in Figure 2.

![Updated time series with extreme and invalid pixels removed](/_files/dea-cloud-and-cloud-shadow-mask/cloud_2.png)

*Figure 2\. Updated time series with extreme and invalid pixels removed*

**Step 3: Identify cloud and cloud shadow pixels**

This is done by applying local time series noise filter on the whole time series, the time series with identified cloud and cloud shadow pixels is shown in Figure 3.

![Time series with cloud and cloud shadow pixels identified](/_files/dea-cloud-and-cloud-shadow-mask/cloud_3.png)

*Figure 3. Time series with cloud and cloud shadow pixels identified*

**Step 4: Repeat Step 3 by varying the length of the local time series noise filter.**

In the current implementation, the local time series noise filter was applied 3 times with N=1,  2 times with N=2 and 1 time with N=3, where 3N is the length of the local time series noise filter. The filtered time series after Step 4 is shown in Figure 4.

![Time series with cloud and cloud shadow pixels removed](/_files/dea-cloud-and-cloud-shadow-mask/cloud_4.png)

*Figure 4. Time series with cloud and cloud shadow pixels removed*

**Step 5: Apply spectral and spatial filters**

Detect ground objects which are wrongly classified as clouds and cloud shadows. Output the identified cloud and cloud shadow pixels as a cloud and cloud shadow mask, as shown in Figure 5.

![The output of cloud and cloud shadow mask for the time series](/_files/dea-cloud-and-cloud-shadow-maskcloud_5.png)

*Figure 5. The output of cloud and cloud shadow mask for the time series*

#### Data requirement for implementation

This product requires Sentinel-2 NBAR-T surface reflectance time series with a minimum of 1-year window and  a minimum of 90 observations. In case number of the observations less than 90, increase the length of the windows to 18 months or 24 months.

## Lineage

Remote sensing images play more and more important roles in a lot of applications. Such applications and other remote sensing activities depends on noise free remote sensing data. Beside sensor abnormality, clouds and clouds shadow pose significant challenges to obtaining desire results. Detecting cloud and cloud shadow pixels and removing them from inputs for remote sensing data is essential for all remote sensing data modelling algorithms.

The time series cloud and cloud shadow detection algorithm provides a robust noise detection method for sentinel-2 imagery. It ensures remote sensing applications able to retrieve noise free Sentinel-2 data from DEA API.

% ## Processing steps

% ## Software

## References

Hagolle, O., Huc, M., Pascual, D. V., & Dedieu, G. (2010). A multi-temporal method for cloud detection, applied to FORMOSAT-2, VENµS, LANDSAT and SENTINEL-2 images. *Remote Sensing of Environment*, *114*(8), 1747–1755. [https://doi.org/10.1016/j.rse.2010.03.002](https://doi.org/10.1016/j.rse.2010.03.002 )

Qi, J., Chehbouni, A., Huete, A. R., Kerr, Y. H., & Sorooshian, S. (1994). A modified soil adjusted vegetation index. *Remote Sensing of Environment*, *48*(2), 119–126. [https://doi.org/10.1016/0034-4257(94)90134-1](//doi.org/10.1016/0034-4257(94)90134-1 )

Qiu, S., Zhu, Z., & He, B. (2019). Fmask 4.0: Improved cloud and cloud shadow detection in Landsats 4–8 and Sentinel-2 imagery. *Remote Sensing of Environment*, *231*, 111205. [https://doi.org/10.1016/j.rse.2019.05.024](https://doi.org/10.1016/j.rse.2019.05.024 )

Xu, H. (2006). Modification of normalised difference water index (Ndwi) to enhance open water features in remotely sensed imagery. *International Journal of Remote Sensing*, *27*(14), 3025–3033. [https://doi.org/10.1080/01431160600589179](https://doi.org/10.1080/01431160600589179 )

Zhu, Z., Wang, S., & Woodcock, C. E. (2015). Improvement and expansion of the Fmask algorithm: Cloud, cloud shadow, and snow detection for Landsats 4–7, 8, and Sentinel 2 images. *Remote Sensing of Environment*, *159*, 269–277. [https://doi.org/10.1016/j.rse.2014.12.014](https://doi.org/10.1016/j.rse.2014.12.014 )

Zhu, Z., & Woodcock, C. E. (2012). Object-based cloud and cloud shadow detection in Landsat imagery. *Remote Sensing of Environment*, *118*, 83–94. [https://doi.org/10.1016/j.rse.2011.10.028](https://doi.org/10.1016/j.rse.2011.10.028 )

