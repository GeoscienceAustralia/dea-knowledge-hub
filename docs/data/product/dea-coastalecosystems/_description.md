% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/product_metadata_fields.html

## Background

Mapping coastal ecosystems is vital for understanding, managing, and protecting the diverse habitats that line our shorelines. These ecosystems—ranging from mangroves and saltmarshes to seagrass meadows and coral reefs—provide essential environmental services, including carbon storage, shoreline protection, and habitat for marine biodiversity. From an economic standpoint, they sustain industries such as fisheries and tourism while reducing costs associated with coastal erosion and storm damage. Accurate and comprehensive mapping underpins management, restoration, and conservation efforts, allowing planners to identify priority areas, monitor ecological change, and assess the effectiveness of interventions.

Achieving this at a continental scale, however, poses significant challenges. Traditional methods such as field surveys, aerial photography, and local-scale sampling are costly, labour-intensive, and constrained in spatial and temporal scope—limitations that are particularly relevant in a country as vast and remote as Australia. Earth Observation (EO) provides an efficient and consistent alternative, allowing large-scale, high-resolution, and repeatable mapping through the use of publicly available satellite imagery.

The Digital Earth Australia (DEA) Coastal Ecosystem Map was developed in response to this need for consistent, continent-wide monitoring. It provides the first national dataset to simultaneously map Australia’s mangrove, saltmarsh, intertidal, and intertidal seagrass ecosystems at 10 m resolution, using Sentinel-2 satellite imagery for the years 2021 and 2022. The mapping process employs a machine learning (ML) framework originally developed by the University of New South Wales (UNSW) and James Cook University (JCU) for global coastal ecosystem mapping on the Google Earth Engine platform. To tailor the approach for Australian conditions, JCU—commissioned by the Department of Climate Change, Energy, the Environment and Water (DCCEEW)—compiled a national training dataset of more than 40,000 annotated points across the continent (Canto et al., 2023; Becker et al., 2023).

This collaboration ensures the resulting maps are ecologically meaningful and complementary to expert mapping undertaken by State Governments and academia. providing a strong foundation for environmental management and reporting, restoration planning, environmental-economic accounting, and long-term coastal conservation.

## What this product offers
The DEA Coastal Ecosystem Map product suite is designed to offer users a categorical classification of four intertidal coastal ecosystems, supported by probability layers for each of the individual ecosystems and selected quality assurance layers to support product interpretation.
Key features of the product suite include:
- Sentinel-2 10m resolution derived classified ecosystem maps for 2021 and 2022 defining dominant ecosystem extents of mangroves, saltmarsh, intertidal, and intertidal seagrass.
- Probability layers for mapped ecosystems to enable user interpretation of mixed and transitional classes. 
- QA/QC layers to provide confidence and assist in product interpretation.
- Publication of ancillary layers used for masking and constraints in the mapping workflow.
- Publication of the national training dataset, metadata, classification schema and acquisition protocol.

% ## Access constraints

% ## Use constraints

## Applications (still todo)

- Accounts – shorter version of text below
- SoE reporting
- Complmenting periodic high resolution expert mapping
- Intergration with other terrestrial and ocean data sets (see Future work)
- Other?

## Lineage

The DEA Coastal Ecosystem Map was initiated as a collaborative project to support the Commonwealth Department of Climate Change, Energy, the Environment and Water (DCCEEW) to underpin the creation of Environmental Economic Accounts (EEA) for ecosystems in Australia’s coastal zone. This followed experimental Ocean Accounts, delivered in 2022 and based on selected individual ecosystem earth observation derived datasets.

