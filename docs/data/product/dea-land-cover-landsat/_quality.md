## Limitations

DEA Land Cover is created by combining multiple layers that each describe features in the landscape. In doing so, the extents of each layer do not necessarily completely align, and some no-data points can cross between outputs. As a result, there are some Level 4 classes that only report detail to Level 3, as the details of cover fraction and water persistence do not have corresponding data in the respective datasets. This specifically relates the classes of Water, Natural Surfaces, and Natural Aquatic Vegetation in areas near water bodies and the intertidal zone; however, the number of affected pixels is small. 

### Level 3 Class limitations

**Cultivated Terrestrial Vegetation (CTV)** 

Managed plantations and some orchards and tree crops are not currently distinguishable from semi-natural or natural terrestrial vegetation and are not yet incorporated in the area of CTV. Reference can be made to Australia’s National Plantation Inventory. In savannah regions (e.g. Queensland, Northern Territory, and Western Australia), variable cycles associated with fires, inundation, drought, and rainfall lead to greening or browning of natural vegetation that mirrors the seasonal or management-induced behaviour of cultivated land. This leads to some areas of NTV, NS, or NAV being misclassified as CTV. For example, the anomalous high levels of rainfall in 2010 led to vegetation growth patterns that were classified as cultivated vegetation and these false positives reduced the precision of the class in that year. Several natural vegetation types, particularly in the monsoonal north, are mapped as CTV due to burning, which can be associated with the indigenous management cycle. Saltmarsh and surface algae on mudflats can also be misclassified. Areas of bare soil exposed for long periods during the agricultural cycle or management activities, and sparse vegetation (when areas are not in use or fallow such as during drought periods) can be assigned as Natural Surfaces (NS). This occurs particularly where areas have experienced low cover for prolonged periods within a year. The CTV machine learning algorithm has not been trained on CTV-woody areas, due to a lack of available training data, therefore leading to possible high rates of misclassification.

**Natural Terrestrial Vegetation (NTV)** 

The NTV category can transition into the NS category between years when a highly variable Landsat satellite spectral signature is observed due to changes in vegetation productivity and moisture content. The transition of NTV to NS is particularly evident when comparing periods with rainfall above or below the average (e.g. 2010 was above; whereas, 2015 was below). Some confusion between surfaces that are primarily bare surfaces and non-photosynthetic vegetation remains and is also partly a function of the spectral reflectance of the underlying soil type. Vegetated areas shadowed by terrain can also be misclassified as non-vegetated. Areas of very low vegetation coverage are associated with the NS rather than NTV category, with the cover percentages shown as percentage bare. The assignment of vegetated suburbs to NTV is largely correct, but AS surfaces located beneath the canopy are not currently represented in the product. Some confusion between CTV and NTV can occur because of natural seasonal changes in native vegetation. The edges of salt lakes may be misclassified as NTV. 

**Natural Aquatic Vegetation (NAV)** 

Currently only mangroves are mapped in the NAV class. Other vegetated natural landscapes (e.g. saltmarsh, river red gum forests in the Murray Valley, surface algae, and other inland wetlands) where water significantly influences edaphic conditions of substrate are not mapped. This is because, in the current implementation, the water mask is included to assist in the differentiation of vegetation and non-vegetation as the presence of water creates excess noise in the underlying Fractional Cover product. To reduce this noise, the [DEA Water Observations](/data/category/dea-water-observations/) product is used as a water mask in the Fractional Cover product, and hence it is unlikely to produce the combination of vegetation and water required for the NAV class.

**Artificial Surfaces (AS)** 

The artifical surfaces machine learning algorithm works best in dense urban areas. Misclassification occurs with natural surfaces, particularly in the arid and semi-arid regions, open cut mine sites, salt lakes and pans, sand dunes and beaches. This is attributed to similarities in the variance of spectral signatures over a year. The Australian Bureau of Statistics - Urban Centre and Locality mask is applied to try and remove some of these misclassifications in rural areas. Urban areas with high concentrations of surrounding vegetation, may not be classified as artifical surfaces. Misclassification occurs in some cultivated areas attributable to the predominance of sparse vegetation or when land is left fallow for most of the year. Cloud and data quality issues can lead to incorrect assignment of other land cover classes to AS such as in south-west Tasmania. Within dense urban centers with high-rise buildings such as Sydney or Melbourne CBD, building are misclassified as water due to the shadows of the high rise buildings. In some industrial areas, buildings can be misclassified as no data due to the bright surface reflectance having a similar signature to cloud.

**Natural Surfaces (NS)** 

