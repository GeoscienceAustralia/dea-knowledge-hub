.. rst-class:: data-products-root

===================================================================
{{ data["title"] }}
===================================================================

.. grid:: 4
    :gutter: 3

    {% for product_type in data["product_types"] %}
    .. grid-item-card:: {{ product_type.get("name") }}
       :img-top: {{ product_type.get("image", "https://www.gifpng.com/300x200") }}
       :link: {{ product_type.get("link") }}
    {% endfor %}
