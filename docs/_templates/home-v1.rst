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

      {% for item in data.knowledge_hub %}
      `{{ item.name }} <{{ item.link }}>`_
      {% endfor %}

      `Get support <{{ config.html_context.support_link }}>`_

   .. grid-item-card::

      Data Products
      ^^^^^^^^^^^^^

      {% for item in data.data_products %}
      `{{ item.name }} <{{ item.link }}>`_
      {% endfor %}
   
   .. grid-item-card::

      DEA Notebooks
      ^^^^^^^^^

      {% for item in data.dea_notebooks %}
      `{{ item.name }} <{{ item.link }}>`_
      {% endfor %}

.. rubric:: About Digital Earth Australia
   :class: rubric-2

Digital Earth Australia (DEA) is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
