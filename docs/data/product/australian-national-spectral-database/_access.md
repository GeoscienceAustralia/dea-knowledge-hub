% ## Access constraints

## Use constraints

Use of the NSD is subject to NSD Terms of Service. Please read the Terms below before accessing the Service.

:::{dropdown} **NSD Terms of Service**
**Geoscience Australia National Spectral Database Terms of Service** 

Last reviewed: 21/07/2021 

Terms of Service (“Terms”) 

Please read these Terms carefully before accessing the National Spectral Database. These Terms cover access to the National Spectral Database (“the Service”, “NSD”) operated by Geoscience Australia (“GA”). 

Your access to and use of the Service is conditional upon your acceptance of and compliance with these Terms. These Terms apply to all visitors, users and others who access the Service. 

By accessing or using the Service you agree to be bound by these Terms. If you disagree with any part of the Terms, you may not access the Service. 

Access to and use of the GA National Spectral Database is subject to the following Terms: 
* The user (you) will not disclose account information, including user name and password or server credentials to any other party. 
* You will not alter your application-set password. If you lose access to your account, please contact the NSD manager. 
* Software is to be used fairly without putting excess strain on services provided, such as spamming server requests or logging in multiple times with the same account. If errors or issues are encountered please advise the database manager or appropriate GA authority. 
* It is your responsibility to ensure that you adhere to the National Spectral Database metadata standard. Data must be correctly formatted and meet the minimum metadata requirements before it can be included into the National Spectral Database. Please advise GA database manager of intent to upload data. 
* New account holders may only view and download existing data. If you would like to upload data or edit metadata of an existing campaign, please contact the GA database manager. For read/write access, you are required to meet the NSD Metadata Standard and operate according to the NSD General Guide. 
* Geoscience Australia does not hold any responsibility for the quality of data imported by 3rd parties or hosted by the Service that were not imported by GA. GA allows data to be uploaded such that it meets minimum metadata standards, but cannot guarantee data was collected in a particular manner or by any sampling protocol. For use of data from campaigns uploaded by bodies other than Geoscience Australia, please contact the campaign owner for information on data quality such as sampling design and field methods before downloading and or utilising data in any way. 

**Termination** 

We may terminate or suspend access to our Service immediately, without prior notice or liability, for any reason whatsoever, including without limitation if you breach the Terms. 

**Data Ownership** 

Data are hosted on behalf of original data providers. GA does not own original data provided by external parties, only data provided under the banner of GA such as ARD field validation data. For information on datasets provided by external parties please contact the data owner using the contact email address provided in metadata. 

**CC BY 4.0 License** 

Geoscience Australia data is licensed and shared under the Creative Commons Attribution 4.0 International license. 

http://creativecommons.org/licenses/by/4.0/legalcode https://creativecommons.org/licenses/by/4.0/

**DOI Minting**

A digital object identifier (DOI) can be created for new datasets upon request for previously unpublished data. Data hosted on the NSD is shared under the CCBY 4.0 License and may be downloaded by users without notice. Users are notified of the data usage policy, but GA cannot guarantee that your work or data will be properly cited. Please contact the database manager for further information and guidance to create a new DOI. 

**GA contact details** 

For read/write access including uploading data and metadata, or for any other queries, please contact the database manager: 

NSDB_manager@ga.gov.au 

Changes may be made at any time, without prior notice, to these Terms. Should new Terms come into place they will be made available at all user landing pages including the National Spectral Database website.
:::

:::{dropdown} How to access the data
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

See the [Details tab](./?tab=details) for further information on navigation through the Specchio client and NSD.
:::

:::{dropdown} How to navigate the client

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
:::

:::{dropdown} Where can I find more information?

* Requirements: Java Runtime Environment (JRE) 8.0 or higher. See [Specchio Release Notes](https://github.com/SPECCHIODB/Guides/raw/master/SPECCHIO_ReleaseNotes.pdf) on supported JRE's. 
* Documentation for the Specchio client: [Specchio website](https://specchio.ch/).
* Technical information on use of the Specchio application, such as connecting to the NSD and downloading data: [Technical usage guide](https://app-public.specchio.sandbox.dea.ga.gov.au/).
:::


