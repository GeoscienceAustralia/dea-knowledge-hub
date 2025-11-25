% See the Product metadata fields documentation: https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/product_metadata_fields.html

## Background

Mapping coastal ecosystems is vital for understanding, managing, and protecting the diverse habitats that line our shorelines. These ecosystems—ranging from mangroves and saltmarshes to seagrass meadows and coral reefs—provide essential environmental services, including carbon storage, coastal protection, and habitat for marine biodiversity. From an economic standpoint, they sustain industries such as fisheries and tourism while reducing costs associated with coastal erosion and storm damage. Accurate and comprehensive mapping underpins management, restoration, and conservation efforts, allowing planners to identify priority areas, monitor ecological change, and assess the effectiveness of interventions.

Achieving this at a continental scale, however, poses significant challenges. Traditional methods such as field surveys, aerial photography, and local-scale sampling are costly, labour-intensive, and constrained in spatial and temporal scope—limitations that are particularly relevant in a country as vast and remote as Australia. Earth Observation (EO) provides an efficient and consistent alternative, allowing large-scale, high-resolution, and repeatable mapping through the use of publicly available satellite imagery.

The **Digital Earth Australia (DEA) Coastal Ecosystems** product suite was developed in response to this need for consistent, continent-wide monitoring. It provides the first national dataset to simultaneously map Australia’s mangrove, saltmarsh, intertidal, and intertidal seagrass ecosystems at 10 m resolution, using annual time-series of Sentinel-2 satellite imagery for consistent mapping at a continental scale. The mapping process employs a machine learning (ML) framework originally developed by the University of New South Wales (UNSW) and James Cook University (JCU) for global coastal ecosystem mapping on the Google Earth Engine platform (Murray et al., 2022). To tailor the approach for Australian conditions, JCU — commissioned by the Department of Climate Change, Energy, the Environment and Water (DCCEEW) — compiled a national training dataset of more than 40,000 annotated points across the continent (Canto et al., 2023; Becker et al., 2023).

This collaboration ensures the resulting maps are ecologically meaningful and complementary to expert mapping undertaken by State Governments and academia. providing a strong foundation for environmental management and reporting, restoration planning, environmental-economic accounting, and long-term coastal conservation.

## What this product offers

The DEA Coastal Ecosystems product suite offers users a categorical classification of four coastal ecosystems, supported by probability layers for individual ecosystems and selected quality assurance layers to support product interpretation.
Key features of the product suite include:
- Sentinel-2 10 m resolution derived annual classification ecosystem maps, defining dominant ecosystem extents of mangroves, saltmarsh, intertidal, and intertidal seagrass.
- Probability layers for mapped ecosystems to enable user interpretation of mixed and transitional classes. 
- QA/QC layers to provide confidence and assist in product interpretation.
- Publication of ancillary layers used for masking and constraints in the mapping workflow.
- Publication of the national training dataset, metadata, classification schema and acquisition protocol.

% ## Access constraints

% ## Use constraints

## Applications

- National Environmental Ecosystem Accounts
- National and Regional State of the Environment reporting
- A complementary mapping product to fill spatial and temporal gaps in higher resolution expert mapping (aerial and drone mapping, field surveys)
- Future integration with other terrestrial and ocean data sets (e.g. Land Cover and Marine Tenure)
- Coastal protection and Hazard modelling

## Lineage

DEA Coastal Ecosystems was initiated as a collaborative project to support the Commonwealth Department of Climate Change, Energy, the Environment and Water (DCCEEW) to underpin the creation of Environmental Economic Accounts (EEA) for ecosystems in Australia’s coastal zone. This followed experimental Ocean Accounts, delivered in 2022 and based on selected individual ecosystem earth observation derived datasets.

