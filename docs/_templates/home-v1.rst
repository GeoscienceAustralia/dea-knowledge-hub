.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

Digital Earth Australia (DEA) is a program of Geoscience Australia, an agency of the Australian Government. We create free and open satellite data products for the benefit of Australia.

The DEA Knowledge Hub brings together information about DEA’s products and services to assist you to take advantage of Australia’s free and open satellite imagery archive. 

.. container:: card-list icons
   :name: data-products

   .. rubric:: Data Products

   Explore DEA’s data products, and learn more about how they were created, how to use and access them, their version history, quality and supporting information and publications.

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

      Find step by step instructions on how to use DEA products and services, as well as important reference articles and DEA publications.

      `Visit the User Guides </guides/>`_

   .. container::

      .. image:: /_files/pages/dea-hero.jpg

.. container:: showcase-panel bg-gradient-forest reverse
   :name: dea-notebooks

   .. container::

      .. rubric:: DEA Notebooks

      Explore a repository of code examples showcasing DEA products, how-to-guides and common earth observation patterns and case studies using Jupyter Notebooks.

      `Visit the DEA Notebooks </notebooks/README/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg

.. container:: showcase-panel
   :name: about-dea

   .. container::

      .. rubric:: About Digital Earth Australia

      It’s DEA’s mission to embed satellite imagery and data into decisions that support a sustainable Australian environment, a resilient society and a strong economy.

      To find out more about the DEA program, our strategy and journey to get here, as well as program news feeds and to `subscribe to the DEA newsletter <https://www.dea.ga.gov.au/news/dea-newsletter-and-communications-archive>`__, `visit the DEA website <https://www.dea.ga.gov.au/>`__.

   .. container::

      .. image:: /_files/themes/sea-ocean-and-coast.* 
