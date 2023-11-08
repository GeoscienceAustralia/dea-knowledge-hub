% ## Access constraints

## Use constraints

Use of the NSD is subject to [NSD Terms of Service](/_files/cmi/NSD_Terms_of_Service.pdf). Please read the Terms before accessing the Service.

## Frequently asked questions

:::{dropdown} How do I access the data?
### How to access the National Spectral Database 

1) Read the **Terms of Service** above. These terms outline your responsibilites and conditions of use.

2) Download the Specchio application. Direct download links are here: [Specchio client zip file](https://github.com/EricHay/NSD_Guides/raw/main/specchio-client.zip) or [.jar installer package](https://github.com/EricHay/NSD_Guides/raw/main/specchio-installer.jar). For further download options see the Specchio website [Downloads page](https://specchio.ch/downloads/).

3) Run the application. Launch the Specchio client from your install directory or command line, it is called "specchio-client.jar".

4) Get started with the NSD: Select "Database" from the top left-hand corner of the client, then "Create a user account". See below: 

![connection_tab](/_files/cmi/connection.jpg)

To access the service enter the following information:

**Web Application Server:** app-public.specchio.sandbox.dea.ga.gov.au

**Port:** 443

**Application Path:** /specchio\_service

**Data Source Name:** jdbc/specchio

**Tick the box** "Use default JVM trust store".

Enter information about yourself, including contact email and intended use of the database in the Description field. If your institute is not listed, please add your institute. If you are not from an institute, such as a research body or private company, please create a new institute as your name, i.e. "First Name Last Name".

See the Details tab above for further information on navigation through the Specchio client and NSD.

### Known issues

Click here to view [Known Issues](/_files/cmi/NSD_Known_Issues_List.pdf). If you are experiencing connectivity issues, please refer to Note 1 relating to the Java Runtime Environment. If you encounter a new issue please contact [NSDB\_Manager@ga.gov.au](mailto:NSDB_Manager@ga.gov.au) with details of the issue.

### Contribute your data to the NSD

If you have spectral data collected in Australia, and have relevant metadata and collection information you can contribute this data to be hosted on the NSD. Please familiarise yourself with the [Metadata Standard](/_files/cmi/NSD_Metadata_Standard.pdf), and follow the steps below to contribute:

1) Ensure you adhere to the Metadata Standard and that your dataset meets minimum requirements. Meeting the metadata standard can be as simple as providing GPS information for spatial data, or species images, description or the scientific name for end-member spectra. Spectra submitted without metadata are unsuitable and won't be accepted.

2) Contact the NSD manager: [NSDB\_Manager@ga.gov.au](mailto:NSDB_Manager@ga.gov.au). In your email include the size of the dataset you wish to ingest and confirm that you meet the [Metadata Standard](/_files/cmi/NSD_Metadata_Standard.pdf), and have read the [Technical usage guide](/_files/cmi/NSD_General_Guide.pdf) & [Write access guide](/_files/cmi/NSD_Write_Access_Guide.pdf).

The guides will help you to understand the process of uploading your data and ingest data most efficiently. If you have further queries please enquire via email.

The public server will allow you to view & download data, not upload it. The NSD manager will provide instruction on how to access the upload server.

#### Use of the NSD service is subject to [NSD Terms of Service](/_files/cmi/NSD_Terms_of_Service.pdf). Data contributed must meet the NSD [Metadata Standard](/_files/cmi/NSD_Metadata_Standard.pdf).

### Digital Object Identifier (DOI) Minting

DOI minting is offered for new datasets that meet the metadata standard, and are new or existing datasets not previously published elsewhere. Your dataset will get a unique DOI that the database manager will append to your dataset metadata within the NSD. The DOI will be stored separately as a Geoscience Australia metadata record. The DOI record can also provide links to further publications from your dataset, and can easily be updated if needed, or further publications stem from your work. The aim of the DOI is to credit those involved in collecting the dataset, and to provide links to further science stemming from the work.

For a DOI to be minted, sufficient metadata is required for the dataset including names of team members involved, location and timestamps of the study (GPS and UTC time associated with measurements), and links to any associated publications such as journal articles. These should be included as metadata for your dataset when ingesting new data. 

Please contat the NSD manager if you would like to contribute or update data: [NSDB\_Manager@ga.gov.au](mailto:NSDB_Manager@ga.gov.au)
:::