Leveraging a methodology that mapped [global shifts in tidal wetlands](https://www.science.org/doi/10.1126/science.abm9583), Geoscience Australia has collaborated with James Cook University and the University of New South Wales to deliver a similar approach for Australia in the DEA Coastal Ecosystems product suite. Initial Beta versions of the  product were used to underpin the February 2025 release of the [National Ecosystem Accounts experimental estimates for the Coastal Realm](https://www.abs.gov.au/statistics/environment/environmental-accounts/national-ecosystem-accounts-experimental-estimates/latest-release#coastal-realm), with the first v1.0.0 release of the DEA Coastal Ecosystems product suite expected to contribute to the upcoming 2026 National Ecosystem Account released by the Australian Bureau of Statistics (ABS)

Targeted stakeholder engagement and product feedback sessions have been conducted throughout the development of the product to ensure, where possible, a complementary alignment of the DEA Coastal Ecosystems product suite to State Government and Academic mapping efforts. These engagements aimed to ensure ease of uptake and integration of the product into a range of environmental reporting applications across jurisdictions (e.g State of the Environment).

Stakeholder engagement at all levels will continue to drive the development of DEA Coastal Ecosystems product in a cycle of continuous improvement, validation, feedback integration and inclusion of additional ecosystem types.

## Technical information

### Product Features

The DEA Coastal Ecosystems product suite is a multi-layered dataset produced delivered as annual summary products. See [Specifications](./?tab=specifications) for individual layer metadata.

### Core Product Layers

Five core layers are included in The DEA Coastal Ecosystems product suite: the classification layer and four probability layers.

#### Classification layer (classification)

The primary layer of DEA Coastal Ecosystems is a categorical classification of the extent of mangrove, saltmarsh, intertidal and intertidal seagrass coastal ecosystems (Figure 1). The layer is built from thresholds of the ecosystem probability layers (below), and constrained, modified and masked with a range of ancillary datasets and QA/QC processes (See [Contextual Editing](#4-contextual-editing)).

Annual classification layers are published with the following categorical class values:

- Intertidal (2)
- Mangrove (3)
- Saltmarsh (4)
- Intertidal Seagrass (5) 

:::{figure} /_files/dea-coastalecosystems/classification_bermagui_2021_LTC.png

**Figure 1.** Bermagui, NSW. Top: The 2021 low-tide [DEA Tidal Composite](/data/product/dea-tidal-composites/). Bottom: The 2021 DEA Coastal Ecosystems classification layer.

:::

#### Probability layers (mangrove-prob, saltmarsh-prob, saltflat-prob, seagrass-prob)

Individual ecosystem probability layers are provided as supporting datasets to aid the interpretation of extents for four ecosystem classes: Mangrove, Saltmarsh, Saltflat and Intertidal Seagrass (Figure 2). Probability values in these layers represent the percentage of random-forest trees that vote at each pixel for a given ecosystem in the relevant [Machine Learning model](#model-training); the Ecosystem Model (Mangroves, Saltmarsh, Saltflat) or the Intertidal Model (Intertidal Seagrass).

The Intertidal class within the Intertidal model has been fixed to the extent of the [DEA Intertidal Extents product](/data/product/dea-intertidal/?tab=description#core-product-layers) (see [Ecosystem Prediction](#ecosystem-prediction)), so the probability layer for this ecosystem is not provided. As the Intertidal Seagrass is modelled within this fixed extent, the corresponding probability layer is also constrained to these extents.

Probabilities for layers in the Ecosystem Model (Mangroves, Saltmarsh and Saltflat) are masked below 20% probability to remove very low confidence pixels and noise from the dataset to improve interpretability.

The Saltflat ecosystem has been excluded from the classification product layer, though the probability layer generated for this ecosystem as part of the Ecosystem Model has been provided. Reasoning and further discussion on this decision can be found in the [Caveats and Limitations](./?tab=quality) section.

Further information on how these Probability layers can be individually interpreted and used to aid in interpretation of the classified ecosystem map, including for mixed or transitional classes, can be found in the Caveats and Limitations.

:::{figure} /_files/dea-coastalecosystems/probabilities_Bermagui_2021.png

**Figure 2.** Bermagui, NSW. DEA Coastal Ecosystems probability layers.

:::

### Quality Assurance Layers

Two quality assurance layers are included in the DEA Coastal Ecosystems product suite.

#### Clear count layer (qa-count-clear)

A layer showing the distribution of clear and valid satellite observations at each [Sentinel-2 pixel](/data/category/dea-surface-reflectance/) during the analysis period. Artefacts that can invalidate pixels include cloud cover/shadow and low geometric accuracy. A pixel only proceeds into the DEA Coastal Ecosystems workflow if it has more than 10 valid observations in a modelling year. 

#### Coastal connectivity layer (qa-coastal-connectivity)

An accumulated cost-distance connectivity layer used as a [covariate](#coastal-connectivity) within the modelling process, and as an additional [contextual editing](#4-contextual-editing) layer for the Saltmarsh class. Values represent the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves. Lower values indicate likely coastal pixels, reflecting both distance inland and topography. The values of the coastal connectivity layer are dimensionless with low values representing high coastal connectivity and high values indicating lower coastal connectivity.

### Data Format

#### Cloud-optimised GeoTIFF

Layers of the DEA Coastal Ecosystems product suite are provided as single continental scale cloud-optimised GeoTIFFs (COGs). For data access and use in geospatial information system (GIS) environments, [streaming](/guides/continental-cogs-geotiff-mosaics/) of these datasets is strongly recommended rather than downloading. Web mapping services (WMS) are also available for all [DEA datasets](./?tab=access).

#### Product naming convention

To stream COG versions of DEA data, you will need to identify the data layers by their full product name. The DEA standard [file naming convention](/guides/reference/collection_3_naming/) has been applied as follows:

```text
{Organisation}_{Platform}_{Product}_{Reporting period}_{Collection}_{Version}_{Tile reference}_{Data date}--{Data period}_{Product status}_{Band name}.{File extension}
```

For example, the 2021 DEA Coastal Ecosystems classification layer is named

```text
ga_s2_coastalecosystems_cyear_3_v1-0-0_AU_2021—P1Y_final_classification.tif
```

## Processing steps

### Workflow

DEA Coastal Ecosystems is a machine learning workflow comprised of four primary components (Figure 3): Training data, Covariate data, Machine learning and Contextual editing. 

:::{figure} /_files/dea-coastalecosystems/CEM_flowchart.png

**Figure 3.** Primary components and outputs of the DEA Coastal Ecosystems workflow.
:::

These components are discussed in further detail below. The validation process is discussed in the [Quality](./?tab=quality) section.

### 1. Training data

::::{dropdown} Data curation
[Continental training data](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/data/training_data_input/MultEcosy_TData_v1_0.geojson), developed for [this work](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/docs/publications/JCU_Coastal_Training_Data_Report_1_27012023_FR%20.pdf) (Canto et al., 2023), comprised a point-record training set of 40,934 Australian coastal ecosystem type occurrences (Figure 4). Development of this dataset was completed for use with multi-ecosystem classification models.

The dataset integrated occurrence records from four data sources:

- Australia coastal ecosystem mapping (Becker et. al, 2023)
- Australia seagrass mapping (Navarro et. al, 2022)
- Australia saltmarsh mapping (Navarro et. al, 2023)
- Global intertidal change (Murray et. al, 2019; Murray et al., 2022)

:::{figure} /_files/dea-coastalecosystems/Original_training_point_distribution.png

**Figure 4.** (After Canto et al., 2023; Becker et al., 2023.) 40,934 expert labelled point occurrences of coastal ecosystem types, distributed continentally around the Australian coastline.
:::
::::

:::{dropdown} Ecosystem definitions
The training data definitions for Australian coastal ecosystems (Table 1; Canto et al., 2023) were sourced from the Blue Carbon Method (CER, 2022) and the International Union for Conservation of Nature Global Ecosystem Typology (Keith et al., 2022). 

Training point class descriptors (level 2, L2) were aggregated into broader level 1 (L1) class categories to form the basis of the DEA Coastal Ecosystems classification schema. The mapping of L2 to L1 ecosystem types, and their definitions, are described in Table 1.

<figure>
    <figcaption>Table 1. Ecosystem definitions and class mappings.</figcaption>
</figure>

| L2 ecosystem type | L1 ecosystem type | L1 Definition |
|-------------------|-------------------|---------------|
| • Land<br>• Supratidal forest<br>• Freshwater wetland<br>• Sand<br>• Water | Terrestrial/Other | Includes natural or anthropogenic land cover types that occur in non-intertidal areas but within the coastal zone such as supratidal forests, frequently inundated croplands, freshwater wetlands and permanent sand dunes. |
| • Seagrass (subtidal) | Permanent water | Refers to a variety of permanent water bodies around the coast but not within the intertidal zone. These water bodies range from deep permanent ocean to freshwater rivers and lakes and include clear and turbid waters. Includes submerged vegetation and substrates such as subtidal seagrass if the bottom is visible. |
| • Mudflat<br>• Intertidal non-vegetated soft sediments | Intertidal | Ecosystem occurring in low-sloping areas of the intertidal zone. Includes muddy, sandy and rocky substrates. In soft sediments, can readily transition to seagrass, mangrove or saltmarsh ecosystems if conditions become favorable for the colonisation of vegetation through changes in sea level or freshwater inundation over time. |
| • Mangrove | Mangrove | Ecosystem comprised of trees and shrubs which a) occupy the intertidal zone or floodplains, including marine and estuarine areas; and b) grow in saline or brackish water. |
| • Saltmarsh<br>• Algal Mats | Saltmarsh | Ecosystem comprised of a) salt-tolerant herbaceous plants and occasionally woody shrubs; and b) occur on floodplains and in estuaries and can be flushed with water from a combinations of sources including rainfall, rivers, groundwater and seawater. This includes saltmarsh in sparsely vegetated saline or hypersaline ecosystems. |
| • Seagrass (intertidal) | Intertidal seagrass | Ecosystem comprised of grass-like plants that grow in shallow intertidal coastal waters. Seagrasses are aquatic flowering plants that form meadows in temperate and tropical regions of Australia. |
| • Saltflat | Saltflat | A subtype of saltmarsh ecosystems comprising bare saltmarsh. Saltflats include sparsely vegetated saline or hypersaline ecosystems |
:::

::::{dropdown} Regional modelling
A bioregional approach was used to improve modelling performance by accounting for regional ecological variations while maintaining the ability to apply a consistent classification schema. 

Seven bioregions (Figure 5) were developed with expert consultation across Geoscience Australia, University of Queensland, James Cook University and University of New South Wales, guided by Natural Resource Management regions, tidal regimes, climate forcing and ecosystem dynamics. 

These regions enabled models to be developed with regional specific training data to account for differences across the common ecosystem classes (e.g. the varied ecological nature of saltmarsh across the country), as well as regional climate and seasonal impacts on the covariate data inputs.

It is important that these regions be regarded as a pragmatic technical choice rather than an attempt at a comprehensive national  bioregionalization. 

:::{figure} /_files/dea-coastalecosystems/Labelled_tile_regions.png

**Figure 5.** Seven biogregions were used to model coastal ecosystems.
:::
::::

:::{dropdown} Training Point Expansion
Introducing modelling regions had implications for the size and balance of the training data sets once split across the seven bioregions, with many ecosystem training point classes falling below a reasonable representative sample number. 

The development of the original training data set on Landsat 30 m data, coupled with an acquisition protocol focused on spatially homogenous regions, presented an opportunity to expand the training data sets when considering the increased resolution of the Sentinel-2-based product. With Sentinel-2's 10 m resolution pixels falling within the tolerance established for the training data point validity (30&ndash;40 m), a semi-automated process was implemented to expand the existing training dataset. This semi-automated approach was particularly effective for densifying training data coverage in homogeneous ecosystem patches while maintaining data quality.

Training data densification was achieved by resampling the original training data points to 10 m resolution. By sampling the surrounding 9 pixels of each original training point, the overall number of training data points was increased to approximately 368,000.

This approach balanced the need for increased training data volume across all seven modelling regions while maintaining data quality and ecological validity (Table 2). The process also included more spatial and spectral variability in the modelling process, resulting in a small but consistent improvement in [accuracy](./?tab=quality#accuracy) when models used the expanded training data set.

<figure>
    <figcaption>Table 2. Expanded training data distribution across model regions. Modelling regions: North West (NW), North East (NE), Gulf of Carpentaria (Gulf), West, South West (SW), South East (SE) and Tasmania (Tas.). Note that no mangroves or saltflat are recorded in Tasmania.</figcaption>
</figure>

| Region | Water | Mudflat | Mangrove | Saltmarsh | Saltflat | Terrestrial/Other | Intertidal seagrass | Total |
|--------|-------|---------|----------|-----------|----------|-------------------|---------------------|-------|
| NW | 4959 | 3135 | 7893 | 4641 | 5583 | 28734 | 186 | 55131 |
| NE | 9354 | 6424 | 8617 | 4473 | 3169 | 20664 | 5072 | 57773 |
| Gulf | 2754 | 2473 | 3960 | 3267 | 2526 | 7818 | 3464 | 26262 |
| West | 1638 | 2385 | 2241 | 2481 | 2898 | 12471 | 1765 | 25879 |
| SW | 2718 | 816 | 441 | 1926 | 126 | 46512 | 1377 | 53916 |
| SE | 9234 | 3891 | 7514 | 15512 | 422 | 64705 | 9734 | 111012 |
| Tas. | 2697 | 1359 | 0 | 3120 | 0 | 5622 | 1319 | 14117 |

:::

### 2. Covariate Data

:::{dropdown} Covariate Data Stack
Covariate data describes the input datasets used to train the ML models. Covariate data stacks were generated using a combination of Sentinel-2 Analysis Ready Data, remote-sensing indices and derived datasets (Table 3). These covariate stacks of 121 total variables were generated for each of the modelling years.

<figure>
    <figcaption>Table 3. Covariate datasets used to model coastal ecosystems.</figcaption>
</figure>

| Data Source | Variable | Percentiles | Total Count |
|-----|-----|-----|-----|
|[Sentinel-2 ARD Reflectance](/data/category/dea-surface-reflectance/) | nbart_blue | 10,20,40,60,80 | 5 |
|  | nbart_green | 10,20,40,60,80 | 5 |
|  | nbart_red | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_1 | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_2 | 10,20,40,60,80 | 5 |
|  | nbart_red_edge_3 | 10,20,40,60,80 | 5 |
|  | nbart_nir_1 | 10,20,40,60,80 | 5 |
|  | nbart_nir_2 | 10,20,40,60,80 | 5 |
|  | nbart_swir_2 | 10,20,40,60,80 | 5 |
|  | nbart_swir_3 | 10,20,40,60,80 | 5 |
| Sentinel-2-derived indices |  |  |  |
|• Automated Water Extraction Index (no shadow) (Feyisa et al., 2014) | AWEI_ns | 10,20,40,60,80 | 5 |
|• Automated Water Extraction Index (shadow) (Feyisa et al., 2014) | AWEI_sh | 10,20,40,60,80 | 5 |
|• Enhanced Vegetation Index (Huete et al., 2002) | EVI | 10,20,40,60,80 | 5 |
|• Leaf Area Index (Boegh et al., 2002) | LAI | 10,20,40,60,80 | 5 |
|• Modified Normalized Difference Water Index (Xu, 1996) | MNDWI | 10,20,40,60,80 | 5 |
|• Normalized Difference Vegetation Index (Rouse et al., 1973) | NDVI | 10,20,40,60,80 | 5 |
|• Normalized Difference Water Index (McFeeters, 1996) | NDWI | 10,20,40,60,80 | 5 |
|• Tasseled Cap Brightness (Crist, 1985) | TCB | 10,20,40,60,80 | 5 |
|• Tasseled Cap Greenness (Crist, 1985) | TCG | 10,20,40,60,80 | 5 |
|• Tasseled Cap Wetness (Crist, 1985) | TCW | 10,20,40,60,80 | 5 |
|• Tasseled Cap Wetness (GSO variant) (Nedkov, 2017) | TCW_GSO | 10,20,40,60,80 | 5 |
|• Water Index (Fisher et al., 2016) | WI | 10,20,40,60,80 | 5 |
| [DEA Tidal Composites](/data/product/dea-tidal-composites/?tab=specifications) | low_blue |  | 1 |
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
|Total Covariates |  |  | 121 |

:::

::::{dropdown} Coastal Connectivity
The Coastal Connectivity layer (also published as a [QA product layer](#quality-assurance-layers)) was designed as an accumulated cost-distance dataset to indicate likely coastal pixels. This was achieved by determining the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves at each pixel location (Figure 6), using the following datasets:

- Shuttle Radar Topography Mission Digital Elevation Model Version 1 (Gallant et al., 2011).
- Highest Astronomical Tide ([Branson, 2023](https://data.csiro.au/collection/csiro%3A61319v1)).
- The extent of the [DEA Mangroves](/data/product/dea-mangroves/) product.

Coastal connectivity is used here as a covariate layer within the modelling process, and as an additional contextual editing layer for the Saltmarsh class. 

:::{figure} /_files/dea-coastalecosystems/connectivity_Mallacoota.png

**Figure 6.** a) Mallacoota, Victoria low-tide [DEA Tidal Composite](/data/product/dea-tidal-composites/) for 2021; b) Low elevation areas, highly connected to tidally-influenced coastlines, have low connectivity values (light grey). Elevated areas are penalised with high connectivity values (dark grey), even if located close to tidally influenced areas.
:::
::::

### 3. Machine Learning

:::{dropdown} Training Point Attribution
For the v1.0.0 implementation of the model, the full expanded Training Point dataset was attributed with covariate data from both the 2021 and 2022 modelling year covariate stacks. Training points where covariates were derived from <10 clear observations in either modelling year were removed from the relevant modelling year dataset.

Both of these attributed annual Training Point datasets were then combined to form the final datasets for Model training.
:::

::::{dropdown} Model training
The DEA Coastal Ecosystems workflow trains two [random-forest classifiers](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) for each of the seven [modelled regions](#regional-modelling) from the covariate-attributed stack of training data: 

- a multi-class ecosystem model (mangrove, saltmarsh and salt flat) and;
- an intertidal model (intertidal and intertidal-seagrass). 

The multi-class ecosystem model utilized all data in the training data library while the Intertidal model was developed using only training data points located within the [DEA Intertidal Extents high confidence intertidal region](/data/product/dea-intertidal/#core-product-layers). Functionally, this meant that within the bounded extents of the Intertidal modelled region, any training points included in the model that were not defined as Intertidal Seagrass were considered Intertidal. For a discussion on the implications of this aspect of the model classification see the [Caveats and Limitations](./?tab=quality#constraint-of-the-intertidal-model-and-definition-of-the-intertidal-class) section.

Multi-class and binary random-forest models were fit for each region using: 

- Number of trees (800): A large ensemble size ensures stable, reliable predictions by aggregating insights from many diverse trees, reducing the impact of any single tree's errors.
- Minimum samples per split (2): Set to the minimum allowed value to give the model maximum flexibility in finding predictive patterns. This is particularly useful when relationships in the data are complex or subtle.
- Minimum samples per leaf (1): Allows the model to capture fine-grained patterns and edge cases in the data without artificially constraining individual tree decisions. The large number of trees (800) provides natural protection against overfitting.
- Maximum depth (10): Limits tree complexity to prevent overfitting while still allowing enough depth to capture meaningful multi-level interactions between variables. Strikes a balance between model expressiveness and generalizability.

A [k-fold cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics) approach was used to assess model behaviour and optimise the model parameters. Optimized model parameters were used to fit the final models using the full training data set for the multi-class model and the intertidal masked training data set for the seagrass model. A monte carlo resampling framework was used to validate the mapping products and calculate accuracy metrics including overall accuracy, class-based accuracy and relevant confidence intervals. Overall model accuracy statistics are reported in the [Quality](./?tab=quality#accuracy) tab. 

The combined 2021 and 2022 stacks of covariate-trained training data ensured the classifier models were suitable for prediction into both years. Common covariates that exhibited a top-10 feature importance for the ecosystem models included the NDVI and MNDWI percentiles as well as the coastal-connectivity. Common top-10 feature importance covariates for the seagrass models included the tasselled cap wetness percentiles and 'red_edge', 'nir' and 'swir' bands from the low-tide [DEA Tidal Composite](/data/product/dea-tidal-composites/) (Figure 7).

:::{figure} /_files/dea-coastalecosystems/ML_Feature_Importance.png

**Figure 7.** Commonality in the top 10 most important covariates for each of the seven regional ecosystem (top) and seagrass (bottom) models. The y-axis represents the number of regional models where the covariate features in the top 10.
:::
::::

:::{dropdown} Ecosystem prediction
Coastal ecosystems were predicted using Covariate data stacks created for each modelling year.

Initial predictions were made using the multi-class ecosystem model, generating interim probability layers for mangrove, saltmarsh and salt flat ecosystems ([Figure 3](#workflow)). An interim classified ecosystem output layer was also generated to capture the highest probability ecosystem class predicted for each pixel and included mangrove, saltmarsh and saltflat classes. Water and Terrestrial classes in this interim layer were classified as `nodata`. 

The Intertidal modelling extent was then set using the high confidence intertidal extent from the [DEA Intertidal](/data/product/dea-intertidal/#core-product-layers) dataset. The Intertidal model was then used to predict Intertidal seagrass from the annual covariate stacks masked to this modelling extent. The output from this process is the interim Intertidal seagrass probability layer (Figure 3).
:::

### 4. Contextual editing

:::{dropdown} Rationale
The interim classified ecosystem layer defines classes based on the highest probability class for each pixel, which can result in a classification based on relatively low probability values were a pixel is modelled as a likely mixed ecosystem. Combined with the inherent uncertainty and resulting misclassification when applying a machine learning mapping methodology at a continental scale, this meant that a range of rulesets and post-processing operations were applied, collectively termed ‘contextual editing’, to deliver the final Classification layer.

Probability layers were also masked in this contextual editing process, as described in the [probability layer description](#probability).

The following section details the rules and processes that were applied, with justifications or links to further discussion points.
:::

:::{dropdown} Classifier rulesets

All classifier rulesets were applied to the interim ecosystem classification layer ([Figure 3](#workflow)) to produce the final Classification dataset.

1. **Remove unused classes**: The ecosystem classification output layer was masked to remove all saltflat pixels (see [Caveats and Limitations](./?tab=quality#saltflat-mapping)). 
1. **Apply probability thresholds**: A probability threshold of 50% was applied to the Saltmarsh and Mangrove pixels, with pixels below this threshold reassigned as `nodata`. A 50% probability threshold was selected based on the alignment of the outputs with external mapping products, and the conservative consideration that 50% provides a clear majority vote by the machine learning models.
1. **Apply environmental corrections**: Saltmarsh pixels were masked to the observed coastal-connectivity range identified by the saltmarsh training data points. To exclude outliers, the saltmarsh connectivity mask was thresholded to the 99.5th percentile connectivity value (254) for all region-combined saltmarsh points from the training data set. This choice was made to remove misclassifications of saltmarsh in regions considered unconnected to coastal regions (see [Coastal Connectivity](#coastal-connectivity)). See [Caveats and Limitations](./?tab=quality#connectivity-masking-and-saltmarsh) for further discussion on the implications of thresholding based on existing distribution of Saltmarsh training data.

:::

:::{dropdown} Classifier masking

1. **Apply mangrove mask**: Mangrove pixels that fell outside of the [Global Mangrove Watch (GMW) Habitat Mask](https://doi.org/10.5281/zenodo.74784913) (Bunting et al. 2025) were removed. This habitat mask defines an ecologically suitable niche for Mangrove occupation, and was used here to align our Mangrove mapping with global approaches and to minimize false-positive Mangrove classification in inhospitable environments.
1. **Apply Intertidal seagrass probability threshold**: Within the defined Intertidal model extent, the Intertidal seagrass probability layer was used to define the Intertidal seagrass classification at a probability of greater than or equal to 70%. The 70% threshold was selected as a conservative value to account for inter-annual variability in seagrass meadows (see [Caveats and Limitations](./?tab=quality#interpretation-of-probability-layers-and-implications-for-change-applications)).
1. **Apply manual mask**: A manual masking process was applied to the Classification layer, based on expert-identified misclassifications (including roads, urban areas, terrain shadow, and data noise). For full traceability, this polygon masking layer is provided here: [supplementary files](http://dea-public-data-dev.s3-website-ap-southeast-2.amazonaws.com/?prefix=derivative/dea_coastalecosystems/supplementary/).
1. **Apply land use mask**: Industrial, urban or road areas as identified in the Australian Catchment Scale Land Use and Management dataset (ABARES, 2021) were removed.
1. **Remove and replace isolated pixel groups**: To reduce pixel-based noise in the data, the Classification layer was sieved to remove and replace isolated pixels in groups of 9 or less with the dominant surrounding class type.

:::

:::{dropdown} Probability masking
1. **Apply probability threshold**: Pixels with values of less than 20% were removed from the Mangrove, Saltmarsh and Saltflat probability layers to remove very low confidence pixels and noise from the dataset to improve interpretability.

:::

## Software

- The [Coastal Ecosystems GitHub](https://github.com/GeoscienceAustralia/dea-coastalecosystems) code repository contains the core functionality required to run the DEA Coastal Ecosystems workflow. The code leverages functions from [DEA Tools](/notebooks/Tools/) that have dependencies on [Scikitlearn](https://scikit-learn.org/stable/).
- The [DEA Tools](/notebooks/Tools/) library contains essential functionality required to generate random-forest models using [DEA Analysis Ready Data](/data/category/dea-surface-reflectance/).
- The [Scikitlearn](https://scikit-learn.org/stable/) library provided the random-forest classification methodologies.

## References

ABARES 2021, Catchment Scale Land Use of Australia – Update December 2020, Australian Bureau of Agricultural and Resource Economics and Sciences, Canberra, February, CC BY 4.0, DOI: 10.25814/aqjw-rq15

Branson, Paul (2023): Coastal carbon - Australia's blue forest future - Water Levels. v1. CSIRO. Data Collection. https://doi.org/10.25919/6672-jx11

Becker, M.L., Navarro, A., Canto, R., & Murray, N.J. (2023) [An Australian coastal ecosystem training library for remote sensing classification models.](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/docs/publications/JCU_Coastal_Training_Data_Report_1_27012023_FR%20.pdf) Unpublished report to the Department of Climate Change, Energy, the Environment and Water. James Cook University, Townsville.

Boegh, E., Soegaard, H., Broge, N., Hasager, C. B., Jensen, N. O., Schelde, K., & Thomsen, A. (2002). Airborne multispectral data for quantifying leaf area index, nitrogen concentration, and photosynthetic efficiency in agriculture. Remote sensing of Environment, 81(2-3), 179-193.

Bunting, P., Rosenqvist, A., Hilarides. (2025) Global Mangrove Watch: Mangrove Habitat Mask v27.0 Dataset. https://doi.org/10.5281/zenodo.7478491

Canto. R., Navarro., A.,Becker, M., Murray, N.J., (2023) [Australian coastal ecosystem training library](https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/data/training_data_input/MultEcosy_TData_v1_0.geojson). Unpublished dataset.

Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. Remote Sensing of Environment, 17(3), 301–306. https://doi.org/10.1016/0034-4257(85)90102-6

Feyisa, G. L., Meilby, H., Fensholt, R., & Proud, S. R. (2014). Automated Water Extraction Index: A new technique for surface water mapping using Landsat imagery. Remote sensing of environment, 140, 23-35.

Fisher, A., Flood, N., & Danaher, T. (2016). Comparing Landsat water index methods for automated water classification in eastern Australia. Remote Sensing of Environment, 175, 167-182.

Gallant, J.C., Dowling, T.I., Read, A.M., Wilson, N., Tickle, P. and Inskeep, C., 2011. 1 second SRTM Derived Digital Elevation Models User Guide. Geoscience Australia www.ga.gov.au/topographic-mapping/digital-elevationdata.html 

Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., & Ferreira, L. G. (2002). Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote sensing of environment, 83(1-2), 195-213.

Keith, D.A., Ferrer-Paris, J.R., Nicholson, E. et al. (2022) A function-based typology for Earth’s ecosystems. Nature 610, 513–518 [https://www.nature.com/articles/s41586-022-05318-4](https://doi.org/10.1038/s41586-022-05318-4). 

Lovelock, C.E., Sippo, J., Fernanda Adame, M., Dittmann, S., Hickey, S., Hutley, L., Jones, A., Kelleway, J., Lavery, P., Macreadie, P., Maher, D., Mosely, L. and Rogers, K (2021) [Blue carbon accounting model (BlueCAM) technical overview](https://cer.gov.au/document/blue-carbon-accounting-model-bluecam-technical-overview). Report to the Clean Energy Regulator. University of Queensland.

Lyons, M.B., Keith, D.A., Phinn, S.R., Mason, T.J., & Elith, J. (2018). A comparison of resampling methods for remote sensing classification and accuracy assessment. Remote Sensing of Environment, 208, 145-153. https://doi.org/10.1016/j.rse.2018.02.026

McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. International journal of remote sensing, 17(7), 1425-1432.

Murray N. J., Canto, R., Worthington, T. A., Lyons, M.B. (2022) Supplementary Data S1 to Losses and gains of Earth's tidal wetlands. Figshare. https://doi.org/10.6084/m9.figshare.19121660.

Murray, N. J., Phinn, S. R., DeWitt, M., Ferrari, R., Johnston, R., Lyons, M. B., Clinton, N., Thau, D. & Fuller, R. A. (2019). The global distribution and trajectory of tidal flats. Nature, 565, 222-225

Murray, N.J., et al., High-resolution mapping of losses and gains of Earth’s tidal wetlands. Science 376, 744-749(2022). DOI: [10.1126/science.abm9583](https://www.science.org/doi/10.1126/science.abm9583)

Navarro, A., Canto, R., Toor, M., & Murray, N.J. (2022) An Australian intertidal seagrass training library for remote sensing classification models. Unpublished report to the Department of Agriculture, Water and the Environment. James Cook University, Townsville.

Navarro, A., Canto, R., Toor, M., Becker, M.L., Lyons, M. & Murray, N.J. (2023) Australian Saltmarsh Map. Unpublished report to the Clean Energy Regulator. James Cook University, Townsville. 

Nedkov, R., (2017). “Orthogonal transformation of segmented images from the satellite Sentinel-2,” Comptes Rendus De lAcad. Bulgare Sci., vol.  70, no.  5, pp.  687–692.

Rouse Jr, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1973). Monitoring the vernal advancement and retrogradation (green wave effect) of natural vegetation (No. NASA-CR-132982).

Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. International journal of remote sensing, 27(14), 3025-3033. 

