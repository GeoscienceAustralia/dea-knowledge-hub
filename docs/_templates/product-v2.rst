{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
   "specifications": load('_specifications.yaml'),
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

{% set data_update_frequency_cadence_terms = {
   "AS_NEEDED": "'As needed' frequency",
   "DAILY": "Daily frequency",
   "WEEKLY": "Weekly frequency",
   "MONTHLY": "Monthly frequency",
   "YEARLY": "Yearly frequency",
   "2_YEARS": "'Every 2 years' frequency",
   "10_MIN": "'Every 10 minutes' frequency",
} %}

{% set data_update_frequency_activity_terms = {
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

{% set specifications_summary_list = [page.data.lineage_type, page.data.spatial_data_type, page.data.resolution] | select("!=", None) | list %}

{% set custom_citations_list = page.data.custom_citations | select("!=", None) | list %}

{% set tags_list = page.data.tags | select("!=", None) | list %}

{% set bands_list_table = page.specifications.bands_table | selectattr("name",  "!=", None) | list %}

{% set page_title = page.data.official_name if page.data.is_latest_version else "{}: {}".format(page.data.product_version, page.data.official_name) %}

{% set product_ids_label = "Product IDs" if product_ids_list | length > 1 else "Product ID" %}

{% set product_ids_comma_separated = product_ids_list | join(", ") %}

{% set currency_report_url = "https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1#:~:text={}".format(page.data.official_name | urlencode) %}

{% set data_update_frequency_cadence = data_update_frequency_cadence_terms.get(page.data.data_update_frequency_cadence, page.data.data_update_frequency_cadence) %}

{% set data_update_frequency_activity = data_update_frequency_activity_terms.get(page.data.data_update_frequency_activity, page.data.data_update_frequency_activity) %}

{% set is_frequency_ongoing = data_update_frequency_activity == data_update_frequency_activity_terms.ONGOING %}

{% set is_cadence_yearly = data_update_frequency_cadence == data_update_frequency_cadence_terms.YEARLY %}

{% set has_access_data = maps_list or data_list or explorers_list or web_services_list or code_samples_list or custom_list %}

{% set has_key_details = (page.data.parent_products.name and page.data.parent_products.link) or (page.data.collection.name and page.data.collection.link) or page.data.collection.name or page.data.doi or page.data.ecat or page.data.published %}

{# Template #}

.. role:: raw-html(raw)
   :format: html

.. rst-class:: product-page

======================================================================================================================================================
{{ page_title }}
======================================================================================================================================================

{# Header panel #}

.. container:: showcase-panel product-header bg-gradient-primary

   .. container::

      .. rubric:: {{ page_title }}

      {% if page.data.full_technical_name %}
      {{ page.data.full_technical_name }}
      {% endif %}

      {%- if page.data.is_latest_version and old_versions_list | length > 0 and page.data.enable_history %} {# If at least one old version exists. #}
      :Version: {{ page.data.product_version }} `Learn more <./?tab=history>`_
      {%- elif page.data.is_latest_version %}
      :Version: {{ page.data.product_version }}
      {%- else %}
      :Version: {{ page.data.product_version }} (`See latest version <{{ page.data.latest_version_link }}>`_)
      {%- endif %}
      {%- if product_ids_list %}
      :{{ product_ids_label }}: {{ product_ids_comma_separated }}
      {%- endif %}
      :Specifications: {{ specifications_summary_list | join(", ") }} `Learn more <./?tab=specifications>`_
      {%- if page.data.time_span_custom %}
      :Temporal extent: {{ page.data.time_span_custom }} `Learn more <./?tab=specifications>`_
      {%- elif page.data.time_span_start and page.data.time_span_end %}
      :Temporal extent: {{ page.data.time_span_start }} to {{ page.data.time_span_end }} `Learn more <./?tab=specifications>`_
      {%- elif page.data.time_span_start  %}
      :Temporal extent: Starts at {{ page.data.time_span_start }} `Learn more <./?tab=specifications>`_
      {%- elif page.data.time_span_end  %}
      :Temporal extent: Ends at {{ page.data.time_span_end }} `Learn more <./?tab=specifications>`_
      {%- endif %}
      {%- if is_frequency_ongoing %}
      :Data updates: {{ data_update_frequency_cadence }}, {{ data_update_frequency_activity }}
      {%- else %}
      :Data updates: {{ data_update_frequency_activity }} (Previously: {{ data_update_frequency_cadence }})
      {%- endif %}

   .. container::

      .. image:: {{ page.data.header_image or "/_files/default/dea-earth-thumbnail.jpg" }}
         :class: no-gallery

{# Notifications section #}

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

.. tab-set::

    {# Overview tab #}

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

       For help accessing the data, see the `Access tab <./?tab=access>`_.

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

       {% if has_key_details %}
       .. rubric:: Key details
          :name: key-details
          :class: h2

       .. list-table::
          :name: key-details-table

          {% if page.data.parent_products %}
          {% if page.data.parent_products.name and page.data.parent_products.link %}
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
          {% if page.data.doi %}
          * - **DOI**
            - `{{ page.data.doi }} <https://doi.org/{{ page.data.doi }}>`_
          {% elif page.data.ecat %}
          * - **Persistent ID**
            - `{{ page.data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ page.data.ecat }}>`_
          {%- endif %}
          {%- if page.data.published %}
          * - **Last updated**
            - {{ page.data.published }}
          {%- endif %}
          {%- if page.data.licence %}
          {%- if page.data.licence.name and page.data.licence.link %}
          * - **Licence**
            - `{{ page.data.licence.name }} <{{ page.data.licence.link }}>`_
          {%- endif %}
          {%- endif %}
          {% if page.data.spatial_data_type != "Vector" and page.data.data_update_frequency_cadence != data_update_frequency_cadence_terms.AS_NEEDED and page.data.data_update_frequency_activity == data_update_frequency_activity_terms.ONGOING %}
          * - **Currency**
            - This product may be included in the `DEA Published Product Currency Report <https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1>`_ (if applicable).
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

       {%- if tags_list and enable_tags %}
       .. tags:: {{ tags_list | join(", ") }}
       {%- endif %}

       .. include:: _overview_2.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {# Details tab #}

    {% if page.data.enable_details %}
    .. tab-item:: Details
       :name: details

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _details.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {# Quality tab #}

    {% if page.data.enable_quality %}
    .. tab-item:: Quality
       :name: quality

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _quality.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {# Specifications tab #}

    {% if page.specifications.enable_specifications %}
    .. tab-item:: Specifications
       :name: specifications

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

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

          * - 
            - Aliases
            - Resolution
            - CRS
            - Nodata
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

       {{ page.specifications.bands_footnote if page.specifications.bands_footnote }}
       {% endif %}
    {% endif %}

    {# Access tab #}

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
            - Learn how to `use DEA Maps </guides/setup/dea_maps/>`_
          {% endif %}

          {% if explorers_list %}
          * - **{{ access_labels.explorer }}**
            - {% for item in explorers_list %}
              * `{{ item.name or access_names.explorer }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Explorer </setup/explorer_guide/>`_
          {% endif %}

          {% if data_list %}
          * - **{{ access_labels.data }}**
            - {% for item in data_list %}
              * `{{ item.name or access_names.data }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </guides/about/faq/#download-dea-data>`_
          {% endif %}

          {% if code_samples_list %}
          * - **{{ access_labels.code_sample }}**
            - {% for item in code_samples_list %}
              * `{{ item.name or access_names.code_sample }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Sandbox </guides/setup/Sandbox/sandbox/>`_
          {% endif %}

          {% if web_services_list %}
          * - **{{ access_labels.web_service }}**
            - {% for item in web_services_list %}
              * `{{ item.name or access_names.web_service }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA's web services </guides/setup/gis/README/>`_
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

    {# History tab #}

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

    {# FAQs tab #}

    {% if page.data.enable_faqs %}
    .. tab-item:: FAQs
       :name: faqs

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _faqs.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {# Credits tab #}

    {% if page.data.enable_credits %}
    .. tab-item:: Credits
       :name: credits

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _credits.md
          :parser: myst_parser.sphinx_
    {% endif %}

.. raw:: html

   <script type="text/javascript" src="/_static/scripts/access-cards-tooltips.js" /></script>
   <script type="text/javascript" src="/_static/scripts/citation-access-date.js" /></script>

