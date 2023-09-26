.. _glossary:

Glossary
========

.. glossary::

   Acquisition
      An image captured by a satellite sensor.

   Advanced Land Observing Satellite (ALOS)
      A Japanese satellite launched in 2006. After five years of service, the satellite
      lost power and ceased communication with Earth, but remains in orbit.

   Advanced Spaceborne Thermal and Reflection radiometer (ASTER)
      An imaging instrument onboard Terra, the flagship satellite of NASA's Earth Observing
      System (EOS) launched in December 1999. ASTER data is used to create detailed maps of
      land surface temperature, reflectance, and elevation.

      For more information, see `NASA: ASTER<https://asterweb.jpl.nasa.gov/>`_.

   Advanced Very-High Resolution Radiometer (AVHRR)
      A radiation-detection sensor that can be used for remotely determining cloud cover
      and the surface temperature. AVHRR instruments are carried by the National Oceanic and
      Atmospheric Administration (NOAA) family of polar orbiting platforms and European MetOp
      satellites.

      For more information, see `ESA: AVHRR<https://earth.esa.int/eogateway/missions/noaa>`_.

   Aerosol optical depth
      Aerosol optical depth is a measure of the extinction of the solar beam by dust and haze.

   Algorithm
      In the context of remote sensing, algorithms generally specify how to determine higher-level
      data products from lower-level source data. For example, algorithms prescribe how atmospheric
      temperature and moisture profiles are determined from a set of radiation observations originally
      sensed by satellite sounding instruments.

   Amazon Web Services (AWS)
      One of the two environments used for hosting Digital Earth Australia.
      Amazon Web Services is a commercial cloud computing provider. Used
      by Digital Earth Australia for our JupyterHub Sandbox and Web Mapping
      Services.

   Analysis Ready Data (ARD)
      Satellite data that has been processed to a minimum set of requirements and organised into a form
      that allows immediate analysis and interoperability through time and with other datasets.

   Application Programming Interface (API)
      A software intermediary that allows two applications to talk to each other. The :term:`Open Data Cube`
      API gives programmers full access to the capabilities of the Cube, allowing query and advanced data retrieval.

   Atmospheric correction
      The process of removing the effects of the atmosphere on the reflectance values of images taken by
      satellite or airborne sensors.

   Australian Geoscience Data Cube (AGDC)
      A collaborative prototype project between Geoscience Australia, CSIRO and :term:`NCI`, which aimed to provide
      better public access to NASA’s extensive Landsat archive. The AGDC has since been superseded by
      :term:`Digital Earth Australia`.

   Australian Research Environment (ARE)
      The `Australian Research Environment <https://are.nci.org.au/>`_ is a tool for
      using the data and software available on the :term:`NCI`. It is a replacement 
      the old :term:`VDI` system.

   Azimuth
      The angle of an object’s position from true north.

   Azimuthal exiting (degrees)
      The angle between true north and the exiting direction in the slope geometry.

   Azimuthal incident (degrees)
      The angle between true north and the incident direction in the slope geometry.

   
   BRDF
      "Bidirectional reflectance distribution function" is a theoretical concept 
      that describes the relationship between light and an opaque surface, 
      using a target's irradiance geometry and the remote sensing system’s 
      relative angle to the target.
   
   C2
   Collection 2
      Digital Earth Australia's second collection of Landsat data. Now 
      superceded by :term:`Collection 3` (C3).
      
   C3
   Collection 3
      The third collection of Digital Earth Australia's Landsat or Sentinel data, 
      published in and the most up-to-date collection available.
   
   CEOS-SEO
      `Committee on Earth Observation Systems Engineering Office <https://ceos-cube.org/>`_ 
      
   COG
      Cloud Optimised GeoTIFF, a data file format optimised for efficient 
      workflows on the cloud and remote reading. 
  
   Collection
     C1, C2, C3 ...n - the whole suite of data from the Landsat or Sentinel mission. 
     Collections are updated when there are fundamental changes and upgrades to the data suite that 
     make it incompatible with the existing collection. Therefore a collection upgrade is more 
     akin to a movie franchise reboot than a re-release.
   
   CSIRO
      `Commonwealth Scientific and Industrial Research Organisation <https://www.csiro.au/>`_

   DEA
   Digital Earth Australia
      A Program of Geoscience Australia that uses spatial data and images 
      recorded by satellites orbiting our planet to detect physical changes 
      across Australia in unprecedented detail. DEA is the Australian implementation of
      the Open Data Cube. For more information see https://www.dea.ga.gov.au/.
      
   DEA Notebooks
      `Digital Earth Australia Notebooks <https://github.com/GeoscienceAustralia/dea-notebooks>`_, an open-source repository containing 
      Jupyter Notebooks, tools and workflows for geospatial analysis with Open 
      Data Cube and xarray. See 
      
   DEA Sandbox
      Digital Earth Australia Sandbox, a learning and analysis environment for 
      getting started with DEA and the Open Data Cube. It includes sample data 
      and Jupyter notebooks that demonstrate the capability of the Open Data Cube. 
      For more information see https://github.com/GeoscienceAustralia/dea-notebooks/wiki.
      
   DE Africa
   Digital Earth Africa
      `Digital Earth Africa <https://www.digitalearthafrica.org/>`_. A sister project to
      Digital Earth Australia but for the African Continent. Originally run out of Geoscience
      Australia, but transitioning to ownership within African Nations.

   EO
      Earth Observation
   
   ESA
      European Space Agency
   
   FC
      Fractional Cover. Fractional Cover (FC) is a measurement that splits the landscape into 
      three parts, or fractions; green (leaves, grass, and growing crops), brown (branches, 
      dry grass or hay, and dead leaf litter), and bare ground (soil or rock). For more 
      information and for details of the methodology, see 
      https://www.dea.ga.gov.au/products/dea-fractional-cover.
   
   GA
      Geoscience Australia
    
   Geomedian
      Geometric median, a robust high-dimensional statistic that maintains 
      relationships between spectral bands.
      
   GEE
      Google Earth Engine
      
   GIS
      Geographic Information System
   
   HLTC
      High and Low Tide Composites, a Digital Earth Australia product providing
      cloud-free imagery mosaics of Australia's coast, estuaries and reefs at low 
      and high tide. For more information see https://www.dea.ga.gov.au/products/dea-high-low.
      
   HPC
      High Performance Computing. 

   ITEM
      Intertidal Extents Model, a Digital Earth Australia product that maps the 
      relative extent of the Australian intertidal zone at regular intervals of 
      the observed tidal range. For more information see https://www.dea.ga.gov.au/products/dea-intertidal-extents.
      
   Jupyter notebook
      A computational "notebook" that allows code to be run and presented alongside 
      explanatory documentation, figures, scientific notation etc.
      
   JupyterLab
      An interactive web-based user interface for editing and running Jupyter notebooks.
      JupyterLab is used as an analysis environment on both the DEA Sandbox and the NCI's
      Virtual Desktop Infrastructure.

   Landsat
      A joint NASA/USGS program of medium resolution satellites that have been 
      collecting publicly available Earth observation data continuously since 1972.
   
   LCCS
      Land Cover Classification Scheme
   
   MADs
      Median Absolute Deviation, used as a form of standard deviation for the geomedians.
   
   MODIS
      Moderate Resolution Imaging Spectroradiometer, a sensor on board NASA's Terra and 
      Aqua satellites that collects publicly available low resolution Earth observation 
      data every one to two days.
   
   NASA
      National Aeronautics and Space Administration (United States)
   
   NBAR
      Nadir-corrected BRDF Adjusted Reflectance, where BRDF stands for Bidirectional
      reflectance distribution function.
      
   NBART
      Nadir-corrected BRDF Adjusted Reflectance with terrain illumination reflectance 
      correction.
   
   NBR
      Normalised Burn Ratio, calculated from near-infrared (NIR) and short wave infrared
      (SWIR).

   NCI

      The Australian `National Computational Infrastructure
      <https://www.nci.org.au/>`_ is Australia's national research computing
      facility. It provides computing facilities for Australian researchers,
      industry and government.

   NDVI
      Normalised Difference Vegetation Index, calculated from visible and near-infrared
      light reflected by vegetation. 
   
   NIDEM
      National Intertidal Digital Elevation Model, a Digital Earth Australia product 
      derived from ITEM that maps the elevation relative to Mean Sea Level of the 
      Australian intertidal zone. For more information see https://www.dea.ga.gov.au/products/dea-intertidal-elevation.
      
   NIR
      Near Infrared, referring to particular bands used to collect Earth observation 
      data
  
   NRT
     Near-real time. NRT data is a less refined/calibrated dataset, which is 
     available much sooner after satellite acquisition than standard ARD data. 
   
   ODC
   Open Data Cube
      The `Open Data Cube <https://www.opendatacube.org>`_ is an international 
      open-source project developing the software used by Digital Earth Australia.

   PostgreSQL
      The high performance database engine used as an index of Datasets by the
      Data Cube. It is both a relational and document database, and the Data
      Cube schema makes use of both of these capabilities.
   
   PQ
     Pixel quality

   Python
      `Python <https://www.python.org/>`_ is the programming language used to 
      develop the Open Data Cube and most of Digital Earth Australia. It is an easy
      to use language, which also provides simple access to high performance 
      processing capabilities.

   SAR
      Synthetic Aperture Radar
   
   Sentinel
      A program of satellites from ESA that collect publicly available Earth 
      observation data. The program includes the medium resolution Sentinel-2 mission, 
      and the Sentinel-1 SAR mission.
   
   SSH
      SSH or Secure Shell is a means to access remote computers using a text based
      terminal interface. It comes build in with Linux, but requires additional software
      to use it from Windows computers.

   USGS
      United States Geological Survey
      
   VDI
      The Virtual Desktop Infrastructure was a service offered by the :term:`NCI`
      that provided a linux desktop environment for scientific computing. It has
      been replaced by :term:`ARE`.

   WOFL
      Water Observation Feature Layer (a WO observation for one point in time)
            
   WO
      Water Observations (previously called Water Observations from Space), 
      a Digital Earth Australia product that provides
      images and data showing where water has been seen in Australia from 1987 to 
      the present. For more information see https://www.dea.ga.gov.au/products/dea-water-observations.
      
   xarray
      An open source project and Python package that for working with labelled 
      multi-dimensional arrays such as those returned by the Open Data Cube (ODC).

   YAML
      `YAML <https://yaml.org/>`_ is a human readable data storage format.
      It is used throughout DEA for metadata files, product
      definitions and other configuration files.

