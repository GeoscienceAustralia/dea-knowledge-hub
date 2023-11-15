.. rst-class:: theme-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "Browse data products." }}

.. grid:: 4
    :gutter: 3
    :class-container: card-list images bg-grey

    {% for page in data.pages %}
    .. grid-item-card:: {{ page.name }}
       :img-top: {{ page.image or "/_files/pages/dea-hero.jpg" }}
       :link: {{ page.link }}
    {% endfor %}
