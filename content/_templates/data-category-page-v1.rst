.. rst-class:: data-category-page

===================================================================
{{ data["title"] }}
===================================================================

{% for catalog in data["catalogues"] %}
.. rubric:: {{ catalog.get("name") }}
   :name: {{ catalog.get("id") }}

.. grid:: 4
   :gutter: 3

   {% for product in catalog["products"] %}
   .. grid-item-card:: {{ product.get("name") }}
      :img-top: {{ product.get("image", "https://www.gifpng.com/300x200") }}
      :link: {{ product.get("link") }}
   {% endfor %}
{% endfor %}
