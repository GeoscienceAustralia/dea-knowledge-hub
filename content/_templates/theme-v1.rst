.. rst-class:: theme-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{% for catalog in data.catalogues %}
.. rubric:: {{ catalog.name }}
   :name: {{ catalog.id }}

.. grid:: 4
   :gutter: 3

   {% for product in catalog.products %}
   .. grid-item-card:: {{ product.name }}
      :img-top: {{ product.image or "https://www.gifpng.com/300x200" }}
      :link: /data/products/{{ product.slug }}
   {% endfor %}
{% endfor %}
