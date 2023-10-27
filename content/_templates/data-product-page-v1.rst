{% set is_latest_version = data.is_latest_version %}

{% set valid_maps = data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = data.data | selectattr("link",  "!=", None) | list %}
{% set valid_explorer = data.explorer | selectattr("link",  "!=", None) | list %}
{% set valid_sandbox = data.sandbox | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_stac = data.stac | selectattr("link",  "!=", None) | list %}
{% set valid_ecat = data.ecat | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = data.code_samples | selectattr("link",  "!=", None) | list %}
{% set valid_files = data.files | selectattr("link",  "!=", None) | list %}
{% set valid_old_versions = data.old_versions | selectattr("slug",  "!=", None) | selectattr("version",  "!=", None) | selectattr("name",  "!=", None) | list %}

{% set valid_product_types = [data.product_type, data.spatial_data_type] | select("!=", None) | join(", ") %}

{% set has_access_data = valid_maps or valid_data or valid_explorer or valid_sandbox or valid_web_services or valid_stac or valid_ecat or valid_code_samples %}

{% set pretty_version = "v" + data.version %}
{% set tab_title = data.title if is_latest_version else pretty_version + ": " + data.title %}
{% set page_title = data.title if is_latest_version else "Old version: " + data.title %}

{% set map_label = "See the data on a map" %}
{% set stac_label = "Get via STAC" %}
{% set explorer_label = "Explore data samples" %}
{% set data_label = "Get the data online" %}
{% set sandbox_label = "Play with the sandbox" %}
{% set ecat_label = "Product catalogue" %}
{% set web_service_label = "Bring the data to you via web service" %}
{% set code_sample_label = "Code sample" %}

{% set map_default_name = "Map" %}
{% set data_default_name = "Data" %}
{% set explorer_default_name = "Data Explorer" %}
{% set sandbox_default_name = "Sandbox" %}
{% set web_service_default_name = "Service" %}
{% set stac_default_name = "STAC" %}
{% set code_sample_default_name = "Code" %}

.. |nbsp| unicode:: 0xA0
   :trim:

.. |copyright| unicode:: 0xA9

.. rst-class:: data-product-page

================================================
{{ tab_title }}
================================================

.. container:: header

   .. container:: title

      {{ page_title }}

   .. container:: subtitle

      {{ data.long_title }}

   .. container:: quick-info

      {% if not is_latest_version %}
      :Version: {{ data.version }} (`See latest version <{{ data.latest_version_link }}>`_)
      {%- else %}
      :Version: {{ data.version }} (Latest)
      {%- endif %}
      {%- if valid_product_types %}
      :Product type: {{ valid_product_types }}
      {%- endif %}
      {%- if data.time_span.start and data.time_span.end %}
      :Time span: {{ data.time_span.start }} – {{ data.time_span.end }}
      {%- elif data.time_span.start  %}
      :Starts at: {{ data.time_span.start }}
      {%- elif data.time_span.end  %}
      :Ends at: {{ data.time_span.end }}
      {%- endif %}
      :Update frequency: {{ data.update_frequency }}
      {%- if data.product_id %}
      :Product ID: {{ data.product_id }}
      {%- endif %}

   .. container:: hero-image

      |nbsp|

{% if not is_latest_version %}
.. container::
   :name: notifications

   .. ADMONITION:: This is an old version ({{ pretty_version }})
      :class: danger
   
      See the `latest version of the product <{{ data.latest_version_link }}>`_.

{% endif %}

