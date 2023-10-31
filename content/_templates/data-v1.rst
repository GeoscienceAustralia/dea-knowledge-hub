.. rst-class:: data-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description }}

.. grid:: 4
    :gutter: 3

    {% for theme in data.themes %}
    .. grid-item-card:: {{ theme.name }}
       :img-top: {{ theme.image or "https://www.gifpng.com/300x200" }}
       :link: /data/themes/{{ theme.slug }}
    {% endfor %}
