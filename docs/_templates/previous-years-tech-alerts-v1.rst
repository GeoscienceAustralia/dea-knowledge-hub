{% set page = {
   "data": load('_data.yaml'),
} %}

.. role:: raw-html(raw)
   :format: html

.. rst-class:: previous-years-tech-alerts-page

{% if page.data.meta_description %}
.. meta::
   :description: {{ page.data.meta_description }}
{%- endif %}

==============
Previous years
==============

{{ page.data.description or "Here you will find tech alerts from previous years." }}

.. container:: card-list tech-alert-notifications
   :name: tech-alert-notifications

   .. grid:: 1 1 1 1
      :gutter: 3

      .. grid-item-card:: 
         :class-item: no-severity

         :fas:`angle-left`:raw-html:`&nbsp;` `Go back to DEA Tech Alerts 2024 </tech-alerts/>`_

.. tableofcontents::

