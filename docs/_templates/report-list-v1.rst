{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

.. rst-class:: report-list-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "I'm interested in ..." }}

{% for report in data.reports %}
.. container:: showcase-panel reverse

   .. container::

      .. rubric:: {{ report.name }}

      {{ report.description }}

      {% if report.custom_link_text %}
      `{{ report.custom_link_text }} <{{ report.link }}>`_
      {% else %}
      `View the report <{{ report.link }}>`_
      {% endif %}

   .. container::

      .. image:: {{ report.image or "/_files/default/dea-earth-thumbnail.jpg" }}
         :class: no-lightbox
         :target: {{ report.link }}
{% endfor %}
