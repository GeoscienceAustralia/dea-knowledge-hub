{% if data.meta_description %}
.. meta::
   :description: {{ data.meta_description }}
{%- endif %}

.. rst-class:: category-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description if data.description else "This category contains the following products." }}

.. tableofcontents::
