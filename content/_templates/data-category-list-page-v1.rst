.. rst-class:: data-category-list-page

===================================================================
{{ data["title"] }}
===================================================================

.. grid:: 4
    :gutter: 3

    {% for theme in data["themes"] %}
    .. grid-item-card:: {{ theme.get("name") }}
       :img-top: {{ theme.get("image", "https://www.gifpng.com/300x200") }}
       :link: themes/{{ theme.get("slug") }}
    {% endfor %}

.. dropdown:: List of all products

   .. tableofcontents::
