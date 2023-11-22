.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description }}

.. container:: card-list icons
   :name: data-products

   .. rubric:: Data Products

   Find product metadata on our data products.

   .. grid:: 2 2 3 5
      :gutter: 3

      {% for item in data.data_product_themes %}
      .. grid-item-card:: :fas:`{{ item.icon }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}

.. container:: showcase-panel bg-gradient-primary
   :name: user-guides

   .. container::

      .. rubric:: User Guides

      Learn how to use our products and services.

      `Visit the User Guides </guides/>`_

   .. container::

      .. image:: /_files/pages/dea-hero.jpg

.. container:: showcase-panel bg-gradient-forest reverse
   :name: dea-notebooks

   .. container::

      .. rubric:: DEA Notebooks

      Learn how to analyse our data using Jupyter notebooks.

      `Visit the DEA Notebooks </notebooks/README/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg

.. container:: showcase-panel
   :name: about-dea

   .. container::

      .. rubric:: About Digital Earth Australia

      Digital Earth Australia (DEA) is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia.

      To find case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.

   .. container::

      .. image:: /_files/themes/sea-ocean-and-coast.* 
