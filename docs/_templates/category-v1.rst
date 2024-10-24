{% if data.description %}
.. meta::
   :description: {{ data.description }}
{%- endif %}

.. rst-class:: category-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "This category contains the following products." }}

.. tableofcontents::
