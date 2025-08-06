## Limitations

Observation of the landscape by this service depends on having clear skies. Both cloud and smoke will obstruct the observation of the Earth’s surface. Furthermore, the satellites do not observe all places all of the time. The three Sentinel-2 satellites (A, B and C), which are the basis for this service, each view a given 320 kilometre wide strip of Australia only once every 10 days. This means there will be up to a five-day gap between observations of any point on the Australian continent. The observations show only what was visible on the day of the satellite pass and at the time it is overhead.

Weather conditions can change rapidly and the condition of vegetation on the ground may differ from what this product reports. No decisions on life or property should be made based on this data. For local updates and alerts, please refer to your state emergency or fire service.

## Quality assurance

The quality of the data is dependent on the underpinning EO data (ARD) – if the ARD scenes do not pass a quality check for georectification they will not be processed for FMC and are left out of the product.

The cloud masking of the product is conducted using Sentinel-2 Fmask algorithm. This algorithm’s performance on Sentinel-2 has known issues and false negatives in cloud detection are a known issue. This is due to Sentinel-2 A, B and C not having a thermal IR band which is beneficial for the detection of clouds. At the time of publication, the Fmask cloud algorithm was the best choice available. In the future other options will be explored as they become available.

% ## Accuracy
