## Accuracy

####  Limitations of the Implementation Method

DEA Land Cover is created by combining multiple layers that each describe features in the landscape. In doing so the extents of each layer do not necessarily completely align, and some no-data points can cross between outputs. As a result, there are some level 4 classes that only report detail to level 3 as the details of cover fraction and water persistence do not have corresponding data in the respective datasets. This specifically relates the classes of Water, NS and NAV in areas near water bodies and the intertidal zone, however the number of affected pixels is small.  

#### Level 3 Class Limitations

**Cultivated Terrestrial Vegetation (CTV)**  

Managed plantations and some orchards and tree crops are not currently distinguishable from semi-natural or natural terrestrial vegetation and are not yet incorporated in the area of CTV.  Reference can be made to Australia’s National Plantation Inventory. In savanna regions (e.g. Queensland, Northern Territory and Western Australia), variable cycles associated with fires, inundation, drought and rainfall lead to greening or browning of natural vegetation that mirrors the seasonal or management-induced behavior of cultivated land. This leads to some areas of NTV, NS or NAV being misclassified as CTV. For example, the anomalous high levels of rainfall in 2010 led to vegetation growth patterns that were classified as cultivated vegetation, these false positives reduced the precision of the class in that year. Several natural vegetation types, particularly in the monsoonal north, are mapped as CTV due to burning, which can be associated with the indigenous management cycle. Saltmarsh and surface algae on mudflats can also be misclassified. Areas of bare soil exposed for long periods during the agricultural cycle or management activities, and sparse vegetation (when areas are not in use or fallow such as during drought periods) can be assigned as Natural Surfaces (NS).  This is particularly the case where areas have experienced low cover for prolonged periods within a year.  

**Natural Terrestrial Vegetation (NTV)**  

The NTV category can transition into the NS category between years when a highly variable Landsat satellite spectral signature is observed due to changes in vegetation productivity and moisture content. The transition of NTV to NS is particularly evident when comparing periods with rainfall above (as in 2010) or below (e.g. drought; as in 2015) the average. Some confusion between surfaces that are primarily bare surfaces and non-photosynthetic vegetation remains and is also partly a function of the spectral reflectance of the underlying soil type. Vegetated areas shadowed by terrain can also be misclassified as non-vegetated. Areas of very low vegetation coverage are associated with the NS rather than NTV category, with the cover percentages shown as percentage bare. The assignment of vegetated suburbs to NTV is largely correct, but AS surfaces located beneath the canopy are not currently represented in the product. Some confusion between CTV and NTV can occur because of natural seasonal changes in native vegetation. The edges of salt lakes may be misclassified as NTV.  

**Natural Aquatic Vegetation (NAV)**  

Currently only mangroves are mapped in the NAV class. Other vegetated natural landscapes (e.g. saltmarsh, river red gum forests in the Murray Valley, surface algae and other inland wetlands) where water significantly influences edaphic conditions of substrate are not mapped. This is because, in the current implementation, the water mask is included to assist in the differentiation of vegetation and non-vegetation as the presence of water creates excess noise in the underlying Fractional Cover product. To reduce this noise, the WOfS product is used as a water mask in the Fractional Cover product, and hence it is unlikely to produce the combination of vegetation and water required for the NAV class.

**Artificial Surfaces (AS)**  

Misclassification occurs with natural surfaces, particularly in the arid and semi-arid regions, open cut mine sites, salt lakes and pans, sand dunes and beaches. This is attributed to similarities in the variance of spectral signatures over a year.  Misclassification occurs in some cultivated areas attributable to the predominance of sparse vegetation or when land is left fallow for most of the year.  The current temporal variance mask is 250 m in spatial resolution, compared to the 30 m land cover product, resulting in artefacts appearing in the land cover from the masking process. In addition, urban areas with an area less than 250 m are often excluded.  Cloud and data quality issues can lead to incorrect assignment of other land cover classes to AS such as in south- west Tasmania.    

**Natural Surfaces (NS)**  

Land used for agriculture may be associated with an NS class if ploughing or tillage has occurred and the vegetation cover remains low during the calendar year. Areas mapped as NS may, under certain circumstances (e.g. during drought) temporarily transition to or from CTV. This occurs because of the dominance of non-persistent vegetation (e.g. short crop life spans), desiccation, removal during dry periods or management practices (e.g. left as fallow).  Where acquisition of cloud-free Landsat satellite sensor data has been infrequent, less information on the inter-annual variability of vegetation is provided. Where cloud cover is extensive (e.g. in Tasmania), the number of scenes for land cover classification is reduced and this can compromise classification of NS, particularly where bare surfaces alternate with vegetation. Confusion between natural surfaces and urban areas occurs because of similar spectral variation over an annual period.  

**Water**  