Land used for agriculture may be associated with an NS class if ploughing or tillage has occurred and the vegetation cover remains low during the calendar year. Areas mapped as NS may, under certain circumstances (e.g. during drought) temporarily transition to or from CTV. This occurs because of the dominance of non-persistent vegetation (e.g. short crop life spans), desiccation, removal during dry periods or management practices (e.g. left as fallow). Where acquisition of cloud-free Landsat satellite sensor data has been infrequent, less information on the inter-annual variability of vegetation is provided. Where cloud cover is extensive (e.g. in Tasmania), the number of scenes for land cover classification is reduced and this can compromise classification of NS, particularly where bare surfaces alternate with vegetation. Confusion between natural surfaces and urban areas occurs because of similar spectral variation over an annual period.

**Water**

Areas of artificial and natural water are not differentiated, although the extent of the former is mapped within the existing Bureau of Meteorology Geofabric product. Due to the 30 m pixel size, rivers and water courses that cover less than a pixel, or with highly vegetated riverbanks are not captured, resulting in a patch-like representation of narrower rivers. Areas of dark, wet soil are often misclassified as water, including in cultivated areas and mud flats. Some pixels surrounding waterbodies have no classification, due to not valid data from Fractional Cover, and Water Observations being unable to determine if the pixels are wet or dry. Classification of pixels over ocean should not be used from Land Cover (the water persistence is often incorrect, and the land cover classification should be applied to land only pixels). Land Cover product should be used with an ocean mask for coastal tiles.
:::

### Level 4 Class limitations

**Lifeform**

The woody discrimination is implemented using the Woody Cover Fraction product (Liao et al, 2020), which models woody cover from inputs of LiDAR including ICESat/GLAS, L-band SAR, field observation and Landsat satellite data. Issues arise in this dataset in areas dominated by short, woody vegetation such as heathland, and swampy regions where underlying water can introduce errors. Areas of woody savannah are also underrepresented due to the influence of the herbaceous understory dominating the observation.

**Vegetation Cover**

The cover of vegetation is derived from the fractional cover product (Scarth et al, 2010), and as such reflects the limitations of that product, mainly difficulty with measurement of non-photosynthetic vegetation, and noise due to the presence of water in a pixel. Thus arid areas can be difficult to fully analyse for cover, leading to misclassifications between NTV, NS and CTV where cover is sparse (lower than 15 %). 

**Water Seasonality**

This product does not yet identify consecutive months but rather the frequency of wet observations in the year, based on the WO product. Therefore, monthly statements are unlikely to be consistent across the continent. Mangroves are currently the only consistently identified NAV and water cannot be easily observed beneath their canopies, which are often dense. Hence, the hydroperiod (and hence seasonality metrics) should be treated with some caution. 

**Water State**

Mapping of ice and snow states has yet to be undertaken. Hence the water state class is currently limited to liquid only. 

**Intertidal**

The intertidal areas carry the limitations of the ITEM product:

* Intertidal areas are determined as a coastal mask, which currently identifies some non-tidal inland water bodies as tidal because of intra-annual changes in water extent. 
 
* This product is static and cannot be used to demonstrate change between two annual continental products. 
 

**Bare Gradation** 

Bare gradation is produced from the fractional cover product. Unlike the Vegetation Cover class, Bare Gradation is calculated from the median bare fraction, rather than consecutive, monthly green and non-photosynthetic fractions. Hence the bare fraction can be as low as 20 %, however this does not imply that the remaining fraction is healthy vegetation. Rather the remaining fraction is a mix of brown, dead and green vegetation, with intermittent green periods through the year, reflective of arid area vegetation types.
:::

### Earth Observation limitations

To generate the land cover classification for each calendar year, annual (January – December) statistics derived from Landsat-5, -7, -8 and -9 observations are currently used, with each satellite sensor potentially observing the Australian landscape every 16 days. This brings an intrinsic limitation to land cover mapping as persistent cloud in some regions reduces the number of useable observations. This is particularly evident in Tasmania, and northern Australia during the monsoon period, where areas may not be observed for extended periods and parts or all of the intra-annual land cover cycle may be missed. These limitations can lead to misclassifications of land cover, particularly in dynamic environments. In a future release, a confidence layer will be included to help identify areas with poor observation frequency or other factors impacting the classification. 

