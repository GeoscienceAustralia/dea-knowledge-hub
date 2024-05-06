.. rst-class:: panel-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

{% for panel in data.panels %}
.. container:: showcase-panel

   .. container::

      .. rubric:: {{ panel.name }}

      {{ panel.description }}

      {% if panel.custom_link_text %}
      `{{ panel.custom_link_text }} <{{ panel.link }}>`_
      {% else %}
      `View the {{ panel.name }} <{{ panel.link }}>`_
      {% endif %}

   .. container::

      .. image:: {{ panel.image }}
         :class: no-gallery
{% endfor %}