Areas of artificial and natural water are not differentiated, although the extent of the former is mapped within the existing Bureau of Meteorology Geofabric product. Due to the 30 m pixel size, rivers and water courses that cover less than a pixel, or with highly vegetated riverbanks are not captured, resulting in a patch-like representation of narrower rivers.  Areas of dark, wet soil are often misclassified as water, including in cultivated areas and mud flats.

#### Level 4 Class Limitations

**Lifeform**  

The woody discrimination is implemented using the Woody Cover Fraction product (Liao et al, 2020), which models woody cover from inputs of LiDAR including ICESat/GLAS, L-band SAR, field observation and Landsat satellite data. Issues arise in this dataset in areas dominated by short, woody vegetation such as heathland, and swampy regions where underlying water can introduce errors. Areas of woody savannah are also underrepresented due to the influence of the herbaceous understory dominating the observation.

**Vegetation Cover**  

The cover of vegetation is derived from the fractional cover product (Scarth et al, 2010), and as such reflects the limitations of that product, mainly difficulty with measurement of non-photosynthetic vegetation, and noise due to the presence of water in a pixel. Thus arid areas can be difficult to fully analyse for cover, leading to misclassifications between NTV, NS and CTV where cover is sparse (lower than 15 %).  

**Water Seasonality**  

This product does not yet identify consecutive months but rather the frequency of wet observations in the year, based on the WOfS product. Therefore, monthly statements are unlikely to be consistent across the continent. Mangroves are currently the only consistently identified NAV and water cannot be easily observed beneath their canopies, which are often dense.  Hence, the hydroperiod (and hence seasonality metrics) should be treated with some caution.    

**Water State**  

Mapping of ice and snow states has yet to be undertaken. Hence the water state class is currently limited to liquid only.  

**Intertidal**  

The intertidal areas carry the limitations of the ITEM product:   

* Intertidal areas are determined as a coastal mask, which currently identifies some non-tidal inland water bodies as tidal because of intra-annual changes in water extent.  
 
* This product is static and cannot be used to demonstrate change between two annual continental products.  
 

**Bare Gradation**  

Bare gradation is produced from the fractional cover product. Unlike the Vegetation Cover class, Bare Gradation is calculated from the median bare fraction, rather than consecutive, monthly green and non-photosynthetic fractions. Hence the bare fraction can be as low as 20 %, however this does not imply that the remaining fraction is healthy vegetation. Rather the remaining fraction is a mix of brown, dead and green vegetation, with intermittent green periods through the year, reflective of arid area vegetation types.   

#### Earth Observation Limitations

To generate the land cover classification for each calendar year, annual (January – December) statistics derived from Landsat-5, -7 and -8 observations are currently used, with each satellite sensor potentially observing the Australian landscape every 16 days. This brings an intrinsic limitation to land cover mapping as persistent cloud in some regions reduces the number of useable observations. This is particularly evident in Tasmania, and northern Australia during the monsoon period, where areas may not be observed for extended periods and parts or all of the intra-annual land cover cycle may be missed. These limitations can lead to misclassifications of land cover, particularly in dynamic environments. In a future release, a confidence layer will be included to help identify areas with poor observation frequency or other factors impacting the classification.  

An additional limitation of the Landsat series is the availability of data due to the ageing of each satellite. Landsat 5 was operational for over 25 years, but for much of the later years, data were only acquired when sunlight directly illuminated its solar panels.  This limited its operation across Australia, with coverage being seasonally dependent, and contracting north to a minimum in winter. In its last years the winter coverage usually only covered the northern coasts of Australia. Landsat 5 ceased regular operations over Australia in 2011, leaving just Landsat 7 until Landsat 8 was launched in 2013. Landsat 7 began service in 1999 as a replacement for Landsat 5. Initially Landsat 5 was switched off, but when Landsat 7 suffered a serious problem in 2003 due to the failure of its scan-line corrector (termed SLC-Off) Landsat 5 resumed service. The SLC-Off failure of Landsat 7 results in severe striping across every image from mid 2003 onwards, apparent in subsequent derived products. Landsat 8 has operated well since launch in 2013, with improved sensitivity, noise characteristics and data correction in comparison to the earlier sensors.   

The result of the availability of the satellites is that the most consistent data availability occurs when two satellites are in operation (most of the 2003 to present period). The least data availability is in 2011 – 2012 when only Landsat 7 was available with data containing the SLC-Off striping issue. The overall data availability for the Landsat satellites is shown in Table 5. The datasets used in this analysis are shown in Table 6. 

![table detailing availability of different Landsat satellites since 1986 and any known issues.](/sites/default/files/inline-images/eo-limitations-table.PNG)

![datasets within DEA used to provide essential descriptor information](/sites/default/files/inline-images/DEA-datasets-used.PNG)

% ## Quality assurance

