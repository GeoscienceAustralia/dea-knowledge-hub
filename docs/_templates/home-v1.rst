.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

.. image:: /_files/pages/home-page-hero.png
   :alt: Digital Earth Australia logo

.. rubric:: DEA Documentation and Metadata Hub
   :class: rubric-1

Here you will find metadata for Geoscience Australia's earth observation data products, services, publications, help and learning, and other documentation.

.. grid:: 3
   :gutter: 3

   .. grid-item-card::

      Knowledge Hub
      ^^^^^^^^^^^^^

      {% for program_link in data.program_links %}
      `{{ program_link.name }} <{{ program_link.link }}>`_
      {% endfor %}

      `Get support <{{ config.html_context.support_link }}>`_

   .. grid-item-card::

      Data Products
      ^^^^^^^^^^^^^

      {% for theme in data.themes %}
      `{{ theme.name }} <{{ theme.link }}>`_
      {% endfor %}
   
   .. grid-item-card::

      DEA Notebooks
      ^^^^^^^^^

      {% for use_link in data.use_links %}
      `{{ use_link.name }} <{{ use_link.link }}>`_
      {% endfor %}

.. rubric:: About Digital Earth Australia
   :class: rubric-2

Digital Earth Australia (DEA) is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
