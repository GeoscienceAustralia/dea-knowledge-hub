## Background

The Australian National Spectral Database (NSD) supports best practice management of reference spectral data collections by providing an extensive suite of standardised metadata for international use. The database has been designed to be consistent with other nationally significant datasets and is a curated repository that will evolve to meet the needs of the Earth observation community.

The NSD is accessed via the application Specchio, initially developed by the University of Zurich, and customised by the University of Wollongong. It represents the collective efforts of many individuals from multiple organisations and is hosted by Geoscience Australia as the custodian of nationally significant geoscientific data. See Hueni et al. (2020) below for further background information.

## What this product offers

The National Spectral Database (NSD) houses spectral data collected by Australian remote sensing scientists. It includes spectra covering targets as diverse as soils, vegetation, waterbodies, coral, macro to micro algae, seagrasses and land surfaces.

The database also includes field-based data routinely collected by Geoscience Australia’s Digital Earth Australia program for calibration and validation measurements, as well as spectral data previously hosted by the University of Wollongong.

Additionally, the NSD features the Aquatic Substrate Library, a dataset covering aquatic spectra collected from 1994 to the present, consisting primarily of end-member and substratum measurements from around Australia.

% ## Data description

## Applications
* Comparison of reflectance measurements from satellite observations e.g. by Landsat 8 and Sentinel 2, to near-coincident ground reference measurements, to verify fitness for purpose of satellite derived data products.
* Development and testing of models describing the relationships between directional spectral reflectance of target surfaces and their biophysical attributes.
* Spectral feature matching for mineralogy applications.
* Application of spectral data to plant physiology studies, geological sciences, soil sciences, limnology, oceanography and atmospheric chemistry, and other research.

## Lineage

### Datasets
* Geoscience Australia field data campaigns: From the ARD Cal/Val team, DEA, GA  
* Aquatic Substrate Library: Compiled by Dr Arnold Dekker (SatDek)  
* University of Wollongong Spectral Datasets: Provided by Dr Laurie Chisolm (UoW)

### Data types
* Spectral data: raw digital numbers (DN), radiance and reflectance.   
* From spectral range VIS-NIR, SWIR1 & SWIR2, wavelengths from 350nm - 2500nm collected with instruments in the field or lab setting.

### Data Collection
* NSD spectral data has been collected by remote sensing scientists in Australia, both in field and lab environments

### Processing
* Where applicable, post-processing is indicated in the relevant metadata field

% ## Processing steps

## Software

Direct download links: [Specchio client zip file](https://github.com/EricHay/NSD_Guides/raw/main/specchio-client.zip) or [.jar installer package](https://github.com/EricHay/NSD_Guides/raw/main/specchio-installer.jar). For further download options see the Specchio website [Downloads page](https://specchio.ch/downloads/).

Specchio is an open source application. The code base is available at the [Specchio GitHub repository](https://github.com/SPECCHIODB/SPECCHIO).

## Contribute your data to the NSD

If you have spectral data collected in Australia, and have relevant metadata and collection information you can contribute this data to be hosted on the NSD. Please familiarise yourself with the [Metadata Standard](/_static/cmi/NSD_Metadata_Standard.pdf), and follow the steps below to contribute:

1) Ensure you adhere to the Metadata Standard and that your dataset meets minimum requirements. Meeting the metadata standard can be as simple as providing GPS information for spatial data, or species images, description or the scientific name for end-member spectra. Spectra submitted without metadata are unsuitable and won't be accepted.
2) Contact the NSD manager: [NSDB\_Manager@ga.gov.au](mailto:NSDB_Manager@ga.gov.au). In your email include the size of the dataset you wish to ingest and confirm that you meet the [Metadata Standard](/_static/cmi/NSD_Metadata_Standard.pdf), and have read the [Technical usage guide](/_static/cmi/NSD_General_Guide.pdf) & [Write access guide](/_static/cmi/NSD_Write_Access_Guide.pdf).

The guides will help you to understand the process of uploading your data and ingest data most efficiently. If you have further queries please enquire via email.

The public server will allow you to view & download data, not upload it. The NSD manager will provide instruction on how to access the upload server.

### Digital Object Identifier (DOI) Minting

DOI minting is offered for new datasets that meet the metadata standard, and are new or existing datasets not previously published elsewhere. Your dataset will get a unique DOI that the database manager will append to your dataset metadata within the NSD. The DOI will be stored separately as a Geoscience Australia metadata record. The DOI record can also provide links to further publications from your dataset, and can easily be updated if needed, or further publications stem from your work. The aim of the DOI is to credit those involved in collecting the dataset, and to provide links to further science stemming from the work.

For a DOI to be minted, sufficient metadata is required for the dataset including names of team members involved, location and timestamps of the study (GPS and UTC time associated with measurements), and links to any associated publications such as journal articles. These should be included as metadata for your dataset when ingesting new data. 

Please contat the NSD manager if you would like to contribute or update data: [NSDB\_Manager@ga.gov.au](mailto:NSDB_Manager@ga.gov.au)

## References

Byrne, G., Walsh, A., Thankappan, M., Broomhall, M., Hay, E. 2021. DEA Analysis Ready Data Phase 1 Validation Project: Data Summary. Geoscience Australia, Canberra. [https://doi.org/10.26186/145101](https://doi.org/10.26186/145101)

Hueni, A., Chisholm, L.A., Ong, C., Malthus, T.J., Wyatt, M., Trim, S.A., Schaepman, M.E., Thankappan, M. 2021. The SPECCHIO Spectral Information System, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 13, pp. 5789-5799, 2020, doi: 10.1109/JSTARS.2020.3025117.

Aasen, H.; Hueni, A.; Machwitz, M.; Malenovský, Z.; Mallick, K.; Paul-Limoges, E.; Schlerf, M.; Schneider, F.D.; Suárez, L.; Van Wittenberghe, S.; Wieneke, S.; Wolf, S. Ecosystem specific Metadata. 2017, 10.13140/RG.2.2.14986.77761

Held, A., Phinn, S., Soto-Berelov, M., & Jones, S. (Eds.). AusCover Good Practice Guidelines: A technical handbook supporting calibration and validation activities of remotely sensed data products. 2015. Version 1.1. TERN AusCover, ISBN 978-0-646-94137-0

Rasaiah, B.A.; Jones, S.D.; Bellman, C.; Malthus, T.J.; Hueni, A. Assessing Field Spectroscopy Metadata Quality. *Remote Sens.* 2015, *7*, 4499-4526

Milton, E.; Schaepman, M.E.; Anderson, K.; Kneubuehler, M.; Fox, N. Progress in field spectroscopy. *Remote Sensing of Environment* 113 Suppl. 2009, 1. 113. 10.1016/j.rse.2007.08.001

