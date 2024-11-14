{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

.. rst-class:: tech-alerts-changelog-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description }}

.. include:: _content.md
   :parser: myst_parser.sphinx_

.. rubric:: Older entries
   :name: older-entries
   :class: h2

View the `tech alerts and changelogs from previous years <./previous-years>`_.

