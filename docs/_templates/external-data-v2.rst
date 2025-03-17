{% set page = {
   "data": load('_data.yaml'),
   "tables": load('_tables.yaml'),
} %}

{% set valid_maps = page.data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = page.data.data | selectattr("link",  "!=", None) | list %}
{% set valid_external_data = page.data.external_data_page if page.data.external_data_page and page.data.external_data_page.link %}
{% set valid_explorers = page.data.explorers | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = page.data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = page.data.code_examples | selectattr("link",  "!=", None) | list %}
{% set valid_custom = page.data.custom | selectattr("icon",  "!=", None) | selectattr("link",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_product_types = [page.data.lineage_type, page.data.spatial_data_type] | select("!=", None) | list %}
{% set valid_product_ids = page.data.product_ids | select("!=", None) | list %}
{% set valid_custom_citations = page.data.custom_citations | select("!=", None) | list %}
{% set valid_tags = page.data.tags + ['external_data'] | select("!=", None) | list %}
{% set valid_bands = page.tables.bands_table | selectattr("name",  "!=", None) | list %}
{% set product_ids_list = page.data.product_ids | select("!=", None) | list %}
{% set product_ids_list_text = product_ids_list | join(", ") %}

{% set external_data_label = "Go to the external data page" %}
{% set map_label = "See it on a map" %}
{% set explorer_label = "Explore data availability" %}
{% set data_label = "Get the data online" %}
{% set web_service_label = "Get via web service" %}
{% set code_sample_label = "Code sample" %}

{% set external_data_default_name = "External data page" %}
{% set map_default_name = "DEA Maps" %}
{% set data_default_name = "DEA Data" %}
{% set explorer_default_name = "Data Explorer" %}
{% set web_service_default_name = "Web service" %}
{% set code_sample_default_name = "Code sample" %}

{% set coordinate_reference_system_terms = {
   "EPSG:3577": "`GDA94 / Australian Albers (EPSG:3577) <https://epsg.org/crs_3577/GDA94-Australian-Albers.html>`_",
   "EPSG:4326": "`WGS 84 (EPSG:4326) <https://epsg.org/crs_4326/WGS-84.html>`_",
   "MULTIPLE_UTM": "Multiple UTM zone CRSs",
} %}

{% set has_access_data = valid_external_data or valid_maps or valid_data or valid_explorers or valid_web_services or valid_code_samples or valid_custom %}
{% set has_key_details = (page.data.licence_name and page.data.licence_link) or page.data.doi or page.data.ecat %}

{% set product_ids_label = "Product IDs" if valid_product_ids | length > 1 else "Product ID" %}
{% set product_types_label = "Types" if valid_product_types | length > 1 else "Type" %}

{% set none_text = "None" %}
{% set not_available_text = "N/A" %}

{% set coordinate_reference_system_term = coordinate_reference_system_terms.get(page.data.coordinate_reference_system, page.data.coordinate_reference_system) %}

{% set bands_table_list = page.tables.bands_table | selectattr("name", "!=", None) | list %}
{% set bands_count = bands_table_list | length %}

{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

{# Tags list component #}

{% set tags_list_component -%}
{% for tag in valid_tags %}`{{tag}} </search/?q=Tag+{{tag}}>`_{% if not loop.last %}, {% endif %}{% endfor %}
{%- endset %}

.. role:: raw-html(raw)
   :format: html

.. rst-class:: product-page

======================================================================================================================================================
{{ page.data.title }}
======================================================================================================================================================

.. container:: showcase-panel product-header bg-gradient-primary

   .. container::

      .. rubric:: {{ page.data.title }}

      {% if valid_product_ids and page.data.enable_specifications %}
      `{{ valid_product_ids | join(", ") }} <./?tab=specifications>`_
      {%- elif valid_product_ids %}
      {{ valid_product_ids | join(", ") }}
      {%- else %}
      External data
      {%- endif %}

      {% if valid_product_types %}
      :{{ product_types_label }}: {{ valid_product_types | join(", ") }}
      {%- endif %}
      {%- if page.data.temporal_coverage %}
      {%- if page.data.temporal_coverage.custom %}
      :Coverage: {{ page.data.temporal_coverage.custom }}
      {%- elif page.data.temporal_coverage.start and page.data.temporal_coverage.end %}
      :Coverage: {{ page.data.temporal_coverage.start }} to {{ page.data.temporal_coverage.end }}
      {%- elif page.data.temporal_coverage.start  %}
      :Coverage start: {{ page.data.temporal_coverage.start }}
      {%- elif page.data.temporal_coverage.end  %}
      :Coverage end: {{ page.data.temporal_coverage.end }}
      {%- endif %}
      {%- endif %}
      :Produced by: {{ page.data.external_party }}

   .. container::

      .. image:: {{ page.data.header_image or "/_files/default/dea-earth-thumbnail.jpg" }}
         :class: no-gallery

.. container::
   :name: notifications

   .. admonition:: External data
      :class: note external-data
   
      This data product is produced by an external party and is not a DEA product. DEA provides this data without modifications except where needed to make it compatible with our systems.

      {% if valid_external_data %}
      {% if valid_external_data.custom_label %}
      `{{ valid_external_data.custom_label }} <{{ valid_external_data.link }}>`_
      {% else %}
      `{{ external_data_label }} ({{ page.data.external_party }}) <{{ valid_external_data.link }}>`_
      {% endif %}
      {% endif %}

.. tab-set::

    {% if page.data.enable_overview %}
    .. tab-item:: Overview
       :name: overview

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _overview.md
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

             {% if valid_external_data %}
             .. grid-item-card:: :fas:`person-walking-arrow-right`
                :link: {{ valid_external_data.link }}
                :link-alt: {{ external_data_default_name }}

                {{ valid_external_data.custom_label or external_data_label }}
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
       .. rubric:: Key specifications
          :name: key-specifications
          :class: h2

       {% if page.data.enable_specifications %}
       For more specifications, see the `Specifications tab <./?tab=specifications>`_.
       {% endif %}

       .. list-table::
          :name: key-specifications-table

          {% if page.data.long_title %}
          * - **Long name**
            - {{ page.data.long_title }}
          {%- endif %}
          {% if bands_table_list and bands_count >= 3 %}
          * - **Bands**
            - `{{ bands_count }} bands of data ({{ bands_table_list[0].name }}, {{ bands_table_list[1].name }}, and more) <./?tab=specifications>`_
          {%- elif bands_table_list and bands_count == 2 %}
          * - **Bands**
            - `{{ bands_count }} bands of data ({{ bands_table_list[0].name }} and {{ bands_table_list[1].name }}) <./?tab=specifications>`_
          {%- elif bands_table_list and bands_count == 1 %}
          * - **Bands**
            - `Single band of data ({{ bands_table_list[0].name }}) <./?tab=specifications>`_
          {%- endif %}
          {%- if page.data.doi and page.data.ecat %}
          * - **DOI**
            - `{{ page.data.doi }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
          {%- elif page.data.doi %}
          * - **DOI**
            - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
          {%- elif page.data.ecat %}
          * - **Persistent ID**
            - `{{ page.data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
          {%- endif %}
          * - **Tags**
            - {{ tags_list_component }}
          {%- if page.data.licence_name and page.data.licence_link %}
          * - **Licence**
            - `{{ page.data.licence_name }} <{{ page.data.licence_link }}>`_
          {% elif page.data.licence_name %}
          * - **Licence**
            - {{ page.data.licence_name }}
          {%- endif %}
       {%- endif %}

       {% if page.data.citations %}
       {% if page.data.citations.data_citation or page.data.citations.paper_citation %}
       .. rubric:: Cite this product
          :name: citations
          :class: h2

       .. list-table::
          :name: citation-table

          {% if page.data.citations.data_citation %}
          * - **Data citation**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ page.data.citations.data_citation }}
          {%- endif %}
          {% if page.data.citations.paper_citation %}
          * - **Paper citation**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ page.data.citations.paper_citation }}
          {%- endif %}
          {% for citation in valid_custom_citations %}
          * - **{{ citation.name }}**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ citation.citation }}
          {% endfor %}
       {%- endif %}
       {%- endif %}

    {% endif %}

    {% if page.data.enable_specifications %}
    .. tab-item:: Specifications
       :name: specifications

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       {% if product_ids_list %}
       {% if product_ids_list | length > 1 %}
       .. rubric:: Product IDs
          :name: product-id
          :class: h2

       The Product IDs are {% for product_id in product_ids_list %}{%- if loop.last and loop.index > 1 %}, and {% elif loop.index > 1 %}, {% endif -%}``{{ product_id }}``{% endfor %}. These IDs are used to `load data from the Open Data Cube (ODC) <load_data_odc_>`_, for example ``dc.load(product="{{ product_ids_list[0] }}", ...)``
       {%- else %}
       .. rubric:: Product ID
          :name: product-id
          :class: h2

       The Product ID is ``{{ product_ids_list[0] }}``. This ID is used to `load data from the Open Data Cube (ODC) <load_data_odc_>`_, for example ``dc.load(product="{{ product_ids_list[0] }}", ...)``
       {%- endif %}

       .. _load_data_odc: /notebooks/Beginners_guide/04_Loading_data/
       {%- endif %}

       {% if valid_bands %}
       .. rubric:: Bands
          :name: bands
          :class: h2

       Bands are distinct layers of data within a product that can be loaded using the Open Data Cube (on the `DEA Sandbox <dea_sandbox_>`_ or `NCI <nci_>`_) or DEA's `STAC API <stac_api_>`_.

       .. _dea_sandbox: https://knowledge.dea.ga.gov.au/guides/setup/Sandbox/sandbox/
       .. _nci: https://knowledge.dea.ga.gov.au/guides/setup/NCI/basics/
       .. _stac_api: https://knowledge.dea.ga.gov.au/guides/setup/gis/stac/

       .. list-table::
          :header-rows: 1

          * - 
            - Type
            - Units
            - Resolution
            - Nodata
            - Aliases
            - Description
          {% for band in valid_bands %}
          * - **{{ band.name }}**
            - {{ band.type or not_available_text }}
            - {{ band.units or none_text }}
            - {{ band.resolution or not_available_text }}
            - {{ band.nodata }}
            - {{ band.aliases|join(', ') if band.aliases else none_text }}
            - {{ band.description or none_text }}
          {% endfor %}

       .. raw:: html

          <br />

       {{ page.tables.bands_footnote if page.tables.bands_footnote }}
       {% endif %}

       .. rubric:: Product information
          :name: product-information
          :class: h2

       This metadata provides general information about the product.

       .. list-table::
          :name: product-information-table

          {% if product_ids_list %}
          * - **{{ product_ids_label }}**
            - {%- for product_id in product_ids_list %}
              | {{ product_id }}
              {%- endfor %}
            - Used to `load data from the Open Data Cube </notebooks/Beginners_guide/04_Loading_data/>`_.
          {%- endif %}
          {% if page.data.long_title %}
          * - **Long name**
            - {{ page.data.long_title }}
            - The full name or technical name of the product.
          {%- endif %}
          * - **External producer**
            - {{ page.data.external_party }}
            - The external party that produces this data.
          {% if valid_product_types %}
          * - **{{ product_types_label }}**
            - {{ valid_product_types | join(", ") }}
            - This may specify the spatial type, lineage type, or both.
          {%- endif %}
          {%- if page.data.temporal_coverage.custom %}
          * - **Temporal coverage**
            - {{ page.data.temporal_coverage.custom }}
            - The time span for which data is available.
          {%- elif page.data.temporal_coverage.start and page.data.temporal_coverage.end %}
          * - **Temporal coverage**
            - {{ page.data.temporal_coverage.start }} to {{ page.data.temporal_coverage.end }}
            - The time span for which data is available.
          {%- elif page.data.temporal_coverage.start %}
          * - **Temporal coverage**
            - Since {{ page.data.temporal_coverage.start }}
            - The time span for which data is available.
          {%- elif page.data.temporal_coverage.end %}
          * - **Temporal coverage**
            - Until {{ page.data.temporal_coverage.end }}
            - The time span for which data is available.
          {%- endif %}
          {% if page.data.coordinate_reference_system %}
          * - **Coordinate Reference System (CRS)**
            - {{ coordinate_reference_system_term }}
            - The method of mapping spatial data to the Earth's surface.
          {%- endif %}
          {%- if page.data.doi %}
          * - **DOI**
            - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
            - The Digital Object Identifier.
          {%- endif %}
          {%- if page.data.ecat %}
          * - **Catalogue ID**
            - `{{ page.data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
            - The Data and Publications catalogue (eCat) ID.
          {%- endif %}
          {%- if page.data.licence_name and page.data.licence_link %}
          * - **Licence**
            - `{{ page.data.licence_name }} <{{ page.data.licence_link }}>`_
            - The licence and copyright.
          {% elif page.data.licence_name %}
          * - **Licence**
            - {{ page.data.licence_name }}
            - The licence and copyright.
          {%- endif %}

       .. rubric:: Product categorisation
          :name: product-categorisation
          :class: h2

       This metadata describes how the product relates to other products.

       .. list-table::
          :name: product-categorisation-table

          * - **Tags**
            - {{ tags_list_component }}
    {% endif %}

    {% if page.data.enable_access %}
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

          {% if valid_external_data %}
          * - **{{ external_data_label }}**
            - 
              * `{{ valid_external_data.custom_label or external_data_default_name }} <{{ valid_external_data.link }}>`_
            - {{ valid_external_data.custom_description or "Learn more about the data from the external provider." }}
          {% endif %}

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

       .. include:: _access.md
          :parser: myst_parser.sphinx_
    {% endif %}

.. raw:: html

   <script type="text/javascript" src="/_static/scripts/access-cards-tooltips.js" /></script>
   <script type="text/javascript" src="/_static/scripts/citation-access-date.js" /></script>
