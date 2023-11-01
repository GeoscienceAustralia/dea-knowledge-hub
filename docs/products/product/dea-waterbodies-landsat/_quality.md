## Accuracy

For a full discussion of the accuracies and limitations of DEA Waterbodies, please refer to [Krause et al. 2021](https://doi.org/10.3390/rs13081437). 

#### Inaccuracies inherited from DEA Water Observations (WO)

Many of the inaccuracies and limitations of the waterbody analysis are inherited from WO, with this product a reanalysis and mapping product built off the WO datasets. WO has a number of known limitations, and these manifest as misclassified waterbodies within this analysis. WO uses the spectral signature of water to classify wet pixels, and is known to be suboptimal in locations where water and vegetation are mixed. This includes locations such as rivers with vegetated riparian zones and vegetated wetlands. The effect of this can be seen by the discontinuity of narrower river features identified within this analysis, and an under representation of water within vegetated wetlands, such as the Macquarie Marshes, NSW.

Other known WO limitations have been limited through the filtering processes used to produce the map of waterbodies. Issues with mixed water and vegetation pixels around features like small farm dams have been avoided by limiting the size of mapped waterbodies to at least five Landsat pixels. Misclassification of water in deep shadows in high density cities has been handled by removing any waterbody polygons identified within CBDs. Intermittently misclassified features, which return valid results only a handful of times over the 32 year study period, are also filtered out by testing for the number of valid observations returned for each pixel.

Despite this, some errors remain in the final waterbodies dataset. Steep terrain shadows present a known difficulty for the WO classifier, due to the shadows produced. While WO has attempted to mitigate this issue, some misclassification remains. We have not specifically attempted to address these errors within this workflow, and as such, a negligible number of the identified waterbodies may in fact be artifacts caused by terrain shadow. The signal to noise ratio over deeper water has also not been addressed here, and may result in some pixels missing from the centre of deeper waterbodies, resulting in doughnut-shaped mapped polygons. Similarly, different water colours may interfere with the decision-tree classifier, resulting in very turbid or coloured waterbodies being misclassified.

The automatic cloud masking algorithm used in this analysis can misclassify bright, white sands seen on the bottom of some waterbodies as clouds. This issue is particularly problematic where these bright sands are only exposed when the waterbody begins to empty, resulting in the bright sands being seen inconsistently over time. It is very difficult to accurately cloud mask these sands, as they are seen in some scenes but not others, in the same way that clouds come and go between scenes. In this version of DEA Waterbodies, we have not addressed this issue, and note it as a limitation that results in short or missing timeseries; the sands are incorrectly classified as cloud, and the scene is thrown out as being unsuitable, resulting in very few ‘clear’ scenes. We hope to address this issue in the next release of the DEA Waterbodies product.

For a full discussion of the limitations and accuracy of WO, see [Mueller et al. (2016)](https://doi.org/10.1016/j.rse.2015.11.003).

% ## Quality assurance

