.. |dot| replace:: **·**

{{ data["title"] }}
===================

.. container:: data-product

   .. container:: header-text

      .. container:: subtitle

         {{ data["long_title"] }}

      .. container:: quick-info

         | **Version:** {{ data["version"] }} ({{ data["release"] }}) |dot| **Product type:** Derivative; Vector
         | **Time span:** 01/01/1988 – 31/12/2022
         | **Update frequency:** Annually {% if data["parent_product"] %} |dot| **Child of:** `{{ data["parent_product"]["name"] }} <{{ data["parent_product"]["link"] }}>`_{% endif %}

   .. container:: header-image

      .. image:: {{ data["image"] }}

   .. tab-set::
   
       .. tab-item:: Overview

          .. grid:: 4
              :gutter: 2

              {% for item in data["maps"] %}
              .. grid-item-card:: {{ item.get("title", "See the map") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Map") }}
              {% endfor %}

              {% for item in data["data"] %}
              .. grid-item-card:: {{ item.get("title", "Get the data") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Data") }}
              {% endfor %}

              {% for item in data["stac"] %}
              .. grid-item-card:: {{ item.get("title", "Get via STAC") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "STAC") }}
              {% endfor %}

              {% for item in data["explorer"] %}
              .. grid-item-card:: {{ item.get("title", "Explore data samples") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Data Explorer") }}
              {% endfor %}

              {% for item in data["sandbox"] %}
              .. grid-item-card:: {{ item.get("title", "Play with the sandbox") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Sandbox") }}
              {% endfor %}

              {% for item in data["ecat"] %}
              .. grid-item-card:: {{ item.get("title", "Product catalogue") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item.get("id") }}

                 ecat {{ item.get("id") }}
              {% endfor %}

              {% for item in data["web_services"] %}
              .. grid-item-card:: {{ item.get("title", "Web service") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Service") }}
              {% endfor %}

              {% for item in data["code_samples"] %}
              .. grid-item-card:: {{ item.get("title", "Code sample") }}
                 :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
                 :link: {{ item.get("link") }}

                 {{ item.get("name", "Code") }}
              {% endfor %}
   
          .. include:: _about.md
             :parser: myst_parser.sphinx_

          .. rubric:: Key information

          {% if data["product_id"] %}
          :Product ID: {{ data["product_id"] }}
          {% endif %}
          {% if data["doi"] %}
          :DOI: {{ data["doi"] }}
          {% endif %}
          {% if data["program"] %}
          :Program: {{ data["program"] }}
          {% endif %}
          {% if data["collection"] %}
          :Collection: {{ data["collection"] }}
          {% endif %}
          {% if data["published"] and data["author"] %}
          :Published: {{ data["published"] }} ({{ data["author"] }})
          {% elif data["published"] %}
          :Published: {{ data["published"] }}
          {% elif data["author"] %}
          :Published by: {{ data["author"] }}
          {% endif %}

          ----

          .. tags:: {{ data["tags"]|join(', ') }}

       .. tab-item:: Access

          .. .. image:: https://www.gifpng.com/896x350
          ..    :alt: Map of the schema / spatial extent
          ..
          .. .. dropdown:: Schema / Spatial Extent data
          ..
          ..    =========================== =========================================
          ..    Update frequency            annually
          ..    Temporal extent             1988-01-01 00:00:00 – 2022-12-31 11:59:59
          ..    Min. longitude              -4846590.00
          ..    Max. longitude              -1887450.00
          ..    Min. latitude               -1015650.00
          ..    Max. latitude               2121650.00
          ..    Coordinate reference system Australian Albers / GDA94 (EPSG: 3577)
          ..    Cell size X                 30.00
          ..    Cell size Y                 30.00
          ..    =========================== =========================================
          ..
          .. .. dropdown:: How do I access the data?
          ..
          ..     Instructions for accessing the data via AWS `Frequently Asked Questions — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_
          ..
          ..     For instructions on Downloading and streaming data using STAC, see this notebook guide `Downloading and streaming data using STAC metadata — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_
          ..
          ..     For information on how to use DEA Maps and download simple datasets, see the user guide here. `DEA Maps — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_
          ..
          ..     For instructions on connecting to DEA's web services, see the user guide here. `DEA Web Services — Digital Earth Australia 1.0.0 documentation <ga.gov.au>`_

          .. rubric:: Access the data

          {% if data["maps"] %}
          :See it on a map:
          {% for item in data["maps"] %}
             * `{{ item.get("name", "Map") }} <{{ item.get("link") }}>`_
          {% endfor %}
          {% endif %}

          {% if data["data"] %}
          :Get the data:
          {% for item in data["data"] %}
             * `{{ item.get("name", "Data") }} <{{ item.get("link") }}>`_
          {% endfor %}
          {% endif %}

          {% if data["stac"] %}
          :Get the data:
          {% for item in data["stac"] %}
             * `{{ item.get("name", "Data") }} <{{ item.get("link") }}>`_
          {% endfor %}
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

          .. rubric:: Previous versions

          {% if data["previous_versions"] %}

          View previous versions of this data product.

          .. list-table::

             {% for item in data["previous_versions"] %}
             * - `v{{ item.get("version") }}, {{ item.get("name") }} <{{ item.get("link") }}>`_
               - {{ item.get("release_date") }}
             {% endfor %}
          {% else %}
          No previous versions available.
          {% endif %}

          .. rubric: Changelog
       
          .. include:: _history.md
             :parser: myst_parser.sphinx_

       .. tab-item:: Credits
       
           .. include:: _credits.md
              :parser: myst_parser.sphinx_
