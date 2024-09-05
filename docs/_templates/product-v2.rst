{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
   "figures": load('_figures.yaml'),
} %}

{# Terms and static strings #}

{% set access_names = {
   "map": "DEA Maps",
   "explorer": "Data Explorer",
   "data": "Data sources",
   "code_sample": "Code sample",
   "web_service": "Web service",
} %}

{% set access_labels = {
   "map": "See it on a map",
   "explorer": "Explore data availability",
   "data": "Get the data online",
   "code_sample": "View a code sample",
   "web_service": "Get via web service",
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
   "AS_NEEDED": "'As needed' frequency",
   "DAILY": "Daily frequency",
   "WEEKLY": "Weekly frequency",
   "MONTHLY": "Monthly frequency",
   "YEARLY": "Yearly frequency",
   "2_YEARS": "'Every 2 years' frequency",
   "10_MIN": "'Every 10 minutes' frequency",
} %}

{% set data_update_activity_terms = {
   "ONGOING": "Ongoing",
   "NO_UPDATES": "No further updates",
   "DEVELOPMENT": "Awaiting development",
   "PAUSED": "Currently paused",
} %}

{% set no_data_terms = {
   "dash": "\-",
} %}

{# Computed variables #}

{% set maps_list = page.data.maps | selectattr("link",  "!=", None) | list %}

{% set data_list = page.data.data | selectattr("link",  "!=", None) | list %}

{% set explorers_list = page.data.explorers | selectattr("link",  "!=", None) | list %}

{% set web_services_list = page.data.web_services | selectattr("link",  "!=", None) | list %}

{% set code_samples_list = page.data.code_examples | selectattr("link",  "!=", None) | list %}

{% set custom_list = page.data.custom | selectattr("icon",  "!=", None) | selectattr("link",  "!=", None) | selectattr("name",  "!=", None) | list %}

{% set old_versions_list = page.data.old_versions | selectattr("slug",  "!=", None) | selectattr("version",  "!=", None) | selectattr("name",  "!=", None) | list %}

{% set product_ids_list = page.data.product_ids | select("!=", None) | list %}

{% set custom_citations_list = page.data.custom_citations | select("!=", None) | list %}

{% set tags_list = page.data.tags | select("!=", None) | list %}

{% set bands_table_list = page.figures.bands_table | selectattr("name",  "!=", None) | list %}

{% set page_title = page.data.official_name if page.data.is_latest_version else "{}: {}".format(page.data.product_version, page.data.official_name) %}

{% set product_ids_label = "Product IDs" if product_ids_list | length > 1 else "Product ID" %}

{% set product_ids_comma_separated = product_ids_list | join(", ") %}

{% set currency_report_url = "https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1#:~:text={}".format(page.data.official_name | urlencode) %}

{% set lineage_type = lineage_type_terms.get(page.data.lineage_type, page.data.lineage_type) %}

{% set spatial_data_type = spatial_data_type_terms.get(page.data.spatial_data_type, page.data.spatial_data_type) %}

{% set product_types_list = [lineage_type, spatial_data_type] | select("!=", None) | list %}

{% set data_update_frequency = data_update_frequency_terms.get(page.data.data_update_frequency, page.data.data_update_frequency) %}

{% set data_update_activity = data_update_activity_terms.get(page.data.data_update_activity, page.data.data_update_activity) %}

{% set is_frequency_ongoing = data_update_activity == data_update_activity_terms.ONGOING %}

{% set is_cadence_yearly = data_update_frequency == data_update_frequency_terms.YEARLY %}

{% set has_access_data = maps_list or data_list or explorers_list or web_services_list or code_samples_list or custom_list %}

{% set has_key_specifications = (page.data.parent_products.name and page.data.parent_products.link) or (page.data.collection.name and page.data.collection.link) or page.data.collection.name or page.data.doi or page.data.ecat or page.data.published %}

{# Restructured Text head component #}

{% set rst_start_component %}
.. role:: raw-html(raw)
   :format: html

.. rst-class:: product-page

======================================================================================================================================================
{{ page_title }}
======================================================================================================================================================
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

      .. rubric:: {{ page_title }}

      {% if page.data.full_technical_name %}
      {{ page.data.full_technical_name }}
      {% endif %}

      {% if page.data.is_latest_version %}
      :Version: {{ page.data.product_version }}
      {%- else %}
      :Version: {{ page.data.product_version }} (`See latest version <{{ page.data.latest_version_link }}>`_)
      {%- endif %}
      :Type: {{ product_types_list | join(", ") }}
      {%- if page.data.resolution %}
      :Resolution: {{ page.data.resolution }}
      {%- endif %}
      {%- if page.data.temporal_extent_custom %}
      :Data from: {{ page.data.temporal_extent_custom }}
      {%- elif page.data.temporal_extent_start and page.data.temporal_extent_end %}
      :Data from: {{ page.data.temporal_extent_start }} to {{ page.data.temporal_extent_end }}
      {%- elif page.data.temporal_extent_start  %}
      :Data since: {{ page.data.temporal_extent_start }}
      {%- elif page.data.temporal_extent_end  %}
      :Data until: {{ page.data.temporal_extent_end }}
      {%- endif %}
      {%- if is_frequency_ongoing %}
      :Data updates: {{ data_update_frequency }}, {{ data_update_activity }}
      {%- else %}
      :Data updates: {{ data_update_activity }} (Previously: {{ data_update_frequency }})
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

         {% for item in maps_list %}
         .. grid-item-card:: :fas:`map-location-dot`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.map }}

            {{ item.name or access_names.map }}
         {% endfor %}

         {% for item in explorers_list %}
         .. grid-item-card:: :fas:`magnifying-glass`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.explorer }}

            {{ item.name or access_names.explorer }}
         {% endfor %}

         {% for item in data_list %}
         .. grid-item-card:: :fas:`database`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.data }}

            {{ item.name or access_names.data }}
         {% endfor %}

         {% for item in code_samples_list %}
         .. grid-item-card:: :fas:`laptop-code`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.code_sample }}

            {{ item.name or access_names.code_sample }}
         {% endfor %}

         {% for item in web_services_list %}
         .. grid-item-card:: :fas:`globe`
            :link: {{ item.link }}
            :link-alt: {{ access_labels.web_service }}

            {{ item.name or access_names.web_service }}
         {% endfor %}

         {% for item in custom_list %}
         .. grid-item-card:: :fas:`{{ item.icon }}`
            :link: {{ item.link }}
            :link-alt: {{ item.label or "" }}
            :class-card: {{ item.class }}

            {{ item.name }}
         {% endfor %}
   {%- endif %}

   {% if has_key_specifications %}
   .. rubric:: Key specifications
      :name: key-specifications
      :class: h2

   {% if page.data.enable_specifications %}
   For more specifications, see the `Specifications tab <./?tab=specifications>`_.
   {% endif %}

   .. list-table::
      :name: key-specifications-table

      {% if page.data.is_currency_reported and is_cadence_yearly %}
      * - **Currency**
        - See `currency and latest and next update dates <{{ currency_report_url }}>`_.
      {% elif page.data.is_currency_reported %}
      * - **Currency**
        - See `currency and latest update date <{{ currency_report_url }}>`_.
      {%- endif %}
      {%- if product_ids_list %}
      * - **{{ product_ids_label }}**
        - {{ product_ids_comma_separated }}
      {%- endif %}
      {%- if page.data.doi %}
      * - **DOI**
        - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
      {%- elif page.data.ecat %}
      * - **Persistent ID**
        - `{{ page.data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
      {%- endif %}
      {%- if page.data.published %}
      * - **Last updated**
        - {{ page.data.published }}
      {%- endif %}
      {%- if page.data.parent_products %}
      {%- if page.data.parent_products.name and page.data.parent_products.link %}
      * - **Parent product(s)**
        - `{{ page.data.parent_products.name }} <{{ page.data.parent_products.link }}>`_
      {%- endif %}
      {%- endif %}
      {%- if page.data.collection %}
      {%- if page.data.collection.name and page.data.collection.link %}
      * - **Collection**
        - `{{ page.data.collection.name }} <{{ page.data.collection.link }}>`_
      {%- elif page.data.collection.name %}
      * - **Collection**
        - {{ page.data.collection.name }}
      {%- endif %}
      {%- endif %}
      {%- if page.data.licence %}
      {%- if page.data.licence.name and page.data.licence.link %}
      * - **Licence**
        - `{{ page.data.licence.name }} <{{ page.data.licence.link }}>`_
      {%- endif %}
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
             :class: citation-table-citation

             {{ page.data.citations.paper_citation }}
      {%- endif %}
      {% for citation in custom_list_citations %}
      * - **{{ citation.name }}**
        - .. code-block:: text
             :class: citation-table-citation

             {{ citation.citation }}
      {% endfor %}
   {%- endif %}
   {%- endif %}

   .. include:: _overview_2.md
      :parser: myst_parser.sphinx_
{% endif %}
{% endset %}

{# Details tab component #}

{% set details_tab_component %}
{% if page.data.enable_details %}
.. tab-item:: Details
   :name: details

   .. raw:: html

      <div class="product-tab-table-of-contents"></div>

   .. include:: _details.md
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

   .. rubric:: Specifications
      :name: specifications-tables
      :class: h2

   .. dropdown:: General

      .. list-table::
         :name: general-specifications-table

         {% if page.data.is_latest_version and old_versions_list | length > 0 and page.data.enable_history %} {# If at least one old version exists. #}
         * - **Version**
           - {{ page.data.product_version }}
           - The version number of the product. See the `version history <./?tab=history>`_.
         {%- elif page.data.is_latest_version %}
         * - **Version**
           - {{ page.data.product_version }}
           - The version number of the product.
         {%- else %}
         * - **Version**
           - {{ page.data.product_version }}
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
           -
         {%- endif %}
         {% if spatial_data_type == spatial_data_type_terms.RASTER %}
         * - **Spatial type**
           - {{ spatial_data_type }}
           - Raster data consists of a grid of pixels.
         {%- elif spatial_data_type == spatial_data_type_terms.VECTOR %}
         * - **Spatial type**
           - {{ spatial_data_type }}
           - Vector data consists of mathematical polygons.
         {%- else %}
         * - **Spatial type**
           - {{ spatial_data_type }}
           -
         {%- endif %}
         {%- if page.data.resolution %}
         * - **Resolution**
           - {{ page.data.resolution }}
           - The size of the small area that the data can represent.
         {%- endif %}
         {%- if page.data.temporal_extent_custom %}
         * - **Temporal extent**
           - {{ page.data.temporal_extent_custom }}
           - The time span for which data is available.
         {%- elif page.data.temporal_extent_start and page.data.temporal_extent_end %}
         * - **Temporal extent**
           - {{ page.data.temporal_extent_start }} to {{ page.data.temporal_extent_end }}
           - The time span for which data is available.
         {%- elif page.data.temporal_extent_start  %}
         * - **Temporal extent**
           - Since {{ page.data.temporal_extent_start }}
           - The time span for which data is available.
         {%- elif page.data.temporal_extent_end  %}
         * - **Temporal extent**
           - Until {{ page.data.temporal_extent_end }}
           - The time span for which data is available.
         {%- endif %}
         {%- if is_frequency_ongoing %}
         * - **Update frequency**
           - {{ data_update_frequency }}
           - The expected frequency of data updates.
         {%- else %}
         * - **Update frequency**
           - Previously: {{ data_update_frequency }}
           - When data updates were active, this was their expected frequency.
         {%- endif %}
         * - **Update activity**
           - {{ data_update_activity }}
           - The activity status of data updates.
         {%- if page.data.is_currency_reported and is_cadence_yearly %}
         * - **Currency**
           - `Currency Report <{{ currency_report_url }}>`_
           - See the report.
         * - **Latest and next update dates**
           - `Currency Report <{{ currency_report_url }}>`_
           - See the report.
         {% elif page.data.is_currency_reported %}
         * - **Currency**
           - `Currency Report <{{ currency_report_url }}>`_
           - See the report.
         * - **Latest update date**
           - `Currency Report <{{ currency_report_url }}>`_
           - See the report.
         {%- endif %}

   .. dropdown:: Classification

      .. list-table::
         :name: classification-specifications-table

         * - **Official name**
           - {{ page.data.official_name }}
           -
         {%- if page.data.full_technical_name %}
         * - **Technical name**
           - {{ page.data.full_technical_name }}
           -
         {%- endif %}
         {%- if product_ids_list %}
         * - **{{ product_ids_label }}**
           - {{ product_ids_comma_separated }}
           - Used by `Open Data Cube <https://www.opendatacube.org/>`_
         {%- endif %}
         {%- if page.data.doi %}
         * - **DOI**
           - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
           -
         {%- endif %}
         {%- if page.data.ecat %}
         * - **Persistent ID**
           - `{{ page.data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
           - eCat ID (internal use)
         {%- endif %}
         {%- if page.data.parent_products %}
         {%- if page.data.parent_products.name and page.data.parent_products.link %}
         * - **Parent product(s)**
           - `{{ page.data.parent_products.name }} <{{ page.data.parent_products.link }}>`_
           -
         {%- endif %}
         {%- endif %}
         {%- if page.data.collection %}
         {%- if page.data.collection.name and page.data.collection.link %}
         * - **Collection**
           - `{{ page.data.collection.name }} <{{ page.data.collection.link }}>`_
           -
         {%- elif page.data.collection.name %}
         * - **Collection**
           - {{ page.data.collection.name }}
           -
         {%- endif %}
         {%- endif %}
         {%- if tags_list %}
         * - **Tags**
           - {{ tags_list | join(", ") }}
           -
         {%- endif %}
         {%- if page.data.licence %}
         {%- if page.data.licence.name and page.data.licence.link and page.data.enable_credits %}
         * - **Licence**
           - `{{ page.data.licence.name }} <{{ page.data.licence.link }}>`_
           - See `Credits <./?tab=credits>`_.
         {%- elif page.data.licence.name and page.data.licence.link %}
         * - **Licence**
           - `{{ page.data.licence.name }} <{{ page.data.licence.link }}>`_
           -
         {%- endif %}
         {%- endif %}

   {% if bands_table_list %}
   .. rubric:: Bands
      :name: bands
      :class: h2

   Bands are distinct layers of data within a product that can be loaded using the Open Data Cube (on the `DEA Sandbox <dea_sandbox_>`_ or `NCI <nci_>`_) or DEA's `STAC API <stac_api_>`_.

   .. _dea_sandbox: https://knowledge.dea.ga.gov.au/guides/setup/Sandbox/sandbox/
   .. _nci: https://knowledge.dea.ga.gov.au/guides/setup/NCI/basics/
   .. _stac_api: https://knowledge.dea.ga.gov.au/guides/setup/gis/stac/

   .. list-table::
      :header-rows: 1
      :name: bands-specifications-table

      * - 
        - Aliases
        - Resolution
        - CRS
        - 'No data'
        - Units
        - Type
        - Description
      {% for band in bands_table_list %}
      * - **{{ band.name }}**
        - {{ band.aliases|join(', ') if band.aliases else no_data_terms.dash }}
        - {{ band.resolution or no_data_terms.dash }}
        - {{ band.crs or no_data_terms.dash }}
        - {{ band.nodata }}
        - {{ band.units or no_data_terms.dash }}
        - {{ band.type or no_data_terms.dash }}
        - {{ band.description or no_data_terms.dash }}
      {% endfor %}

   {{ page.figures.bands_footnote if page.figures.bands_footnote }}
   {% endif %}
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

      {% if maps_list %}
      * - **{{ access_labels.map }}**
        - {% for item in maps_list %}
          * `{{ item.name or access_names.map }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use DEA Maps </guides/setup/dea_maps/>`_.
      {% endif %}

      {% if explorers_list %}
      * - **{{ access_labels.explorer }}**
        - {% for item in explorers_list %}
          * `{{ item.name or access_names.explorer }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use the DEA Explorer </setup/explorer_guide/>`_.
      {% endif %}

      {% if data_list %}
      * - **{{ access_labels.data }}**
        - {% for item in data_list %}
          * `{{ item.name or access_names.data }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `access the data via AWS </guides/about/faq/#download-dea-data>`_.
      {% endif %}

      {% if code_samples_list %}
      * - **{{ access_labels.code_sample }}**
        - {% for item in code_samples_list %}
          * `{{ item.name or access_names.code_sample }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use the DEA Sandbox </guides/setup/Sandbox/sandbox/>`_.
      {% endif %}

      {% if web_services_list %}
      * - **{{ access_labels.web_service }}**
        - {% for item in web_services_list %}
          * `{{ item.name or access_names.web_service }} <{{ item.link }}>`_
          {% endfor %}
        - Learn how to `use DEA's web services </guides/setup/gis/README/>`_.
      {% endif %}

      {% for item in custom_list %}
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

   {% if old_versions_list | length > 0 %}

   View previous releases of this product. Versions are numbered using the `Semantic Versioning <semver_>`_ scheme (MAJOR.MINOR.PATCH).

   .. _semver: https://semver.org/

   .. list-table::

      * - {{ page.data.product_version }}: Current version
      {% for item in old_versions_list %}
      * - `{{ item.version }}: {{ item.title }} </data/version-history/{{ item.slug }}/>`_
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

{# Constructing the template #}

{{ rst_start_component }}

{{ header_panel_component }}

{{ notifications_section_component }}

.. tab-set::

   {{ overview_tab_component | indent(3, True) }}

   {{ details_tab_component | indent(3, True) }}

   {{ quality_tab_component | indent(3, True) }}

   {{ specifications_tab_component | indent(3, True) }}

   {{ access_tab_component | indent(3, True) }}

   {{ history_tab_component | indent(3, True) }}

   {{ faqs_tab_component | indent(3, True) }}

   {{ credits_tab_component | indent(3, True) }}

{{ html_end_scripts_component }}
