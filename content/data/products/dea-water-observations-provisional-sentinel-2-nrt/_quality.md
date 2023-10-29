## Accuracy

#### Accuracy

This is a rapid, provisional, product. It has not been validated and is of unknown accuracy. The accuracy of the original Water Observations from Space (WOfS) algorithms was assessed using an independent set of 3.4 million validation points using Landsat imagery only. A similar validation has not yet been performed on this Sentinel-2 product, and the accuracy described below may serve as only a rough indicator. 

Landsat WOfS validation points were identified based on visual interpretation of Landsat imagery within 20 test areas across Australia The points were identified in the same locations as the training data, but were selected from different years (i.e. imagery from one set of years was used to generate points to train the algorithm, and imagery from a separate set of years was used to generate the points that were used evaluate the accuracy of the algorithm).

The classification has an overall accuracy of 97%. Areas identified as water within the accuracy assessment data are being correctly identified 93% of the time and are being misclassified as not water 7% of the time. These errors of omission typically occur along rivers, small waterbodies and swamps where the presence of both water and vegetation within the pixel leads a failure to identify water. This means that the DEA Water Observations product is likely to underestimate the extent of water in locations that contain mixed water and vegetation pixels. As a consequence of this the product may not be fit for applications that require information about the inundation characteristics of vegetated wetlands, small farm dams, and rivers less than 50 metres wide. 

Water can be incorrectly detected by the classification algorithm in areas where steep terrain or tall buildings cause frequently shaded pixels. These errors of commission are occurring in 8% of samples used to evaluate the accuracy of the classification. This means that the product may overestimate the amount of water in locations that are adjacent to steep terrain or in dense urban areas. Terrain masks and urban masks were used in the confidence layer to reduce this overestimation, however some residual errors remain. As a consequence of this the product may not be fit for applications that require information about the inundation characteristics of urban areas or locations adjacent to steep terrain.

In addition to the limitations of the classification algorithm, the satellite observation frequency also introduces limitations to the product. The product is likely to be underestimating the extent of inundation for infrequent flood events because the 5 day revisit frequency (best case scenario notwithstanding the possibility of cloud obscuring the floodwaters) will potentially fail to observe the flood peak. This is an intrinsic limitation of the observation strategy. As a consequence of this limitation, the product is not suited to applications that require a. the identification of a ‘maximum extent of inundation’ line, or b. detailed information about the extent of infrequent flood events.

#### Limitations

Observation of Earth by the satellites used for this service depends on clear skies. Furthermore, the satellites do not observe all places every day. Each of the Sentinel-2 satellites, which are the basis for this service, view a given 290 kilometre wide strip of Australia only once every 10 days. The observations show only what was visible on the day of the satellite pass. As a result, not all historical floods will have been observed by satellite.

The automated surface water detection algorithm, which has been developed by Geoscience Australia, can sometimes mistakenly label large buildings; cloud shadow; large uniform black tarpaulins; or snow as "water". The algorithm is designed to locate large areas of water and as a result may miss small water bodies. 

The algorithm also uses 'fmask' for cloud masking, this method is known to have limitations in correctly identifying clouds, particularly across bright substrates like urban areas, beaches and salt-pans.

The satellite archive used for this service is of limited duration (most recent 3 months), and subject to the cloud and repeat coverage restrictions noted above. In addition, Australia is subject to wide variations in weather and climate which can lead to lengthy periods where areas are not observable.

This product is produced at 10 metre resolution. This is achieved by resampling the 20 metre Sentinel-2 spectral bands to 10 metre resolution using "bilinear" resampling. This is likely to affect the ability of the product to correctly classify narrow areas of water (e.g. less than 20 metres in width).

% ## Quality assurance

