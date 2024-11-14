{# Data loaded from source files #}

{% set page = {
   "data": load('_data.yaml'),
} %}

{# Computed values #}

{% set quick_links_list = page.data.quick_links | selectattr("link", "!=", None) | list %}

{% if page.data.meta_description %}
.. meta::
   :description: {{ page.data.meta_description }}
{%- endif %}

.. rst-class:: tech-alerts-page

======================================================================================================================================================
{{ page.data.title }}
======================================================================================================================================================

{{ page.data.description }}

{% if page.data.quick_links | length > 1 %}
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

