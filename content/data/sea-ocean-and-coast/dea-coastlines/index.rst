.. |middledot| unicode:: 0xB7

.. datatemplate:yaml:: ./_data.yaml

   {{ data["title"] }}
   ^^^^^^^^^^^^^^^^^^^

   {{ data["long_title"] }}

   | **Version:** {{ data["version"] }} :bdg-success:`{{ data["release"] }}` |middledot| **Product type:** Derivative; Vector
   | **Time span:** 01/01/1988 – 31/12/2022 |middledot| **Update frequency:** Annually

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

          .. rubric:: About

          .. include:: _about.md
             :parser: myst_parser.sphinx_

          .. rubric:: Key information

          :Product ID: geodata_coast_100k
          :DOI: 10.26186/116268
          :Program: Digital Earth Australia
          :Collection: Geoscience Australia Landsat Collection 3
          :Published: 15/08/2023 (Sagar Stephen)

       .. tab-item:: Access

          .. rubric:: Sources

          :Test: A
       
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
