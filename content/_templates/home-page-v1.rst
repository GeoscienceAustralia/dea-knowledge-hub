.. rst-class:: home

===================================================================
{{ data["title"] }}
===================================================================

.. image:: _static/images/home-page-hero.png
   :alt: Digital Earth Australia logo

.. rubric:: Welcome to the DEA Documentation
   :class: rubric-1

.. grid:: 3
   :gutter: 3

   .. grid-item-card::

      Access the data ...
      ^^^^^^^^^^^^^^^^^^^

      {% for access_link in data["access_links"] %}
      `{{ access_link.get("name") }} <{{ access_link.get("link") }}>`_
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

Digital Earth Australia is an analysis platform for satellite imagery and other Earth observations. To see case studies, learning modules, developer portal, and more, `visit the DEA website <https://www.dea.ga.gov.au/>`_.
