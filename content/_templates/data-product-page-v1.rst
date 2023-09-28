.. |nbsp| unicode:: 0xA0 
   :trim:

.. rst-class:: data-product

{% if not data["is_latest_version"] %}
{{ "v" + data["version"] + ":" }} {{ data["title"] }} (Old version)
===================================================================
{% else %}

{{ data["title"] }}
===================================================================
{% endif %}

.. container:: header

   .. container:: subtitle

      {{ data["long_title"] }}

   .. container:: quick-info

      {% if not data["is_latest_version"] %}:Version: {{ data["version"] }} (`See latest version <{{ data["latest_version_link"] }}>`_){% else %}:Version: {{ data["version"] }} (Latest){% endif %}
      :Product type: {{ data["product_type"] }}; {{ data["spatial_data_type"] }}
      :Time span: {{ data["time_span"]["start"] }} – {{ data["time_span"]["end"] }}
      :Update frequency: {{ data["update_frequency"] }}
      :Product ID: {{ data["product_id"] }}

      .. container:: hero-box

         .. container:: hero-image

            |nbsp|

.. tab-set::

    .. tab-item:: Overview
       :name: overview-tab

       .. container::
          :name: notifications

          {% if not data["is_latest_version"] %}
          .. ADMONITION:: This is an old version (v{{ data["version"] }})
          
             See the `latest version of the product <{{ data["latest_version_link"] }}>`_.
          {% endif %}

       .. container::
          :name: access-cards

          .. grid:: 4
             :gutter: 3

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

       .. rubric:: About
          :name: about

       .. include:: _about.md
          :parser: myst_parser.sphinx_

       .. rubric:: Key information
          :name: key-information

       {% if data["parent_product"] %}
       :Parent product(s): `{{ data["parent_product"]["name"] }} <{{ data["parent_product"]["link"] }}>`_
       {% endif %}
       {% if data["collection"] %}
       :Collection: `{{ data["collection"] }} <example.com>`_
       {% endif %}
       {% if data["doi"] %}
       :DOI: {{ data["doi"] }}
       {% endif %}
       {% if data["published"] and data["author"] %}
       :Published: {{ data["published"] }} ({{ data["author"] }})
       {% elif data["published"] %}
       :Published: {{ data["published"] }}
       {% elif data["author"] %}
       :Published by: {{ data["author"] }}
       {% endif %}

    .. tab-item:: Access
       :name: access-tab

       .. rubric:: Access the data
          :name: access-data

       .. list-table::
          :name: access-table

          {% if data["maps"] %}
          * - **See the map**
            - {% for item in data["maps"] %}
              * `{{ item.get("name", "Map") }} <{{ item.get("link") }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps </setup/dea_maps.html>`_.
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
            - Learn how to `access and stream the data using STAC </notebooks/How_to_guides/Downloading_data_with_STAC.html>`_.
          {% endif %}

          {% if data["explorer"] %}
          * - **Explore data samples**
            - {% for item in data["explorer"] %}
              * `{{ item.get("name", "Data Explorer") }} <{{ item.get("link") }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </about/faq.html#how-do-i-download-data-from-dea>`_.
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
            - Learn how to `connect to DEA's web services </setup/gis/README.html>`_.
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
       :name: details-tab

       .. include:: _details.md
          :parser: myst_parser.sphinx_

    .. tab-item:: Quality
       :name: quality-tab

       .. include:: _quality.md
          :parser: myst_parser.sphinx_

    .. tab-item:: History
       :name: history-tab

       .. rubric:: Previous versions
          :name: previous-versions

       {% if data["previous_versions"] %}

       View previous versions of this data product.

       .. list-table::

          {% for item in data["previous_versions"] %}
          * - `v{{ item.get("version") }}: {{ item.get("name") }} <{{ item.get("link") }}>`_
            - {{ item.get("release_date") }}
          {% endfor %}
       {% else %}
       No previous versions available.
       {% endif %}

       .. include:: _history.md
          :parser: myst_parser.sphinx_

    .. tab-item:: Credits
       :name: credits-tab
    
       .. include:: _credits.md
          :parser: myst_parser.sphinx_
