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

      `{{ custom_link_text or f"View the {panel.name}" }} <{{ panel.link }}>`_

   .. container::

      .. image:: {{ panel.image }}
         :class: no-gallery
{% endfor %}
