{% set valid_maps = data["maps"] | selectattr("link",  "!=", None) %}
{% set valid_data = data["data"] | selectattr("link",  "!=", None) %}
{% set valid_explorer = data["explorer"] | selectattr("link",  "!=", None) %}
{% set valid_sandbox = data["sandbox"] | selectattr("link",  "!=", None) %}
{% set valid_web_services = data["web_services"] | selectattr("link",  "!=", None) %}
{% set valid_stac = data["stac"] | selectattr("link",  "!=", None) %}
{% set valid_ecat = data["ecat"] | selectattr("link",  "!=", None) %}
{% set valid_code_samples = data["code_samples"] | selectattr("link",  "!=", None) %}

{% set has_valid_maps = data["maps"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_data = data["data"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_explorer = data["explorer"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_sandbox = data["sandbox"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_web_services = data["web_services"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_stac = data["stac"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_ecat = data["ecat"] | selectattr("link",  "!=", None) | list | length > 0 %}
{% set has_valid_code_samples = data["code_samples"] | selectattr("link",  "!=", None) | list | length > 0 %}

{% set has_access_data = has_valid_maps or has_valid_data or has_valid_explorer or has_valid_sandbox or has_valid_web_services or has_valid_stac or has_valid_ecat or has_valid_code_samples %}

.. |nbsp| unicode:: 0xA0
   :trim:

.. |copyright| unicode:: 0xA9

.. rst-class:: data-product-page

{% if not data["is_latest_version"] %}
================================================
{{ "v" + data["version"] }}: {{ data["title"] }}
================================================
{% else %}
================================================
{{ data["title"] }}
================================================
{% endif %}

.. container:: header

   .. container:: title

      {% if not data["is_latest_version"] %}
      Old Version: {{ data["title"] }}
      {% else %}
      {{ data["title"] }}
      {% endif %}

   .. container:: subtitle

      {{ data["long_title"] }}

   .. container:: quick-info

      {% if not data["is_latest_version"] %}
      :Version: {{ data["version"] }} (`See latest version <{{ data["latest_version_link"] }}>`_)
      {% else %}:Version: {{ data["version"] }} (Latest)
      {% endif %}
      :Product type: {{ data["product_type"] }}, {{ data["spatial_data_type"] }}
      {% if data["time_span"]["start"] and data["time_span"]["end"] %}
      :Time span: {{ data["time_span"]["start"] }} – {{ data["time_span"]["end"] }}
      {% elif data["time_span"]["start"] or data["time_span"]["end"]  %}
      :Time span: {{ data["time_span"]["start"] or data["time_span"]["end"] }}
      {% endif %}
      :Update frequency: {{ data["update_frequency"] }}
      {% if data["product_id"] %}
      :Product ID: {{ data["product_id"] }}
      {% endif %}

   .. container:: hero-image

      |nbsp|

{% if not data["is_latest_version"] %}
.. container::
   :name: notifications

   .. ADMONITION:: This is an old version ({{ "v" + data["version"] }})
      :class: danger
   
      See the `latest version of the product <{{ data["latest_version_link"] }}>`_.

{% endif %}

.. tab-set::

    .. tab-item:: Overview
       :name: overview-tab

       .. container:: table-of-contents

          .. container::
             :name: overview-table-of-contents

             |nbsp|

       .. include:: _overview.md
          :parser: myst_parser.sphinx_

       .. rubric:: Access the data
          :name: access-the-data-cards

       {% if data["is_latest_version"] and has_access_data %}
       .. container::
          :name: access-cards

          .. grid:: 4
             :gutter: 3

             {% for item in valid_maps %}
             .. grid-item-card:: {{ item["title"] or "See it on a map" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Map" }}
             {% endfor %}

             {% for item in valid_data %}
             .. grid-item-card:: {{ item["title"] or "Get the data online" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Data" }}
             {% endfor %}

             {% for item in valid_explorer %}
             .. grid-item-card:: {{ item["title"] or "Explore data samples" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Data Explorer" }}
             {% endfor %}

             {% for item in valid_sandbox %}
             .. grid-item-card:: {{ item["title"] or "Play with the sandbox" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Sandbox" }}
             {% endfor %}

             {% for item in valid_web_services %}
             .. grid-item-card:: {{ item["title"] or "Bring the data to you via web service" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Service" }}
             {% endfor %}

             {% for item in valid_stac %}
             .. grid-item-card:: {{ item["title"] or "Get via STAC" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "STAC" }}
             {% endfor %}

             {% for item in valid_ecat %}
             .. grid-item-card:: {{ item["title"] or "View the product catalogue" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item["id"] }}

                ecat {{ item["id"] }}
             {% endfor %}

             {% for item in valid_code_samples %}
             .. grid-item-card:: {{ item["title"] or "Code sample" }}
                :img-top: {{ item["image"] or "https://www.gifpng.com/300x200" }}
                :link: {{ item["link"] }}

                {{ item["name"] or "Code" }}
             {% endfor %}
       {% endif %}

       .. rubric:: Key details
          :name: key-details

       {% if data["parent_product"] %}
       :Parent product(s): `{{ data["parent_product"]["name"] }} <{{ data["parent_product"]["link"] }}>`_
       {% endif %}
       {% if data["collection"] %}
       :Collection: {{ data["collection"] }}
       {% endif %}
       {% if data["doi"] %}
       :DOI: {{ data["doi"] }}
       {% endif %}
       {% if data["published"] %}
       :Last updated: {{ data["published"] }}
       {% endif %}

       .. include:: _publications.md
          :parser: myst_parser.sphinx_

    .. tab-item:: Access
       :name: access-tab

       .. container:: table-of-contents

          .. container::
             :name: access-table-of-contents

             |nbsp|

       .. rubric:: Access the data
          :name: access-the-data-table

       {% if data["is_latest_version"] and has_access_data %}
       .. list-table::
          :name: access-table

          {% if has_valid_maps %}
          * - **See the data on a map**
            - {% for item in valid_maps %}
              * `{{ item["name"] or "Map" }} <{{ item["link"] }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps <{{ config.html_context["learn_access_dea_maps_link"] }}>`_.
          {% endif %}

          {% if has_valid_stac %}
          * - **Get via STAC**
            - {% for item in valid_stac %}
              * `{{ item["name"] or "STAC" }} <{{ item["link"] }}>`_
              {% endfor %}
            - Learn how to `access and stream the data using STAC <{{ config.html_context["learn_access_stac_link"] }}>`_.
          {% endif %}

          {% if has_valid_explorer %}
          * - **Explore data samples**
            - {% for item in valid_explorer %}
              * `{{ item["name"] or "Data Explorer" }} <{{ item["link"] }}>`_
              {% endfor %}
            -
          {% endif %}

          {% if has_valid_data %}
          * - **Get the data online**
            - {% for item in valid_data %}
              * `{{ item["name"] or "Data" }} <{{ item["link"] }}>`_
              {% endfor %}
            -
          {% endif %}

          {% if data["sandbox"] %}
          * - **Play with the sandbox**
            - {% for item in data["sandbox"] %}
              * `{{ item["name"] or "Sandbox" }} <{{ item["link"] }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS <{{ config.html_context["learn_access_data_AWS_link"] }}>`_.
          {% endif %}

          {% if data["ecat"] %}
          * - **Product catalogue**
            - {% for item in data["ecat"] %}
              * `ecat {{ item["id"] }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item["id"] }}>`_
              {% endfor %}
            - Learn how to `use DEA's Sandbox environment <{{ config.html_context["learn_access_DEA_Sandbox_link"] }}>`_.
          {% endif %}

          {% if data["web_services"] %}
          * - **Bring the data to you via web service**
            - {% for item in data["web_services"] %}
              * `{{ item["name"] or "Web service" }} <{{ item["link"] }}>`_
              {% endfor %}
            - Learn how to `connect to DEA's web services <{{ config.html_context["learn_access_web_service_link"] }}>`_.
          {% endif %}

          {% if data["code_samples"] %}
          * - **Code sample**
            - {% for item in data["code_samples"] %}
              * `{{ item["name"] or "Code" }} <{{ item["link"] }}>`_
              {% endfor %}
            -
          {% endif %}

       {% else %}
       There are no data source links available at the present time.
       {% endif %}

       {% if data["files"] %}

       .. rubric:: Additional files
          :name: additional-files

       .. list-table::
          :name: additional-files-table

          {% for item in data["files"] %}
          * - `{{ item["name"] or "File" }} <{{ item["link"] }}>`_
            - {{ item["description"] }}
          {% endfor %}
       {% endif %}

       {% if not data["is_latest_version"] %}
       You can find the data source links in the `latest version of the product <{{ data["latest_version_link"] }}>`_.
       {% endif %}

       .. include:: _access.md
          :parser: myst_parser.sphinx_

    .. tab-item:: Details
       :name: details-tab

       .. container:: table-of-contents

          .. container::
             :name: details-table-of-contents

             |nbsp|

       .. include:: _details.md
          :parser: myst_parser.sphinx_

    .. tab-item:: Quality
       :name: quality-tab

       .. container:: table-of-contents

          .. container::
             :name: quality-table-of-contents

             |nbsp|

       .. include:: _quality.md
          :parser: myst_parser.sphinx_

    .. tab-item:: History
       :name: history-tab

       .. container:: table-of-contents

          .. container::
             :name: history-table-of-contents

             |nbsp|

       {% if not data["is_latest_version"] %}
       You can find the history in the `latest version of the product <{{ data["latest_version_link"] }}>`_.
       {% else %}
       .. rubric:: Old versions
          :name: old-versions

       {% if data["old_versions"] %}

       View previous versions of this data product.

       .. list-table::

          {% for item in data["old_versions"] %}
          * - `v{{ item["version"] }}: {{ item["name"] }} </data/old-versions/{{ item["slug"] }}>`_
            - {{ item["release_date"] }}
          {% endfor %}
       {% else %}
       No old versions available.
       {% endif %}

       .. include:: _history.md
          :parser: myst_parser.sphinx_
       {% endif %}

    .. tab-item:: Credits
       :name: credits-tab

       .. container:: table-of-contents

          .. container::
             :name: credits-table-of-contents

             |nbsp|
    
       .. include:: _credits.md
          :parser: myst_parser.sphinx_

       |copyright| Commonwealth of Australia (Geoscience Australia).

.. raw:: html

   <script type="text/javascript" src="/_static/scripts/tocbot.min.js"></script>
   <script type="text/javascript" src="/_static/scripts/tocbot-data-product.js" /></script>
