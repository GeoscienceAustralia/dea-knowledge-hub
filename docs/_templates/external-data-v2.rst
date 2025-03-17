{% set Data = load('_data.yaml') %}
{% set Tables = load('_tables.yaml') %}

{% set valid_maps = Data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = Data.data | selectattr("link",  "!=", None) | list %}
{% set valid_external_data = Data.external_data_page if Data.external_data_page and Data.external_data_page.link %}
{% set valid_explorers = Data.explorers | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = Data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = Data.code_examples | selectattr("link",  "!=", None) | list %}
{% set valid_custom = Data.custom | selectattr("icon",  "!=", None) | selectattr("link",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_product_types = [Data.lineage_type, Data.spatial_data_type] | select("!=", None) | list %}
{% set valid_product_ids = Data.product_ids | select("!=", None) | list %}
{% set valid_custom_citations = Data.custom_citations | select("!=", None) | list %}
{% set valid_tags = Data.tags | select("!=", None) | list %}
{% set valid_bands = Tables.bands.bands_table | selectattr("name",  "!=", None) | list %}

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
{% set has_key_details = (Data.licence_name and Data.licence_link) or Data.doi or Data.ecat %}

{% set product_ids_label = "Product IDs" if valid_product_ids | length > 1 else "Product ID" %}
{% set product_types_label = "Types" if valid_product_types | length > 1 else "Type" %}

{% set none_text = "None" %}
{% set not_available_text = "N/A" %}

{% set coordinate_reference_system_term = coordinate_reference_system_terms.get(page.data.coordinate_reference_system, page.data.coordinate_reference_system) %}

{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

.. role:: raw-html(raw)
   :format: html

.. rst-class:: product-page

======================================================================================================================================================
{{ Data.title }}
======================================================================================================================================================

.. container:: showcase-panel product-header bg-gradient-primary

   .. container::

      .. rubric:: {{ Data.title }}

      {% if valid_product_ids and Data.enable_specifications %}
      `{{ valid_product_ids | join(", ") }} <./?tab=specifications>`_
      {%- elif valid_product_ids %}
      {{ valid_product_ids | join(", ") }}
      {%- else %}
      External data
      {%- endif %}

      {% if valid_product_types %}
      :{{ product_types_label }}: {{ valid_product_types | join(", ") }}
      {%- endif %}
      {%- if Data.temporal_coverage %}
      {%- if Data.temporal_coverage.start and Data.temporal_coverage.end %}
      :Coverage: {{ Data.temporal_coverage.start }} to {{ Data.temporal_coverage.end }}
      {%- elif Data.temporal_coverage.start  %}
      :Coverage start: {{ Data.temporal_coverage.start }}
      {%- elif Data.temporal_coverage.end  %}
      :Coverage end: {{ Data.temporal_coverage.end }}
      {%- endif %}
      {%- endif %}
      :Produced by: {{ Data.external_party }}

   .. container::

      .. image:: {{ Data.header_image or "/_files/default/dea-earth-thumbnail.jpg" }}
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
      `{{ external_data_label }} ({{ Data.external_party }}) <{{ valid_external_data.link }}>`_
      {% endif %}
      {% endif %}

.. tab-set::

    {% if Data.enable_overview %}
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

       {% if Data.enable_specifications %}
       For more specifications, see the `Specifications tab <./?tab=specifications>`_.
       {% endif %}

       .. list-table::
          :name: key-specifications-table

          {% if Data.long_title %}
          * - **Long title**
            - {{ Data.long_title }}
          {%- endif %}
          {%- if Data.doi and Data.ecat %}
          * - **DOI**
            - `{{ Data.doi }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ Data.ecat }}>`_
          {%- elif Data.doi %}
          * - **DOI**
            - `{{ Data.doi }} <https://doi.org/{{ Data.doi }}>`_
          {%- elif Data.ecat %}
          * - **Persistent ID**
            - `{{ Data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ Data.ecat }}>`_
          {%- endif %}
          {%- if valid_tags %}
          * - **Tags**
            - {% for tag in valid_tags %}`{{tag}} </search/?q=Tag+{{tag}}>`_{% if not loop.last %}, {% endif %}{% endfor %}
          {%- endif %}
          {%- if Data.licence_name and Data.licence_link %}
          * - **Licence**
            - `{{ Data.licence_name }} <{{ Data.licence_link }}>`_
          {% elif Data.licence_name %}
          * - **Licence**
            - {{ Data.licence_name }}
          {%- endif %}
       {%- endif %}

       {% if Data.citations %}
       {% if Data.citations.data_citation or Data.citations.paper_citation %}
       .. rubric:: Cite this product
          :name: citations
          :class: h2

       .. list-table::
          :name: citation-table

          {% if Data.citations.data_citation %}
          * - **Data citation**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ Data.citations.data_citation }}
          {%- endif %}
          {% if Data.citations.paper_citation %}
          * - **Paper citation**
            - .. code-block:: text
                 :class: citation-table-citation citation-access-date

                 {{ Data.citations.paper_citation }}
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

    {% if Data.enable_specifications %}
    .. tab-item:: Specifications
       :name: specifications

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

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

       {{ Tables.bands.footnotes if Tables.bands.footnotes }}
       {% endif %}

       .. rubric:: Product information
          :name: product-information
          :class: h2

       This metadata provides general information about the product.

       .. list-table::
          :name: product-information-table

          {% if Data.coordinate_reference_system %}
          * - **Coordinate Reference System (CRS)**
            - {{ coordinate_reference_system_term }}
            - The method of mapping spatial data to the Earth's surface.
          {%- endif %}
          {%- if Data.doi %}
          * - **DOI**
            - `{{ Data.doi }} <https://doi.org/{{ Data.doi }}>`_
            - The Digital Object Identifier.
          {%- endif %}
          {%- if Data.ecat %}
          * - **Catalogue ID**
            - `{{ Data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ Data.ecat }}>`_
            - The Data and Publications catalogue (eCat) ID.
          {%- endif %}
          {%- if Data.licence_name and Data.licence_link %}
          * - **Licence**
            - `{{ Data.licence_name }} <{{ Data.licence_link }}>`_
            - The licence and copyright.
          {% elif Data.licence_name %}
          * - **Licence**
            - {{ Data.licence_name }}
            - The licence and copyright.
          {%- endif %}
    {% endif %}

    {% if Data.enable_access %}
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
