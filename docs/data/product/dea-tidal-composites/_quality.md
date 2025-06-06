## Limitations

* Natural biases exist in the imaging of coastal tide ranges by orbiting spectral satellites such as Sentinel-2. Attempts to quantify these offsets are reported in the supporting [DEA Intertidal Tide Attribute layers](/data/product/dea-intertidal/?tab=description#tidal-attribute-layers). These biases mean that while DEA Tidal Composites represent the upper and lower 15 % of all satellite observations of the local tide range, they do not represent the upper and lower 15 % of the full astronomical tide range. This means DEA Tidal Composites may not capture the extreme ends of the local tide range at some locations.
* These biases may extend to seasonal and diurnal effects in the imagery, where the low- and high-tide imagery from which the composites are derived may not be evenly distributed across seasons in different geographic regions. We recommend users to refer to the accompanying graphs of satellite observations and their tidal distribution provided through the DEA Maps platform to assess potential impacts.
* DEA Tidal Composites is delivered as an annually updated dataset, generated from rolling 3-year epochs of input data. In some locations, particularly those affected by regular cloud cover, the number of clear images from the upper and lower parts of the observed tide range may be few, resulting in artefacts in the imagery. 
* To maximise data density for clear geomedian outputs, we use a minimum number of 20 input observations. For pixels where less than 20 observations were available during the epoch, the resulting spectral geomedian values should be considered unreliable. The [qa_count_clear](./?tab=specifications#bands) layer identifies these pixel locations.
* Tidal modelling is used to subset and select imagery to represent the tidal stages of oceanic and coastal intertidal regions.  The geomedian values for terrestrial pixels produced as part of this subsetting process will vary based on these tidal subsets, but are not reflective of any specific terrestrial environment constraints.
* Data input into the compositing process has been filtered by sun angle and satellite acquisition geometry to remove observations with a high likelihood of sun glint. However, some residual glint may still occur, particular in the north-eastern regions of the country, reducing the quality of the geomedian imagery.
* Offshore shallow water regions such as the Great Barrier Reef can be impacted by a lower quality and number of ARD observations in the Sentinel-2 archive. These regions have been excluded from the current release of the DEA Tidal Composites product, resulting in notable gaps particularly across south-eastern extents of the reef. The impact and extent of this issue varies across each annual composite and is under investigation for future iterations of the product.
* Due to a scarcity of quality input data available for the 2016 layer of this dataset, this layer is less complete than other years with no datasets available for a range of locations across the country. In many places, low quality data inputs also mean that fewer extreme tidal observations were likely captured, resulting in less representative low and high tide coverage.

## Accuracy

### Tide modelling

The ensemble tide modelling for this product utilised the same input data, models, and temporal epochs as is used in the generation of the [DEA Intertidal](/data/product/dea-intertidal/) product suite. Therefore the [DEA Intertidal Elevation Uncertainty](/data/product/dea-intertidal/?tab=description#core-product-layers) dataset is useful to evaluate both a) highly dynamic coastal environments where tide modelling is less certain and b) geographic influences on tide modelling uncertainty. The latter exist in places where underlying inputs to tide modelling (such as local bathymetry) results in lower certainty in the global tide model. An outcome of this type of uncertainty is that the absolute modelled tide height values may be incorrect. For DEA Tidal Composites, this may result in a slight offset in absolute tide heights at some locations but is unlikely to alter the images that are selected in the upper and lower 15th percentile ranges of tide heights as the overall trends in tidal changes are still maintained by the tide modelling.

### Geomedian calculation

Accuracies and limitations related to geomedian compositing of observations are discussed in [Roberts et al. (2017)](https://doi.org/10.1109/TGRS.2017.2723896).

## Quality assurance

### Data pre-processing

Only high-quality data was included as an input into DEA Tidal Composites. Data pre-processing was conducted, involving identifying and removing pixels that are impacted by clouds, cloud-shadow, and sunglint.

### Code testing

Code used to generate DEA Tidal Composites is run against automated [integration tests](https://github.com/GeoscienceAustralia/dea-intertidal/tree/develop/tests) to ensure that data quality is maintained after the code has been updated. These tests verify that the entire product generation workflow is performing as expected and is a way that we track changes in product accuracy over time.

% ## Known issues

% :::{dropdown} 1 Jan 2020: Example issue
% :open:
%
% This uses the `:open:` option because it is an open issue.
% :::

