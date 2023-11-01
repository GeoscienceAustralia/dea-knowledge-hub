.. rst-class:: data-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

.. grid:: 4
    :gutter: 3

    {% for page in data.pages %}
    .. grid-item-card:: {{ page.name }}
       :img-top: {{ page.image or "https://www.gifpng.com/300x200" }}
       :link: {{ page.link }}
    {% endfor %}
