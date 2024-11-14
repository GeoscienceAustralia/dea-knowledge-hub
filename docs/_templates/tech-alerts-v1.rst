{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
} %}

{# Constant values #}

{% set max_page_title_length = 200 %}

{# Computed values #}

{% set quick_links_list = page.data.quick_links | selectattr("link", "!=", None) | list %}

{# Page template #}

{% if page.data.meta_description %}
.. meta::
   :description: {{ page.data.meta_description }}
{%- endif %}

.. rst-class:: tech-alerts-page

{{ "=" * max_page_title_length }}
{{ page.data.title }}
{{ "=" * max_page_title_length }}

{{ page.data.description }}

{% if quick_links_list %}
.. rubric:: Quick links
   :name: quick-links
   :class: h2

.. container:: card-list icons
   :name: quick-links-cards

   .. grid:: 2 2 3 5
      :gutter: 3

      {% for item in quick_links_list %}
      .. grid-item-card:: :fas:`{{ item.icon or "link" }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}
{%- endif %}

.. include:: _content.md
   :parser: myst_parser.sphinx_

.. rubric:: Older entries
   :name: older-entries
   :class: h2

View the `tech alerts and changelogs from previous years <./previous-years>`_.

