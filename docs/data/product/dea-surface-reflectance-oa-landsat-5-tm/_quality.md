## Accuracy

For information on the accuracy of the algorithms for test locations, see Zhu and Woodcock (2012) and Zhu, Wang and Woodcock (2015).

### Limitations

#### Fmask

Fmask has limitations due to the complex nature of detecting natural phenomena, such as cloud. For example, bright targets, such as beaches, buildings and salt lakes often get mistaken for clouds.

Fmask is designed to be used as an immediate/rapid source of information screening. The idea is that over a temporal period enough observations will be made to form a temporal likelihood. For example, if a feature is consistently being masked as cloud, it is highly probable that it is not cloud. As such, derivative processes can be created to form an information layer containing feature probabilities.

Edges and fringes of clouds tend to be more opaque and can be missed by the cloud detection algorithm. In this instance, applying a morphological dilation will grow the original cloud object and capture edges and fringes of clouds. However, it is important to note that other cloud objects could also be dilated. Be mindful of single-pixel objects that could grow to become large objects. Consider filtering out these small objects prior to analysis.

#### Angular measurement and shadow classification

The Digital Elevation Model (DEM) is used for identifying terrain shadow, as well as producing incident and exiting angles. It is derived from the Shuttle Radar Topography Mission (SRTM) and produced with approximately 30 m resolution. As such, any angular measurements and shadow classifications are limited to the precision of the DEM itself. The DEM is known to be noisy across various locations, so to reduce any potential extrema, a Gaussian smooth is applied prior to analysis.

## Quality assurance

The authors evaluated the Fmask algorithm using a total of 188 randomly selected Worldwide Reference System (WRS) locations across nine latitudinal zones. From these locations, 212 Landsat scenes were used as a reference set as part of the accuracy assessment. The average accuracy for cloud detection was 96.4%.

The calculation of the satellite and solar positional geometry datasets are largely influenced by the publicly available ephemeris data and whether the satellite has an on-board GPS, as well as the geographical information that resides with the imagery data and the metadata published by the data providers. The code to generate the geometry grids is routinely tested and evaluated for accuracy at >6 decimal places of precision.

The technical report containing the data summary for the Phase 1 DEA Surface Reflectance Validation is available: [DEA Analysis Ready Data Phase 1 Validation Project : Data Summary](http://pid.geoscience.gov.au/dataset/ga/145101)

