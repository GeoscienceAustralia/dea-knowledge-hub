% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/product_metadata_fields.html

## Caveats and Limitations

### Accuracy Considerations

- **Training data composition:** Regional training sets remain unbalanced for rare classes (e.g. [salt flat, seagrass in Region 1](./?tab=description#training-data)), which contributes to wider accuracy intervals and should be considered when interpreting those classes.
- **Probability masking:** Accuracy statistics only include samples with greater than or equal to 50% model probability. Areas with persistent cloud, haze, or spectral ambiguity may be masked operationally and will not have associated accuracy estimates.
- **Spatial extrapolation:** Spatial stratification reduces autocorrelation bias, but accuracy can still degrade in locations far from labelled samples or outside the environmental gradients represented in the combined parquet.
- **Model uncertainty:** Reported medians and 95% intervals reflect Monte Carlo sampling only; additional uncertainty from sensor noise, ancillary covariates, or downstream post-processing is not captured here.

### Sensor Tidal Bias

- **Sensor coverage and tidal phase:** Sentinel 2 acquisitions do not uniformly sample the [tidal cycle](/data/product/dea-intertidal/?tab=quality#caveats-and-limitations), so in some regions intertidal habitats may be under-represented or not fully characterised in either the training data or the predictions. For example, in a region where the highest portion of the tidal range/cycle is not observed by the sensor, training data and the associated covariates for classes such as saltmarsh may be biased towards a lower tide representation of that class.
- **Intertidal Seagrass Training Points:** Due to sensor tidal bias, some Intertidal Seagrass training points fall outside of the Intertidal Extent that is observed by the sensor, and which is used to constrain the extent of Intertidal/Seagrass model. These training data points are excluded from the model, as they fall below the Lowest Observed Tide of the sensor, meaning they will only be observed as sub-tidal seagrass points.

### Saltflat Mapping

Saltflat mapping accuracy results in the Classification layer were observed to be highly variable between the regional models. Reasons for this may include:

- limited proportional representation of Training Points for this class for regions where Saltflat is known to exist (e.g. in the South-East),
- lack of similar terrestrial class training points for differentiation resulting in false positives across Urban and Sand/Beach areas, and
- issues with cloud masking of highly reflective bright surfaces.

For these reasons, the Saltflat class has been removed from the core Classification layer, so these issues can be addressed in future versions of the product. The Saltflat probability layer has been retained, so users can make their own interpretation of the mapping extents based on local and regional knowledge, whilst considering the issues highlighted above.

### Constraint of the Intertidal Model and Definition of the Intertidal Class

To align with the extents of the DEA Intertidal product, the extent of the Intertidal/Seagrass model has been constrained to the high-confidence DEA Intertidal Extents product. All training data points that are located in this extent, and are not Intertidal Seagrass, are considered Intertidal for the purposes of the binary Intertidal/Seagrass model. 

By constraining the extent of this model, we are forcing the classification of pixels in this Intertidal class that likely represent L2 classes beyond Mudflats and Intertidal soft sediments that are not represented in the training data (e.g. rocky intertidal substratum and exposed coral reefs/platforms). This may have implications on the binary classification of the Intertidal Seagrass in the model and is an additional reason why we have conservatively mapped this class at a 70% probability in the classification model.

Future work will involve densification of the training data to include a more fully representative range of L2 classes considered in this Intertidal class.

### Connectivity Masking and Saltmarsh

The Saltmarsh connectivity thresholding assumes that the training data (which are located in predominantly near-shore coastal locations) encompass all possible saltmarsh locations and connectivity values. The limitations of this approach are acknowledged, as demonstrated by hard boundaries visible in the classified saltmarsh dataset such as in Princess Charlotte Bay, Qld. Future work will broaden the spatial range of saltmarsh training data that will improve the connectivity masking threshold used in this part of the workflow.

### Global Mangrove Watch Masking

The [Global Mangrove Watch (GMW) Habitat Mask](https://doi.org/10.5281/zenodo.7478491) (Bunting et al. 2025) is widely used in the coastal mapping and scientific community as a layer to constrain the mapping of Mangroves to suitable ecological conditions and zones. It is however acknowledged as a living dataset, with updates contributed by the community of new identified mangroves and mapping extents. For example, in the early stages of this project, new regions not captured by the GMW were identified in Batemans Bay, NSW, and these regions were added by GMW to the most recent version of the Habitat mask. 

Although the Classification layer has been masked by the GMW Habitat Mask, the Mangroves probability layer has not, and it is possible that users may be able to identify small areas of high-probability Mangroves not mapped by the masked classification layer. Users are encouraged to provide DEA with this feedback, so that we can continue to help the GMW initiative to provide the most suitable masking and mapping layers.

### Interpretation of Probability Layers and Implications for Change Applications

**Mixed and Transitional ecosystems:** Many ecosystems exist as highly mixed types or transitional ecosystems. These types of ecosystems, particularly when they exist in relatively even-cover proportions, are not well represented by categorical mapping products. These zones are often not captured in the 50% probability thresholded Classification layer, and may for example consist of pixels that are modelled with 34% Mangrove, 40% Saltmarsh and 26% Saltflat Probabilities.

**Probability Thresholding and Interpretation:** The 50% probability threshold applied to the Classification of Saltmarsh and Mangroves in the Classification layer is designed to provide a high-confidence model of the dominant ecosystem in each coastal pixel. As described above, in mixed or transitional pixels not mapped by the classification layer; or in instances where local knowledge of ecosystem characteristics or vegetation density/canopy cover requires a more nuanced approach, the Ecosystem probability layers are designed to support this interpretation.

Intertidal Seagrass is thresholded in the Classified layer at a 70% probability, primarily to account for inter-annual variability in this ecosystem, aimed at mapping regions of persistent cover over time. It is expected that the Probability layers for this ecosystem are used by seagrass mapping practitioners to enable a more detailed analysis of specific regions or ecosystem characterisation.

**Implications for Change Applications**: Change-based applications utilising the Classification layers are to be approached with caution:

- For classified ecosystems that are mapped at a probability of greater than 50%, these classes are still often in transition and may shift across those thresholds from year to year. Using the classified layer could potentially note the loss (or gain) of that ecosystem erroneously. Users should make use of the model probability layers to identify these areas and make case-specific judgement on usage. 
- In mixed or transitional ecosystems it is expected that change metrics will be highly sensitive and potentially erroneous in these cases. Again, users should make use of the model probability layers to identify these areas and make case-specific judgement on usage. 

It is important to note that annual models of ecosystem extents are influenced by:

- the seasonal characteristics of the year being modelled,
- the currency of the training data being applied to the modelling year, and
- the quality and number of EO datasets acquired and available over the modelling year.

Whilst the modelling process in this product has been designed to mitigate these influences and differences between annual products where possible, each of these factors impacts the modelling accuracy and characteristics of both the probability and classified layers of the product for each year. This should be considered when using any of the Product layers for change applications, and we recommend utilising the full suite of QA/QC layers and Accuracy results to assist with any change applications or metrics.

## Accuracy

The DEA Coastal Ecosystems mapping was validated using a Monte Carlo resampling workflow with spatial stratification (32 km tiles) to limit spatial autocorrelation (Lyons et al. 2018). Each iteration trains on ~80% of tiles, tests on the remainder, filters predictions by a greater-than-or-equal-to 50% class-probability threshold (to replicate the mapping methodology), and then reports accuracy for both the ecosystem model and the final output after seagrass modelling is applied to the tidal flat area. The validation metrics are thus indicative of the accuracy of the final categorical classification product, and are not strictly relevant to the model probability layers. Final accuracy metrics are summarised from the sampling distributions as the median with a 95% interval (which can be used as area multipliers if desired). Validation statistics are reported separately for the 2021 and 2022 mapping.

Comprehensive methodology notes are documented in the code repository (see the [Validation README](https://data.dev.dea.ga.gov.au/derivative/ga_s2_coastalecosystems_cyear_3_v1/auxiliaries/validation/Validation%20readme.pdf)), and the complete per-class/per-year outputs are available in the [full validation results](https://data.dev.dea.ga.gov.au/derivative/ga_s2_coastalecosystems_cyear_3_v1/auxiliaries/validation/coastal_ecosystem_validation_results.pdf).

### Regional summary per year

#### Year 2021

| Region | Overall Accuracy (Median [95% interval]) |
|--------|----------------------------------------|
| 1 | 0.949 [0.909, 0.971] |
| 2 | 0.915 [0.880, 0.944] |
| 3 | 0.883 [0.793, 0.930] |
| 4 | 0.932 [0.899, 0.970] |
| 5 | 0.973 [0.939, 0.994] |
| 6 | 0.947 [0.915, 0.970] |
| 7 | 0.941 [0.878, 0.976] |

#### Year 2022

| Region | Overall Accuracy (Median [95% interval]) |
|--------|----------------------------------------|
| 1 | 0.945 [0.901, 0.968] |
| 2 | 0.911 [0.871, 0.945] |
| 3 | 0.875 [0.785, 0.926] |
| 4 | 0.936 [0.904, 0.969] |
| 5 | 0.972 [0.939, 0.993] |
| 6 | 0.945 [0.914, 0.970] |
| 7 | 0.946 [0.888, 0.979] |

### Regional summary per class (combined years)

#### Region 1 (North West)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.874 [0.671, 0.979] | 0.947 [0.859, 0.986] |
| Mangrove | 0.989 [0.960, 0.999] | 0.982 [0.963, 0.995] |
| Saltmarsh | 0.909 [0.512, 0.989] | 0.634 [0.348, 0.821] |
| Seagrass | 0.000 [0.000, 0.933] | 0.000 [0.000, 0.033] |

#### Region 2 (North East)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.780 [0.641, 0.909] | 0.928 [0.839, 0.980] |
| Mangrove | 0.971 [0.933, 0.995] | 0.978 [0.934, 0.993] |
| Saltmarsh | 0.808 [0.537, 0.951] | 0.573 [0.417, 0.777] |
| Seagrass | 0.883 [0.746, 0.969] | 0.668 [0.433, 0.827] |

#### Region 3 (Gulf of Carpentaria)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.620 [0.393, 0.843] | 0.870 [0.711, 0.977] |
| Mangrove | 0.989 [0.961, 1.000] | 0.990 [0.973, 1.000] |
| Saltmarsh | 0.904 [0.455, 0.983] | 0.764 [0.605, 0.913] |
| Seagrass | 0.891 [0.664, 0.983] | 0.685 [0.296, 0.897] |

#### Region 4 (West)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.845 [0.671, 0.970] | 0.982 [0.930, 1.000] |
| Mangrove | 0.993 [0.907, 1.000] | 0.990 [0.941, 1.000] |
| Saltmarsh | 0.864 [0.582, 0.980] | 0.805 [0.501, 0.951] |
| Seagrass | 0.929 [0.066, 1.000] | 0.768 [0.059, 1.000] |

#### Region 5 (South West)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.858 [0.000, 1.000] | 0.873 [0.000, 1.000] |
| Mangrove | 0.992 [0.000, 1.000] | 0.897 [0.000, 1.000] |
| Saltmarsh | 0.858 [0.608, 0.975] | 0.632 [0.294, 0.904] |
| Seagrass | 0.867 [0.104, 1.000] | 0.896 [0.306, 1.000] |

#### Region 6 (South East)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.865 [0.701, 0.956] | 0.923 [0.791, 0.987] |
| Mangrove | 0.949 [0.843, 0.993] | 0.951 [0.813, 0.982] |
| Saltmarsh | 0.919 [0.816, 0.968] | 0.786 [0.584, 0.908] |
| Seagrass | 0.934 [0.859, 0.984] | 0.941 [0.874, 0.977] |

#### Region 7 (Tasmania)

| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.947 [0.786, 1.000] | 0.964 [0.654, 1.000] |
| Saltmarsh | 0.926 [0.729, 0.996] | 0.894 [0.684, 0.975] |
| Seagrass | 0.969 [0.519, 1.000] | 0.927 [0.764, 1.000] |

## Quality assurance

Code used to generate the DEA Coastal Ecosystem Map is run against automated integration tests to ensure that product quality is maintained as updates and improvements are made. These tests verify that the entire product generation workflow is performing as expected and track changes in product accuracy over time.

% ## Known issues

% :::{dropdown} 1 Jan 2020: Example issue
% :open:
%
% This uses the `:open:` option because it is an open issue.
% :::

## References

Lyons, M.B., Keith, D.A., Phinn, S.R., Mason, T.J., & Elith, J. (2018). A comparison of resampling methods for remote sensing classification and accuracy assessment. *Remote Sensing of Environment*, 208, 145-153. <https://doi.org/10.1016/j.rse.2018.02.026>

