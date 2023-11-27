% ## Accuracy

% ## Quality assurance

## Known issues
Last updated: 11/07/2022

Currently there are no known issues. After updating the Ocean Optics Flame and Spectral Evolution SR-3500 parsers, data import and export is functioning as intended. 


Note 1: Your Java Runtime Environment (JRE) may cause connection issues if it is not compatible. The best JRE to use with Specchio is:
* java version "1.8.0_291"
* Java(TM) SE Runtime Environment (build 1.8.0_291-b10)

* Newer JRE’s are generally ok. If you are experiencing connection issues, please check your installed JRE, and download the one specified above and run the Specchio client in command line specifying the JRE:

`<path_to_jre>/bin/java.exe -jar Executable.jar`

Or more specifically:

`<path_to_jre>/bin/java.exe -jar -Djdk.security.allowNonCaAnchor=true specchio-client.jar`

With the path pointing to the 1.8 JRE.

Note 2: Data within the NSD are stored hierarchically so data should be exported by selecting the folder above the desired data. If you do not download data from its root folder, you will lose folder sub-structure labels. See below for an example:

:::{figure} /_files/cmi/NSD_known_issues.png
:alt: NSD browser screen grab
:::

If you wish to download the Flame_10m_lines data (highlighted) you can select the folder containing that data to download “Flame_10m_lines”. You may be able to download smaller campaigns in their entirety (dependent on the size of metadata, if your download is stalling try to go to lower folders in the hierarchy). For example you can download all of the flame data for the 04MAY20 dataset by selecting the “Flame_data” folder, though you will lose the sub-folder information i.e. 10m lines vs 2.1m lines.

Please let the NSD manager know if you experience any issues or have any questions. You can reach the NSD manager via email at earth.observations@ga.gov.au.

