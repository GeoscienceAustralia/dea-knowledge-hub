## Accuracy

For a full discussion of the accuracies and limitations of DEA Waterbodies, please refer to [Krause et al. 2021](https://doi.org/10.3390/rs13081437). 

This product shows the wet surface area of waterbodies as estimated from satellites. It does not show depth, volume, purpose of the waterbody, nor the source of the water. Larger waterbodies are easier to detect, and smaller or narrower waterbodies are harder to detect. Area estimates should be compared to additional data for verification.  

### Inaccuracies inherited from DEA Water Observations (WO)

Many of the inaccuracies and limitations of DEA Waterbodies polygons are inherited from the DEA Water Observations (WO) product on which it is based. WO has a number of known limitations, affecting the classification of DEA Waterbodies. WO uses the spectral signature of water to classify wet pixels and is known to be less accurate in locations where water and vegetation are mixed. This includes locations such as rivers with vegetated riparian zones and vegetated wetlands. The effect of this can be seen by the discontinuity of narrower river features identified within DEA Waterbodies and an under-representation of water within vegetated wetlands, such as the Macquarie Marshes, NSW.

Other known WO limitations have been minimised by our filtering processes used to produce the DEA Waterbodies polygons. Issues with mixed water and vegetation pixels around features like small farm dams have been avoided by limiting the size of mapped waterbodies to at least three Landsat pixels. Misclassification of dark shadows as water in high-density cities has been handled by removing any waterbody polygons within CBDs. Intermittently misclassified features — which return valid results only a handful of times over the 32-year study period — are also filtered out by testing for the number of valid observations returned for each pixel.

Despite these fixes, some errors remain in the final waterbodies dataset. Steep terrain shadows present a known difficulty for the WO classifier, due to the presence of dark shadows. While WO has attempted to mitigate this issue, some misclassification remains. We have not specifically attempted to address these errors within this version of the product. As such, a negligible number of the identified waterbodies may in fact be artifacts caused by terrain shadow. The signal-to-noise ratio over deep water areas has also not been addressed here and may result in some pixels missing from the centre of deep waterbodies. This may result in some doughnut-shaped mapped polygons. Similarly, different water colours may interfere with the decision-tree classifier, resulting in very turbid or coloured waterbodies being misclassified.

The automatic cloud-masking algorithm used in this analysis can misclassify bright, white sands seen on the bottom of some waterbodies as clouds. This issue is particularly problematic where these bright sands are only exposed when the waterbody begins to empty, resulting in the bright sands being seen inconsistently over time. It is very difficult to accurately cloud-mask these sands as they are seen in some scenes but not others, in the same way that clouds come and go between scenes. When these sands are incorrectly classified as cloud, the scene is thrown out as being unsuitable resulting in very few ‘clear’ scenes. In this version of DEA Waterbodies, we note it as a limitation that results in short or missing timeseries. 

Some larger salt lakes in Australia have very few records currently available due to this issue. If less than 90% of the total waterbody is observed on any one day, due to cloud cover or missing data, then that observation is marked as a missing value. For larger bodies, which may cross multiple swath boundaries or suffer from misclassifications, this can be problematic. 

For a full discussion of the limitations and accuracy of WO, see [Mueller et al. (2016)](https://doi.org/10.1016/j.rse.2015.11.003).

% ## Quality assurance

