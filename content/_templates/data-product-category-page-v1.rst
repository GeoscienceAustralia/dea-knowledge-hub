.. rst-class:: data-product-category

{{ data["title"] }}
===================================================================

{% for item in data["items"] %}
.. rubric:: {{ item.get("name") }}
   :name: {{ item.get("id") }}

.. grid:: 4
   :gutter: 3

   {% for item in item["items"] %}
   .. grid-item-card:: {{ item.get("name") }}
      :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
      :link: {{ item.get("link") }}
   {% endfor %}
{% endfor %}
