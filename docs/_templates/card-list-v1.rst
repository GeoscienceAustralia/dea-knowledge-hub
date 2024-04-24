.. rst-class:: card-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. container:: card-list images

   .. grid:: 2 2 3 4
       :gutter: 3

       {% for page in data.pages %}
       .. grid-item-card::
          :link: {{ page.link }}

          .. container:: image-container

             .. image:: {{ page.image or "/_files/pages/dea-hero.jpg" }}
                :class: no-gallery

          .. rubric:: {{ page.name }}
       {% endfor %}
