## Accuracy

The accuracy of the original Water Observations from Space (WOfS) algorithms was assessed using an independent set of 3.4 million validation points. The points were identified based on visual interpretation of Landsat imagery within 20 test areas across Australia. The points were identified in the same locations as the training data, but were selected from different years (i.e. imagery from one set of years was used to generate points to train the algorithm, and imagery from a separate set of years was used to generate the points that were used evaluate the accuracy of the algorithm).

The classification has an overall accuracy of 97%. Areas identified as water within the accuracy assessment data are being correctly identified 93% of the time and are being misclassified as not water 7% of the time. These errors of omission typically occur along rivers, small waterbodies and swamps where the presence of both water and vegetation within the pixel leads a failure to identify water. This means that the DEA Water Observations product is likely to underestimate the extent of water in locations that contain mixed water and vegetation pixels. As a consequence of this the product may not be fit for applications that require information about the inundation characteristics of vegetated wetlands, small farm dams, and rivers less than 50 metres wide. 

Water can be incorrectly detected by the classification algorithm in areas where steep terrain or tall buildings cause frequently shaded pixels. These errors of commission are occurring in 8% of samples used to evaluate the accuracy of the classification. This means that the product may overestimate the amount of water in locations that are adjacent to steep terrain or in dense urban areas. Terrain masks and urban masks were used in the confidence layer to reduce this overestimation, however some residual errors remain. As a consequence of this the product may not be fit for applications that require information about the inundation characteristics of urban areas or locations adjacent to steep terrain.

In addition to the limitations of the classification algorithm, the satellite observation frequency also introduces limitations to the product. The product is likely to be underestimating the extent of inundation for infrequent flood events because the 8 day revisit frequency (best case scenario notwithstanding the possibility of cloud obscuring the floodwaters) will potentially fail to observe the flood peak. This is an intrinsic limitation of the observation strategy. As a consequence of this limitation, the product is not suited to applications that require a. the identification of a ‘maximum extent of inundation’ line, or b. detailed information about the extent of infrequent flood events.

## Limitations

Observation of Earth by the satellites used for this service depends on clear skies. Furthermore, the satellites do not observe all places every day. The Landsat satellites, which are the basis for this service, view a given 185 kilometre wide strip of Australia only once every 16 days. The observations show only what was visible on the day of the satellite pass. As a result, not all historical floods will have been observed by satellite.

The automated surface water detection algorithm, which has been developed by Geoscience Australia, can sometimes mistakenly label large buildings; cloud shadow; large uniform black tarpaulins; or snow as "water". The algorithm is designed to locate large areas of water and as a result may miss small water bodies. 

The satellite archive used for this service is of limited duration (1986 to present), and subject to the cloud and repeat coverage restrictions noted above. In addition, Australia is subject to wide variations in weather and climate. Therefore the absence of water observations prior to 1986 in a particular location does not provide certainty that surface water **will never** be observed there in future.

The probability that surface water may appear at a given location may vary over time due to changes in drainage and other infrastructure (such as dams). Where such changes have occurred, the historical water observations for that location may no longer give a true picture of the future probability of surface water being observed.

% ## Quality assurance

