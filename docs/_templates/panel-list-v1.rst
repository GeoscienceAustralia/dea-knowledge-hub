.. rst-class:: panel-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

{% for panel in data.panels %}
.. container:: showcase-panel reverse

   .. container::

      .. rubric:: {{ panel.name }}

      {{ panel.description }}

      {% if panel.custom_link_text %}
      `{{ panel.custom_link_text }} <{{ panel.link }}>`_
      {% else %}
      `View the {{ panel.name }} <{{ panel.link }}>`_
      {% endif %}

   .. container::

      .. image:: {{ panel.image or "/_files/pages/dea-hero.jpg" }}
         :class: no-gallery
         :target: {{ panel.link }}
{% endfor %}