{% if not is_latest_version %}
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

       {% if is_latest_version and has_access_data %}
       .. container::
          :name: access-cards

          .. grid:: 4
             :gutter: 3

             {% for item in valid_maps %}
             .. grid-item-card:: {{ item.title or map_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or map_default_name }}
             {% endfor %}

             {% for item in valid_explorer %}
             .. grid-item-card:: {{ item.title or explorer_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or explorer_default_name }}
             {% endfor %}

             {% for item in valid_data %}
             .. grid-item-card:: {{ item.title or data_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or data_default_name }}
             {% endfor %}

             {% for item in valid_code_samples %}
             .. grid-item-card:: {{ item.title or code_sample_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or code_sample_default_name }}
             {% endfor %}

             {% for item in valid_web_services %}
             .. grid-item-card:: {{ item.title or web_service_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or web_service_default_name }}
             {% endfor %}

             {% for item in valid_stac %}
             .. grid-item-card:: {{ item.title or stac_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or stac_default_name }}
             {% endfor %}

             {% for item in valid_ecat %}
             .. grid-item-card:: {{ item.title or ecat_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item.id }}

                ecat {{ item.id }}
             {% endfor %}

             {% for item in valid_sandbox %}
             .. grid-item-card:: {{ item.title or sandbox_label }}
                :img-top: {{ item.image or "https://www.gifpng.com/300x200" }}
                :link: {{ item.link }}

                {{ item.name or sandbox_default_name }}
             {% endfor %}
       {% endif %}

       .. rubric:: Key details
          :name: key-details

       {% if data.parent_products %}
       :Parent product(s): `{{ data.parent_products.name }} <{{ data.parent_products.link }}>`_
       {%- endif %}
       {%- if data.collection.name and data.collection.link %}
       :Collection: `{{ data.collection.name }} <{{ data.collection.link }}>`_
       {%- elif data.collection.name %}
       :Collection: {{ data.collection.name }}
       {%- endif %}
       {%- if data.doi %}
       :DOI: {{ data.doi }}
       {%- endif %}
       {%- if data.published %}
       :Last updated: {{ data.published }}
       {%- endif %}

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

       {% if is_latest_version and has_access_data %}
       .. list-table::
          :name: access-table

          {% if valid_maps %}
          * - **{{ map_label }}**
            - {% for item in valid_maps %}
              * `{{ item.name or map_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps </setup/dea_maps.html>`_.
          {% endif %}

          {% if valid_explorer %}
          * - **{{ explorer_label }}**
            - {% for item in valid_explorer %}
              * `{{ item.name or explorer_default_name }} <{{ item.link }}>`_
              {% endfor %}
            -
          {% endif %}

          {% if valid_data %}
          * - **{{ data_label }}**
            - {% for item in valid_data %}
              * `{{ item.name or data_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </about/faq.html#how-do-i-download-data-from-dea>`_.
          {% endif %}

          {% if valid_code_samples %}
          * - **{{ code_sample_label }}**
            - {% for item in valid_code_samples %}
              * `{{ item.name or code_sample_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `connect to the DEA Sandbox </setup/Sandbox/sandbox.html>`_.
          {% endif %}

          {% if valid_web_services %}
          * - **{{ web_service_label }}**
            - {% for item in valid_web_services %}
              * `{{ item.name or web_service_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `connect to DEA's web services </setup/gis/README.html>`_.
          {% endif %}

          {% if valid_stac %}
          * - **{{ stac_label }}**
            - {% for item in valid_stac %}
              * `{{ item.name or stac_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access and stream the data using STAC </notebooks/How_to_guides/Downloading_data_with_STAC.html>`_.
          {% endif %}

          {% if valid_ecat %}
          * - **{{ ecat_label }}**
            - {% for item in valid_ecat %}
              * `ecat {{ item.id }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item.id }}>`_
              {% endfor %}
            -
          {% endif %}

          {% if valid_sandbox %}
          * - **{{ sandbox_label }}**
            - {% for item in valid_sandbox %}
              * `{{ item.name or sandbox_default_name }} <{{ item.link }}>`_
              {% endfor %}
            -
          {% endif %}

       {% else %}
       There are no data source links available at the present time.
       {% endif %}

       {% if valid_files %}

       .. rubric:: Additional files
          :name: additional-files

       .. list-table::
          :name: additional-files-table

          {% for item in valid_files %}
          * - `{{ item.name or item.link }} <{{ item.link }}>`_
            - {{ item.description }}
          {% endfor %}
       {% endif %}

       {% if not is_latest_version %}
       You can find the data source links in the `latest version of the product <{{ data.latest_version_link }}>`_.
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

       {% if not is_latest_version %}
       You can find the history in the `latest version of the product <{{ data.latest_version_link }}>`_.
       {% else %}
       .. rubric:: Old versions
          :name: old-versions

       {% if valid_old_versions %}

       View previous versions of this data product.

       .. list-table::

          {% for item in valid_old_versions %}
          * - `v{{ item.version }}: {{ item.name }} </data/old-versions/{{ item.slug }}>`_
            - {{ item.release_date or "" }}
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
