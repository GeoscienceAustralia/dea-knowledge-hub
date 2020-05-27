

.. _changelog:

===========
 Changelog
===========

2020-01-09
==========

The `DEA Notebooks repository <https://github.com/GeoscienceAustralia/dea-notebooks/>`_ 
and the DEA user guide received a `major update <https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/notebooks_refresh>`_ which includes a simplified directory structure and set of improved and easier to use Jupyter notebooks.

These updated notebooks include a new Beginner's Guide aimed at introducing users to DEA and the Open Data Cube. To view these
new notebooks, navigate to the :ref:`#beginner-s-guide` section of the User Guide.

2019-03-12
==========

Users are now required to join all projects containing data they wish to use. Before this change
all the DEA data was public to NCI users without any further steps.

See :ref:`data_access` for more details.

2018-02-28
==========


 * Rename module to `dea`. Most people should now run::

    module use /g/data/v10/public/modules
    module load dea

 * Include JupyterLab_ as an alternative to Jupyter Notebooks. To use, from a shell run::

      jupyter-lab

 * Include pre-release version 1.6 of Open Data Cube

 * Drop support for Python 2





.. _JupyterLab: https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906
