.. |dot| replace:: **·**

{{ data["title"] }}
^^^^^^^^^^^^^^^^^^^

.. container:: data-product

   .. container:: long-title

      {{ data["long_title"] }}

   .. container:: quick-details

      | **Version:** {{ data["version"] }} ({{ data["release"] }}) |dot| **Product type:** Derivative; Vector
      | **Time span:** 01/01/1988 – 31/12/2022 |dot| **Update frequency:** Annually

   .. tab-set::
   
       .. tab-item:: Overview

          .. grid:: 4
              :gutter: 2

              .. grid-item-card:: See it on a map
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://maps.dea.ga.gov.au/story/DEACoastlines

                 DEACoastlines

              .. grid-item-card:: Get the data
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://data.dea.ga.gov.au/?prefix=derivative/dea_coastlines/2-1-0/

                 dea_coastlines
   
              .. grid-item-card:: Explore data samples
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://explorer.prod.dea.ga.gov.au/products/geodata_coast_100k
              
                 AWS

              .. grid-item-card:: Code example
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://docs.dea.ga.gov.au/notebooks/DEA_products/DEA_Coastlines.html

                 Jupyter notebook
              
              .. grid-item-card:: Code example
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://github.com/GeoscienceAustralia/dea-coastlines
              
                 GitHub repository

          .. include:: _about.md
             :parser: myst_parser.sphinx_

          .. rubric:: Key information

          :Product ID: geodata_coast_100k
          :DOI: 10.26186/116268
          :Program: Digital Earth Australia
          :Collection: Geoscience Australia Landsat Collection 3
          :Published: 15/08/2023 (Sagar Stephen)

       .. tab-item:: Access

          .. image:: https://www.gifpng.com/896x350
             :alt: Map of the schema / spatial extent

          .. dropdown:: Schema / Spatial Extent data

             =========================== =========================================
             Update frequency            annually
             Temporal extent             1988-01-01 00:00:00 – 2022-12-31 11:59:59
             Min. longitude              -4846590.00
             Max. longitude              -1887450.00
             Min. latitude               -1015650.00
             Max. latitude               2121650.00
             Coordinate reference system Australian Albers / GDA94 (EPSG: 3577)
             Cell size X                 30.00
             Cell size Y                 30.00
             =========================== =========================================

          .. dropdown:: How do I access the data?

              Instructions for accessing the data via AWS `Frequently Asked Questions — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_

              For instructions on Downloading and streaming data using STAC, see this notebook guide `Downloading and streaming data using STAC metadata — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_

              For information on how to use DEA Maps and download simple datasets, see the user guide here. `DEA Maps — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_

              For instructions on connecting to DEA's web services, see the user guide here. `DEA Web Services — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_

          .. rubric:: Sources

          {% if data["maps"] %}
          :See it on a map:
             * `DEACoastlines <https://maps.dea.ga.gov.au/story/DEACoastlines>`_
          {% endif %}
          {% if data["data"] %}
          :Get the data:
             * `dea_coastlines <https://data.dea.ga.gov.au/?prefix=derivative/dea_coastlines/2-1-0/>`_
          {% endif %}
          {% if data["explorer"] %}
          :Explore data samples:
             * `AWS <https://explorer.prod.dea.ga.gov.au/products/geodata_coast_100k>`_
          {% endif %}
       
          .. include:: _access.md
             :parser: myst_parser.sphinx_

       .. tab-item:: Details

          .. include:: _details.md
             :parser: myst_parser.sphinx_

       .. tab-item:: Quality

          .. include:: _quality.md
             :parser: myst_parser.sphinx_

       .. tab-item:: History
       
          .. include:: _history.md
             :parser: myst_parser.sphinx_

       .. tab-item:: Credits
       
           .. include:: _credits.md
              :parser: myst_parser.sphinx_
