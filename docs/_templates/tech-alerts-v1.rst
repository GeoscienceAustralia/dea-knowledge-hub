{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
} %}

{# Constant values #}

{% set max_page_title_length = 200 %}

{# Computed values #}

{% set is_current_year = page.data.year == environment.current_year %}

{% set quick_links_custom_list = page.data.quick_links_custom | selectattr("link", "!=", None) | list %}

{% set system_status_notifications_list = page.data.system_status_notifications | selectattr("description", "!=", None) | selectattr("severity", "!=", None) | selectattr("severity", ">", 0) | sort(attribute='severity') | list %}

{# SEO head component #}

{% set seo_head_component %}
{% if page.data.meta_description %}
.. meta::
   :description: {{ page.data.meta_description }}
{%- endif %}
{% endset %}

{# Restructured Text head component #}

{% set rst_head_component %}
.. role:: raw-html(raw)
   :format: html

.. rst-class:: tech-alerts-page
{% endset %}

{# Page title component #}

{% set page_title_component %}
{{ "=" * max_page_title_length }}
{%- if is_current_year %}
DEA Tech Alerts
{%- else %}
DEA Tech Alerts {{ page.data.year }}
{%- endif %}
{{ "=" * max_page_title_length }}
{% endset %}

{# Page description component #}

{% set page_description_component %}
{% if is_current_year %}
{{ page.data.description or "Keep up with the latest updates, releases, outages, and planned maintenance." }}
{% else %}
{{ page.data.description or "View updates, releases, outages, and planned maintenance from the previous year of {}.".format(page.data.year) }}
{% endif %}
{% endset %}

{# Quick links component #}

{% set quick_links_component %}
.. container:: card-list icons
   :name: quick-links

   .. grid:: 2 2 3 5
      :gutter: 3

      .. grid-item-card:: :fas:`chart-simple`
         :link: https://monitoring.dea.ga.gov.au/

         Monitor service status

      .. grid-item-card:: :fas:`newspaper`
         :link: https://communication.ga.gov.au/dea-news-subscribe

         Subscribe to our newsletter

      .. grid-item-card:: :fas:`address-card`
         :link: https://www.ga.gov.au/scientific-topics/dea/contact-us

         Contact us

      {% for item in quick_links_custom_list %}
      .. grid-item-card:: :fas:`{{ item.icon or "link" }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}
{% endset %}

{# Notifications component #}

{% set notifications_component %}
.. container:: card-list tech-alert-notifications
   :name: tech-alert-notifications

   {% if system_status_notifications_list and is_current_year %}
   .. grid:: 2 2 3 3
      :gutter: 3

      {% for item in system_status_notifications_list %}
      {% if item.severity == 1 %}
      .. grid-item-card:: 
         :class-item: high-severity

         :fas:`triangle-exclamation` **{{ item.status_custom or "Alert" }}:** {{ item.description }}

      {% elif item.severity == 2 %}
      .. grid-item-card::
         :class-item: medium-severity

         :fas:`circle-exclamation`:raw-html:`&nbsp;` **{{ item.status_custom or "Warning" }}:** {{ item.description }}

      {% elif item.severity == 3 %}
      .. grid-item-card::
         :class-item: low-severity

         :fas:`circle-info`:raw-html:`&nbsp;` **{{ item.status_custom or "Note" }}:** {{ item.description }}

      {% else %}
      .. grid-item-card::
         :class-item: no-severity

         :fas:`circle-info`:raw-html:`&nbsp;` **{{ item.status_custom or "Note" }}:** {{ item.description }}

      {% endif %}
      {% endfor %}
   {%- else %}
   .. grid:: 1 1 1 1
      :gutter: 3

      .. grid-item-card:: 
         :class-item: no-severity

         :fas:`angle-left`:raw-html:`&nbsp;` `Go back to the current year ({{ environment.current_year }}) </tech-alerts/>`_

   {%- endif %}
{% endset %}

{# Content component #}

{% set content_component %}
.. include:: _content.md
   :parser: myst_parser.sphinx_
{% endset %}

{# Other years component #}

{% set other_years_component %}
{% if is_current_year %}
.. rubric:: Other years
   :name: other-years
   :class: h2

`View tech alerts from previous years </tech-alerts/previous-years>`_
{% else %}
.. rubric:: Other years
   :name: other-years
   :class: h2

View tech alerts from the `current year </tech-alerts/>`_ or `other years </tech-alerts/previous-years>`_.
{% endif %}
{% endset %}

{# Assembling the page #}

{{ rst_head_component }}

{{ seo_head_component }}

{{ page_title_component }}

{{ page_description_component }}

{{ quick_links_component }}

{{ notifications_component }}

{{ content_component }}

{{ other_years_component }}
