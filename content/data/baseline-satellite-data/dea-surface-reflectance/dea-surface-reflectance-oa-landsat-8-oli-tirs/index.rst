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

              .. grid-item-card:: Get the data
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://dapds00.nci.org.au/thredds/catalog/xu18/catalog.html

                 NCI - THREDDS

              .. grid-item-card:: Get the data
                 :img-top: https://www.gifpng.com/300x200
                 :link: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls8c_ard_3/

                 DEA Public

          .. include:: _about.md
             :parser: myst_parser.sphinx_

          .. rubric:: Key information

          :Product ID: ga_ls8c_ard_3
          :DOI: 10.26186/116268
          :Program: Digital Earth Australia
          :Collection: Geoscience Australia Landsat Collection 3
          :Published: 15/08/2023 (Sagar Stephen)
          :NCI project code: xu18
          :Security classification: Unclassified

       .. tab-item:: Access

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
             * `NCI - THREDDS <https://dapds00.nci.org.au/thredds/catalog/xu18/catalog.html>`_
             * `DEA Public <https://data.dea.ga.gov.au/?prefix=baseline/ga_ls8c_ard_3/>`_
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