Leveraging a methodology that mapped [global shifts in tidal wetlands](https://www.science.org/doi/10.1126/science.abm9583), Geoscience Australia has collaborated with James Cook University and the University of New South Wales to deliver a similar approach for Australia in this Coastal Ecosystem Map product suite. Initial Beta versions of the DEA Coastal Ecosystem Map have been used to underpin the February 2025 release of the [National Ecosystem Accounts experimental estimates for the Coastal Realm](https://www.abs.gov.au/statistics/environment/environmental-accounts/national-ecosystem-accounts-experimental-estimates/latest-release#coastal-realm), with the first V1.0.0 release of the DEA Coastal Ecosystem Map expected to contribute to the upcoming 2026 National Ecosystem Account released by the Australian Bureau of Statistics (ABS)

Targeted stakeholder engagement and product feedback sessions have been conducted throughout the development of the product to ensure where possible a complementary alignment of the DEA Coastal Ecosystem Map product to State Government and Academic mapping efforts. These efforts are aimed at ensuring the ease of uptake and integration of the product into a range of environmental reporting applications across jurisdictions (e.g State of the Environment).

Stakeholder engagement at all levels will continue to drive the development of the Coastal Ecosystem Map product in a cycle of continuous improvement, validation, feedback integration and inclusion of additional ecosystem types (see [Caveats/FAQS](./?tab=quality)). 

## Technical information

### Product Features

The DEA Coastal Ecosystem Map is a multi-layered dataset and is produced for two years, 2021 and 2022. See [Specifications](./?tab=specifications) for individual layer metadata.

### Core Product Layers
Five core layers are included in The DEA Coastal Ecosystem Map: the classification and four probability layers.
#### *Classification*
The primary layer of the DEA Coastal Ecosystem Map is a categorical classification of the extent of mangrove, saltmarsh, intertidal and intertidal seagrass coastal ecosystems (Fig 1). The layer is built from thresholds of the ecosystem probability layers (below), and constrained, modified and masked with a range of ancillary datasets and QA/QC processes (See [Contextual Editing](#4-contextual-editing)).

Product layers for 2021 and 2022 are published with the following categorical class values:

- Intertidal (2)
- Mangrove (3)
- Saltmarsh (4)
- Intertidal Seagrass (5) 

:::{figure} /_files/dea-coastalecosystems/low_tide_composite_2021_bermagui.png
{figure} /_files/dea-coastalecosystems/classification_bermagui_2021.png

**Figure 1** Bermagui, NSW. Above: the 2021 low tide [DEA Tidal Composite](https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/). Below: the 2021 DEA Coastal Ecosystem Map.

:::

#### *Probability*
Individual ecosystem probability layers are provided as supporting datasets to aid the interpretation of extents for four ecosystem classes, Mangrove, Saltmarsh, Saltflat and Intertidal Seagrass (Fig 2). Probability values in these layers represent the percentage of random-forest trees that vote at each pixel for a given ecosystem in the relevant [Machine Learning model](#model-training); the Ecosystem Model (Mangroves, Saltmarsh, Saltflat) and the Intertidal Model (Intertidal Seagrass).

The Intertidal class within the Intertidal model has been fixed to the extent of the [DEA Intertidal Extents product](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/?tab=description#core-product-layers) (see [Ecosystem Prediction](#ecosystem-prediction)), so the probability layer for this ecosystem is not provided. As the Intertidal Seagrass is modelled within this fixed extent, the corresponding probability layer is also constrained to these extents.

Probability layers for ecosystem layers in the Ecosystem Model (Mangroves, Saltmarsh and Saltflat) are masked below 20% probability to remove very low confidence pixels and noise from the dataset to improve interpretability.

The Saltflat ecosystem has been excluded from the classification product layer, though the probability layer generated for this ecosystem as part of the Ecosystem Model has been provided. For the reasoning behind this decision, and a discussion on further work required on this ecosystem class, see Saltflats [Caveats](./?tab=quality) section.

For further information how these Probability layers can be interpreted and used to aid in interpretation of the classified ecosystem map, including for mixed or transitional classes, see [Prob Caveats]((./?tab=quality)).

:::{figure} /_files/dea-coastalecosystems/probabilities_Bermagui_2021.png

**Figure 2** Bermagui, NSW. DEA Coastal Ecosystem Map probability layers.

:::

### Quality Assurance Layers
Two quality assurance layers (Figure C) are included in the DEA CEM product suite: 
#### Clear count (*qa-count-clear*) (todo: links and figs)

A layer showing the distribution of clear and valid satellite observations at each Sentinel-2 (link to S2 ARD) pixel during the analysis period. Artefacts that can invalidate pixels include cloud cover/shadow and low geometric accuracy. A pixel only proceeds into the DEA Coastal Ecosystem Map workflow if it has more than 10 valid observations. The qa-count-clear layer shows that the maximum number of clear observations for any single pixel was 130 +/-1 in both years of the dataset.

#### Coastal connectivity (*qa-coastal-connectivity*) (todo: links and figs)
An accumulated cost-distance connectivity layer used as a covariate layer within the modelling process, and as an additional contextual editing layer for the Saltmarsh class. Values represent the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves. Lower values indicate likely coastal pixels, reflecting both distance inland and topography. The values of the coastal connectivity layer are dimensionless.

[Placeholder: Figure C]

### Data Format (todo: links)
#### Cloud-optimised GeoTIFF
Layers of the DEA Coastal Ecosystem Map are provided as single continental scale cloud-optimised GeoTIFFs. For data access and use in geospatial information system (GIS) environments, streaming (link to mosaic access KH page) of these datasets is strongly recommended over downloading of the datasets. Web mapping services (WMS) are also available for all DEA datasets (link to access page).
#### Product naming convention
The DEA standard [file naming convention](/guides/reference/collection_3_naming/) has been applied as follows:

```text
{Organisation}_{Platform}_{Product}_{Reporting period}_{Collection}_{Version}_{Tile reference}_{Data date}--{Data period}_{Product status}_{Band name}.{File extension}
```

For example, the 2021 DEA Coastal Ecosystem Map classification layer is named
```
ga_s2_coastalecosystems_cyear_3_v1-0-0_AU_2021—P1Y_final_classification.tif
```

## Processing steps

### Workflow
The DEA Coastal Ecosystem Map is a machine learning workflow comprised of four primary components (Figure 4): Training data, Covariate data, Machine learning and Contextual editing. 

These components are discussed in further detail below. The validation process is discussed in the [Quality](./?tab=quality) tab.

:::{figure} /_files/dea-coastalecosystems/CEM_flowchart.png

**Figure 4** Primary components and outputs of the DEA Coastal Ecosystem Map workflow
:::

### 1. Training data

#### Data curation

[Continental training data](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/data/training_data_input/MultEcosy_TData_v1_0.geojson), developed for [this work](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/docs/publications/JCU_Coastal_Training_Data_Report_1_27012023_FR%20.pdf) (Canto et al., 2023), comprised a point-record training set of 40,934 Australian coastal ecosystem type occurrences (Fig. 5). Development of this dataset was completed for use with multi-ecosystem classification models.

The dataset integrated occurrence records from four data sources:

- Australia coastal ecosystem mapping (Becker et. al, 2023)
- Australia seagrass mapping (Navarro et. al, 2022)
- Australia saltmarsh mapping (Navarro et. al, 2023)
- Global intertidal change (Murray et. al, 2019; Murray et al., 2022)

:::{figure} /_files/dea-coastalecosystems/Original_training_point_distribution.png

**Figure 5** after Canto et al., 2023; Becker et al., 2023. 40,934 expert labelled point occurrences of coastal ecosystem types, distributed continentally around the Australian coastline.
:::

#### Ecosystem definitions
The training data definitions for Australian coastal ecosystems (Table 1, Canto et al., 2023) were sourced from the Blue Carbon Method (CER, 2022) and the International Union for Conservation of Nature Global Ecosystem Typology (Keith et al., 2022). 

Training point class descriptors (level 2, L2) were aggregated into broader level 1 (L1) class categories to form the basis of the DEA Coastal Ecosystem Map. The mapping of L2 to L1 ecosystem types, and their definitions, are described in Table 1

**Table 1** Ecosystem definitions and class mappings

| L2 ecosystem type | L1 ecosystem type | L1 Definition |
|-------------------|-------------------|---------------|
| • Land<br>• Supratidal forest<br>• Freshwater wetland<br>• Sand<br>• Water | Terrestrial/Other | Includes natural or anthropogenic land cover types that occur in non-intertidal areas but within the coastal zone such as supratidal forests, frequently inundated croplands, freshwater wetlands and permanent sand dunes. |
| • Seagrass (subtidal) | Permanent water | Refers to a variety of permanent water bodies around the coast but not within the intertidal zone. These water bodies range from deep permanent ocean to freshwater rivers and lakes and include clear and turbid waters. Includes submerged vegetation and substrates such as subtidal seagrass if the bottom is visible. |
| • Mudflat<br>• Intertidal non-vegetated soft sediments | Intertidal | Ecosystem occurring in low-sloping areas of the intertidal zone. Includes muddy, sandy and rocky substrates. Can readily transition to seagrass, mangrove or saltmarsh ecosystems if conditions become favorable for the colonization of vegetation through changes in sea level or freshwater inundation over time. |
| • Mangrove | Mangrove | Ecosystem comprised of trees and shrubs which a) occupy the intertidal zone or floodplains, including marine and estuarine areas; and b) grow in saline or brackish water. |
| • Saltmarsh<br>• Algal Mats | Saltmarsh | Ecosystem comprised of a) salt tolerant herbaceous plants and occasionally woody shrubs; and b) occur on floodplains and in estuaries and can be flushed with water from a combinations of sources including rainfall, rivers, groundwater and seawater. This includes saltmarsh in sparsely vegetated saline or hypersaline ecosystems. |
| • Seagrass (intertidal) | Intertidal seagrass | Ecosystem comprised of grass-like plants that grow in shallow intertidal coastal waters. Seagrasses are aquatic flowering plants that form meadows in temperate and tropical regions of Australia. |
| • Saltflat | Saltflat | A subtype of saltmarsh ecosystems comprising bare saltmarsh. Saltflats include sparsely vegetated saline or hypersaline ecosystems |

#### Regional modelling
A bioregional approach was used to improve modelling performance by accounting for regional ecological variations while maintaining the ability to apply a consistent classification schema. 

Seven bioregions (Fig. 6) were developed with expert consultation across Geoscience Australia, University of Queensland, James Cook University and University of New South Wales, guided by Natural Resource Management regions, tidal regimes, climate forcing and ecosystem dynamics. 

These regions enabled models to be developed with regional specific training data to account for differences across the common ecosystem classes (e.g. the varied ecological nature of saltmarsh across the country), as well as regional climate and seasonal impacts on the covariate data inputs.

It is important that these regions be regarded as a pragmatic technical choice rather than an attempt at a comprehensive bioregionalization. 

:::{figure} /_files/dea-coastalecosystems/Labelled_tile_regions.png

***Figure 6*** Seven biogregions were used to model coastal ecosystems

:::

#### Training Point Expansion
Introducing the modelling regions had implications for the size and balance of the training data sets once split across the seven bioregions, with many ecosystem training point classes falling below a reasonable representative sample number. 

The development of the original training data set on Landsat 30m data, coupled with an acquisition protocol focused on spatially homogenous regions, presented an opportunity to expand the training data sets when considering the increased resolution of the CEM product. With Sentinel-2's 10m resolution pixels falling within the tolerance established for the training data point validity (30-40m), a semi-automated process was implemented to expand the existing training dataset. This semi-automated approach was particularly effective for expanding coverage in homogeneous ecosystem patches while maintaining data quality.

This was achieved by resampling the original training data points to 10 m resolution, sampling the surrounding 9 pixels of each original training point, to increase the overall number of training data points, to approx 368,000.

This approach balanced the need for increased training data volume across all seven modelling regions while maintaining data quality and ecological validity (Table 2). The process also included more spatial and spectral variability in the modelling process, resulting in a small but consistent improvement in [accuracy](./?tab=quality) when using the expanded training data set.

| Region | Water | Mudflat | Mangrove | Saltmarsh | Saltflat | Terrestrial/Other | Intertidal seagrass | Total |
|--------|-------|---------|----------|-----------|----------|-------------------|---------------------|-------|
| NW | 4959 | 3135 | 7893 | 4641 | 5583 | 28734 | 186 | 55131 |
| NE | 9354 | 6424 | 8617 | 4473 | 3169 | 20664 | 5072 | 57773 |
| Gulf | 2754 | 2473 | 3960 | 3267 | 2526 | 7818 | 3464 | 26262 |
| West | 1638 | 2385 | 2241 | 2481 | 2898 | 12471 | 1765 | 25879 |
| SW | 2718 | 816 | 441 | 1926 | 126 | 46512 | 1377 | 53916 |
| SE | 9234 | 3891 | 7514 | 15512 | 422 | 64705 | 9734 | 111012 |
| Tas. | 2697 | 1359 | 0 | 3120 | 0 | 5622 | 1319 | 14117 |

**Table 2** Expanded training data distribution across model regions. Modelling regions: North West (NW), North East (NE), Gulf of Carpentaria (Gulf), West, South West (SW), South East (SE) and Tasmania (Tas.). **N.b.** No mangroves or saltflat are recorded in Tasmania.

### 2. Covariate Data
Covariate data stacks were generated using a combination of Sentinel-2 Analysis Ready Data, calculated indices and derived datasets (Table 3). These covariate stacks of 131 total variables were generated for each of the modelling years.

**Table 3** Covariate datasets used to model coastal ecosystems
| Data Source | Variable | Percentiles | Total Count |
|-----|-----|-----|-----|
|[Sentinel-2 ARD Reflectance](https://knowledge.dea.ga.gov.au/data/category/dea-surface-reflectance/) | nbart_blue | 10,20,40,60,80 | 5 |
|  | nbart_green | 10,20,40,60,80 | 5 |
|  | nbart_red | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_1 | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_2 | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_3 | 10,20,40,60,80 | 5 |
|  | nbart_nir | 10,20,40,60,80 | 5 |
|  | nbart_nir_1 | 10,20,40,60,80 | 5 |
|  | nbart_nir_2 | 10,20,40,60,80 | 5 |
|  | nbart_swir_1 | 10,20,40,60,80 | 5 |
|  | nbart_swir_2 | 10,20,40,60,80 | 5 |
|  | nbart_swir_3 | 10,20,40,60,80 | 5 |
| **Sentinel-2 derived indices** |  |  |  |
|- Automated Water Extraction Index (no shadow) (Feyisa et al., 2014) | AWEI_ns | 10,20,40,60,80 | 5 |
|- Automated Water Extraction Index (shadow) (Feyisa et al., 2014) | AWEI_sh | 10,20,40,60,80 | 5 |
|- Enhanced Vegetation Index (Huete et al., 2002) | EVI | 10,20,40,60,80 | 5 |
|- Leaf Area Index (Boegh et al., 2002) | LAI | 10,20,40,60,80 | 5 |
|- Modified Normalized Difference Water Index (Xu, 1996) | MNDWI | 10,20,40,60,80 | 5 |
|- Normalized Difference Vegetation Index (Rouse et al., 1973) | NDVI | 10,20,40,60,80 | 5 |
|- Normalized Difference Water Index (McFeeters, 1996) | NDWI | 10,20,40,60,80 | 5 |
|- Tasseled Cap Brightness (Crist, 1985) | TCB | 10,20,40,60,80 | 5 |
|- Tasseled Cap Greenness (Crist, 1985) | TCG | 10,20,40,60,80 | 5 |
|- Tasseled Cap Wetness (Crist, 1985) | TCW | 10,20,40,60,80 | 5 |
|- Tasseled Cap Wetness (GSO variant) (Nedkov, 2017) | TCW_GSO | 10,20,40,60,80 | 5 |
|- Water Index (Fisher et al., 2016) | WI | 10,20,40,60,80 | 5 |
| [DEA Tidal Composites](https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/?tab=specifications) | low_blue |  | 1 |
|  | low_green |  | 1 |
|  | low_red |  | 1 |
|  | low_red_edge_1 |  | 1 |
|  | low_red_edge_2 |  | 1 |
|  | low_red_edge_3 |  | 1 |
|  | low_nir_1 |  | 1 |
|  | low_nir_2 |  | 1 |
|  | low_swir_2 |  | 1 |
|  | low_swir_3 |  | 1 |
| Coastal Connectivity | Cost-distance |  | 1 |
|Total Covariates |  |  | 131 |

#### Coastal Connectivity
The Coastal connectivity layer (also published as a [QA product layer](#quality-assurance-layers)) is designed as an accumulated cost-distance dataset to indicate likely coastal pixels. This is achieved by determining the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves at each pixel location (Fig. 7), using the following datasets:

- Shuttle Radar Topography Mission (SRTM) Digital Elevation Model Version 1 (Gallant et al., 2011)
- A Highest Astronomical Tide Dataset developed at CSIRO [(Branson, 2023)](https://data.csiro.au/collection/csiro%3A61319v1)
- The extent of the DEA Mangroves product
Coastal connectivity is used here as a covariate layer within the modelling process, and as an additional contextual editing layer for the Saltmarsh class. 

:::{figure} /_files/dea-coastalecosystems/connectivity_Mallacoota.png

**Figure 7**  *a*) Mallacoota, Victoria; *b*) Highly connected areas have low connectivity values e.g. low elevations, connected to tidally influenced areas, have low connectivity values(light grey). Elevated areas are penalised with high connectivity values (dark grey), even if located close to tidally influenced areas.

:::

### 3. Machine Learning
#### Training Point Attribution
The full expanded Training Point dataset was attributed with covariate data from both the 2021 and 2022 modelling year covariate stacks. Training points where covariates were derived from <10 clear observations in either modelling year were removed from the relevant modelling year dataset, along with training points for the Sub-tidal Seagrass classification (see [Future Work](./?tab=quality)).

Both of these attributed annual Training Point datasets were then combined to form the final datasets for Model training.
#### Model training (todo: links and expert review)
The DEA Coastal Ecosystem Map workflow trains two [random-forest classifiers](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) for each of the seven [modelled regions](#regional-modelling) from the covariate-attributed stack of training data: 

- a multi-class ecosystem model (mangrove, saltmarsh and salt flat) and;
- an intertidal model (intertidal and intertidal-seagrass). 

The multi-class ecosystem model utilized all data in the training data datasets while the Intertidal model were developed using only training data points located within the [DEA Intertidal Extents high confidence intertidal region](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/#core-product-layers). Functionally, this meant that within the bounded extents of the Intertidal modelled region, any training points included in the model that were not defined as Intertidal Seagrass were considered Intertidal. For a discussion on the implications of this aspect of the model classification see Intertidal [Caveat](./?tab=quality) section.

Multi-class and binary random-forest models were fit for each region using:

- 800 estimators (trees?)
- Minimum samples split of 2
- Minimum samples leaf of 1
- Maximum (tree? Branch?) depth of 10

Each model was first trained and evaluated using a [k-fold cross-validation train/test split](https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics) of the training data  to report accuracy statistics and refine optimal model parameters. Overall model accuracy statistics are reported in the [Quality](./?tab=quality) tab. Optimized model parameters were then used to retrain the final random-forest classifiers using the full training data set for the multi-class model and the intertidal masked training data set for the seagrass model.
The combined 2021 and 2022 stacks of covariate-trained training data ensure the classifier models are suitable for prediction into both years. Common covariates that exhibited a top-10 feature importance for the ecosystem models include the NDVI and MNDWI percentiles as well as the coastal-connectivity (Fig. 8).

:::{figure} /_files/dea-coastalecosystems/ML_Feature_Importance.png

**Figure 8** shows the commonality between covariates that appear in the top 10 most important covariates for each of the seven regional ecosystem models. The y-axis represents the number of regional models where the covariate features in the top-10.

:::

#### Ecosystem prediction
Coastal ecosystems were predicted into the Covariates stacks created for the CEM product extents for each modelling year.

Initial predictions were made using the multi-class ecosystem model, generating interim probability layers for mangrove, saltmarsh and salt flat ecosystems. An interim classified ecosystem output layer is also generated to capture the highest probability ecosystem class predicted for each pixel by the model.

The interim classified ecosystem output layer includes mangrove, saltmarsh and saltflat classes ([Fig. 4](#workflow)). Water and Terrestrial classes in this interim layer are classified as `NoData`. 

The Intertidal modelling extent is then set using the high confidence intertidal extent from the [DEA Intertidal](https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/#core-product-layers) dataset. The Intertidal model is then used to predict Intertidal seagrass into the annual covariate stacks masked to this modelling extent. The output from this process is the interim Intertidal seagrass probability layer.

### 4. Contextual editing
The interim classified ecosystem layer defines classes based on the highest probability class for each pixel, which can result in a classification based on relatively low probability values were a pixel is modelled as a likely mixed ecosystem. Combined with the inherent uncertainty and resulting misclassification when applying a ML mapping methodology at a continental scale, this meant that a range of rulesets and post-processing operations were applied, collectively termed ‘contextual editing’, to deliver the final Classification CEM product layer.

Probability layers are also masked in this contextual editing process, as described in the layer description.

The following rules and processes were applied, with justifications or links to further discussion points included below:

#### Classifier rulesets

1. **Remove unused classes**: The ecosystem classification output layer was masked to remove all saltflat pixels (link to Caveats section in Quality tab). 
1. **Apply probability thresholds**: A probability threshold of 50% was applied to the Saltmarsh and Mangrove pixels within the interim ecosystem classification layer, with pixels of these classes with a probability below this threshold assigned as “nodata”. A 50% probability threshold was selected based on the alignment of the outputs with external mapping products, and the conservative consideration that 50% provides a clear majority vote by the ML models.
1. **Apply environmental corrections**: Saltmarsh pixels were masked to the observed coastal-connectivity range identified by the saltmarsh training data points. To exclude outliers, the saltmarsh connectivity mask was thresholded to the 99.5th percentile connectivity value for all region-combined saltmarsh points from the training data set. This choice was made to remove misclassifications of saltmarsh in regions considered unconnected to coastal regions (see Connectivity Layer). For further discussion on the implications of thresholding based on existing distribution of training data see Saltmarsh Connect Caveat
#### Classifier masking
1. **Apply mangrove mask**: Mangrove pixels that fell outside of the mangrove habitat layer, identified by Global Mangrove Watch (Bunting et al., 2022 link to dataset) were removed. This habitat mask is widely used in Mangrove mapping studies (do we need a ref?) to define the ecologically suitable habitats that Mangrovesexisting and, and was used here to align our Mangrove mapping with these global approaches and minimize the false positives of Mangrove classification in not-suitable areas.
1. **Apply Intertidal seagrass probability threshold**: Within the defined Intertidal model extent the Intertidal seagrass probability layer was used to define the Intertidal seagrass classification at a probability of greater than or equal to 70 %. The 70 % threshold was selected as conservative value to account for the inter-annual variability of seagrass meadows (see Prob layer discussion)
1. **Apply manual mask**: A manual masking process was applied to the Classification layer, based on expert identified misclassifications in the layer (including roads, urban areas, terrain shadow, data noise). For full traceability this polygon masking layer is provided here. (link to dataset on Github??)
1. **Apply land use mask**: Industrial, urban or road areas as identified in the Australian Catchment Scale Land Use and Management dataset (ACLUM) (link to dataset) were removed.
1. **Remove and replace isolated pixel groups**: To reduce pixel based noise in the data, the classification layer was sieved to remove and replace isolated pixels in groups of 9 or less with the dominant surrounding class type.
#### Probability masking
1. **Apply probability threshold**: Pixels with values of less than 20 % were removed from the Mangrove, Saltmarsh and Saltflat probability layers to remove very low confidence pixels and noise from the dataset to improve interpretability.

## Software (todo)

## References (todo)

1. Branson, Paul (2023): Coastal carbon - Australia's blue forest future - Water Levels. v1. CSIRO. Data Collection. https://doi.org/10.25919/6672-jx11
1. Becker, M.L., Navarro, A., Canto, R., & Murray, N.J. (2023) [An Australian coastal ecosystem training library for remote sensing classification models.](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/docs/publications/JCU_Coastal_Training_Data_Report_1_27012023_FR%20.pdf) Unpublished report to the Department of Climate Change, Energy, the Environment and Water. James Cook University, Townsville.
1. Boegh, E., Soegaard, H., Broge, N., Hasager, C. B., Jensen, N. O., Schelde, K., & Thomsen, A. (2002). Airborne multispectral data for quantifying leaf area index, nitrogen concentration, and photosynthetic efficiency in agriculture. Remote sensing of Environment, 81(2-3), 179-193.
1. Bunting, P., Rosenqvist, A., Hilarides, L., Lucas, R., Thomas, N., Tadono, T., Worthington, T., Spalding, M., Murray, N., Rebelo, L.-M., (2022) Global Mangrove Watch (1996 - 2020) Version 3.0 Dataset. https://doi.org/10.5281/zenodo.6894273
1. Canto. R., Navarro., A.,Becker, M., Murray, N.J., (2023) [Australian coastal ecosystem training library](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/data/training_data_input/MultEcosy_TData_v1_0.geojson). Unpublished dataset.
1. Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. Remote Sensing of Environment, 17(3), 301–306. https://doi.org/10.1016/0034-4257(85)90102-6
1. Feyisa, G. L., Meilby, H., Fensholt, R., & Proud, S. R. (2014). Automated Water Extraction Index: A new technique for surface water mapping using Landsat imagery. Remote sensing of environment, 140, 23-35.
1. Fisher, A., Flood, N., & Danaher, T. (2016). Comparing Landsat water index methods for automated water classification in eastern Australia. Remote Sensing of Environment, 175, 167-182.
1. Gallant, J.C., Dowling, T.I., Read, A.M., Wilson, N., Tickle, P. and Inskeep, C., 2011. 1 second SRTM Derived Digital Elevation Models User Guide. Geoscience Australia www.ga.gov.au/topographic-mapping/digital-elevationdata.html 
1. Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., & Ferreira, L. G. (2002). Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote sensing of environment, 83(1-2), 195-213.
1. Keith, D.A., Ferrer-Paris, J.R., Nicholson, E. et al. (2022) A function-based typology for Earth’s ecosystems. Nature 610, 513–518 [https://www.nature.com/articles/s41586-022-05318-4](https://doi.org/10.1038/s41586-022-05318-4). 
1. Lovelock, C.E., Sippo, J., Fernanda Adame, M., Dittmann, S., Hickey, S., Hutley, L., Jones, A., Kelleway, J., Lavery, P., Macreadie, P., Maher, D., Mosely, L. and Rogers, K (2021) [Blue carbon accounting model (BlueCAM) technical overview](https://cer.gov.au/document/blue-carbon-accounting-model-bluecam-technical-overview). Report to the Clean Energy Regulator. University of Queensland.
1. Lyons, M.B., Keith, D.A., Phinn, S.R., Mason, T.J., & Elith, J. (2018). A comparison of resampling methods for remote sensing classification and accuracy assessment. Remote Sensing of Environment, 208, 145-153. https://doi.org/10.1016/j.rse.2018.02.026
1. McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. International journal of remote sensing, 17(7), 1425-1432.
1. Murray N. J., Canto, R., Worthington, T. A., Lyons, M.B. (2022) Supplementary Data S1 to Losses and gains of Earth's tidal wetlands. Figshare. https://doi.org/10.6084/m9.figshare.19121660.
1. Murray, N. J., Phinn, S. R., DeWitt, M., Ferrari, R., Johnston, R., Lyons, M. B., Clinton, N., Thau, D. & Fuller, R. A. (2019). The global distribution and trajectory of tidal flats. Nature, 565, 222-225
1. Murray, N.J., et al., High-resolution mapping of losses and gains of Earth’s tidal wetlands. Science 376, 744-749(2022). [DOI:10.1126/science.abm9583](https://www.science.org/doi/10.1126/science.abm9583)
1. Navarro, A., Canto, R., Toor, M., & Murray, N.J. (2022) An Australian intertidal seagrass training library for remote sensing classification models. Unpublished report to the Department of Agriculture, Water and the Environment. James Cook University, Townsville.
1. Navarro, A., Canto, R., Toor, M., Becker, M.L., Lyons, M. & Murray, N.J. (2023) Australian Saltmarsh Map. Unpublished report to the Clean Energy Regulator. James Cook University, Townsville. 
1. Nedkov, R., (2017). “Orthogonal transformation of segmented images from the satellite Sentinel-2,” Comptes Rendus De lAcad. Bulgare Sci., vol.  70, no.  5, pp.  687–692.
1. Rouse Jr, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1973). Monitoring the vernal advancement and retrogradation (green wave effect) of natural vegetation (No. NASA-CR-132982).
1. Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. International journal of remote sensing, 27(14), 3025-3033. 
