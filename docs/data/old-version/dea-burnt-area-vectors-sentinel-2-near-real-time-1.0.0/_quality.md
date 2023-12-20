## Accuracy

There are a number of limitations when using this dataset to locate or map burnt area. There are limitations that apply to all Earth Observations with satellites and those specific to this product.

#### *Limitations of Earth Observations*

Observation of the landscape by this service depends on having clear skies. Both cloud and smoke will obstruct the observation of the Earth’s surface. Furthermore, the satellites do not observe all places all of the time. The two Sentinel 2 satellites (A and B), which are the basis for this service, each view a given 320 kilometre wide strip of Australia only once every 10 days. This means there will be up to a five day gap between observations of any point on the Australian continent. The observations show only what was visible on the day of the satellite pass and at the time it is overhead.

Fires are fast moving and the situation on the ground can change rapidly. No decisions on life or property should be made based on this data. For local updates and alerts, please refer to your state emergency or fire service.

#### *Limitations specific to this dataset*

A number of changes in the landscape with similar characteristics to burn appear in this dataset. These include but are not limited to:

* Forestry harvesting
* Land clearing
* Vegetation dieback
* Extreme dry conditions during a drought
* Increase in water body area

A number of factors may contribute to a burnt area from an actual fire not being visible in this product. Potential situations in which a burnt area may appear to have very little or no change from the baseline state are as follows:

* A burn in shrubland or grassland that experience a seasonal or less frequent cycle of greening and drying out will not appear strongly in the dataset. This is due to the baseline image being quite dry. As a result this area will appear sparsely vegetated in the baseline and little change will be seen to occur.
* Burns with low severity that only burn the understory in forested areas will be difficult to identify. This is due to the remaining green canopy obscuring the signal of the burn. This is likely to affect the detection and mapping of cool season control burns.

## Quality assurance

Product accuracy is firstly dependent on the accuracy of the underpinning Earth Observation data. The daily Sentinel-2 (A and B combined) NRT provisional satellite data provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

These Earth Observation metrics are based on rigorous and peer reviewed research and have been used within the wider scientific community to understand burn characteristics within the landscape. However, this methodology has not been used as a near real-time and continuously processing continental scale output, such as in our web mapping service. The use of these metrics and this data is preliminary and provisional in nature and is still undergoing further development. These metrics should be used as a preliminary screening tool, and not an accurate identification of fire extent. These metrics should be used in combination with each other and can be used with other datasets to strengthen the agreement that the area has indeed been burnt. No decisions on life or property should be made based on this data.

To mitigate the impact of poor quality observations and other artefacts, locations with nodata (-999) values have been removed from the input dataset and then the data are screened using the Pixel Quality product (fmask) to remove cloud, cloud shadow, water and snow; leaving only “valid” data. However, it should be noted some poor pixels are likely to still be included in the data after screening.

