{% set data = load('_data.yaml') %}
{% set bands = load('_bands.yaml') %}

{% set is_latest_version = data.is_latest_version %}

{% set valid_maps = data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = data.data | selectattr("link",  "!=", None) | list %}
{% set valid_explorers = data.explorers | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = data.code_examples | selectattr("link",  "!=", None) | list %}
{% set valid_custom = data.custom | selectattr("icon",  "!=", None) | selectattr("link",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_files = data.files | selectattr("link",  "!=", None) | list %}
{% set valid_old_versions = data.old_versions | selectattr("slug",  "!=", None) | selectattr("version",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_product_types = [data.product_type, data.spatial_data_type] | select("!=", None) | list %}
{% set valid_product_ids = data.product_ids | select("!=", None) | list %}
{% set valid_custom_citations = data.custom_citations | select("!=", None) | list %}
{% set valid_tags = data.tags | select("!=", None) | list %}

{% set map_label = "See it on a map" %}
{% set explorer_label = "Explore data availability" %}
{% set data_label = "Get the data online" %}
{% set web_service_label = "Get via web service" %}
{% set code_sample_label = "Code sample" %}

{% set map_default_name = "DEA Maps" %}
{% set data_default_name = "DEA Data" %}
{% set explorer_default_name = "Data Explorer" %}
{% set web_service_default_name = "Web service" %}
{% set code_sample_default_name = "Code sample" %}

{% set has_access_data = valid_maps or valid_data or valid_explorers or valid_web_services or valid_code_samples or valid_custom %}
{% set has_key_details = (data.licence.name and data.licence.link) or data.doi or data.ecat %}

{% set page_title = data.title if is_latest_version else data.version + ": " + data.title %}

{% set product_ids_label = "Product IDs" if valid_product_ids | length > 1 else "Product ID" %}
{% set product_types_label = "Product types" if valid_product_types | length > 1 else "Product type" %}

.. |nbsp| unicode:: 0xA0
   :trim:

.. rst-class:: product-page

======================================================================================================================================================
{{ page_title }}
======================================================================================================================================================

.. container:: showcase-panel product-header bg-gradient-primary

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
      {%- if data.time_span %}
      {%- if data.time_span.start and data.time_span.end %}
      :Time span: {{ data.time_span.start }} – {{ data.time_span.end }}
      {%- elif data.time_span.start  %}
      :Starts at: {{ data.time_span.start }}
      {%- elif data.time_span.end  %}
      :Ends at: {{ data.time_span.end }}
      {%- endif %}
      {%- endif %}
      :Update frequency: {{ data.update_frequency }}
      {%- if data.next_update %}
      :Next update: {{ data.next_update }}
      {%- endif %}
      {%- if valid_product_ids %}
      :{{ product_ids_label }}: {{ valid_product_ids | join(", ") }}
      {%- endif %}

   .. container::

      .. image:: {{ data.header_image or "/_files/pages/dea-hero.jpg" }}
         :class: no-gallery

.. container::
   :name: notifications

   .. admonition:: External product
      :class: note
   
      This dataset is developed by an external party, and is not a DEA product.

      {% if data.dataset_website %}
      {% if data.dataset_website.link %}
      `{{ data.dataset_website.custom_name or "View the external dataset website" }} <{{ data.dataset_website.link }}>`_
      {% endif %}
      {% endif %}

{% if not is_latest_version %}
{% endif %}

.. tab-set::

    {% if data.enable_overview %}
    .. tab-item:: Overview
       :name: overview

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _overview_1.md
          :parser: myst_parser.sphinx_

       {% if has_access_data %}
       .. rubric:: Access the data
          :name: access-the-data
          :class: h2

       For help accessing the data, see the `Access tab <./?tab=access>`_.

       .. container:: card-list icons
          :name: access-the-data-cards

          .. grid:: 2 2 3 5
             :gutter: 3

             {% if data.dataset_website %}
             {% if data.dataset_website.link %}
             .. grid-item-card:: :fas:`arrow-up-right-from-square`
                :link: {{ data.dataset_website.link }}
                :link-alt: The website of the external dataset.

                {{ data.dataset_website.custom_name or "View the external dataset website" }}
             {% endif %}
             {% endif %}

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

             {% for item in valid_custom %}
             .. grid-item-card:: :fas:`{{ item.icon }}`
                :link: {{ item.link }}
                :link-alt: {{ item.label or "" }}
                :class-card: {{ item.class }}

                {{ item.name }}
             {% endfor %}
       {%- endif %}

       {% if has_key_details %}
       .. rubric:: Key details
          :name: key-details
          :class: h2

       .. list-table::
          :name: key-details-table

          {%- if data.doi and data.ecat %}
          * - **DOI**
            - `{{ data.doi }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ data.ecat }}>`_
          {% elif data.doi %}
          * - **DOI**
            - `{{ data.doi }} <https://doi.org/{{ data.doi }}>`_
          {% elif data.ecat %}
          * - **Persistent ID**
            - `{{ data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ data.ecat }}>`_
          {%- endif %}
          {% if data.licence %}
          {% if data.licence.name and data.licence.link %}
          * - **Licence**
            - `{{ data.licence.name }} <{{ data.licence.link }}>`_
          {% endif %}
          {% endif %}
       {%- endif %}

       {% if data.citations %}
       {% if data.citations.data_citation or data.citations.paper_citation %}
       .. rubric:: Cite this product
          :name: citations
          :class: h2

       .. list-table::
          :name: citation-table

          {% if data.citations.data_citation %}
          * - **Data citation**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ data.citations.data_citation }}
          {%- endif %}
          {% if data.citations.paper_citation %}
          * - **Paper citation**
            - .. code-block:: text
                 :class: citation-table-citation

                 {{ data.citations.paper_citation }}
          {%- endif %}
          {% for citation in valid_custom_citations %}
          * - **{{ citation.name }}**
            - .. code-block:: text
                 :class: citation-table-citation

                 {{ citation.citation }}
          {% endfor %}
       {%- endif %}
       {%- endif %}

       .. {%- if valid_tags %}
       .. .. tags:: {{ valid_tags | join(", ") }}
       .. {%- endif %}

    {% endif %}

    {% if data.enable_details %}
    .. tab-item:: Details
       :name: details

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       {% for product in bands.products %}
       .. list-table::
          :header-rows: 1

          * - Band name
            - Aliases
            - Resolution
            - CRS
            - Nodata
            - Data type
            - Description
          {% for band in product.bands %}
          * - {{ band.name }}
            - {{ band.aliases|join(', ') }}
            - {{ band.resolution }}
            - {{ band.crs }}
            - {{ band.nodata }}
            - {{ band.type }}
            - {{ band.description }}
          {% endfor %}
       {% endfor %}

       .. include:: _details.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if data.enable_access %}
    .. tab-item:: Access
       :name: access

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. rubric:: Access the data
          :name: access-the-data-2
          :class: h2

       {% if has_access_data %}
       .. list-table::
          :name: access-table

          {% if valid_maps %}
          * - **{{ map_label }}**
            - {% for item in valid_maps %}
              * `{{ item.name or map_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps </guides/setup/dea_maps/>`_
          {% endif %}

          {% if valid_explorers %}
          * - **{{ explorer_label }}**
            - {% for item in valid_explorers %}
              * `{{ item.name or explorer_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Explorer </setup/explorer_guide/>`_
          {% endif %}

          {% if valid_data %}
          * - **{{ data_label }}**
            - {% for item in valid_data %}
              * `{{ item.name or data_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </guides/about/faq/#download-dea-data>`_
          {% endif %}

          {% if valid_code_samples %}
          * - **{{ code_sample_label }}**
            - {% for item in valid_code_samples %}
              * `{{ item.name or code_sample_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Sandbox </guides/setup/Sandbox/sandbox/>`_
          {% endif %}

          {% if valid_web_services %}
          * - **{{ web_service_label }}**
            - {% for item in valid_web_services %}
              * `{{ item.name or web_service_default_name }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA's web services </guides/setup/gis/README/>`_
          {% endif %}

          {% for item in valid_custom %}
          * - **{{ item.label or "" }}**
            - * `{{ item.name }} <{{ item.link }}>`_
            - {{ item.description or "" }}
          {% endfor %}
       {% else %}
       There are no data source links available at the present time.
       {% endif %}

       {% if valid_files %}

       .. rubric:: Additional files
          :name: additional-files
          :class: h2

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

.. raw:: html

   <script type="text/javascript" src="/_static/scripts/access-cards-tooltips.js" /></script>
   <script type="text/javascript" src="/_static/scripts/citation-access-date.js" /></script>
