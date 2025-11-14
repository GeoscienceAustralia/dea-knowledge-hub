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

## Lineage (todo fix links)

The DEA Coastal Ecosystem Map was initiated as a collaborative project to support the Commonwealth Department of Climate Change, Energy, the Environment and Water (DCCEEW) to underpin the creation of Environmental Economic Accounts (EEA) for ecosystems in Australia’s coastal zone. This followed experimental Ocean Accounts, delivered in 2022 and based on selected individual ecosystem earth observation derived datasets.

Leveraging a methodology that mapped global shifts in tidal wetlands (https://www.science.org/doi/10.1126/science.abm9583), Geoscience Australia has collaborated with James Cook University and the University of New South Wales to deliver a similar approach for Australia in this Coastal Ecosystem Map product suite. Initial Beta versions of the DEA Coastal Ecosystem Map have been used to underpin the February 2025 release of the National Ecosystem Accounts experimental estimates for the Coastal Realm (https://www.abs.gov.au/statistics/environment/environmental-accounts/national-ecosystem-accounts-experimental-estimates/latest-release#coastal-realm), with the first V1.0.0 release of the DEA Coastal Ecosystem Map expected to contribute to the upcoming 2026 National Ecosystem Account released by the Australian Bureau of Statistics (ABS)

Targeted stakeholder engagement and product feedback sessions have been conducted throughout the development of the product to ensure where possible a complementary alignment of the DEA Coastal Ecosystem Map product to State Government and Academic mapping efforts. These efforts are aimed at ensuring the ease of uptake and integration of the product into a range of environmental reporting applications across jurisdictions (e.g State of the Environment).

Stakeholder engagement at all levels will continue to drive the development of the Coastal Ecosystem Map product in a cycle of continuous improvement, validation, feedback integration and inclusion of additional ecosystem types (see Caveats/FAQS). 

## Technical information

### Product Features

The DEA Coastal Ecosystem Map is a multi-layered dataset and is produced for two years, 2021 and 2022. See [Specifications](_tables.yaml) for individual layer metadata.

### Core Product Layers
Five core layers are included in The DEA Coastal Ecosystem Map: the classification and four probability layers.
#### *Classification* (todo: fix links, add figures)
The primary layer of the DEA Coastal Ecosystem Map is a categorical classification of the extent of mangrove, saltmarsh, intertidal and intertidal seagrass coastal ecosystems (Figure A). The layer is built from thresholds of the ecosystem probability layers (link to below), and constrained, modified and masked with a range of ancillary datasets and QA/QC processes (See Contextual Editing).
Product layers for each calendar year of the product time range are published with the following categorical class values:

- Intertidal (2)
- Mangrove (3)
- Saltmarsh (4)
- Intertidal Seagrass (5) 

[Placeholder Figure A]

#### *Probability* (todo: links and figures)
Individual ecosystem probability layers are provided as supporting datasets to aid the interpretation of extents for four ecosystem classes, Mangroves, Saltmarsh, Saltflat and Intertidal Seagrass (Figure B). Probability values in these layers represent the percentage of random-forest trees that vote at each pixel for a given ecosystem in the relevant Machine Learning model; the Ecosystem Model (Mangroves, Saltmarsh, Saltflat) and the Intertidal Model (Intertidal Seagrass).

The Intertidal class within the Intertidal model has been fixed to the extent of the DEA Intertidal Extents product (see Machine Learning/Ecosystem Prediction), so the probability layer for this ecosystem is not provided. As the Intertidal Seagrass is modelled within this fixed extent, the corresponding probability layer is also constrained to these extents.

Probability layers for ecosystem layers in the Ecosystem Model (Mangroves, Saltmarsh and Saltflat) are masked below 20% probability to remove very low confidence pixels and noise from the dataset to improve interpretability.

The Saltflat ecosystem has been excluded from the classification product layer, though the probability layer generated for this ecosystem as part of the Ecosystem Model has been provided. For the reasoning behind this decision, and a discussion on further work required on this ecosystem class, see Saltflats Caveats section.

For further information how these Probability layers can be interpreted and used to aid in interpretation of the classified ecosystem map, including for mixed or transitional classes, see Prob Caveats 

[Placeholder Figure B]

### Quality Assurance Layers (todo: links and figs)
Two quality assurance layers (Figure C) are included in the DEA CEM product suite: 
#### Clear count (*qa-count-clear*)

A layer showing the distribution of clear and valid satellite observations at each Sentinel-2 (link to S2 ARD) pixel during the analysis period. Artefacts that can invalidate pixels include cloud cover/shadow and low geometric accuracy. A pixel only proceeds into the DEA Coastal Ecosystem Map workflow if it has more than 10 valid observations. The qa-count-clear layer shows that the maximum number of clear observations for any single pixel was 130 +/-1 in both years of the dataset.

#### Coastal connectivity (*qa-coastal-connectivity*)
An accumulated cost-distance connectivity layer used as a covariate layer within the modelling process, and as an additional contextual editing layer for the Saltmarsh class. Values represent the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves. Lower values indicate likely coastal pixels, reflecting both distance inland and topography. The values of the coastal connectivity layer are dimensionless.

[Placeholder: Figure C]

### Data Format (todo: links)
#### Cloud-optimised GeoTIFF
Layers of the DEA Coastal Ecosystem Map are provided as single continental scale cloud-optimised GeoTIFFs. For data access and use in geospatial information system (GIS) environments, streaming (link to mosaic access KH page) of these datasets is strongly recommended over downloading of the datasets. Web mapping services (WMS) are also available for all DEA datasets (link to access page).
#### Product naming convention
A standard DEA naming convention (link to KH user guide) has been adopted for DEA Coastal Ecosystem Map datasets. For example, the 2021 DEA Coastal Ecosystem Map classification layer is named
`ga_s2_coastalecosystems_cyear_3_v1-0-0_AU_2021—P1Y_final_classification.tif`

interpreted as `[Product ID]_[Layer specifics]` where:
- Product ID = `[Geoscience Australia]_[Sentinel-2 dataset]_[Product Name]_[Temporal resolution-calendar year]_[Imagery collection]_[Major product version]`
- Layer specifics = `[Product minor/patch version]_[Spatial resolution - Australia]_[Year]--[Frequency]_[Dataset maturity]_[Layer name].[filetype]`

## Processing steps

### Workflow (todo: links and figs)
The DEA Coastal Ecosystem Map is a machine learning workflow comprised of four primary components (Figure D): Training data, Covariate data, Machine learning and Contextual editing. 

These components are discussed in further detail below. The validation process is discussed in the ‘Quality’ tab (link to tab).

[Placeholder: Figure D]

### 1.	Training data
#### Data curation (todo: links and figs)
Continental training data, developed for this work (Canto et al., 2023 https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/docs/publications/JCU_Coastal_Training_Data_Report_1_27012023_FR%20.pdf, https://github.com/GeoscienceAustralia/dea-coastalecosystems/blob/main/data/training_data_input/MultEcosy_TData_v1_0.geojson ),comprised a point-record training set of 40,934 Australian coastal ecosystem type occurrences (Fig. E). Development of this dataset was completed for use with multi-ecosystem classification models.
The dataset integrated occurrence records from four data sources:

- Australia coastal ecosystem mapping (Becker et. al, 2023)
- Australia seagrass mapping (Navarro et. al, 2022)
- Australia saltmarsh mapping (Navarro et. al, 2023)
- Global intertidal change (Murray et. al, 2019; Murray et al., 2022)

[Placeholder: Figure E]

#### Ecosystem definitions (todo: links and figs)
The training data definitions for Australian coastal ecosystems (Fig q, Canto et al., 2023) were sourced from the Blue Carbon Method (a tidal restoration of blue carbon ecosystems method by the Clean Energy Regulator, CER 2022) and the International Union for Conservation of Nature Global Ecosystem Typology (Keith et al., 2022). 

The granular level 2 class descriptors (L2) of the training datapoints were aggregated into broader level 1 class (L1) categories which form the basis of the DEA Coastal Ecosystem Map. The mapping of L2 to L1 ecosystem types, and their definitions, are described in Table 1

[Placeholder: table 1]

#### Regional modelling (todo: links and figs)
A bioregional approach was used to improve modelling performance by accounting for regional ecological variations while maintaining the ability to apply a consistent classification schema. 

Seven bioregions (Fig F) were developed with expert consultation across Geoscience Australia, University of Queensland, James Cook University and University of New South Wales, guided by Natural Resource Management regions, tidal regimes, climate forcing and ecosystem dynamics. 

These regions enabled models to be developed with regional specific training data to account for differences across the common ecosystem classes (e.g. the varied ecological nature of saltmarsh across the country), as well as regional climate and seasonal impacts on the covariate data inputs.

It is important that these regions be regarded as a pragmatic technical choice rather than an attempt at a comprehensive bioregionalization. 

[Placeholder: Figure F]

#### Training Point Expansion (todo: links and table)
Introducing the modelling regions had implications for the size and balance of the training data sets once split across the seven bioregions, with many ecosystem training point classes falling below a reasonable representative sample number. 

The development of the original Training data set on Landsat 30m data, coupled with an acquisition protocol focused on spatially homogenous regions, presented an opportunity to expand the training data sets when considering the increased resolution of the CEM product. With Sentinel-2's 10m resolution pixels falling within the tolerance established for the training data point validity (30-40m), a semi-automated process was implemented to expand the existing training dataset. This semi-automated approach was particularly effective for expanding coverage in homogeneous ecosystem patches while maintaining data quality.

This was achieved by resampling the original training data points to 10 m resolution, sampling the surrounding 9 pixels of each original training point, to increase the overall number of training data points, to approx 368,000.

This approach balanced the need for increased training data volume across all seven modelling regions (Table 2) while maintaining data quality and ecological validity. The process also included more spatial and spectral variability in the modelling process, resulting in a small but consistent improvement in accuracy when using the expanded training data set (see Quality/Validation)

[Placeholder: Table 2]

### 2.	Covariate Data (todo: links and table)
Covariate data stacks were generated using a combination of Sentinel-2 Analysis Ready Data, calculated indices and derived datasets (Tables 3-4). These covariate stacks of 131 total variables were generated for the extent of the CEM Product Grid (reference/link), for each of the modelling years.

[Placeholders: Tables 3,4]

#### Coastal Connectivity (todo: links)
The Coastal connectivity layer (also published as a QA product layer) is designed as an accumulated cost-distance dataset to indicate likely coastal pixels. This is achieved by determining the cumulative elevation above Highest Astronomical Tide that must be traversed along the shortest path from tidally influenced coastal waters and mangroves at each pixel location (Figure G), using the following datasets:

- Shuttle Radar Topography Mission (SRTM) Digital Elevation Model Version 1 (Gallant et al., 2011)
- A Highest Astronomical Tide Dataset developed at CSIRO (https://data.csiro.au/collection/csiro%3A61319v1)
- The extent of the DEA Mangroves product
Coastal connectivity is used here as a covariate layer within the modelling process, and as an additional contextual editing layer for the Saltmarsh class. 

[Placeholder: Figure G (new fig demonstrating coastal connectivity)]

### 3.	Machine Learning
#### Training Point Attribution
The full expanded Training Point dataset was attributed with covariate data from both the 2021 and 2022 modelling year covariate stacks. Training points where covariates were derived from <10 clear observations in either modelling year were removed from the relevant modelling year dataset, along with training points for the Sub-tidal Seagrass classification (see Future Work).

Both of these attributed annual Training Point datasets were then combined to form the final datasets for Model training.
#### Model training (todo: links and expert review)
The DEA Coastal Ecosystem Map workflow trains two random-forest classifiers for each of the seven modelled regions (link to scikitlearn Random Forest doco https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html, link to modelling regions) from the covariate-attributed stack of training data: 

- a multi-class ecosystem model (mangrove, saltmarsh and salt flat) and 
- an Intertidal model (intertidal and intertidal-seagrass). 

The multi-class ecosystem model utilized all data in the training data datasets while the Intertidal model were developed using only training data points located within the DEA Intertidal Extents high confidence intertidal region (link). Functionally, this meant that within the bounded extents of the Intertidal modelled region, any training points included in the model that were not defined as Intertidal Seagrass were considered Intertidal. For a discussion on the implications of this aspect of the model classification see Intertidal Caveat section

Multi-class and binary random-forest models were fit for each region using:

- 800 estimators (trees?)
- Minimum samples split of 2
- Minimum samples leaf of 1
- Maximum (tree? Branch?) depth of 10

Each model was first trained and evaluated using a k-fold cross-validation train/test split of the training data (https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics) to report accuracy statistics and refine optimal model parameters. Using a 5-fold cross-validation, the overall mean of the regional ecosystem model accuracy-means was 0.95 with a mean standard deviation of 0.01. Optimized model parameters were then used to retrain the final random-forest classifiers using the full training data set for the multi-class model and the intertidal masked training data set for the seagrass model.
The combined 2021 and 2022 stacks of covariate-trained training data ensure the classifier models are suitable for prediction into both years. Common covariates that exhibited a top-10 feature importance for the ecosystem models include the NDVI and MNDWI percentiles as well as the coastal-connectivity (Figure H).

[Placeholder: Figure H]

#### Ecosystem prediction (todo: links)
Coastal ecosystems were predicted into the Covariates stacks created for the CEM product extents for each modelling year.

Initial predictions were made using the multi-class ecosystem model, generating interim probability layers for mangrove, saltmarsh and salt flat ecosystems. An interim classified ecosystem output layer is also generated to capture the highest probability ecosystem class predicted for each pixel by the model.

The interim classified ecosystem output layer includes mangrove, saltmarsh and saltflat classes (See Interim Outputs, Figure B). Water and Terrestrial classes in this interim layer are then classified as NoData. 

The Intertidal modelling extent is then set using the high confidence intertidal extent from the DEA Intertidal dataset. The Intertidal model is then used to predict Intertidal seagrass into the annual covariate stacks masked to this modelling extent. The output from this process is the interim Intertidal seagrass probability layer.

### 4.	Contextual editing
The interim classified ecosystem layer defines classes based on the highest probability class for each pixel, which can result in a classification based on relatively low probability values were a pixel is modelled as a likely mixed ecosystem. Combined with the inherent uncertainty and resulting misclassification when applying a ML mapping methodology at a continental scale, this meant that a range of rulesets and post-processing operations were applied, collectively termed ‘contextual editing’, to deliver the final Classification CEM product layer.

Probability layers are also masked in this contextual editing process, as described in the layer description.

The following rules and processes were applied, with justifications or links to further discussion points included below:

#### Classifier rulesets

1. **Remove unused classes**: The ecosystem classification output layer was masked to remove all saltflat pixels (link to Caveats section in Quality tab). 
1. **Apply probability thresholds**: A probability threshold of 50% was applied to the Saltmarsh and Mangrove pixels within the interim ecosystem classification layer, with pixels of these classes with a probability below this threshold assigned as “nodata”. A 50% probability threshold was selected based on the alignment of the outputs with external mapping products, and the conservative consideration that 50% provides a clear majority vote by the ML models.
1. **Apply environmental corrections**: Saltmarsh pixels were masked to the observed coastal-connectivity range identified by the saltmarsh training data points. To exclude outliers, the saltmarsh connectivity mask was thresholded to the 99.5th percentile connectivity value for all region-combined saltmarsh points from the training data set. This choice was made to remove misclassifications of saltmarsh in regions considered unconnected to coastal regions (see Connectivity Layer). For further discussion on the implications of thresholding based on existing distribution of training data see Saltmarsh Connect Caveat
#### Classifier masking
1. **Apply mangrove mask**: Mangrove pixels that fell outside of the mangrove habitat layer, identified by Global Mangrove Watch (link to dataset) were removed. This habitat mask is widely used in Mangrove mapping studies (do we need a ref?) to define the ecologically suitable habitats that Mangrovesexisting and, and was used here to align our Mangrove mapping with these global approaches and minimize the false positives of Mangrove classification in not-suitable areas.
1. **Apply Intertidal seagrass probability threshold**: Within the defined Intertidal model extent the Intertidal seagrass probability layer was used to define the Intertidal seagrass classification at a probability of greater than or equal to 70 %. The 70 % threshold was selected as conservative value to account for the inter-annual variability of seagrass meadows (see Prob layer discussion)
1. **Apply manual mask**: A manual masking process was applied to the Classification layer, based on expert identified misclassifications in the layer (including roads, urban areas, terrain shadow, data noise). For full traceability this polygon masking layer is provided here. (link to dataset on Github??)
1. **Apply land use mask**: Industrial, urban or road areas as identified in the Australian Catchment Scale Land Use and Management dataset (ACLUM) (link to dataset) were removed.
1. **Remove and replace isolated pixel groups**: To reduce pixel based noise in the data, the classification layer was sieved to remove and replace isolated pixels in groups of 9 or less with the dominant surrounding class type.
#### Probability masking
1. **Apply probability threshold**: Pixels with values of less than 20 % were removed from the Mangrove, Saltmarsh and Saltflat probability layers to remove very low confidence pixels and noise from the dataset to improve interpretability.


## Software (todo)

## References (todo)