An additional limitation of the Landsat series is the availability of data due to the ageing of each satellite. Landsat 5 was operational for over 25 years, but for much of the later years, data were only acquired when sunlight directly illuminated its solar panels. This limited its operation across Australia, with coverage being seasonally dependent, and contracting north to a minimum in winter. In its last years the winter coverage usually only covered the northern coasts of Australia. Landsat 5 ceased regular operations over Australia in 2011, leaving just Landsat 7 until Landsat 8 was launched in 2013. Landsat 7 began service in 1999 as a replacement for Landsat 5. Initially Landsat 5 was switched off, but when Landsat 7 suffered a serious problem in 2003 due to the failure of its scan-line corrector (termed SLC-Off) Landsat 5 resumed service. The SLC-Off failure of Landsat 7 results in severe striping across every image from mid 2003 onwards, apparent in subsequent derived products. Landsat 8 has operated well since launch in 2013, and Landsat 9 since 2022 with improved sensitivity, noise characteristics and data correction in comparison to the earlier sensors.

The result of the availability of the satellites is that the most consistent data availability occurs when two satellites are in operation (most of the 2003 to present period). The least data availability is in 2011 – 2012 when only Landsat 7 was available with data containing the SLC-Off striping issue. The overall data availability for the Landsat satellites is shown in Table 5. The datasets used in this analysis are shown in Table 6. 

![eo-limitations-table](/_files/land_cover/table5-overall-landsat-sensor-data-availability-in-dea-dc-used-for-lc-classification.PNG)

*Table 1.* Overall Landsat sensor data availability in the DEA data cube used for the Land Cover classification.

![DEA-datasets-used](/_files/land_cover/table6-datasets-DEA-Essential-Descriptor-info-for-DEA-LC-classification.PNG)

*Table 2.* Datasets within DEA used to provide Essential Descriptor information for the DEA Land Cover classification.

### Inconsistent data presence in three Western Australia tiles

An issue has been identified with data presence in three tiles in Western Australia, particularly between 1988 and 2005. The affected tiles are *x39y49*, *x40y47*, *x41y45*. For a quick visualisation of these locations, the [DEA Explorer](https://explorer.dea.ga.gov.au/products/ga_ls_landcover_class_cyear_3) can be consulted. 

This issue arises due to the Ground Quality Assured (GQA) value falling below the acceptable threshold set by the DEA for products derived from Landsat. The root cause of this anomalous behaviour lies in the [Analysis Ready Data (ARD)](https://knowledge.dea.ga.gov.au/guides/reference/analysis_ready_data_corrections/), which serves as the source for the Land Cover product. The areas affected by this issue correspond to regions where ground control points may experience movement over time, such as shifting sand dunes, leading to inconsistencies in the orthorectification process.

![timeseries missing data tiles](/_files/land_cover/gqa_tiles_timeseries_geomad_obs_count_gmad.gif)

*Figure 1.* Timeseries animation showing the frequency of missing data in the tiles *x39y49*, *x40y47*, *x41y45*. On the left, true colours timeseries of the yearly geomedian. On the right, timeseries of the yearly clear observation count.

## Accuracy

A validation assessment has been undertaken for both the versions of Land Cover: the former Collection 2 (C2; i.e., Version 1), and the current Collection 3 (C3; i.e., Version 2). The below section outlines the accuracy of both versions to assist users in understanding the differences between the two versions.
The validation metrics reported were produced for Level 3 and they integrate the results from the validation of the sub-components of Level 1, the Artificial Surface model, and the Cultivated model.

### Summary of differences between Land Cover C2 (version 1) and C3 (version 2)

* Collection 3 generally aligns with Collection 2 in terms of classification performance, with trends across time periods and classes mostly consistent. However, some deviations from this pattern have been observed across different locations and times, particularly in the Cultivated Vegetation class.
* Collection 3 classification shows better overall consistency across different validation methods.
* An improvement in artificial surface classification was observed in C3. More urban areas appear to be correctly identified, although there is a slight increase in false positive identification of urban areas in the central Australian desert or sandy regions. 
* Slight improvement is seen in Woody Cover for the Terrestrial Vegetation classification.
* Substantial increase in Landsat 7 stripe artefacts in C3, due to  Landsat 8 scenes being filtered out by bad geometric quality assessments.
* General increase in number pixels with no data surrounding water bodies.
* Misclassification of water persistence over the ocean in C3.


|   |   |   |
|---|---|---|
| a) ![Improvement artificial class Degradation water persistence, Level 4](/_files/land_cover/2.degr_ocean_water_persistance-degr_stripes-impr_urban.gif) | b) ![Improvement woody cover, Level 4](/_files/land_cover/10.improvement-woody_cover_pine_plantation-zoomed-in-level4.gif) | c) ![Degradation cultivated, Level 4](/_files/land_cover/11b.example_cultivated_degradation_level4._2015gif.gif) |

