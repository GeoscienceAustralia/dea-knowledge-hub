{% set Data = load('_data.yaml') %}

{% set access_names = {
   "map": "DEA Maps",
   "explorer": "Data Explorer",
   "data": "DEA Data",
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

{% set data_published_frequency_terms = {
   "AS_NEEDED": "As needed",
   "DAILY": "Daily",
   "WEEKLY": "Weekly",
   "MONTHLY": "Monthly",
   "YEARLY": "Yearly",
   "2_YEARS": "Every 2 years",
   "10_MIN": "Every 10 minutes",
} %}

{% set data_published_activity_terms = {
   "ONGOING": "Ongoing data publishing",
   "NO_UPDATES": "No further data to be published",
   "PAUSED": "Data publishing is currently paused",
} %}

{% set is_latest_version = Data.is_latest_version %}

{% set valid_maps = Data.maps | selectattr("link",  "!=", None) | list %}
{% set valid_data = Data.data | selectattr("link",  "!=", None) | list %}
{% set valid_explorers = Data.explorers | selectattr("link",  "!=", None) | list %}
{% set valid_web_services = Data.web_services | selectattr("link",  "!=", None) | list %}
{% set valid_code_samples = Data.code_examples | selectattr("link",  "!=", None) | list %}
{% set valid_custom = Data.custom | selectattr("icon",  "!=", None) | selectattr("link",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_old_versions = Data.old_versions | selectattr("slug",  "!=", None) | selectattr("version",  "!=", None) | selectattr("name",  "!=", None) | list %}
{% set valid_product_ids = Data.product_ids | select("!=", None) | list %}
{% set valid_custom_citations = Data.custom_citations | select("!=", None) | list %}
{% set valid_tags = Data.tags | select("!=", None) | list %}

{% set has_access_data = valid_maps or valid_data or valid_explorers or valid_web_services or valid_code_samples or valid_custom %}
{% set has_key_details = (Data.parent_products.name and Data.parent_products.link) or (Data.collection.name and Data.collection.link) or Data.collection.name or Data.doi or Data.ecat or Data.published %}

{% set page_title = Data.short_name if is_latest_version else Data.version + ": " + Data.short_name %}
{% set product_ids_label = "Product IDs" if valid_product_ids | length > 1 else "Product ID" %}

.. rst-class:: product-page

======================================================================================================================================================
{{ page_title }}
======================================================================================================================================================

.. container:: showcase-panel product-header bg-gradient-primary

   .. container::

      .. rubric:: {{ page_title }}

      {% if Data.full_technical_name %}
      :Full name: {{ Data.full_technical_name }}
      {%- endif %}
      {%- if is_latest_version %}
      :Product version: {{ Data.version }}
      {%- else %}
      :Product version: {{ Data.version }} (`See latest product version <{{ Data.latest_version_link }}>`_)
      {%- endif %}
      {%- if valid_product_ids %}
      :{{ product_ids_label }}: {{ valid_product_ids | join(", ") }}
      {%- endif %}
      :Type: {{ Data.type.product_type }}, {{ Data.type.spatial_data_type }}
      {%- if Data.resolution %}
      :Resolution: {{ Data.resolution }}
      {%- endif %}
      {%- if Data.time_span %}
      {%- if Data.time_span.start and Data.time_span.end %}
      :Data time span: {{ Data.time_span.start }} – {{ Data.time_span.end }}
      {%- elif Data.time_span.start  %}
      :Data time span: Starts at {{ Data.time_span.start }}
      {%- elif Data.time_span.end  %}
      :Data time span: Ends at {{ Data.time_span.end }}
      {%- endif %}
      {%- endif %}
      {% if Data.data_published.frequency == "NO_UPDATES" %}
      :Data published: {{ data_published_activity_terms.NO_UPDATES }} (previously '{{ data_published_frequency_terms.get(Data.data_published.frequency, Data.data_published.frequency) }}')
      {%- else %}
      :Data published: {{ data_published_frequency_terms.get(Data.data_published.frequency, Data.data_published.frequency) }}, {{ data_published_activity_terms.get(Data.data_published.activity, Data.data_published.activity) }}
      {%- endif %}

   .. container::

      .. image:: {{ Data.header_image or "/_files/pages/dea-hero.jpg" }}
         :class: no-gallery

.. container::
   :name: notifications

   {% if not is_latest_version %}
   .. admonition:: Old version
      :class: note
   
      This is an old version of the product. See the `latest version <{{ Data.latest_version_link }}>`_.

   {% endif %}
   {% if Data.is_provisional %}
   .. admonition:: Provisional product
      :class: note

      This is a `provisional product </guides/reference/dataset_maturity_guide/>`_, meaning it has not yet passed quality control and/or been finalised for release.

   {% endif %}

{% if not is_latest_version %}
{% endif %}

.. tab-set::

    {% if Data.enable_overview %}
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

             {% for item in valid_maps %}
             .. grid-item-card:: :fas:`map-location-dot`
                :link: {{ item.link }}
                :link-alt: {{ access_labels.map }}

                {{ item.name or access_names.map }}
             {% endfor %}

             {% for item in valid_explorers %}
             .. grid-item-card:: :fas:`magnifying-glass`
                :link: {{ item.link }}
                :link-alt: {{ access_labels.explorer }}

                {{ item.name or access_names.explorer }}
             {% endfor %}

             {% for item in valid_data %}
             .. grid-item-card:: :fas:`database`
                :link: {{ item.link }}
                :link-alt: {{ access_labels.data }}

                {{ item.name or access_names.data }}
             {% endfor %}

             {% for item in valid_code_samples %}
             .. grid-item-card:: :fas:`laptop-code`
                :link: {{ item.link }}
                :link-alt: {{ access_labels.code_sample }}

                {{ item.name or access_names.code_sample }}
             {% endfor %}

             {% for item in valid_web_services %}
             .. grid-item-card:: :fas:`globe`
                :link: {{ item.link }}
                :link-alt: {{ access_labels.web_service }}

                {{ item.name or access_names.web_service }}
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

          {% if Data.parent_products %}
          {% if Data.parent_products.name and Data.parent_products.link %}
          * - **Parent product(s)**
            - `{{ Data.parent_products.name }} <{{ Data.parent_products.link }}>`_
          {%- endif %}
          {%- endif %}
          {%- if Data.collection %}
          {%- if Data.collection.name and Data.collection.link %}
          * - **Collection**
            - `{{ Data.collection.name }} <{{ Data.collection.link }}>`_
          {%- elif Data.collection.name %}
          * - **Collection**
            - {{ Data.collection.name }}
          {%- endif %}
          {%- endif %}
          {%- if Data.doi and Data.ecat %}
          * - **DOI**
            - `{{ Data.doi }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ Data.ecat }}>`_
          {% elif Data.doi %}
          * - **DOI**
            - `{{ Data.doi }} <https://doi.org/{{ Data.doi }}>`_
          {% elif Data.ecat %}
          * - **Persistent ID**
            - `{{ Data.ecat }} <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/{{ Data.ecat }}>`_
          {%- endif %}
          {%- if Data.published %}
          * - **Last updated**
            - {{ Data.published }}
          {%- endif %}
          {%- if Data.licence %}
          {%- if Data.licence.name and Data.licence.link %}
          * - **Licence**
            - `{{ Data.licence.name }} <{{ Data.licence.link }}>`_
          {%- endif %}
          {%- endif %}
          {% if Data.spatial_data_type != "Vector" and Data.data_published.frequency != data_published_frequency_terms.AS_NEEDED and Data.data_published.activity == data_published_activity_terms.ONGOING %}
          * - **Currency**
            - This product may be included in the `DEA Published Product Currency Report <https://mgmt.sandbox.dea.ga.gov.au/public-dashboards/d22241dbfca54b1fa9f73938ef26e645?orgId=1>`_ (if applicable).
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
                 :class: citation-table-citation

                 {{ Data.citations.paper_citation }}
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

       .. include:: _overview_2.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if Data.enable_details %}
    .. tab-item:: Details
       :name: details

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _details.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if Data.enable_quality %}
    .. tab-item:: Quality
       :name: quality

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _quality.md
          :parser: myst_parser.sphinx_
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

          {% if valid_maps %}
          * - **{{ access_labels.map }}**
            - {% for item in valid_maps %}
              * `{{ item.name or access_names.map }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use DEA Maps </guides/setup/dea_maps/>`_
          {% endif %}

          {% if valid_explorers %}
          * - **{{ access_labels.explorer }}**
            - {% for item in valid_explorers %}
              * `{{ item.name or access_names.explorer }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Explorer </setup/explorer_guide/>`_
          {% endif %}

          {% if valid_data %}
          * - **{{ access_labels.data }}**
            - {% for item in valid_data %}
              * `{{ item.name or access_names.data }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `access the data via AWS </guides/about/faq/#download-dea-data>`_
          {% endif %}

          {% if valid_code_samples %}
          * - **{{ access_labels.code_sample }}**
            - {% for item in valid_code_samples %}
              * `{{ item.name or access_names.code_sample }} <{{ item.link }}>`_
              {% endfor %}
            - Learn how to `use the DEA Sandbox </guides/setup/Sandbox/sandbox/>`_
          {% endif %}

          {% if valid_web_services %}
          * - **{{ access_labels.web_service }}**
            - {% for item in valid_web_services %}
              * `{{ item.name or access_names.web_service }} <{{ item.link }}>`_
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

    {% if Data.enable_history %}
    .. tab-item:: History
       :name: history

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       {% if not is_latest_version %}
       .. rubric:: Other versions
          :name: other-versions
          :class: h2

       You can find the history in the `latest version of the product <{{ Data.latest_version_link }}?tab=history>`_.
       {% else %}
       .. rubric:: Old versions
          :name: old-versions
          :class: h2

       {% if valid_old_versions %}

       View previous versions of this data product.

       .. list-table::

          {% for item in valid_old_versions %}
          * - `{{ item.version }}: {{ item.title }} </data/old-version/{{ item.slug }}/>`_
          {% endfor %}
       {% else %}
       No old versions available.
       {% endif %}

       .. include:: _history.md
          :parser: myst_parser.sphinx_
       {% endif %}
    {% endif %}

    {% if Data.enable_faqs %}
    .. tab-item:: FAQs
       :name: faqs

       .. raw:: html

          <div class="product-tab-table-of-contents"></div>

       .. include:: _faqs.md
          :parser: myst_parser.sphinx_
    {% endif %}

    {% if Data.enable_credits %}
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

