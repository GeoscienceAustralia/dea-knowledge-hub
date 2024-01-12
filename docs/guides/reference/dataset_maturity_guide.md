# DEA Dataset Maturity

In December 2022, DEA implemented **dataset maturity** levels to provide a more streamlined user 
experience and access mechanism for DEA Analysis Ready Data ([ARD](/guides/about/glossary/#ard)) datasets. All ARD data for a single sensor is now 
provided in a single product, streamlining the user experience and minimising the data handling required by users. 

As higher quality corrections become available, they replace the rapid near real-time data within the same product. 
This upgrade provides users a simplified experience whereby they now only need to connect to one data feed which 
provides the best possible, most up-to-date information at any point in time.

Dataset maturity metadata attributes are currently implemented across all Sentinel 2 and Landsat Collection 3 ARD products. 

## How does 'dataset maturity' work?

DEA produces ARD data to three maturity levels: 
* **Near Real-Time (NRT)**
* **Interim**
* **Final**

{#nrt}
### Near Real-Time (NRT)

**Near Real-Time (NRT)** is a rapid ARD product produced within 48 hours of image capture. NRT 
data is corrected using existing long term climatology data, rather than observed conditions on the day of the 
satellite capture (because these observational datasets, called [ancillaries](/guides/about/glossary/#ancillary), take a few weeks to be received by DEA). Due to the use of average
condition data, rather than observational data to perform the corrections to produce ARD, NRT data can be published 
quickly, however is considered to be of slightly lower quality than '**final**' ARD data.

Over the next few weeks, higher quality ancillary datasets become available describing the specific 
atmospheric conditions at the time and location the satellite image was captured. Using these 
ancillaries, ‘**final**’ maturity ARD is produced. This replaces the '**NRT**' or '**interim**' product (see below).  

{#final}
### Final

**Final** ARD is DEA’s best quality ARD, produced using high quality ancillary datasets derived 
from observed data. These ancillary datasets are slower to produce but are observational 
datasets of the conditions at the time of image capture and so provide our most accurate dataset 
corrections. 

DEA uses the following dynamic ancillary datasets to produce its **final** ARD:
* Bidirectional reflectance distribution function ([BRDF](/guides/about/glossary/#brdf)) data from the United States Geological Survey 
* Water Vapour from USA National Oceanographic and Atmospheric Administration

{#interim}
### Interim

If high quality ancillaries required for the **final** ARD model don’t become available **within 23 days** of image capture,
‘**interim**’ maturity data is produced as a *stand-in* until the full ancillaries are available to produce the ‘**final**’ version.
This is our fall-back until the issue is resolved.

**Interim** production means that one or more ancillary datasets were not available at the time of production, and the dataset has 
instead been corrected using a combination of **NRT** climatological ancillaries, and **final** observed 
ancillaries. If there are no delays in the ancillary datasets, then **interim** maturity is skipped and 
datasets move directly from **NRT** to **final**.

## Dataset maturity flowchart

All three maturity levels can be present inside a single product, with the maturity information stored 
in the product metadata and as part of the filename, enabling users to choose an appropriate dataset 
maturity level to suit their requirements. Datasets with lower maturity level will be replaced by more 
mature dataset versions (interim and final) as they are generated. 

![dataset_maturity_flowchart](/_files/reference/dataset_maturity_flowchart.drawio.svg)

**Tip:** to view larger, right-click then select **open image in new tab**

% Diagram editing notes for internal use:
% The SVG above contains an embedded copy of the source used to generate it.
% Download it, then drop it into https://app.diagrams.net/ to edit. 
% When finished, *save* it, OR use *export as SVG* with the **Include a copy of my diagram** option checked.
% Then commit it back to the repo.

## How is this different from what DEA used to do? 

Previously, DEA produced two separate products: 

* Near Real-Time, which was kept as a rolling 90 day archive; 
* ARD, published 9 to 16 days after satellite acquisition. 

The user was then able to select which product they wanted to use according to their purpose. 
It was more difficult to combine products as both NRT and the final ARD product contained data 
for the same time step.  

## How do I load only Near Real-Time/Interim/Final data using the datacube? 

DEA data can be filtered to specific dataset maturity levels using `dataset_maturity` 
metadata field. Valid options are 'final', 'nrt' or 'interim'; for example, 
to load only 'final' maturity Landsat 8 data

```
import datacube
dc = datacube.Datacube()

dc.load(product="ga_ls8c_ard_3",
        measurements=['nbart_red'],
        x=(150, 150.1),
        y=(-30, -30.1),
        time=('2022-01', '2022-02'),
        dataset_maturity="final")
```

{#provisional}
## What about provisional?

The term **provisional** is used by DEA to denote products or services that have not yet passed quality control, and/or
have not yet been finalised for release. Products or services tagged as provisional could be e.g. beta versions 
of new products, could represent other stages of product development, or could not yet have passed 
DEA's quality control standards for a product or service. 

**Provisional products are available for use, but should be used with appropriate caution.** See the individual product 
or service metadata pages for information on product limitations and use. 

Once a product is formally released, it is renamed to remove the provisional tag.  