![legend Level 4](/_files/land_cover/legend_lc_level4_horizontal.png)

*Figure 2.* Animations showing examples of differences in Level 4 classification between Land Cover C3 and C2 (i.e., version 2 (V2) and version 1 (V1), respectively). *a)* illustrates the improved artificial surface classification in the greater Melbourne area; stripe artifacts and incorrect water persistence classification can also be observed. *b)* displays a pine plantation near Kinglake West (VIC), which Collection 3 (i.e., V2) appears to classify correctly as being > 65% woody cover. *c)* shows an example of degradation in cultivated area classification in the Cassowary Coast (northern QLD), primarily due to the misclassification of cultivated land as herbaceous natural vegetation.


|   |   |   |
|---|---|---|
| a) ![Degradation false positives artificial, Level 3](/_files/land_cover/1.degradation-urban_false_positives-level3.gif) | b) ![Improvement, cultivated better classified, Level 3](/_files/land_cover/12b.improvement_cultivated_level3_2015.gif) | c) ![Degradation missing pixels around waterbodies, Level 3](/_files/land_cover/9.degradation-missing_pixels_waterbodies-level_3.gif) |

![legend Level 3](/_files/land_cover/legend_lc_level3_horizontal.png)

*Figure 3.* Animations showing examples of differences in Level 3 classification between Land Cover C3 and C2 (i.e., version 2 (V2) and version 1 (V1), respectively). *a)* shows Portland (VIC) and the surrounding area, where an improvement in the artificial surface classification in Collection 3 (i.e., V2) can be observed in the town to the east, although false positives can also be seen on the sandy terrain in the western part of the displayed area. *b)* displays an instance where Collection 3 (i.e., V2) more accurately identifies cultivated areas in a region on the southern coast of Western Australia, particularly in the northern part of the image, while the eastern part appears slightly noisier. *c)* highlights the increase in pixels with missing values around water bodies in Collection 3 (i.e., V2) at Lake Eildon in Victoria. 


### Collection 2 Validation

The product was validated using 6000 points spatially distributed over Australia. These points were created using a stratified random sampling approach slightly adjusted for oversampling. This process was conducted for 2010 and 2015 creating 12000 samples in total. After removing points with No Data and spurious values the total number was 11750. The sample points were divided into clusters for visual assessment against the outputs from the classification and assessed individually from a pool of 10 people. To compare the individual biases of the individual assessors, an additional set of validation points were created that all assessors evaluated, the results are shown in Table 4. Where assessors could identify a predominant land cover (i.e. not "mixed" pixels or "unsure"), all assessors agreed 75 % of the time. 

*Table 3* contains the overall accuracy for all classes. The term "support" refers to the number of validation points used in the calculation of that accuracy value. 

![Overall accuracy of DEA Land Cover is 80%. 2010 accuracy is 82%, 2015 accuracy is 78%.](/_files/land_cover/table2-overall-accuracy-dea-lc.PNG)

*Table 3*. Overall accuracy of DEA Land Cover.

*Table 4* contains per-class accuracy information. "Precision" refers to the ability of a classification model to return only relevant instances. "Recall" refers to the ability to identify all relevant instances. The “F1 score” is a combination of precision and recall and an overall measure of accuracy. Classes such as artificial surfaces, natural aquatic vegetation and water had high accuracies. Classifying cultivated terrestrial vegetation and bare surfaces was challenging and accuracies were the lowest of the six classes presented here.

![Table showing accuracy per class, including precision, recall, F1 score and support values per class. ](/_files/land_cover/table3-per-class-accuracy-info-dea-lc.PNG)

*Table 4*. Per-class accuracy information for DEA Land Cover.

![table showing the agreement between assessors.](/_files/land_cover/table4-inter-assessor-agreement.PNG)

*Table 5*. Inter-assessor agreement.

### Collection 3 Validation

