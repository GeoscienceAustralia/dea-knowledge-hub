.. rst-class:: card-clickable-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. container:: card-list images

   .. grid:: 2 2 3 4
       :gutter: 3

       {% for card in data.cards %}
       .. grid-item-card::
          :link: {{ card.link }}

          .. container:: image-container

             .. image:: {{ card.image or "/_files/default/dea-earth-thumbnail.jpg" }}
                :class: no-lightbox

          .. rubric:: {{ card.name }}
       {% endfor %}
