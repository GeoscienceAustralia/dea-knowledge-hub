.. _introduction:

About DEA
=========

Digital Earth Australia (DEA) is a program of Geoscience Australia, an agency of the Australian Government. We create free and open satellite data products for the benefit of Australia.

.. contents:: In this guide
   :local:
   :backlinks: none

Overview
--------

Digital Earth Australia is a platform designed to ...

* Catalogue large amounts of Earth Observation data.
* Provide a :term:`Python` based :term:`API` for high performance querying and data access.
* Give scientists and other users easy ability to perform Exploratory Data Analysis.
* Allow scalable continent scale processing of the stored data.
* Track the provenance of all the contained data to allow for quality control and updates.

For more information, see the `DEA website <https://www.dea.ga.gov.au/>`_.

Background
----------

DEA builds upon the globally recognised innovation, the `Australian Geoscience Data Cube`_
which was the winner of the 2016 Content Platform of the Year at the Geospatial World
Leadership Awards and was developed as a partnership between `Geoscience Australia`_ (GA),
the `Commonwealth Scientific and Industrial Research Organisation`_ (CSIRO) and the
`National Computational Infrastructure`_ (NCI).

.. _Australian Geoscience Data Cube: http://www.datacube.org.au/
.. _Geoscience Australia: http://www.ga.gov.au/
.. _Commonwealth Scientific and Industrial Research Organisation: https://www.csiro.au/
.. _National Computational Infrastructure: https://nci.org.au/

Technology
----------

DEA is powered by `Open Data Cube <http://opendatacube.org/>`_ (ODC), an open-source library for the management, analysis, and processing of Geographic Information System (GIS) data -- namely Earth Observation satellite data. It is a global initiative to increase the value and use of satellite data by providing users with access to free data management technologies and analysis platforms. At its core, ODC is a set of Python libraries and a PostgreSQL database that facilitate working with geospatial raster data.

The ODC source code can be `found on GitHub <https://github.com/opendatacube/datacube-core>`_.