In order to understand the extent of change between the versions, validation against three data sources was undertaken: ``validation points`` reused from Collection 2, with the addition of point attributes from Köppen Climate Zone and State/Territory, added to facilitate segment analysis; the [``GLANCE (Global Land Cover Estimation)``](https://www.nature.com/articles/s41597-023-02798-5) global dataset of independent "ground truth" data; and the Land Cover ``Collection 2 data``. 

To account for the additional validation points, the Collection 2 (C2) validation was run again and compared with the results from Collection 3 (C3).

Both C3 and C2 showed overall degradation in 2010 compared to 2015, a trend that is propagated from the Level 1 and individual ML models results. The performance metrics with the validation points show an overall alignment of the two collections, with minimal differences across categories, except for the Recall values of Cultivated Vegetation and Artificial Surface (both higher in C3 for the year 2010) (*Tables 6 and 9*).
C3 demonstrated a more reasonable classification on the GLANCE dataset, particularly for the Natural Vegetation class, which can be intuitively interpreted as the Agriculture category of the GLANCE dataset (*Tables 7, 8, 10, 11*).

C3 exhibited better consistency in results against the validation points and the GLANCE data. However, some disalignment between ground truth datasets is present in both collections for certain classes (e.g., Bare Surfaces). Some classes, such as the Artificial Surface, have too few validation points to be considered statistically significant. Hence, the classification metrics should be interpreted with caution and understood in relative terms, highlighting the differences between C2 and C3, rather than the absolute performance of each.

When C3 was compared directly with the output of C2 (*Table 16*), it showed good agreement for most of the Level 3 classes. Two notable exceptions were the Cultivated Vegetation class and the Artificial Surface class. For Cultivated Vegetation, the performance against the validation data did not suggest a substantial difference in overall accuracy between C2 and C3; thus, the disalignment observed in *Table 16* could be due to possible inconsistencies in classification between the two collections, but not necessarily an improvement or degradation. The difference observed in the Artificial Surface classification may be influenced by the increased accuracy of C3. 

**Validation Points 2010**

|   |   |
|---|---|
| a) ![C2 2010 Accuracy](/_files/land_cover/c2_l3-13.png) | b) ![C3 2010 Accuracy](/_files/land_cover/c3_l3-14.png) |

*Table 6*. Classification metrics of Collection 2 (*a*) and Collection 3 (*b*) in the year 2010, using the validation points as ground truth.

The ``Macro-Average`` is the unweighted mean of each metric calculated independently for all classes. Each class contributes equally, regardless of its frequency in the dataset. It should be interpreted as "unbiased" due to the highly skewed nature of the validation points. 

The ``Weighted-Average`` is the average of each metric weighted by the support (TP + FN; i.e., True Positives and False Negatives) for each class. The weight reflects the proportion of each class in the "Truth" such that more frequent classes have a greater impact on the overall average.

![C2 2010 Matrix](/_files/land_cover/c2_l3-15.png)

*Table 7*. Confusion matrix: Collection 2 predictions vs. validation points for 2010.

![C3 2010 Matrix](/_files/land_cover/c3_l3-16.png)

*Table 8*. Confusion matrix: Collection 3 predictions vs. validation points for 2010.

**Validation Points 2015**

|   |   |
|---|---|
| a) ![C2 2015 Accuracy](/_files/land_cover/c2_l3-9.png) | b) ![C3 2015 Accuracy](/_files/land_cover/c3_l3-10.png) |

*Table 9*. Classification metrics of Collection 2 (*a*) and Collection 3 (*b*) in the year 2015, using the validation points as ground truth.

![C2 2015 Matrix](/_files/land_cover/c2_l3-11.png)

*Table 10*. Confusion matrix: Collection 2 predictions vs. validation points for 2015.

![C3 2015 Matrix](/_files/land_cover/c3_l3-12.png)

*Table 11*. Confusion matrix: Collection 3 predictions vs. validation points for 2015.

**GLANCE 2010**

![C2 2010 GLANCE C2](/_files/land_cover/c2_l3-19.png)

*Table 12*. Confusion matrix: Collection 2 predictions vs. GLANCE dataset for 2010.

![C3 2010 GLANCE C3](/_files/land_cover/c3_l3-20.png)

*Table 13*. Confusion matrix: Collection 3 predictions vs. GLANCE dataset for 2010.

**GLANCE 2015**

![C2 2015 GLANCE C2](/_files/land_cover/c2_l3-17.png)

*Table 14*. Confusion matrix: Collection 2 predictions vs. GLANCE dataset for 2015.

![C3 2015 GLANCE C3](/_files/land_cover/c3_l3-18.png)

*Table 15*. Confusion matrix: Collection 3 predictions vs. GLANCE dataset for 2015.

**C3 vs C2**

|   |   |
|---|---|
| a) ![C3 vs C2 2010](/_files/land_cover/c3_c2_l3-22.png) | b) ![C3 vs C2 2015](/_files/land_cover/c3_c2_l3-21.png) |

*Table 16*. Classification metrics generated by using C2 data as "ground truth" for the C3 output for 2010 (*a*) and 2015 (*b*) .


% ## Quality assurance
