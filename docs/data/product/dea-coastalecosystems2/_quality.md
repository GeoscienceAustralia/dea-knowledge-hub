% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/product_metadata_fields.html

## Caveats and Limitations

- **Sensor coverage and tidal phase**: Sentinel‑2 acquisitions do not uniformly sample the tidal cycle, so some intertidal habitats may be under-represented in either the training data or the predictions, especially in microtidal or persistently turbid zones.
- **Training data composition**: Regional training sets remain unbalanced for rare classes (e.g. salt flat, seagrass in Region 1), which contributes to wider accuracy intervals and should be considered when interpreting those classes.
- **Probability masking**: Accuracy statistics only include samples with ≥50 % model probability. Areas with persistent cloud, haze, or spectral ambiguity may be masked operationally and will not have associated accuracy estimates.
- **Spatial extrapolation**: Spatial stratification reduces autocorrelation bias, but accuracy can still degrade in locations far from labelled samples or outside the environmental gradients represented in the combined parquet.
- **Model uncertainty**: Reported medians and 95 % intervals reflect Monte Carlo sampling only; additional uncertainty from sensor noise, ancillary covariates, or downstream post-processing is not captured here.
- **Mosaic and mixed ecosystems**: Many ecosystems exist as highly mixed types or mosaics/transitional ecosystems. These types of ecosystems, particularly when they exist in relatively even cover proportions, are not well represented by categorical mapping products. Thus it is to be expected that change metrics will be highly sensitive and potentially erroneous in these cases - users should make use of the model probability layers to identify these areas and make case-specific judgement on usage.

## Accuracy

The DEA Coastal Ecosystems mapping was validated using a Monte Carlo resampling workflow with spatial stratification (32 km tiles) to limit spatial autocorrelation (Lyons et al. 2018). Each iteration trains on ~80 % of tiles, tests on the remainder, filters predictions by a ≥50 % class-probability threshold (to replicate the mapping methodology), and then reports accuracy for both the ecosystem model and the final output after seagrass modelling is applied to the tidal flat area. The validation metrics are thus indicative of the accuracy of the final categorical classification product, and are not strictly relevant tot the model probability layers. Final accuracy metrics are summarised from the sampling distributions as the median with a 95 % interval (which can be used as area multipliers if desired). Validation statistics are reported separately for the 2021 and 2022 mapping.

Comprehensive methodology notes are documented in [Validation README](validation_README.md), and the complete per-class/per-year outputs are available in [full validation results](coastal_ecosystem_validation_results.md) (assuming GitHub repository is made public).

### Regional summary per year
**Year 2021**
| Region | Overall Accuracy (Median [95% interval]) |
|--------|----------------------------------------|
| 1 | 0.948 [0.905, 0.971] |
| 2 | 0.914 [0.880, 0.943] |
| 3 | 0.881 [0.796, 0.932] |
| 4 | 0.932 [0.898, 0.969] |
| 5 | 0.973 [0.938, 0.993] |
| 6 | 0.947 [0.915, 0.970] |
| 7 | 0.942 [0.879, 0.977] |

**Year 2022**
| Region | Overall Accuracy (Median [95% interval]) |
|--------|----------------------------------------|
| 1 | 0.944 [0.896, 0.969] |
| 2 | 0.908 [0.873, 0.944] |
| 3 | 0.873 [0.779, 0.922] |
| 4 | 0.935 [0.900, 0.969] |
| 5 | 0.972 [0.936, 0.993] |
| 6 | 0.945 [0.913, 0.970] |
| 7 | 0.947 [0.889, 0.981] |

### Regional summary per region (combined years)
#### Region 1 [North West]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.877 [0.671, 0.983] | 0.945 [0.861, 0.985] |
| Mangrove | 0.989 [0.960, 0.999] | 0.982 [0.963, 0.995] |
| Saltmarsh | 0.900 [0.523, 0.991] | 0.635 [0.373, 0.823] |
| Seagrass | 0.000 [0.000, 0.211] | 0.000 [0.000, 0.015] |

#### Region 2 [North East]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.777 [0.637, 0.904] | 0.927 [0.832, 0.980] |
| Mangrove | 0.970 [0.928, 0.994] | 0.977 [0.932, 0.993] |
| Saltmarsh | 0.803 [0.551, 0.945] | 0.571 [0.408, 0.772] |
| Seagrass | 0.881 [0.731, 0.973] | 0.651 [0.423, 0.826] |

#### Region 3 [Gulf of Carpentaria]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.611 [0.387, 0.827] | 0.864 [0.649, 0.972] |
| Mangrove | 0.989 [0.962, 1.000] | 0.990 [0.974, 1.000] |
| Saltmarsh | 0.895 [0.416, 0.983] | 0.766 [0.580, 0.907] |
| Seagrass | 0.891 [0.691, 0.981] | 0.676 [0.311, 0.887] |

#### Region 4 [West]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.843 [0.675, 0.994] | 0.982 [0.932, 1.000] |
| Mangrove | 0.992 [0.909, 1.000] | 0.991 [0.939, 1.000] |
| Saltmarsh | 0.865 [0.565, 0.988] | 0.800 [0.471, 0.949] |
| Seagrass | 0.938 [0.163, 1.000] | 0.775 [0.148, 1.000] |

#### Region 5 [South West]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.852 [0.000, 1.000] | 0.886 [0.000, 1.000] |
| Mangrove | 0.994 [0.000, 1.000] | 0.897 [0.000, 1.000] |
| Saltmarsh | 0.866 [0.618, 0.974] | 0.621 [0.257, 0.900] |
| Seagrass | 0.863 [0.186, 1.000] | 0.895 [0.311, 1.000] |

#### Region 6 [South East]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.862 [0.709, 0.958] | 0.925 [0.775, 0.985] |
| Mangrove | 0.951 [0.855, 0.992] | 0.945 [0.810, 0.982] |
| Saltmarsh | 0.919 [0.821, 0.969] | 0.782 [0.592, 0.911] |
| Seagrass | 0.933 [0.848, 0.985] | 0.939 [0.853, 0.977] |

#### Region 7 [Tasmania]
| Class | User's Accuracy | Producer's Accuracy |
|-------|-----------------|---------------------|
| Tidal flat | 0.951 [0.781, 1.000] | 0.969 [0.674, 1.000] |
| Saltmarsh | 0.928 [0.732, 0.995] | 0.893 [0.682, 0.978] |
| Seagrass | 0.970 [0.549, 1.000] | 0.928 [0.763, 1.000] |

## Quality assurance

Code used to generate the DEA Coastal Ecosystem Map is [run against automated integration tests](https://github.com/GeoscienceAustralia/dea-coastalecosystems/tree/main/tests) to ensure that product quality is maintained as updates and improvements are made. These tests verify that the entire product generation workflow is performing as expected, and track changes in product accuracy over time.

% ## Known issues

% :::{dropdown} 1 Jan 2020: Example issue
% :open:
%
% This uses the `:open:` option because it is an open issue.
% :::

## References
**Lyons, M.B., Keith, D.A., Phinn, S.R., Mason, T.J., & Elith, J. (2018).** A comparison of resampling methods for remote sensing classification and accuracy assessment. *Remote Sensing of Environment*, 208, 145-153. https://doi.org/10.1016/j.rse.2018.02.026

