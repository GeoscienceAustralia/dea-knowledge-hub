## Accuracy

Atmospheric correction accuracy is dependent on the quality of aerosol data available to determine the atmospheric profile at time of image acquisition.

BRDF correction is based on low resolution imagery (MODIS) which is assumed to be relevant to medium resolution imagery such as Landsat TM/ETM+/OLI. BRDF correction is applied to each whole Landsat TM/ETM+/OLI scenes and does not account for changes in land cover. It also excludes effects due to topographic shading and local BRDF. This algorithm is dependent on the availability of relevant MODIS BRDF data.

Topographic shading correction algorithm is designed for medium resolution imagery and assumes that hill slopes are resolved by the sensor system (Li et al., 2012). The algorithm assumes that: a. BRDF effect for inclined surfaces is modelled by the surface slope and does not account for land cover orientation relative to gravity (as occurs for some broad leaf vegetation with vertical leaf orientation).

## Quality assurance

Validate combined atmospheric and surface BRDF correction using field reflectance measurements at two very different sites, Gwydir, NSW, and Lake Frome, SA; correlation (measured as r) between corrected image values and field data was > 0.95.

Validate surface BRDF correction using data from image overlap areas of adjacent paths acquired one week apart in northeast Queensland - normalised reflectance factor was very close in corrected images, but not in original images, and difference in reflectance factor values between corrected and uncorrected images can be > 0.05.

Cross-validate Landsat TM data for accuracy of spectral reflectance using the MODIS reflectance product for Lake Frome; correlation (measured as r2) between corrected Landsat TM image values and MODIS reflectance product was 0.93-0.97 in all bands except Landsat TM band 5, which was 0.90.

Topographic Correction As detailed in Li et al. (2012), two high relief areas in southeast Australia (Australian Alps in northeast Victoria and the Blue Mountains in NSW) were used to test the algorithm against eight Landsat images with varying solar angles (seasons), and terrain types.

Visual assessment showed that the algorithm removed much of the topographic effect and detected deep shadows in all eight images. An indirect validation based on the change in correlation between the data and terrain slope showed that the correlation coefficient between the surface reflectance factor and the cosine of the incident (sun) angle reduced dramatically after the topographic correction algorithm was applied. The correlation coefficient typically reduced from 0.80-0.70 to 0.05 in areas of significant relief. It was also shown how the corrected surface reflectance can provide suitable input data for multi-temporal land cover classification in areas of high relief based on spectral signatures and spectral albedo, while the products based only on BRDF and atmospheric correction cannot. To provide comparison with previous work and to validate the proposed algorithm, two empirical methods based on the C-correction were used as well as the established sun-canopy-sensor SCS-method to provide benchmarks. The proposed method was found to achieve the same measures of shade reduction without empirical regression.

The Geometric QA software utilises an area based image-to-image correlation technique to assess and compare the difference between the target image and the reference image at regular gridded QA points. The residual of each QA point will be derived and scene statistics such as number of valid QA points, mean residual X/Y, STD residual X/Y and CEP90 will be recorded in v2 AGDC.

Because each scene recorded in v2 AGDC will have a GQA assessment result, the minimum GCP number threshold has been lowered to enable more products processed to Ortho level, especially for coastal scenes where only a very small portion of the image contains land for GCP identification purpose.

Product generation process is fully automated and there are checks in place to ensure that each step results in output meeting relevant product specification criteria. For example, the production system performs geometry QA before generating the final version of the product. Failed processes are rerun according to set up routines to ensure completeness of data. A sample of final data is verified manually for conformance to product specification.

At the end of the process, the system generates a companion dataset, the Pixel Quality assessment (PQ25). The PQ25 is a classification that represents an assessment of whether an image pixel represents an unobscured unsaturated observation of the Earth's surface and whether the pixel is represented in each spectral band. In particular, whether a pixel contains:
* Spectral Contiguity
* Per band saturation assessment
* Cloud detection
* Cloud shadow estimation
* Offshore (sea)
* Onshore (land)

The PQ25 product allows users to produce masks which can be used to exclude affected pixels which don't meet quality criteria from further analysis.

