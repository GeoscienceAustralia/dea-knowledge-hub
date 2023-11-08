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

## Technical information

Requirements: Java Runtime Environment (JRE) 8.0 or higher. See [Specchio Release Notes](https://github.com/SPECCHIODB/Guides/raw/master/SPECCHIO_ReleaseNotes.pdf) on supported JRE's. 

Documentation for the Specchio client: [Specchio website](https://specchio.ch/).

Technical information on use of the Specchio application, such as connecting to the NSD and downloading data: [Technical usage guide](/_files/cmi/NSD_General_Guide.pdf).

Information for uploading data (write-access users only): [Write access guide](/_files/cmi/NSD_Write_Access_Guide.pdf).

### Navigating the client

The NSD contains datasets or campaigns of data that can be viewed in two ways.

1) View the NSD folder structure via the data browser:

![data_browser](/_files/cmi/data_browser.jpg)

![data_browser_2](/_files/cmi/data_browser2.jpg)

Expand folders to the desired level, then view (show report), plot spectra, and export data. You may also manually subset data from folders by selecting multiple individual files, shown above. The report applies to the selected spectra: either at the folder or individual file level. 

2) Query the NSD for specific metadata parameters:

![query_builder](/_files/cmi/query_1.jpg)

Select the metadata category you wish to filter by on the left-hand side. For example, to retrieve all entries for NSW, select the Location category on the left, then add "NSW" to the "State/Territory" field and hit Run Query on the right:

![query_2](/_files/cmi/query_2.jpg)

As in the Data Browser, spectra found from the Query Builder can be viewed and exported in the same way.

For a full guide on the use of the Specchio application, please see the [Specchio website](https://specchio.ch/).

## Lineage

Datasets

\- Geoscience Australia field data campaigns: From the ARD Cal/Val team, DEA, GA  
\- Aquatic Substrate Library: Compiled by Dr Arnold Dekker (SatDek)  
\- University of Wollongong Spectral Datasets: Provided by Dr Laurie Chisolm (UoW)

Data types

\- Spectral data: raw digital numbers (DN), radiance and reflectance.   
\- From spectral range VIS-NIR, SWIR1 & SWIR2, wavelengths from 350nm - 2500nm collected with instruments in the field or lab setting.

Data Collection

\- NSD spectral data has been collected by remote sensing scientists in Australia, both in field and lab environments

Processing

\- Where applicable, post-processing is indicated in the relevant metadata field

% ## Processing steps

## Software

Direct download links: [Specchio client zip file](https://github.com/EricHay/NSD_Guides/raw/main/specchio-client.zip) or [.jar installer package](https://github.com/EricHay/NSD_Guides/raw/main/specchio-installer.jar). For further download options see the Specchio website [Downloads page](https://specchio.ch/downloads/).

Specchio is an open source application. The code base is available at the [Specchio GitHub repository](https://github.com/SPECCHIODB/SPECCHIO).

## References

Byrne, G., Walsh, A., Thankappan, M., Broomhall, M., Hay, E. 2021. DEA Analysis Ready Data Phase 1 Validation Project: Data Summary. Geoscience Australia, Canberra. [https://doi.org/10.26186/145101](https://doi.org/10.26186/145101)

Hueni, A., Chisholm, L.A., Ong, C., Malthus, T.J., Wyatt, M., Trim, S.A., Schaepman, M.E., Thankappan, M. 2021. The SPECCHIO Spectral Information System, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 13, pp. 5789-5799, 2020, doi: 10.1109/JSTARS.2020.3025117.

Aasen, H.; Hueni, A.; Machwitz, M.; Malenovský, Z.; Mallick, K.; Paul-Limoges, E.; Schlerf, M.; Schneider, F.D.; Suárez, L.; Van Wittenberghe, S.; Wieneke, S.; Wolf, S. Ecosystem specific Metadata. 2017, 10.13140/RG.2.2.14986.77761

Held, A., Phinn, S., Soto-Berelov, M., & Jones, S. (Eds.). AusCover Good Practice Guidelines: A technical handbook supporting calibration and validation activities of remotely sensed data products. 2015. Version 1.1. TERN AusCover, ISBN 978-0-646-94137-0

Rasaiah, B.A.; Jones, S.D.; Bellman, C.; Malthus, T.J.; Hueni, A. Assessing Field Spectroscopy Metadata Quality. *Remote Sens.* 2015, *7*, 4499-4526

Milton, E.; Schaepman, M.E.; Anderson, K.; Kneubuehler, M.; Fox, N. Progress in field spectroscopy. *Remote Sensing of Environment* 113 Suppl. 2009, 1. 113. 10.1016/j.rse.2007.08.001

