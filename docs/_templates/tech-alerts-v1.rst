{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
} %}

{# Constant values #}

{% set max_page_title_length = 200 %}

{# Computed values #}

{% set quick_links_list = page.data.quick_links | selectattr("link", "!=", None) | list %}

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
.. rst-class:: tech-alerts-page
{% endset %}

{# Page title component #}

{% set page_title_component %}
{{ "=" * max_page_title_length }}
DEA Tech Alerts {{ page.data.year }}
{{ "=" * max_page_title_length }}
{% endset %}

{# Page description component #}

{% set page_description_component %}
{{ page.data.description or "Keep up with the latest updates, releases, outages, and planned maintenance." }}
{% endset %}

{# Quick links component #}

{% set quick_links_component %}
{% if quick_links_list %}
.. container:: card-list icons
   :name: quick-links

   .. grid:: 2 2 3 5
      :gutter: 3

      {% for item in quick_links_list %}
      .. grid-item-card:: :fas:`{{ item.icon or "link" }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}
{%- endif %}
{% endset %}

{# System status notifications component #}

{% set system_status_notifications_component %}
{% if system_status_notifications_list %}
.. container:: card-list system-status-notifications
   :name: system-status-notifications

   .. grid:: 2 2 3 3
      :gutter: 0

      {% for item in system_status_notifications_list %}
      {% if item.severity == 1 %}
      .. grid-item-card:: 
         :class-item: high-severity

         :fas:`triangle-exclamation` {{ item.description }}

      {% elif item.severity == 2 %}
      .. grid-item-card::
         :class-item: medium-severity

         :fas:`circle-exclamation` {{ item.description }}

      {% else %}
      .. grid-item-card::
         :class-item: low-severity

         :fas:`circle-info` {{ item.description }}

      {% endif %}
      {% endfor %}
{%- endif %}
{% endset %}

{# Content component #}

{% set content_component %}
.. include:: _content.md
   :parser: myst_parser.sphinx_
{% endset %}

{# Previous years component #}

{% set previous_years_component %}
.. rubric:: Previous years
   :name: previous-years
   :class: h2

`View tech alerts from previous years <./previous-years>`_
{% endset %}

{# Assembling the page #}

{{ rst_head_component }}

{{ seo_head_component }}

{{ page_title_component }}

{{ page_description_component }}

{{ quick_links_component }}

{{ system_status_notifications_component }}

{{ content_component }}

{{ previous_years_component }}
