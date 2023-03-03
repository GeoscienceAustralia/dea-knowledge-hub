DEA dataset maturity explained 
==============================

In December 2022, DEA implemented **dataset maturity** levels to provide a more streamlined user 
experience and access mechanism for DEA ARD (Analysis Ready Data) datasets. Dataset metadata 
attributes are currently implemented across all Sentinel 2 and Landsat Collection 3 ARD products. 

DEA produces data to three maturity levels: 

* **Near Real Time (NRT)**
* **Interim**
* **Final**


Near Real Time (NRT)
--------------------
**Near Real Time (NRT)**
is a rapid ARD product produced within 48 hours after image capture. NRT 
data is corrected using existing long term climatology data that is of slightly lower 
quality, allowing NRT data to be published quickly. 

Over the next few weeks, higher quality ancillary datasets become available describing the specific 
atmospheric conditions at the time and location the satellite image was captured. Using these 
ancillaries, ‘**Final**’ maturity ARD is produced. This replaces the '**NRT**' or '**interim**' product (see below).  

Final
------------
**Final**
ARD is DEA’s best quality ARD, produced using high quality ancillary datasets derived 
from observed data. These ancillary datasets are slower to produce but are observational 
datasets of the conditions at the time of image capture and so provide our most accurate dataset 
corrections. DEA uses the following dynamic ancillary datasets to produce its **Final** ARD:

  * Bidirectional reflectance distribution function (BRDF) data from the United States Geological Survey 
  * Water Vapour from USA National Oceanographic and Atmospheric Administration

Interim
------------
If high quality ancillaries required for the **final** ARD model don’t become available **within 23 days** of image capture,
‘**interim**’ maturity data is produced as a *stand-in* until the full ancillaries are available to produce the ‘**final**’ version.
This is our fall-back until the issue is resolved.

**Interim**
Interim production means that one or more ancillary datasets were not available at the time of production, and the dataset has 
instead been corrected using a combination of NRT climatological ancillaries, and Final observed 
ancillaries. If there are no delays in the ancillary datasets, then **interim** maturity is skipped and 
datasets move directly from **NRT** to **Final**.

All three maturity levels can be present inside a single product, with the maturity information stored 
in the product metadata and as part of the filename, enabling users to choose an appropriate dataset 
maturity level to suit their requirements. Datasets with lower maturity level will be replaced by more 
mature dataset versions (interim and final) as they are generated. 

Dataset maturity flowchart
--------------------------
|dataset_maturity_flowchart|

.. |dataset_maturity_flowchart| image:: ./images/dataset_maturity_flowchart.drawio.svg

**Tip:** to view larger, right-click then select **open image in new tab**

..
  Diagram editing notes for internal use:
  The SVG above contains an embedded copy of the source used to generate it.
  Download it, then drop it into https://app.diagrams.net/ to edit.
  When finished, *save* it, OR use *export as SGV* with the **Include a copy of my diagram** option checked.
  Then commit it back to the repo.

How is this different from what DEA used to do? 
-----------------------------------------------

Previously, DEA produced two separate products: 

* Near Real Time, which was kept as a rolling 90 day archive; 
* ARD, published 9 to 16 days after satellite acquisition. 

The user was then able to select which product they wanted to use according to their purpose. 
It was more difficult to combine products as both NRT and the final ARD product contained data 
for the same time step.  

What about provisional? 
-----------------------

The term **provisional** is used by DEA to denote products that are in the process of being 
developed but haven’t been released yet. Products tagged as provisional could be beta versions 
of new products, or could represent other stages of product development.  

Once a product is released, it is renamed to remove the provisional tag.  

How do I load only Near Real Time/Interim/Final data using the datacube? 
------------------------------------------------------------------------

DEA data can be filtered to specific dataset maturity levels using `dataset_maturity` 
metadata field. Valid options are “final”, “nrt” or “interim”; for example, 
to load only “final” maturity Landsat 8 data::

  import datacube  
  dc = datacube.Datacube()  

  dc.load(product="ga_ls8c_ard_3", 
          measurements=['nbart_red'], 
          x=(150, 150.1), 
          y=(-30, -30.1), 
          time=('2022-01', '2022-02'), 
          dataset_maturity="final") 
