.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description }}

.. container:: showcase-panel bg-gradient-primary reverse

   .. container::

      .. rubric:: Knowledge Hub

      Learn how to use our products and services.

      `Visit the Knowledge Hub </knowledge/>`_

   .. container::

      .. image:: /_files/pages/dea-hero.jpg

.. container:: card-list icons bg-grey

   .. rubric:: Data Products

   Find product metadata on our data products.

   .. grid:: 5
      :gutter: 3

      {% for item in data.data_products %}
      .. grid-item-card:: :fas:`{{ item.icon }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}

.. container:: showcase-panel bg-gradient-forest reverse

   .. container::

      .. rubric:: DEA Notebooks

      Learn how to analyse our data using Jupyter notebooks.

      `Visit the DEA Notebooks </notebooks/README/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg

.. container:: showcase-panel bg-grey

   .. container::

      .. rubric:: About Digital Earth Australia

      Digital Earth Australia (DEA) is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
