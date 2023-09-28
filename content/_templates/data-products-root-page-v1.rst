.. rst-class:: data-products-root

{{ data["title"] }}
===================

.. grid:: 4
    :gutter: 3

    {% for item in data["items"] %}
    .. grid-item-card:: {{ item.get("name") }}
       :img-top: {{ item.get("image", "https://www.gifpng.com/300x200") }}
       :link: {{ item.get("link") }}
    {% endfor %}
