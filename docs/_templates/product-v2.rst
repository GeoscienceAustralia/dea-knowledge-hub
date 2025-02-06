{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
   "tables": load('_tables.yaml'),
} %}

{# Constant values #}

{% set max_page_title_length = 200 %}

{% set no_data_terms = {
   "dash": "\-",
} %}

{% set access_labels = {
   "map": "DEA Maps",
   "explorer": "DEA Explorer",
   "data": "Data sources",
   "web_service": "Web services",
   "code_sample": "Code examples",
} %}

{% set access_names = {
   "map": "See it on a map",
   "explorer": "Explore data availability",
   "data": "Get the data online",
   "web_service": "Get via web service",
   "code_sample": "View code examples",
} %}

{% set lineage_type_terms = {
   "BASELINE": "Baseline",
   "DERIVATIVE": "Derivative",
} %}

{% set spatial_data_type_terms = {
   "RASTER": "Raster",
   "VECTOR": "Vector",
} %}

{% set data_update_frequency_terms = {
   "AS_NEEDED": "As needed",
   "DAILY": "Daily",
   "WEEKLY": "Weekly",
   "MONTHLY": "Monthly",
   "YEARLY": "Yearly",
   "2_YEARS": "Every 2 years",
   "10_MIN": "Every 10 minutes",
} %}

{% set data_update_activity_terms = {
   "ONGOING": "Ongoing",
   "NO_UPDATES": "No further updates",
   "DEVELOPMENT": "Awaiting development",
   "PAUSED": "Currently paused",
} %}

{% set coordinate_reference_system_terms = {
   "EPSG:3577": "GDA94 / Australian Albers (EPSG:3577)",
} %}

{# Macros #}

{% macro format_version_number(version_number) -%} {# If the version number starts with a number, add a 'v' to it e.g. "v1.0.0". #}
{%- if (version_number|string)[0].isdigit() -%}
{{ "v" ~ version_number }}
{%- else -%}
{{ version_number }}
{%- endif -%}
{%- endmacro %}

{# Computed values #}

{% set access_links_maps_list = page.data.access_links_maps | selectattr("link", "!=", None) | list %}

{% set access_links_data_list = page.data.access_links_data | selectattr("link", "!=", None) | list %}

{% set access_links_explorers_list = page.data.access_links_explorers | selectattr("link", "!=", None) | list %}

{% set access_links_web_services_list = page.data.access_links_web_services | selectattr("link", "!=", None) | list %}

{% set access_links_code_samples_list = page.data.access_links_code_examples | selectattr("link", "!=", None) | list %}

{% set access_links_custom_list = page.data.access_links_custom | selectattr("icon", "!=", None) | selectattr("link", "!=", None) | selectattr("name", "!=", None) | list %}

{% set previous_versions_list = page.data.previous_versions | selectattr("slug", "!=", None) | selectattr("version_number", "!=", None) | selectattr("name", "!=", None) | list %}

{% set product_ids_list = page.data.product_ids | select("!=", None) | list %}

{% set product_ids_list_text = product_ids_list | join(", ") %}

{% set citations_custom_list = page.data.citations_custom | select("!=", None) | list %}

{% set tags_list = page.data.tags | select("!=", None) | list %}

{% set parent_products_list = page.data.parent_products | selectattr("name", "!=", None) | list %}

{% set collections_list = page.data.collections | selectattr("name", "!=", None) | list %}

{% set bands_table_list = page.tables.bands_table | selectattr("name", "!=", None) | list %}

{% set bands_count = bands_table_list | length %}

{% set layers_table_list = page.tables.layers_table | selectattr("name", "!=", None) | list %}

{% set layers_count = layers_table_list | length %}

{% set page_title = page.data.short_name if page.data.is_latest_version else format_version_number(page.data.version_number) ~ ". " ~ page.data.short_name %}

{% set display_title = page.data.short_name if page.data.is_latest_version else page.data.short_name ~ " " ~ format_version_number(page.data.version_number) %}

{% set product_ids_label = "Product IDs" if product_ids_list | length > 1 else "Product ID" %}

{% set parent_products_label = "Parent products" if parent_products_list | length > 1 else "Parent product" %}

{% set collections_label = "Collections" if collections_list | length > 1 else "Collection" %}

{% set currency_report_url = "https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1#:~:text=" ~ (page.data.short_name | urlencode) %}

{% set lineage_type = lineage_type_terms.get(page.data.lineage_type, page.data.lineage_type) %}

{% set spatial_data_type = spatial_data_type_terms.get(page.data.spatial_data_type, page.data.spatial_data_type) %}

{% set product_types_list = [lineage_type, spatial_data_type] | select("!=", None) | list %}

{% set data_update_frequency = data_update_frequency_terms.get(page.data.data_update_frequency, page.data.data_update_frequency) %}

{% set data_update_activity = data_update_activity_terms.get(page.data.data_update_activity, page.data.data_update_activity) %}

{% set coordinate_reference_system_term = coordinate_reference_system_terms.get(page.data.coordinate_reference_system, page.data.coordinate_reference_system) %}

{% set is_frequency_ongoing = data_update_activity == data_update_activity_terms.ONGOING %}

{% set is_cadence_yearly = data_update_frequency == data_update_frequency_terms.YEARLY %}

{% set is_frequency_multiple_words = data_update_frequency.split(" ") | length > 1 %}

{% set has_access_data = access_links_maps_list or access_links_data_list or access_links_explorers_list or access_links_web_services_list or access_links_code_samples_list or access_links_custom_list %}

{# Parent products component #}

{% set parent_products_list_component -%}
{% for parent_product in parent_products_list %}{% if parent_product.link %}`{{ parent_product.name }} <{{ parent_product.link }}>`_{% else %}{{ parent_product.name }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}
{%- endset %}

{# Collections component #}

{% set collections_list_component -%}
{% for collection in collections_list %}{% if collection.link %}`{{ collection.name }} <{{ collection.link }}>`_{% else %}{{ collection.name }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}
{%- endset %}

{# Tags list component #}

{% set tags_list_component -%}
{% for tag in tags_list %}`{{tag}} </search/?q=Tag+{{tag}}>`_{% if not loop.last %}, {% endif %}{% endfor %}
{%- endset %}

{# Restructured Text head component #}

{% set rst_head_component %}
.. role:: raw-html(raw)
   :format: html

.. rst-class:: product-page
{% endset %}

{# SEO head component #}

{% set seo_head_component %}
{% if page.data.meta_description %}
.. meta::
   :description: {{ page.data.meta_description }}
{%- endif %}
{% endset %}

{# Page title component #}

{% set page_title_component %}
{{ "=" * max_page_title_length }}
{{ page_title | truncate(max_page_title_length) }}
{{ "=" * max_page_title_length }}
{% endset %}

{# HTML end scripts component #}

{% set html_end_scripts_component %}
.. raw:: html

   <script type="text/javascript" src="/_static/scripts/access-cards-tooltips.js" /></script>
   <script type="text/javascript" src="/_static/scripts/citation-access-date.js" /></script>
{% endset %}

{# Header panel component #}

{% set header_panel_component %}
.. container:: showcase-panel product-header bg-gradient-primary

   .. container::

      .. rubric:: {{ display_title }}

      {% if product_ids_list and page.data.enable_specifications %}
      `{{ product_ids_list_text }} <./?tab=specifications>`_
      {%- elif product_ids_list %}
      {{ product_ids_list_text }}
      {%- elif spatial_data_type == spatial_data_type_terms.VECTOR %}
      Vector product
      {%- else %}
      Data product
      {%- endif %}

      {% if page.data.is_latest_version and page.data.enable_history %}
      :Version: `{{ page.data.version_number }} <./?tab=history>`_
      {%- elif page.data.is_latest_version %}
      :Version: {{ page.data.version_number }}
      {%- else %}
      :Version: {{ page.data.version_number }} (`See latest version <{{ page.data.latest_version_link }}>`_)
      {%- endif %}
      :Type: {{ product_types_list | join(", ") }}
      {%- if page.data.resolution %}
      :Resolution: {{ page.data.resolution }}
      {%- endif %}
      {%- if page.data.temporal_coverage_custom %}
      :Coverage: {{ page.data.temporal_coverage_custom }}
      {%- elif page.data.temporal_coverage_start and page.data.temporal_coverage_end %}
      :Coverage: {{ page.data.temporal_coverage_start }} to {{ page.data.temporal_coverage_end }}
      {%- elif page.data.temporal_coverage_start %}
      :Coverage start: {{ page.data.temporal_coverage_start }}
      {%- elif page.data.temporal_coverage_end %}
      :Coverage end: {{ page.data.temporal_coverage_end }}
      {%- endif %}
      {%- if is_frequency_ongoing and is_frequency_multiple_words %}
      :Data updates: {{ data_update_frequency }}, {{ data_update_activity }}
      {%- elif is_frequency_ongoing %}
      :Data updates: {{ data_update_frequency }} frequency, {{ data_update_activity }}
      {%- elif is_frequency_multiple_words %}
      :Data updates: {{ data_update_activity }} (Previously: {{ data_update_frequency }})
      {%- else %}
      :Data updates: {{ data_update_activity }} (Previously: {{ data_update_frequency }} frequency)
      {%- endif %}

   .. container::

      .. image:: {{ page.data.header_image or "/_files/default/dea-earth-thumbnail.jpg" }}
         :class: no-gallery
{% endset %}

{# Notification section component #}

{% set notifications_section_component %}
.. container::
   :name: notifications

   {% if not page.data.is_latest_version %}
   .. admonition:: Old version
      :class: note
   
      This is an old version of the product. See the `latest version <{{ page.data.latest_version_link }}>`_.

   {% endif %}
   {% if page.data.is_provisional %}
   .. admonition:: Provisional product
      :class: note

      This is a `provisional product </guides/reference/dataset_maturity_guide/>`_, meaning it has not yet passed quality control and/or been finalised for release.

   {% endif %}
{% endset %}

{# Overview tab component #}

{% set overview_tab_component %}
{% if page.data.enable_overview %}
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

   {% if page.data.enable_access %}
   For help accessing the data, see the `Access tab <./?tab=access>`_.
   {% endif %}

   .. container:: card-list icons
      :name: access-the-data-cards

      .. grid:: 2 2 3 5
         :gutter: 3

         {% for item in access_links_maps_list %}
         .. grid-item-card:: :fas:`map-location-dot`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.map }}

            {{ item.name or access_names.map }}
         {% endfor %}

         {% for item in access_links_explorers_list %}
         .. grid-item-card:: :fas:`magnifying-glass`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.explorer }}

            {{ item.name or access_names.explorer }}
         {% endfor %}

         {% for item in access_links_data_list %}
         .. grid-item-card:: :fas:`database`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.data }}

            {{ item.name or access_names.data }}
         {% endfor %}

         {% for item in access_links_code_samples_list %}
         .. grid-item-card:: :fas:`laptop-code`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.code_sample }}

            {{ item.name or access_names.code_sample }}
         {% endfor %}

         {% for item in access_links_web_services_list %}
         .. grid-item-card:: :fas:`globe`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.web_service }}

            {{ item.name or access_names.web_service }}
         {% endfor %}

         {% for item in access_links_custom_list %}
         .. grid-item-card:: :fas:`{{ item.icon or "link" }}`
            :link: {{ item.link }}
            :link-alt: {{ item.label or "" }}
            :class-card: {{ item.class }}

            {{ item.name }}
         {% endfor %}
   {%- endif %}

   .. rubric:: Key specifications
      :name: key-specifications
      :class: h2

   {% if page.data.enable_specifications %}
   For more specifications, see the `Specifications tab <./?tab=specifications>`_.
   {% endif %}

   .. list-table::
      :name: key-specifications-table

      {% if page.data.full_technical_name %}
      * - **Technical name**
        - {{ page.data.full_technical_name }}
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
      {% if layers_table_list and layers_count >= 3 %}
      * - **Layers**
        - `{{ layers_count }} layers of data ({{ layers_table_list[0].name }}, {{ layers_table_list[1].name }}, and more). View their attribute fields. <./?tab=specifications>`_
      {%- elif layers_table_list and layers_count == 2 %}
      * - **Layers**
        - `{{ layers_count }} layers of data ({{ layers_table_list[0].name }} and {{ layers_table_list[1].name }}). View their attribute fields. <./?tab=specifications>`_
      {%- elif layers_table_list and layers_count == 1 %}
      * - **Layers**
        - `Single layer of data ({{ layers_table_list[0].name }}). View attribute fields. <./?tab=specifications>`_
      {%- endif %}
      {%- if page.data.doi %}
      * - **DOI**
        - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
      {%- elif page.data.ecat_id %}
      * - **Catalogue ID**
        - `{{ page.data.ecat_id }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat_id }}>`_
      {%- endif %}
      {% if page.data.is_currency_reported and is_cadence_yearly %}
      * - **Currency**
        - `See currency and the latest and next update dates <{{ currency_report_url }}>`_
      {% elif page.data.is_currency_reported %}
      * - **Currency**
        - `See currency and the latest update date <{{ currency_report_url }}>`_
      {%- endif %}
      {%- if parent_products_list %}
      * - **{{ parent_products_label }}**
        - {{ parent_products_list_component }}
      {%- endif %}
      {%- if collections_list %}
      * - **{{ collections_label }}**
        - {{ collections_list_component }}
      {%- endif %}
      {%- if tags_list %}
      * - **Tags**
        - {{ tags_list_component }}
      {%- endif %}
      {%- if page.data.licence_name and page.data.licence_link %}
      * - **Licence**
        - `{{ page.data.licence_name }} <{{ page.data.licence_link }}>`_
      {% elif page.data.licence_name %}
      * - **Licence**
        - {{ page.data.licence_name }}
      {%- endif %}

   {% if page.data.citation_data or page.data.citation_paper or page.data.citations_custom %}
   .. rubric:: Cite this product
      :name: citations
      :class: h2

   .. list-table::
      :name: citation-table

      {% if page.data.citation_data %}
      * - **Data citation**
        - .. code-block:: text
             :class: citation-table-citation citation-access-date

             {{ page.data.citation_data }}
      {%- endif %}
      {% if page.data.citation_paper %}
      * - **Paper citation**
        - .. code-block:: text
             :class: citation-table-citation

             {{ page.data.citation_paper }}
      {%- endif %}
      {% for citation in citations_custom_list %}
      * - **{{ citation.name }}**
        - .. code-block:: text
             :class: citation-table-citation

             {{ citation.citation }}
      {% endfor %}
   {%- endif %}

   .. include:: _overview_2.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Description tab component #}

{% set description_tab_component %}
{% if page.data.enable_description %}
.. tab-item:: Description
   :name: description

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   .. include:: _description.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Quality tab component #}

{% set quality_tab_component %}
{% if page.data.enable_quality %}
.. tab-item:: Quality
   :name: quality

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   .. include:: _quality.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Specifications tab component #}

{% set specifications_tab_component %}
{% if page.data.enable_specifications %}
.. tab-item:: Specifications
   :name: specifications

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   {% if bands_table_list %}
   .. rubric:: Bands
      :name: bands
      :class: h2

   Bands are distinct layers of data within a product that can be loaded using the Open Data Cube (on the `DEA Sandbox <dea_sandbox_>`_ or `NCI <nci_>`_) or DEA's `STAC API <stac_api_>`_.{{ " Note that the Coordinate Reference System (CRS) of these bands is {}.".format(coordinate_reference_system_term) if coordinate_reference_system_term }}{% if product_ids_list | length > 1 %} The products {{ product_ids_list_text }} contain the following bands.{%- elif product_ids_list %} The product {{ product_ids_list_text }} contains the following bands.{%- endif %}

   .. _dea_sandbox: https://knowledge.dea.ga.gov.au/guides/setup/Sandbox/sandbox/
   .. _nci: https://knowledge.dea.ga.gov.au/guides/setup/NCI/basics/
   .. _stac_api: https://knowledge.dea.ga.gov.au/guides/setup/gis/stac/

   .. list-table::
      :header-rows: 1
      :name: bands-table
      :class: margin-bottom-2em

      * - 
        - Type
        - Units
        - Resolution
        - No-data
        - Aliases
        - Description
      {% for band in bands_table_list %}
      * - **{{ band.name }}**
        - {{ band.type or no_data_terms.dash }}
        - {{ band.units or no_data_terms.dash }}
        - {{ band.resolution if band.resolution or band.resolution == 0 else no_data_terms.dash }}
        - {{ band.nodata if band.nodata or band.nodata == 0 else "" }}
        - {%- if band.aliases %}
          {%- for alias in band.aliases %}
          | {{ alias }}
          {%- endfor %}
          {%- else %}
          {{ no_data_terms.dash }}
          {%- endif %}
        - {{ band.description or no_data_terms.dash }}
      {% endfor %}

   {{ page.tables.bands_footnote if page.tables.bands_footnote }}
   {% endif %}

   {% if layers_table_list %}
   .. rubric:: Layers
      :name: layers
      :class: h2

   Vector products contain one or more distinct layers of data, and each layer can contain multiple attribute fields. The product {{ product_ids_list_text }} contains the following layers: {% for layer in layers_table_list %}`{{ layer.name }} <#{{ layer.name }}>`_{% if not loop.last %}, {% endif %}{% endfor %}.

   {% for layer in layers_table_list %}
   .. rubric:: {{ layer.name }}
      :name: {{ layer.name }}
      :class: h3

   {{ layer.description or no_data_terms.dash }}

   .. list-table::
      :header-rows: 1
      :name: layers-table
      :class: margin-bottom-2em

      * -
        - Type
        - Units
        - Description
      {% for attribute in layer.attributes %}
      * - **{{ attribute.name }}**
        - {{ attribute.type or no_data_terms.dash }}
        - {{ attribute.units or no_data_terms.dash }}
        - {{ attribute.description }}
      {% endfor %}
   {% endfor %}

   {{ page.tables.layers_footnote if page.tables.layers_footnote }}

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
      * - **Short name**
        - {{ page.data.short_name }}
        - The name that is commonly used to refer to the product.
      {% if page.data.full_technical_name %}
      * - **Technical name**
        - {{ page.data.full_technical_name }}
        - The full technical name that refers to the product and its specific provider, sensors, and collection.
      {%- endif %}
      {%- if page.data.is_latest_version and previous_versions_list | length > 0 and page.data.enable_history %} {# If at least one old version exists. #}
      * - **Version**
        - {{ page.data.version_number }}
        - The version number of the product. See the `History tab <./?tab=history>`_.
      {%- elif page.data.is_latest_version %}
      * - **Version**
        - {{ page.data.version_number }}
        - The version number of the product.
      {%- else %}
      * - **Version**
        - {{ page.data.version_number }}
        - This is an old version of the product. See the `latest version <{{ page.data.latest_version_link }}>`_.
      {%- endif %}
      {% if lineage_type == lineage_type_terms.DERIVATIVE %}
      * - **Lineage type**
        - {{ lineage_type }}
        - Derivative products are derived from other products.
      {%- elif lineage_type == lineage_type_terms.BASELINE %}
      * - **Lineage type**
        - {{ lineage_type }}
        - Baseline products are produced directly from satellite data.
      {%- else %}
      * - **Lineage type**
        - {{ lineage_type }}
        - Our standard lineage types are 'Baseline' and 'Derivative'.
      {%- endif %}
      {% if spatial_data_type == spatial_data_type_terms.RASTER %}
      * - **Spatial type**
        - {{ spatial_data_type }}
        - Raster data consists of a grid of pixels.
      {%- elif spatial_data_type == spatial_data_type_terms.VECTOR %}
      * - **Spatial type**
        - {{ spatial_data_type }}
        - Vector data consists of spatial polygons, lines, and points.
      {%- else %}
      * - **Spatial type**
        - {{ spatial_data_type }}
        - The most common spatial types are raster and vector.
      {%- endif %}
      {%- if coordinate_reference_system_term %}
      * - **Coordinate Reference System (CRS)**
        - {{ coordinate_reference_system_term }}
        - The mathematical method of assigning coordinates to locations on the Earth's surface.
      {%- endif %}
      {%- if page.data.resolution %}
      * - **Spatial resolution**
        - {{ page.data.resolution }}
        - The size of the pixels in the raster.
      {%- endif %}
      {%- if page.data.spatial_coverage %}
      * - **Spatial coverage**
        - {{ page.data.spatial_coverage }}
        - The spatial area for which data is available.
      {%- endif %}
      {%- if page.data.temporal_coverage_custom %}
      * - **Temporal coverage**
        - {{ page.data.temporal_coverage_custom }}
        - The time span for which data is available.
      {%- elif page.data.temporal_coverage_start and page.data.temporal_coverage_end %}
      * - **Temporal coverage**
        - {{ page.data.temporal_coverage_start }} to {{ page.data.temporal_coverage_end }}
        - The time span for which data is available.
      {%- elif page.data.temporal_coverage_start %}
      * - **Temporal coverage**
        - Since {{ page.data.temporal_coverage_start }}
        - The time span for which data is available.
      {%- elif page.data.temporal_coverage_end %}
      * - **Temporal coverage**
        - Until {{ page.data.temporal_coverage_end }}
        - The time span for which data is available.
      {%- endif %}
      {%- if is_frequency_ongoing %}
      * - **Update frequency**
        - {{ data_update_frequency }}
        - The expected frequency of data updates. Also called 'Temporal resolution'.
      {%- else %}
      * - **Update frequency**
        - {{ data_update_frequency }} (Inactive)
        - Previously, when data updates were active, this was their expected frequency. Also called 'Temporal resolution'.
      {%- endif %}
      * - **Update activity**
        - {{ data_update_activity }}
        - The activity status of data updates.
      {%- if page.data.is_currency_reported %}
      * - **Currency**
        - `See the Currency Report <{{ currency_report_url }}>`_
        - Currency is a measure based on data publishing and update frequency.
      {%- endif %}
      {%- if page.data.is_currency_reported and is_cadence_yearly %}
      * - **Latest and next update dates**
        - `See the Currency Report <{{ currency_report_url }}>`_
        - See Table B of the report.
      {% elif page.data.is_currency_reported %}
      * - **Latest update date**
        - `Currency Report <{{ currency_report_url }}>`_
        - See Table A of the report.
      {%- endif %}
      {%- if page.data.doi %}
      * - **DOI**
        - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
        - The Digital Object Identifier.
      {%- endif %}
      {%- if page.data.ecat_id %}
      * - **Catalogue ID**
        - `{{ page.data.ecat_id }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat_id }}>`_
        - The Data and Publications catalogue (eCat) ID.
      {%- endif %}
      {%- if page.data.licence_name %}
      * - **Licence**
        - {% if page.data.licence_link %}`{{ page.data.licence_name }} <{{ page.data.licence_link }}>`_{% else %}{{ page.data.licence_name }}{% endif %}
        - {% if page.data.enable_credits %}See the `Credits tab <./?tab=credits>`_.{% endif %}
      {%- endif %}

   .. rubric:: Product categorisation
      :name: product-categorisation
      :class: h2

   This metadata describes how the product relates to other DEA products.

   .. list-table::
      :name: product-categorisation-table

      {% if parent_products_list %}
      * - **{{ parent_products_label }}**
        - {{ parent_products_list_component }}
      {%- endif %}
      {%- if collections_list %}
      * - **{{ collections_label }}**
        - {{ collections_list_component }}
      {%- endif %}
      {%- if tags_list %}
      * - **Tags**
        - {{ tags_list_component }}
      {%- endif %}

{% endif %}
{% endset %}

{# Access tab component #}

{% set access_tab_component %}
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

      {% if access_links_maps_list %}
      * - **{{ access_labels.map }}**
        - {% for item in access_links_maps_list %}
          * `{{ item.name or access_names.map }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use DEA Maps </guides/setup/dea_maps/>`_.
      {% endif %}

      {% if access_links_explorers_list %}
      * - **{{ access_labels.explorer }}**
        - {% for item in access_links_explorers_list %}
          * `{{ item.name or access_names.explorer }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use the DEA Explorer </setup/explorer_guide/>`_.
      {% endif %}

      {% if access_links_data_list %}
      * - **{{ access_labels.data }}**
        - {% for item in access_links_data_list %}
          * `{{ item.name or access_names.data }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `access the data via AWS </guides/about/faq/#download-dea-data>`_.
      {% endif %}

      {% if access_links_code_samples_list %}
      * - **{{ access_labels.code_sample }}**
        - {% for item in access_links_code_samples_list %}
          * `{{ item.name or access_names.code_sample }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use the DEA Sandbox </guides/setup/Sandbox/sandbox/>`_.
      {% endif %}

      {% if access_links_web_services_list %}
      * - **{{ access_labels.web_service }}**
        - {% for item in access_links_web_services_list %}
          * `{{ item.name or access_names.web_service }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use DEA's web services </guides/setup/gis/README/>`_.
      {% endif %}

      {% for item in access_links_custom_list %}
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
{% endset %}

{# History tab component #}

{% set history_tab_component %}
{% if page.data.enable_history %}
.. tab-item:: History
   :name: history

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   {% if not page.data.is_latest_version %}
   .. rubric:: Version history
      :name: version-history
      :class: h2

   You can find the version history in the `latest version of the product <{{ page.data.latest_version_link }}?tab=history>`_.
   {% else %}
   .. rubric:: Version history
      :name: version-history
      :class: h2

   {% if previous_versions_list | length > 0 %}

   Versions are numbered using the `Semantic Versioning <semver_>`_ scheme (Major.Minor.Patch). Note that this list may include name changes and predecessor products.

   .. _semver: https://semver.org/

   .. list-table::

      * - {{ format_version_number(page.data.version_number) }}
        - \-
        - Current version
      {% for item in previous_versions_list %}
      * - {{ format_version_number(item.version_number) }}
        - of
        - `{{ item.title }} </data/version-history/{{ item.slug }}/>`_
      {% endfor %}
   {% else %}
   No previous versions are available.
   {% endif %}

   .. include:: _history.md
      :parser: myst_parser.sphinx_
   {% endif %}
{% endif %}
{% endset %}

{# FAQs tab component #}

{% set faqs_tab_component %}
{% if page.data.enable_faqs %}
.. tab-item:: FAQs
   :name: faqs

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   .. include:: _faqs.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Credits tab component #}

{% set credits_tab_component %}
{% if page.data.enable_credits %}
.. tab-item:: Credits
   :name: credits

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   .. include:: _credits.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Assembling the page components #}

{{ rst_head_component }}

{{ seo_head_component }}

{{ page_title_component }}

{{ header_panel_component }}

{{ notifications_section_component }}

.. tab-set::

   {{ overview_tab_component | indent(3, True) }}

   {{ description_tab_component | indent(3, True) }}

   {{ quality_tab_component | indent(3, True) }}

   {{ specifications_tab_component | indent(3, True) }}

   {{ access_tab_component | indent(3, True) }}

   {{ history_tab_component | indent(3, True) }}

   {{ faqs_tab_component | indent(3, True) }}

   {{ credits_tab_component | indent(3, True) }}

{{ html_end_scripts_component }}
