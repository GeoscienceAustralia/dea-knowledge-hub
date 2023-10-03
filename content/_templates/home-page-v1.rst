.. rst-class:: home-page

===================================================================
{{ data["title"] }}
===================================================================

.. image:: _static/images/home-page-hero.png
   :alt: Digital Earth Australia logo

.. rubric:: DEA Documentation and Metadata Hub
   :class: rubric-1

Here you will find metadata for Geoscience Australia's earth observation data products and also documentation for using this data.

.. grid:: 3
   :gutter: 3

   .. grid-item-card::

      Access the data ...
      ^^^^^^^^^^^^^^^^^^^

      {% for theme in data["themes"] %}
      `{{ theme.get("name") }} <{{ theme.get("link") }}>`_
      {% endfor %}

   .. grid-item-card::

      Use the data ...
      ^^^^^^^^^^^^^^^^
   
      `Get started with DEA <example.com>`_

      `View all notebooks <example.com>`_

      `Use the DEA Tools package <example.com>`_

      `Additional resources <example.com>`_

   .. grid-item-card::

      Our program ...
      ^^^^^^^^^^^^^^^

      `View our service catalogue <example.com>`_

      `Get support <{{ config.html_context["support_link"] }}>`_

.. rubric:: About the DEA
   :class: rubric-2

Digital Earth Australia is an analysis platform for satellite imagery and other Earth observations. It is a program of Geoscience Australia. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
