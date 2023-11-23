{% set is_latest_version = data.is_latest_version %}

{% set valid_maps = data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = data.data | selectattr("link",  "!=", None) | list %}
{% set valid_explorers = data.explorers | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = data.code_examples | selectattr("link",  "!=", None) | list %}
{% set valid_files = data.files | selectattr("link",  "!=", None) | list %}
{% set valid_old_versions = data.old_versions | selectattr("slug",  "!=", None) | selectattr("version",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_product_types = [data.product_type, data.spatial_data_type] | select("!=", None) | list %}
{% set valid_product_ids = data.product_ids | select("!=", None) | list %}
{% set valid_ecat = data.ecat | select("!=", None) | list %}
{% set valid_dois = data.dois | select("!=", None) | list %}
{% set valid_tags = data.tags | select("!=", None) | list %}

{% set map_label = "See it on a map" %}
{% set explorer_label = "Explore data samples" %}
{% set data_label = "Get the data online" %}
{% set web_service_label = "Get via web service" %}
{% set code_sample_label = "Code sample" %}

{% set map_default_name = "DEA Map" %}
{% set data_default_name = "DEA Data" %}
{% set explorer_default_name = "Data Explorer" %}
{% set web_service_default_name = "Web service" %}
{% set code_sample_default_name = "Code sample" %}

{% set has_access_data = valid_maps or valid_data or valid_explorers or valid_web_services or valid_ecat or valid_code_samples %}

{% set pretty_version = "v" + data.version %}
{% set page_title = data.title if is_latest_version else "Old version: " + data.title %}

{% set product_ids_label = "Product IDs" if valid_product_ids | length > 1 else "Product ID" %}
{% set product_types_label = "Product types" if valid_product_types | length > 1 else "Product type" %}
{% set dois_label = "DOIs" if valid_dois | length > 1 else "DOI" %}
{% set ecat_label = "Persistent IDs" if valid_dois | length > 1 else "Persistent ID" %}

.. |nbsp| unicode:: 0xA0
   :trim:

.. rst-class:: product-page

======================================================================================================================================================
{{ page_title }}
======================================================================================================================================================

.. container:: showcase-panel bg-gradient-primary

   .. container::

      .. rubric:: {{ page_title }}

      {{ data.long_title }}

      {% if not is_latest_version %}
      :Version: {{ data.version }} (`See latest version <{{ data.latest_version_link }}>`_)
      {%- else %}
      :Version: {{ data.version }} (Latest)
      {%- endif %}
      {%- if valid_product_types %}
      :{{ product_types_label }}: {{ valid_product_types | join(", ") }}
      {%- endif %}
      {%- if data.time_span.start and data.time_span.end %}
      :Time span: {{ data.time_span.start }} – {{ data.time_span.end }}
      {%- elif data.time_span.start  %}
      :Starts at: {{ data.time_span.start }}
      {%- elif data.time_span.end  %}
      :Ends at: {{ data.time_span.end }}
      {%- endif %}
      :Update frequency: {{ data.update_frequency }}
      {%- if valid_product_ids %}
      :{{ product_ids_label }}: {{ valid_product_ids | join(", ") }}
      {%- endif %}

   .. container::

      .. image:: {{ data.header_image or "/_files/pages/dea-hero.jpg" }}

{% if not is_latest_version %}
.. container::
   :name: notifications

   .. admonition:: This is an old version ({{ pretty_version }})
      :class: danger
   
      See the `latest version of the product <{{ data.latest_version_link }}>`_.

{% endif %}

{% if not is_latest_version %}
{% endif %}

.. tab-set::

    {% if data.enable_overview %}
    .. tab-item:: Overview
       :name: overview-tab

       .. container:: table-of-contents

          .. container::
             :name: overview-table-of-contents

             |nbsp|

       .. include:: _overview_1.md
          :parser: myst_parser.sphinx_

       .. rubric:: Access the data
          :name: access-the-data

       For help accessing the data, see the 'Access' tab.

       {% if is_latest_version and has_access_data %}
       .. container:: card-list icons
          :name: access-the-data-cards

          .. grid:: 2 2 3 5
             :gutter: 3

             {% for item in valid_maps %}
             .. grid-item-card:: :fas:`map-location-dot`
                :link: {{ item.link }}
                :link-alt: {{ map_label }}

                {{ item.name or map_default_name }}
             {% endfor %}

             {% for item in valid_explorers %}
             .. grid-item-card:: :fas:`magnifying-glass`
                :link: {{ item.link }}
                :link-alt: {{ explorer_label }}

                {{ item.name or explorer_default_name }}
             {% endfor %}

             {% for item in valid_data %}
             .. grid-item-card:: :fas:`database`
                :link: {{ item.link }}
                :link-alt: {{ data_label }}

                {{ item.name or data_default_name }}
             {% endfor %}

             {% for item in valid_code_samples %}
             .. grid-item-card:: :fas:`laptop-code`
                :link: {{ item.link }}
                :link-alt: {{ code_sample_label }}

                {{ item.name or code_sample_default_name }}
             {% endfor %}

             {% for item in valid_web_services %}
             .. grid-item-card:: :fas:`globe`
                :link: {{ item.link }}
                :link-alt: {{ web_service_label }}

                {{ item.name or web_service_default_name }}
             {% endfor %}
       {%- endif %}

       .. rubric:: Key details
          :name: key-details

       .. list-table::
          :name: key-details-table

          {% if data.parent_products.name and data.parent_products.link %}
          * - **Parent product(s)**
            - `{{ data.parent_products.name }} <{{ data.parent_products.link }}>`_
          {%- endif %}
          {%- if data.collection.name and data.collection.link %}
          * - **Collection**
            - `{{ data.collection.name }} <{{ data.collection.link }}>`_
          {%- elif data.collection.name %}
          * - **Collection**
            - {{ data.collection.name }}
          {%- endif %}
          {%- if valid_dois %}
          * - **{{ dois_label }}**
            - {% for item in valid_dois %}`{{ item }} <https://doi.org/{{ item }}>`_{% if not loop.last %}, {% endif %}{% endfor %}
          {%- endif %}
          {%- if valid_ecat %}
          * - **{{ ecat_label }}**
            - {% for item in valid_ecat %}`{{ item }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ item }}>`_{% if not loop.last %}, {% endif %}{% endfor %}
          {%- endif %}
          {%- if data.published %}
          * - **Last updated**
            - {{ data.published }}
          {%- endif %}
          {%- if valid_tags %}
          * - **Tags**
            - {{ valid_tags | join(", ") }}
          {%- endif %}

       .. include:: _overview_2.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if data.enable_access %}
    .. tab-item:: Access
       :name: access-tab

       .. container:: table-of-contents

          .. container::
             :name: access-table-of-contents

             |nbsp|

       .. rubric:: Access the data
          :name: access-the-data-2

       {% if is_latest_version and has_access_data %}
       .. list-table::
          :name: access-table

          {% if valid_maps %}
          * - **{{ map_label }}**
            - {% for item in valid_maps %}
              * `{{ item.name or map_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps </guides/setup/dea_maps>`_.
          {% endif %}

          {% if valid_explorers %}
          * - **{{ explorer_label }}**
            - {% for item in valid_explorers %}
              * `{{ item.name or explorer_default_name }} <{{ item.link }}>`_
              {% endfor %}
            -
          {% endif %}

          {% if valid_data %}
          * - **{{ data_label }}**
            - {% for item in valid_data %}
              * `{{ item.name or data_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </guides/about/faq#how-do-i-download-data-from-dea>`_.
          {% endif %}

          {% if valid_code_samples %}
          * - **{{ code_sample_label }}**
            - {% for item in valid_code_samples %}
              * `{{ item.name or code_sample_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `connect to the DEA Sandbox </guides/setup/Sandbox/sandbox>`_.
          {% endif %}

          {% if valid_web_services %}
          * - **{{ web_service_label }}**
            - {% for item in valid_web_services %}
              * `{{ item.name or web_service_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `connect to DEA's web services </guides/setup/gis/README>`_.
          {% endif %}
       {% elif not is_latest_version %}
       You may find data source links in the `latest version of the product <{{ data.latest_version_link }}>`_.
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

       .. include:: _access.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if data.enable_details %}
    .. tab-item:: Details
       :name: details-tab

       .. container:: table-of-contents

          .. container::
             :name: details-table-of-contents

             |nbsp|

       .. include:: _details.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if data.enable_quality %}
    .. tab-item:: Quality
       :name: quality-tab

       .. container:: table-of-contents

          .. container::
             :name: quality-table-of-contents

             |nbsp|

       .. include:: _quality.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if data.enable_history %}
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
    {% endif %}

    {% if data.enable_credits %}
    .. tab-item:: Credits
       :name: credits-tab

       .. container:: table-of-contents

          .. container::
             :name: credits-table-of-contents

             |nbsp|
    
       .. include:: _credits.md
          :parser: myst_parser.sphinx_
    {% endif %}

.. raw:: html

   <script type="text/javascript" src="/_static/scripts/tocbot.min.js"></script>
   <script type="text/javascript" src="/_static/scripts/tocbot-data-product.js" /></script>
   <script type="text/javascript" src="/_static/scripts/access-cards-tooltips.js" /></script>
