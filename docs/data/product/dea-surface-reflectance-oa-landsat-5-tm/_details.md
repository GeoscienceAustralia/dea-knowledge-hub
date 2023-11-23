## Background

***

*This is a sub-product of [**DEA Surface Reflectance (Landsat 5 TM)**](/data/product/dea-surface-reflectance-landsat-5-tm). See the parent product for more information.*

***

The contextual information related to a dataset is just as valuable as the data itself. This information, also known as data provenance or data lineage, includes details such as the data’s origins, derivations, methodology and processes. It allows the data to be replicated and increases the reliability of derivative applications.

Data that is well-labelled and rich in spectral, spatial and temporal attribution can allow users to investigate patterns through space and time. Users are able to gain a deeper understanding of the data environment, which could potentially pave the way for future forecasting and early warning systems.

The surface reflectance data produced by NBAR and NBART requires accurate and reliable data provenance. Attribution labels, such as the location of cloud and cloud shadow pixels, can be used to mask out these particular features from the surface reflectance analysis, or used as training data for machine learning algorithms. Additionally, the capacity to automatically exclude or include pre-identified pixels could assist with emerging multi-temporal and machine learning analysis techniques.

## What this product offers

This product contains a range of pixel-level **observation attributes (OA)** derived from satellite observation, providing rich data provenance:
* null pixels
* clear pixels
* cloud pixels
* cloud shadow pixels
* snow pixels
* water pixels
* spectrally contiguous pixels
* terrain shaded pixels

It also features the following pixel-level information pertaining to **satellite, solar and sensing geometries**:
* solar zenith
* solar azimuth
* satellite view
* incident angle
* exiting angle
* azimuthal incident
* azimuthal exiting
* relative azimuth
* timedelta

% ## Data description

% ## Applications

## Technical information

### How observation attributes can be used

This product provides pixel- and acquisition-level information that can be used in a variety of services and applications. This information includes:

* data provenance, which:
  * denotes which inputs/parameters were used in running the algorithm  
  * demonstrates how a particular result was achieved  
  * can be used as evidence for the reasoning behind particular decisions  
  * enables traceability
* training data for input into machine learning algorithms, or additional likelihood metrics for image feature content, where pre-classified content includes:
  * cloud  
  * cloud shadow  
  * snow  
  * water
* additional pixel filtering (e.g. exclude pixels with high incident angles)
* pre-analysis filtering based on image content (e.g. return acquisitions that have less than 10% cloud coverage)
* input into temporal statistical summaries to produce probability estimates on classification likelihood

This product allows you to screen your data for undesired anomalies that can occur during any phase: from the satellite’s acquisition, to the processing of surface reflectance, which relies on various auxiliary sources each having their own anomalies and limitations.

Pixel-level information on satellite and solar geometries is useful if you wish to exclude pixels that might be deemed questionable based on their angular measure. This is especially useful if you are using the NBAR product, where pixels located on sloping surfaces can exhibit a lower than expected surface reflectance due to a higher incidence or solar zenith angle.

### ***Example - Terrain shadow and high incident angles***

These images depict an area containing high topographic relief, terrain shadow, and high incident angles. Applications, such as water classification, can mis-classify dark regions as water due to the effect of high incident angles in regions of high topographic relief.

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 1.png
:alt: NBAR, terrain shadow, high incident angle, NBAR+ mask overlay, NBART
:::

*Figure 1. (A) Surface Reflectance (Landsat 5 TM NBAR) image; (B) terrain shadow mask; (C) high incident angle mask (>65); (D) NBAR+ mask overlay; (E) equivalent Surface Reflectance (Landsat 5 TM NBART) image.*

### Terminology for satellite, solar and sensing geometries

* **Zenith**  
 The point in the sky or celestial sphere directly above a point of interest (in this case, the point being imaged on Earth).
* **Solar zenith (degrees)**  
 The angle between the zenith and the centre of the sun’s disc.
* **Solar azimuth (degrees)**  
 The angle of the sun’s position from true north; i.e. the angle between true north and a vertical circle passing through the sun and the point being imaged on Earth. 
* **Satellite view or satellite zenith (degrees)**  
 The angle between the zenith and the satellite.
* **Satellite azimuth (degrees)**  
 The angle of the satellite’s position from true north; i.e. the angle between true north and a vertical circle passing through the satellite and the point being imaged on Earth. 
* **Incident angle (degrees)**  
 The angle between a ray incident on a surface and the line perpendicular to the surface at the point of incidence. 
* **Exiting angle (degrees)**  
 The angle between a ray reflected from a surface and the line perpendicular to the surface at the point of emergence.
