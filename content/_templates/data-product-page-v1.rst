.. |dot| replace:: **·**

{{ "Deprecated: " if data["is_deprecated"] }}{{ data["title"] }}{{ ", v" + data["version"] if not data["is_latest_version"] }}
==============================================================================================================================

.. container:: data-product

   .. container:: header-text

      .. container:: subtitle

         {{ data["long_title"] }}

      .. container:: quick-info

         | **Version:** {{ data["version"] }} ({{ "Latest" if data["is_latest_version"] else "Previous version" }}) |dot| **Product type:** {{ data["product_type"] }}; {{ data["spatial_data_type"] }}
         | **Time span:** {{ data["time_span"]["start"] }} – {{ data["time_span"]["end"] }}
         | **Update frequency:** {{ data["update_frequency"] }} {% if data["parent_product"] %} |dot| **Child of:** `{{ data["parent_product"]["name"] }} <{{ data["parent_product"]["link"] }}>`_{% endif %}

   .. container:: header-image

      .. image:: {{ data["image"] }}

   .. tab-set::
   
       .. tab-item:: Overview

          {% if data["is_deprecated"] %}
          .. admonition:: This product is deprecated

             {% if data["new_product_link"] %}
             It is no longer active or in use. See the `new data product <{{ data["new_product_link"] }}>`_.
             {% else %}
             It is no longer active or in use.
             {% endif %}
          {% endif %}

          {% if data["is_latest_version"] %}
          .. admonition:: A newer version exists
         
             {% if data["new_product_link"] %}
             See the `latest version of this data product <{{ data["new_product_link"] }}>`_.
             {% else %}
             Please see the latest version of this data product.
             {% endif %}
          {% endif %}

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

          .. rubric:: Access the data

          .. list-table::

             {% if data["maps"] %}
             * - **See the map**
               - {% for item in data["maps"] %}
                 * `{{ item.get("name", "Map") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               - Learn how to `use DEA Maps <example.com>`_.
             {% endif %}

             {% if data["data"] %}
             * - **Get the data**
               - {% for item in data["data"] %}
                 * `{{ item.get("name", "Data") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               -
             {% endif %}

             {% if data["stac"] %}
             * - **Get via STAC**
               - {% for item in data["stac"] %}
                 * `{{ item.get("name", "STAC") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               - Learn how to `access and stream the data using STAC <example.com>`_.
             {% endif %}

             {% if data["explorer"] %}
             * - **Explore data samples**
               - {% for item in data["explorer"] %}
                 * `{{ item.get("name", "Data Explorer") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               - Learn how to `access the data via AWS <example.com>`_.
             {% endif %}

             {% if data["sandbox"] %}
             * - **Play with the sandbox**
               - {% for item in data["sandbox"] %}
                 * `{{ item.get("name", "Sandbox") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               -
             {% endif %}

             {% if data["ecat"] %}
             * - **Product catalogue**
               - {% for item in data["ecat"] %}
                 * `ecat {{ item.get("id") }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item.get("id") }}>`_
                 {% endfor %}
               -
             {% endif %}

             {% if data["web_services"] %}
             * - **Web service**
               - {% for item in data["web_services"] %}
                 * `{{ item.get("name", "Web service") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               - Learn how to `connect to DEA's web services <example.com>`_.
             {% endif %}

             {% if data["code_samples"] %}
             * - **Code sample**
               - {% for item in data["code_samples"] %}
                 * `{{ item.get("name", "Code") }} <{{ item.get("link") }}>`_
                 {% endfor %}
               -
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
             * - `v{{ item.get("version") }} – {{ item.get("name") }} <{{ item.get("link") }}>`_
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
