.. rst-class:: home-page

===================================================================
{{ data.title }}
===================================================================

.. image:: /_files/home-page/home-page-hero.png
   :alt: Digital Earth Australia logo

.. rubric:: DEA Documentation and Metadata Hub
   :class: rubric-1

Here you will find metadata for Geoscience Australia's earth observation data products and also documentation for using this data.

.. grid:: 3
   :gutter: 3

   .. grid-item-card::

      Access the data ...
      ^^^^^^^^^^^^^^^^^^^

      {% for theme in data.themes %}
      `{{ theme.name }} <data/themes/{{ theme.slug }}>`_
      {% endfor %}

   .. grid-item-card::

      Use the data ...
      ^^^^^^^^^^^^^^^^

      {% for use_link in data.use_links %}
      `{{ use_link.name }} <{{ use_link.link }}>`_
      {% endfor %}
   
   .. grid-item-card::

      Our program ...
      ^^^^^^^^^^^^^^^

      {% for program_link in data.program_links %}
      `{{ program_link.name }} <{{ program_link.link }}>`_
      {% endfor %}

      `Get support <{{ config.html_context.support_link }}>`_

.. rubric:: About Digital Earth Australia
   :class: rubric-2

Digital Earth Australia (DEA) is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
