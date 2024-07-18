.. rst-class:: card-description-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. container:: card-list descriptions

   .. grid:: 2 2 2 3
       :gutter: 3

       {% for card in data.cards %}
       .. grid-item-card::

          .. container:: image-container

             .. image:: {{ card.image or "/_files/default/dea-earth-thumbnail.jpg" }}
                :class: no-gallery

          .. rubric:: {{ card.name }}

          {{ card.description }}
       {% endfor %}
