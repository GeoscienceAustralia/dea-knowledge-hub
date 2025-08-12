## Limitations

This product depends on having clear skies in order to observe the landscape, as both cloud and smoke will obstruct the observation of the Earth’s surface. Furthermore, the three Sentinel-2 satellites (A, B, and C) which are the basis of this service each view a given 320 km wide strip of Australia once every 10 days. This means there will be up to a 5-day gap between observations of any point on the Australian continent. The observations show only what was visible at the time that the satellite passed overhead. Since weather conditions can change rapidly, the actual condition of vegetation on the ground may change between the last time that the satellite went overhead and the next time it passes the same location.

No decisions on life or property should be made based on this data. For local updates and alerts, please refer to your state emergency or fire service

## Quality assurance

The quality of the data is dependent on the underlying Analysis Ready Data (ARD). If the ARD scenes do not pass a quality check for georeferencing accuracy they will not be included in the DEA FMC product. Geometric Quality Assessment (GQA) metadata provides information about the georeferencing accuracy of each ARD scene. Scenes are excluded from processing for DEA FMC if QGA indicates they are not accurate to within one pixel.

Cloud masking is conducted using the Sentinel-2 Fmask algorithm. This algorithm’s performance on Sentinel-2 has known issues, in particular the issue of false negatives in cloud detection. This is due to Sentinel-2 A, B, and C lacking a thermal IR band which would be used for detecting clouds. At the time of publication, the Fmask cloud algorithm is the best choice available; however, in the future, other options may become available.
