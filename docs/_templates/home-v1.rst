{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description }}

.. container:: card-list icons
   :name: data-products

   .. rubric:: Data Products

   .. raw:: html

      <p>Browse our <a href="/data/">catalogue of data products</a> to find supporting information and ways to access the data.</p>

   .. grid:: 2 2 3 6
      :gutter: 3

      {% for item in data.product_themes %}
      .. grid-item-card:: :fas:`{{ item.icon }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}

.. container:: showcase-panel bg-gradient-primary
   :name: user-guides

   .. container::

      .. rubric:: User Guides

      Find documentation, step-by-step instructions, and DEA publications on a variety of topics.

      `Visit the User Guides </guides/>`_

   .. container::

      .. image:: /_files/default/dea-earth-thumbnail.jpg
         :class: no-gallery

.. container:: showcase-panel bg-gradient-forest reverse
   :name: dea-notebooks

   .. container::

      .. rubric:: DEA Notebooks

      Explore visual walkthroughs that show how to analyse our data using Python, including the use our DEA Tools package.

      `Visit the DEA Notebooks </dea-notebooks/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg
         :class: no-gallery

.. container:: showcase-panel bg-gradient-stone
   :name: dea-notebooks

   .. container::

      .. rubric:: Validation reports

      How well does DEA's satellite-derived Analysis Ready Data compare with field-derived surface reflectance data? These reports provide this comparison.

      `Visit the Validation reports </validation/>`_

   .. container::

      .. image:: /_files/validation/validation-drone-thumbnail.jpg
         :class: no-gallery

.. container:: showcase-panel bg-gradient-space reverse
   :name: changelog

   .. container::

      .. rubric:: DEA Tech Alerts and Changelog

      Find out about the latest updates to DEA's products and services, planned maintenance, and any outages that may occur.

      `Visit the DEA Tech Alerts and Changelog </tech-alerts-changelog/>`_

   .. container::

      .. image:: /_files/reference/Reporting_dashboard.png
         :class: no-gallery

.. container:: showcase-panel
   :name: about-dea

   .. container::

      .. rubric:: About Digital Earth Australia

      `Digital Earth Australia <https://www.dea.ga.gov.au/>`_ (DEA) is a program of `Geoscience Australia <https://www.ga.gov.au/>`_, an entity of the Australian Government.

      It is our mission is to embed satellite imagery and data into decisions that support a sustainable Australian environment, a resilient society, and a strong economy.

      `Visit the DEA website <https://www.dea.ga.gov.au/>`_

      `Subscribe to our newsletter <https://communication.ga.gov.au/dea-news-subscribe>`_

   .. container::

      .. image:: /_files/themes/sea-ocean-and-coast.* 
         :class: no-gallery