* **Azimuthal incident (degrees)**  
 The angle between true north and the incident direction in the slope geometry.
* **Azimuthal exiting (degrees)**  
 The angle between true north and the exiting direction in the slope geometry.
* **Relative azimuth (degrees)**  
 The relative azimuth angle between the sun and view directions. 
* **Relative slope (degrees)**  
 The relative azimuth angle between the incident and exiting directions in the slope geometry. 
* **Timedelta (seconds)**  
 The time from satellite apogee (the point of orbit at which the satellite is furthest from the Earth).

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 2.png
:alt: Zenith angles
:::

*Figure 2. Zenith angles. Image modified from Support to Aviation Control Service (2011).*

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 3.png
:alt: Zenith and azimuth angles
:::

*Figure 3. Zenith and azimuth angles. θs = solar zenith; θν = satellite view; Φs = solar azimuth (green); Φν = satellite azimuth (blue); Φ = relative azimuth (red). Image modified from Hudson et al. (2006).*

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 4.png
:alt: Incident (i) and exiting (e) angles
:::

*Figure 4. Incident (i) and exiting (e) angles for a level and inclined surface. Image modified from Dymond and Shepherd (1999).*

### The Fmask algorithm

Fmask allows you to have pre-classified image content for use within their applications. This can include:
* additional confidence metrics in image content classifiers
* pre-labelled data for machine learning classifiers
* pixel screening for cloud and cloud shadow
* on-the-fly mapping applications for water and snow

The result of the Fmask algorithm contains mutually exclusive classified pixels, and the numerical schema for the pixels are as follows:
* 0 = null
* 1 = clear
* 2 = cloud
* 3 = cloud shadow
* 4 = snow
* 5 = water

The spectrally contiguous pixels which have a valid observation in each spectral band. This is particularly useful for applications undertaking band math, as it allows non-contiguous data to be ignored during the band math evaluation or masked during post-evaluation. The product can be utilised as a strict mask, and the numerical schema for the pixels are as follows:
* 0 = non-contiguous
* 1 = contiguous

The terrain-shaded pixels product can be utilised as a strict mask and exclude pixels that were unobservable by the sun or sensor. The numerical schema for the pixels are as follows:
* 0 = shaded
* 1 = not shaded

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 5.png
:alt: Different types of terrain-shaded pixels
:::

*Figure 5. Different types of terrain-shaded pixels. C = point of interest; D = point located along the direction of the sun; 90-θS = solar zenith; Z0 = elevation at location C; Zd = elevation at location D. Image sourced from Jupp et al. (2012).*

### ***Example - Fmask***

Some analyses might want to exclude targets that are obscured by cloud or cloud shadow. This is particularly useful for applications looking to harvest statistical information for particular regions of interest, such as field crops, where large swaths of data aren't required to be loaded into computer memory. Instead, only the regions of interest are loaded, analysed and summarised, reducing computational costs.

The following images represent the surface reflectance image and derived Fmask classification result for visual context. The colours for the Fmask classification are displayed as:
* Black = clear
* Magenta = cloud
* Yellow = cloud shadow
* Cyan = snow
* Dark blue = water

:::{image} /_files/cmi/Surface\ Reflectance\ OA\ 3\ -\ figure\ 6.png
:alt: False colour composite and the resulting Fmask classification
:::

*Figure 6. (A) False colour composite; (B) the resulting Fmask classification.*

For this product, the Fmask dataset has had the object dilation for the cloud and cloud shadow layers removed. This enables you to customise object dilation to meet your needs for specific applications. For example, one application might work better having a 7-pixel dilation, whereas another might require 5.

You can also choose your own kernel shape and size in which to apply a particular dilation. Dilation can be useful for filling holes within objects and extending the edges of detected objects. It is important to note that small objects (e.g. 1 or 2 pixels in size) will be dilated and become large objects. If this is an undesired outcome, it is best to filter out any small objects prior to applying dilation filters.

