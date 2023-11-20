.. rst-class:: data-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. container:: card-list images

   .. grid:: 4
       :gutter: 3

       {% for page in data.themes %}
       .. grid-item-card::
          :link: {{ page.link }}

          .. container:: image-container

             .. image:: {{ page.image or "/_files/pages/dea-hero.jpg" }}

          .. rubric:: {{ page.name }}
       {% endfor %}
