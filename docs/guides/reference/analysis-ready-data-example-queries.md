# Analysis Ready Data: Open Data Cube

The [Open Data Cube (ODC)](/guides/about/glossary/#odc) is an open-source solution for accessing, managing, and analysing large quantities of 
Geographic Information System (GIS) data &mdash; namely Earth observation data. It is a global initiative to increase the 
value and use of satellite data by providing users with access to free and open data management technologies and 
analysis platforms.

At its core, ODC is a set of Python libraries and a [PostgreSQL](/guides/about/glossary/#postgresql) database that allows you to work with geospatial raster 
data.

This article will show you how to query the DEA Open Data Cube.

:::{contents} In this guide
:depth: 1
:local:
:backlinks: none
:::

## Example 1 &ndash; Analysis Ready Data product

The following Python code is an example Open Data Cube query to return the following properties:

-   green, red and near-infrared measurements from the **GA Landsat 5 TM NBAR Collection 3** and **GA Landsat 5 TM NBART Collection 3** products
-   Fmask layer from the **GA Landsat 5 TM OA Collection 3** product
-   Region of Interest (ROI): *Longitude 146.54 → 147.94; latitude -19.42 → -21.03*
-   Acquisition time of interest: *1990-07-20*

All products are nestled under the parent product **GA Landsat 5 TM Analysis Ready Data Collection 3** (Open Data Cube product ID: *ga_ls5t_ard_3*).

```python
data = dc.load(
    product='ga_ls5t_ard_3',
    measurements=['nbart_swir_2', 'nbart_blue', 'nbart_green', 'nbart_red', 'nbart_nir', 'nbar_green', 'nbar_red', 'nbar_nir', 'oa_fmask', 'nbart-contiguity'],
    lon=(146.54, 147.94),
    lat=(-19.42, -21.03),
    time=('1990-07-20', '1990-07-21'),
    output_crs='EPSG:3577',
    resolution=(-30, 30)
)
```

The Data Cube query produces the following images:

![AB 3](/_files/cmi/figure_AB_new_3.JPG)

**Image A** is the false colour composite ['nbart_nir', 'nbart_red', 'nbart_green'] displayed as [Red, Green, Blue] from the **GA Landsat 5 TM NBART Collection 3 **product.

**Image B** is the false colour composite ['nbart_nir', 'nbart_red', 'nbart_green'] displayed as [Red, Green, Blue] from the **GA Landsat 5 TM NBAR Collection 3 **product.

![CD 2](/_files/cmi/figure_CD_new_2.JPG)

**Image C** is another **GA Landsat 5 TM NBART Collection 3** false colour composite, but uses a different combination of spectral bands ['nbart_swir_2', 'nbart_nir', 'nbart_blue'] displayed as [Red, Green, Blue].

**Image D** is the relative slope dataset.

![E 2](/_files/cmi/figure_E_new_2.JPG)

**Image E** is the Fmask classification result from the **GA Landsat 5 TM NBART Collection 3** product. The colours for the Fmask classification are displayed as:

-   Black = clear
-   Magenta = cloud
-   Yellow = cloud shadow
-   Cyan = snow
-   Dark blue = water

![FG 1](/_files/cmi/figure_FG_new_0.JPG)

**Images F and G** represent the **GA Landsat 5TM NBART Collection 3** false colour composite, with pre- and post-application of the contiguity mask, respectively.

Note that the different spectral bands have different data extents at the edges of the scene (denoted by yellow and red strips). When using the contiguity mask, the data edges have been cut back to where data coexists for all spectral bands.

## Example 2 &ndash; NBAR product

The following Python code is an example Open Data Cube query to return the following properties:

-   green, red and near-infrared measurements from the **GA Landsat 5 TM NBAR Collection 3** product
-   Fmask layer from the **GA Landsat 5 TM OA Collection 3** product
-   Region of Interest (ROI): *Longitude 146.54 → 147.94; latitude -19.42 → -21.03*
-   Acquisition time of interest: *1990-07-20*

Both products are nestled under the parent product **GA Landsat 5 TM Analysis Ready Data Collection 3** (Open Data Cube product ID: ga_ls5t_ard_3).

```python
data = dc.load(
    product='ga_ls5t_ard_3',
    measurements=['nbar_green', 'nbar_red', 'nbar_nir', 'oa_fmask'],
    lon=(146.54, 147.94),
    lat=(-19.42, -21.03),
    time=('1990-07-20', '1990-07-21'),
    output_crs='EPSG:3577',
    resolution=(-30, 30)
)
```

The Data Cube query produces the following image, which is the false colour composite ['nbar_nir', 'nbar_red', 'nbar_green'] displayed as [Red, Green, Blue].

![nbar new](/_files/cmi/nbar_new.JPG)

## Example 3 &ndash; NBART product

The following Python code is an example Open Data Cube query to return the following properties:

-   green, red and near-infrared measurements from the **GA Landsat 5 TM NBART Collection 3** product
-   Fmask layer from the **GA Landsat 5 TM OA Collection 3** product
-   Region of Interest (ROI): *Longitude 146.54 → 147.94; latitude -19.42 → -21.03*
-   Acquisition time of interest: *1990-07-20*

Both products are nestled under the parent product **GA Landsat 5 TM Analysis Ready Data Collection 3** (Open Data Cube product ID: *ga_ls5t_ard_3*).

```python
data = dc.load(
    product='ga_ls5t_ard_3',
    measurements=['nbart_green', 'nbart_red', 'nbart_nir', 'oa_fmask'],
    lon=(146.54, 147.94),
    lat=(-19.42, -21.03),
    time=('1990-07-20', '1990-07-21'),
    output_crs='EPSG:3577',
    resolution=(-30, 30)
)
```

The Data Cube query produces the following images:

![nbart new](/_files/cmi/nbart_new.JPG)

**Image A** is the false colour composite ['nbart_nir', 'nbart_red', 'nbart_green'] displayed as [Red, Green, Blue].

**Image B** is the Fmask classification result. The colours for the Fmask classification are displayed as:

-   Black = clear
-   Magenta = cloud
-   Yellow = cloud shadow
-   Cyan = snow
-   Dark blue = water

## Product file naming convention

DEA product files follow a specific naming convention on Open Data Cube:

**{product}-{minor version}-{patch version}_{spatial location}_{acquisition date}_{label}_{description id}.{extension}**

The fields are defined as follows:

<table class="table">
    <tbody>
        <tr>
            <td><strong>{product}</strong></td>
            <td>Open Data Cube product ID (e.g.&nbsp;<em>ga_ls5t_nbar_3</em>)</td>
        </tr>
        <tr>
            <td><strong>{minor version}</strong></td>
            <td>A single integer</td>
        </tr>
        <tr>
            <td><strong>{patch version}</strong></td>
            <td>A single integer</td>
        </tr>
        <tr>
            <td><strong>{spatial location}</strong></td>
            <td>The combination of 'path' and 'row' locations. Both 'path' and 'low' are zero-padded strings of length 3, which make a 6-integer number when combined (e.g.&nbsp;<em>092</em>&nbsp;and&nbsp;<em>084</em>&nbsp;make&nbsp;<em>092084</em>)</td>
        </tr>
        <tr>
            <td><strong>{acquisition date}</strong></td>
            <td>Has the form&nbsp;<em>yyyy-mm-dd</em></td>
        </tr>
        <tr>
            <td><strong>{label}</strong></td>
            <td>
                <p>Can be one of the following:</p>
                <p><em>nrt</em></p>
                <ul>
                    <li>If the acquisition file is processed within 48 hours of the acquisition date</li>
                </ul>
                <p><em>interim</em></p>
                <ul>
                    <li>If the acquisition date is pre-2002-07-01&nbsp;<strong>AND</strong>&nbsp;fallback water vapour data is used (i.e. water vapour is not sourced from the same day as the acquisition date)<br /><strong>OR</strong></li>
                    <li>If the acquisition date is post-2002-07-01&nbsp;<strong>AND</strong>&nbsp;fallback water vapour data is used<br /><strong>OR</strong></li>
                    <li>If the acquisition date is post-2002-07-01, fallback water vapour data is not used (i.e. water vapour is sourced from the same day as the acquisition date)&nbsp;<strong>AND</strong>&nbsp;fallback BRDF data is used</li>
                </ul>
                <p><em>final</em></p>
                <ul>
                    <li>If the acquisition date is pre-2002-07-01&nbsp;<strong>AND</strong>&nbsp;fallback water vapour data is not used<br /><strong>OR</strong></li>
                    <li>If the acquisition date is post-2002-07-01, fallback water vapour is not used&nbsp;<strong>AND</strong>&nbsp;fallback BRDF data is not used</li>
                </ul>
                <p>(See&nbsp;<strong>flow process</strong>&nbsp;diagram below)</p>
            </td>
        </tr>
        <tr>
            <td><strong>{description ID}</strong></td>
            <td>e.g.&nbsp;<em>band01, band02, band03, thumbnail, fmask, satellite-view</em></td>
        </tr>
        <tr>
            <td><strong>{extension}</strong></td>
            <td>e.g.&nbsp;<em>tif, jpg</em></td>
        </tr>
    </tbody>
</table>

### Flow process for determining the label (nrt, interim or final)

![logic max](/_files/cmi/nrt-interim-final-logic.png)

### Example files

Below is a list of representative samples which demonstrate the application of the naming conventions. The folders follow the *product ID, path, row, year, month, day* format.

#### Example 1 - GA Landsat 5 TM Analysis Ready Data Collection 3

```
└── ga_ls5t_ard_3              <== Product ID
     └── 092                   <== Path
         └── 084               <== Row
             └── 2009          <== Year
                 └── 12        <== Month
                     └── 17    <== Day
                         ├── ga_ls5t_ard_3-0-0_092084_2009-12-17_final.odc-metadata.yaml
                         ├── ga_ls5t_ard_3-0-0_092084_2009-12-17_final.proc-info.yaml
                         ├── ga_ls5t_ard_3-0-0_092084_2009-12-17_final.sha1
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band01.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band02.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band03.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band04.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band05.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_band07.tif
                         ├── ga_ls5t_nbar_3-0-0_092084_2009-12-17_final_thumbnail.jpg
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band01.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band02.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band03.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band04.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band05.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_band07.tif
                         ├── ga_ls5t_nbart_3-0-0_092084_2009-12-17_final_thumbnail.jpg
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_azimuthal-exiting.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_azimuthal-incident.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_combined-terrain-shadow.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_exiting-angle.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_fmask.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_incident-angle.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_nbar-contiguity.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_nbart-contiguity.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_relative-azimuth.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_relative-slope.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_satellite-azimuth.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_satellite-view.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_solar-azimuth.tif
                         ├── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_solar-zenith.tif
                         └── ga_ls5t_oa_3-0-0_092084_2009-12-17_final_time-delta.tif
```

#### Example 2 - GA Landsat 7 ETM+ Analysis Ready Data Collection 3

```
└── ga_ls7e_ard_3              <== Product ID
     └── 092                   <== Path
         └── 084               <== Row
             └── 2016          <== Year
                 └── 06        <== Month
                     └── 04    <== Day
                         ├── ga_ls7e_ard_3-0-0_092084_2016-06-04_final.odc-metadata.yaml
                         ├── ga_ls7e_ard_3-0-0_092084_2016-06-04_final.proc-info.yaml
                         ├── ga_ls7e_ard_3-0-0_092084_2016-06-04_final.sha1
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band01.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band02.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band03.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band04.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band05.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band07.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_band08.tif
                         ├── ga_ls7e_nbar_3-0-0_092084_2016-06-04_final_thumbnail.jpg
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band01.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band02.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band03.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band04.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band05.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band07.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_band08.tif
                         ├── ga_ls7e_nbart_3-0-0_092084_2016-06-04_final_thumbnail.jpg
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_azimuthal-exiting.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_azimuthal-incident.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_combined-terrain-shadow.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_exiting-angle.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_fmask.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_incident-angle.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_nbar-contiguity.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_nbart-contiguity.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_relative-azimuth.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_relative-slope.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_satellite-azimuth.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_satellite-view.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_solar-azimuth.tif
                         ├── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_solar-zenith.tif
                         └── ga_ls7e_oa_3-0-0_092084_2016-06-04_final_time-delta.tif
```

#### Example 3 - GA Landsat 8 OLI/TIRS Analysis Ready Data Collection 3

```
└── ga_ls8c_ard_3              <== Product ID
     └── 092                   <== Path
         └── 084               <== Row
             └── 2016          <== Year
                 └── 06        <== Month
                     └── 28    <== Day
                         ├── ga_ls8c_ard_3-0-0_092084_2016-06-28_final.odc-metadata.yaml
                         ├── ga_ls8c_ard_3-0-0_092084_2016-06-28_final.proc-info.yaml
                         ├── ga_ls8c_ard_3-0-0_092084_2016-06-28_final.sha1
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band01.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band02.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band03.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band04.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band05.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band06.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band07.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_band08.tif
                         ├── ga_ls8c_nbar_3-0-0_092084_2016-06-28_final_thumbnail.jpg
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band01.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band02.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band03.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band04.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band05.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band06.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band07.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_band08.tif
                         ├── ga_ls8c_nbart_3-0-0_092084_2016-06-28_final_thumbnail.jpg
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_azimuthal-exiting.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_azimuthal-incident.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_combined-terrain-shadow.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_exiting-angle.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_fmask.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_incident-angle.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_nbar-contiguity.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_nbart-contiguity.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_relative-azimuth.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_relative-slope.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_satellite-azimuth.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_satellite-view.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_solar-azimuth.tif
                         ├── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_solar-zenith.tif
                         └── ga_ls8c_oa_3-0-0_092084_2016-06-28_final_time-delta.tif
```