For more information on dilation, see:
* [Mathematical morphology (Wikipedia)](https://en.wikipedia.org/wiki/Mathematical_morphology)
* [Dilation (Wikipedia)](https://en.wikipedia.org/wiki/Dilation_%28morphology%29)
* [Multi-dimensional binary dilation (SciPy.org)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_dilation.html#scipy.ndimage.binary_dilation)

Other uses of Fmask:
* **For training data for use with machine learning classifiers**  
 Fmask can help refine the result and produce a more accurate classification result. The data can also be combined with other classifiers, creating a confidence metric that users can then filter by. For example, you can filter cloud pixels rated >70% as a combined metric from the combination of cloud classifiers. 
* **For input into a statistical summary**  
 It can provide another information product that can be used to indicate the probability of being a particular classified feature. For example, a statistical summary of cloud and/or cloud shadow can highlight pixels that are consistently being detected as a cloud or cloud shadow. As clouds and cloud shadows are non-persistent features, pixels with a high cloud or cloud shadow frequency can be labelled or attributed as highly probable of not being cloud or cloud shadow. 

### Image format specifications

#### Fmask

|                                |                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Format                         | GeoTIFF                                                                                                                          |
| Resolution                     | 30m                                                                                                                              |
| Datatype                       | UInt8                                                                                                                            |
| Classification ENUM            | 0 = null <br /> 1 = clear <br /> 2 = cloud <br /> 3 = cloud shadow <br /> 4 = snow <br /> 5 = water                              |
| Valid data range               | [0,5]                                                                                                                            |
| Tiled with X and Y block sizes | 512x512                                                                                                                          |
| Compression                    | Deflate, Level 9, Predictor 2                                                                                                    |
| Pyramids                       | Levels: [8,16,32] <br /> Compression: deflate <br /> Resampling: mode <br /> Overview X&Y block sizes: 512x512                   |
| Contrast stretch               | None                                                                                                                             |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum                                                            | 

#### nbar-contiguity, nbart-contiguity

|                                |                                                                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Format                         | GeoTIFF                                                                                                                             |
| Resolution                     | 30m                                                                                                                                 |
| Datatype                       | UInt8                                                                                                                               |
| Classification ENUM            | 0 = non-contiguous (spectral information not present in each band) <br /> 1 = contiguous (spectral information present in each band)|
| Valid data range               | [0,1]                                                                                                                               |
| Tiled with X and Y block sizes | 512x512                                                                                                                             |
| Compression                    | Deflate, Level 9, Predictor 2                                                                                                       |
| Pyramids                       | Levels: [8,16,32] <br /> Compression: deflate <br /> Resampling: GDAL default (nearest) <br /> Overview X&Y block sizes: 512x512    |
| Contrast stretch               | None                                                                                                                                |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum                                                               |

#### combined-terrain-shadow

|                                |                                                                           |
|--------------------------------|---------------------------------------------------------------------------|
| Format                         | GeoTIFF                                                                   |
| Resolution                     | 30m                                                                       |
| Datatype                       | UInt8                                                                     |
| Classification ENUM            | 0 = terrain shadow <br /> 1 = not terrain shadow                          |
| Valid data range               | [0,1]                                                                     |
| Tiled with X and Y block sizes | 512x512                                                                   |
| Compression                    | Deflate, Level 9, Predictor 2                                             |
| Pyramids                       | None                                                                      |
| Contrast stretch               | None                                                                      |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum     |       

 #### incident, exiting, azimuthal-incident, azimuthal-exiting, relative-azimuth, relative-slope, timedelta

|                                |                                                                       |
|--------------------------------|-----------------------------------------------------------------------|
| Format                         | GeoTIFF                                                               |
| Resolution                     | 30m                                                                   |
| No data value                  | NaN (IEEE 754)                                                        |
| Tiled with X and Y block sizes | 512x512                                                               |
| Compression                    | Deflate, Level 9, Predictor 2                                         |
| Pyramids                       | None                                                                  |
| Contrast stretch               | None                                                                  |
| Output CRS                     | As specified by source dataset; source is UTM with WGS84 as the datum |

% ## Lineage

## Processing steps

1. [Longitude and Latitude Calculation](/guides/reference/analysis_ready_data_corrections#lon-lat-calculation)
2. [Satellite and Solar Geometry Calculation](/guides/reference/analysis_ready_data_corrections#sat-sol-geom-calculation)
3. [Elevation Retrieval and Smoothing](/guides/reference/analysis_ready_data_corrections#elev-retr-smth)
4. [Slope and Aspect Calculation](/guides/reference/analysis_ready_data_corrections#slp-asp-calc)
5. [Incidence and Azimuthal Incident Angles Calculation](/guides/reference/analysis_ready_data_corrections#inc-azm-ang-calc)
6. [Exiting and Azimuthal Exiting Angles Calculation](/guides/reference/analysis_ready_data_corrections#ext-azm-ang-calc)
7. [Relative Slope Calculation](/guides/reference/analysis_ready_data_corrections#rel-slp-calc)
8. [Terrain Occlusion Mask](/guides/reference/analysis_ready_data_corrections#terr-occ-msk)
9. [Function of Mask (Fmask)](/guides/reference/analysis_ready_data_corrections#fmask)
10. [Contiguous Spectral Data Mask Calculation](/guides/reference/analysis_ready_data_corrections#cont-spec-data-mask-calc)

% ## Software

% ## References

