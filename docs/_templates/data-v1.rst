.. rst-class:: data-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. container:: card-list images bg-grey

   .. grid:: 4
       :gutter: 3

       {% for page in data.pages %}
       .. grid-item-card:: {{ page.name }}
          :img-top: {{ page.image or "/_files/pages/dea-hero.jpg" }}
          :link: {{ page.link }}
       {% endfor %}
