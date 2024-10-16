# Frequently Asked Questions

Here you will find answers to frequently asked questions about DEA’s products and services.

:::{dropdown} How do I download data from DEA?
:name: download-dea-data

There are several options for downloading data from DEA depending on your use case:

**1) You want to download a small area of data from a specific satellite image**

Use [DEA Maps](/guides/setup/dea_maps/) to directly export a small amount of data from the map using the [Export functionality](/guides/setup/dea_maps/#dea-maps-exporting). This is the easiest method, but it is not suitable for downloading large areas of data or multiple steps (see below).

**2) You want to download all available data for a bounding box and/or time range**

Use DEA's STAC metadata to find the data you are interested in using the [Downloading and streaming data using STAC metadata guide](/notebooks/How_to_guides/Downloading_data_with_STAC/).

**3) You want to download specific files from DEA's Amazon S3 buckets**

Download data directly from our [Amazon S3 buckets](/guides/setup/AWS/data_and_metadata/) using the AWS Command Line Interface (AWS CLI). For this you will need to know the path of the file you want to download on DEA's S3 buckets. For example, to download a single file

```
aws s3 cp s3://dea-public-data/derivative/ga_ls_wo_fq_cyear_3/1-6-0/x11/y21/1992--P1Y/ga_ls_wo_fq_cyear_3_x11y21_1992--P1Y_final_frequency.tif . --no-sign-request
```

To download multiple files, for example each annual DEA Water Observations frequency layer for the tile `x11/y21`

```
aws s3 cp s3://dea-public-data/derivative/ga_ls_wo_fq_cyear_3/1-6-0/x11/y21/ . --recursive --exclude "*" --include "*P1Y_final_frequency.tif" --no-sign-request
```
:::

:::{dropdown} What data limitations does Landsat have?
:name: landsat-data-limitations

Earth observation satellites only view a small portion of the world at any one time. Typically the ones used by Digital Earth Australia (DEA) only observe a small strip, north-south across the landscape, and over several days the whole landscape is finally observed in full. For example the Landsat satellites take 16 days to create a full coverage, and then only if the surface of the earth is not obscured by clouds. Hence there can be difficulties in capturing imagery over persistently cloudy locations such as Tasmania and northern Australia during the monsoonal months, and areas may not be observed at all for extended periods. Where the satellite data is being analysed as a time series, these long periods can cause important changes to be missed entirely, or parts of a cyclic environment to be misinterpreted (such as vegetation phenology and cropping cycles).

An additional limitation of the Landsat series is the availability of data due to the ageing of each satellite. Landsat 5 was operational for over 25 years, but for much of the later years, data were only acquired when sunlight directly illuminated its solar panels.  This limited its operation across Australia, with coverage being seasonally dependent, and contracting north to a minimum in winter. In its last years the winter coverage usually only covered the northern coasts of Australia. Landsat 5 ceased regular operations over Australia in 2011, leaving just Landsat 7 until Landsat 8 was launched in 2013. Landsat 7 began service in 1999 as a replacement for Landsat 5. Initially Landsat 5 was switched off, but when Landsat 7 suffered a serious problem in 2003 due to the failure of its scan-line corrector (termed SLC-Off) Landsat 5 resumed service. The SLC-Off failure of Landsat 7 results in striping across every image from mid 2003 onwards, apparent in subsequent derived products. Landsat 8 has operated well since launch in 2013, with improved sensitivity, noise characteristics and data correction in comparison to the earlier sensors.

The result of the availability of the satellites is that the most consistent data availability occurs when two satellites are in operation (most of the 2003 to present period). The least data availability is in 2011 – 2012 when only Landsat 7 was available with data containing the SLC-Off striping issue. 

Landsat 9 was launched on September 27, 2021, joining Landsats 7 and 8 in orbit, providing optical imagery to the DEA program.

On 6 April 2022, Landsat 7 reached the [end of its nominal science mission](https://www.usgs.gov/landsat-missions/news/landsat-7-nominal-science-mission-ending). It was put into a lower Earth orbit that removed it from a repeating ground track, meaning acquisitions are no longer aligned to the World Reference System. Even though Landsat 7 continues to collect data in the [Landsat 7 Extended Science Mission](https://www.usgs.gov/landsat-missions/landsat-7-extended-science-mission), DEA does not process this data as part of its data collection and ceased data production at the end of Landsat 7's nominal science mission in April 2022.

The overall data availability for the Landsat satellites is shown in Table 1.

| Years                  | Satellite and Sensor                      | Issues                                                                                                             |
|------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 1986                   | Landsat 5 Thematic Mapper (TM)            | Only part of the year available in DEA                                                                             |
| 1987 - 1999            | Landsat 5 TM                              | Normal operation                                                                                                   |
| 1999 - early 2003      | Landsat 5 TM                              | Switched off with availability of Landsat 7                                                                        |
| 1999 - early 2003      | Landsat 7 Enhanced Thematic Mapper (ETM+) | Normal operation                                                                                                   |
| Late 2003 - early 2011 | Landsat 5                                 | Gradually degrading operation and increasing observations failure. </br> Total failure of Landsat 5 in early 2011. |
| Late 2003 - early 2022 | Landsat 7 ETM +                           | Operating with SLC-Off stripes in imagery. End of nominal science mission, April 2022.                             |
| Early 2013 - present   | Landsat 8 Optical Land Imager (OLI)       | Normal operation                                                                                                   |
| Late 2021 - present    | Landsat 9 OLI                             | Normal operation                                                                                                   |
| *Early 2022 - present* | *Landsat 7 ETM+*                          | *Moved into lower Earth orbit. Now in Extended Science Mission. Data NOT used by DEA*                              |

Table 1: Availability of the Landsat satellites for Earth observation and related issues for product generation

:::

:::{include} ../../_components/thermal-bands-availability-faq.md
:::

:::{dropdown} Is there an easy way to learn the basics of Earth Observation and DEA data?
:name: easy-way-learn-dea

If you like podcasts, you can listen to the [13 October 2024 episode of Fuzzy Logic](https://www.2xxfm.org.au/shows/fuzzy-logic/) to hear some of our scientists discuss Earth Observation and the kinds of data that DEA uses. You may want to share this podcast with friends and family who are interested!
:::
