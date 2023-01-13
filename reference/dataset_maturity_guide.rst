DEA dataset maturity explained 
==============================

In December 2022, DEA implemented **dataset maturity** levels to provide a more streamlined user 
experience and access mechanism for DEA ARD (Analysis Ready Data) datasets. Dataset metadata 
attributes are currently implemented across all Sentinel 2 and Landsat Collection 3 ARD products. 

DEA produces data to three maturity levels: 
- **Near Real Time (NRT)** is a rapid ARD product produced < 48hours after image capture. 
  NRT data is corrected using existing long term climatology data that is of slightly 
  lower quality, allowing NRT data to be published quickly. 

Over the next few weeks, higher quality ancillary datasets become available describing the specific 
atmospheric conditions at the time and location the satellite image was captured. Using these 
ancillaries, ‘Final’ maturity ARD is produced.  
- **Final** ARD is DEA’s best quality ARD, produced using high quality ancillary datasets derived 
  from observed data. These ancillary datasets are slower to produce but are observational 
  datasets of the conditions at the time of image capture and so provide our most accurate dataset 
  corrections.  
- DEA uses the following dynamic ancillary datasets to produce its Final ARD 
    - Bidirectional reflectance distribution function (BRDF) data from the United States Geological Survey 
    - Water Vapour from USA National Oceanographic and Atmospheric Administration 
As the higher quality ancillary datasets become available, a “Final” version of the data is produced, 
which replaces the NRT or interim product (see below).  

If the ancillaries don’t become available within 18 days of the satellite capture, ‘interim’ maturity 
data is produced as a stand-in until full ancillaries are available to produce the ‘final’ version.  
- **Interim** ARD – If there are extended delays (>18 days) in delivery of inputs to the final ARD model, 
  we fall back to interim production until the issue is resolved. Interim production means that 
  one or more ancillary dataset wasn’t available at the time of production, and the dataset has 
  instead been corrected using a combination of NRT climatological ancillaries, and Final observed 
  ancillaries. If there are no delays in the ancillary datasets, then interim maturity is skipped and 
  datasets move directly from NRT to Final.  

All three maturity levels can be present inside a single product, with the maturity information stored 
in the product metadata and as part of the filename, enabling users to choose an appropriate dataset 
maturity level to suit their requirements. Datasets with lower maturity level will be replaced by more 
mature dataset versions (interim and final) as they are generated. 

How is this different from what DEA used to do? 
-----------------------------------------------

Previously, DEA produced two separate products: 

- Near Real Time, which was kept as a rolling 90 day archive; 
- ARD, published 9 to 16 days after satellite acquisition. 

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
