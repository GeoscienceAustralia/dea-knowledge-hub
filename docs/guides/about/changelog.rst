

.. _changelog:

===========
 Changelog
===========

2023-08-11
==========

Technical DEA internals which have changed in the last week.

- Some tweaks to DEA Sandbox DNS resolution last Friday.
- The URL https://explorer.dea.ga.gov.au/ will be changed to show data in 
  the DEA AWS data holdings instead of the NCI holdings.
- Some data gap filling of Lansat 8 ARD, Landsat 8 FC and Landsat 8 WO for 2023.
- Reduced the delay between Sentinel 2 ARD data being produced (on the NCI), and being 
  delivered to AWS. It was *up to 48 hours* and should now be *up to 24 hours*.



2021-07-16
==========

Thanks to the `Geoscience Australia Landsat Collection Upgrade (video)
<https://www.youtube.com/watch?v=BNEIG91lu44>`_, our data catalogue now
includes Collection 3 data for `DEA Surface Reflectance
<https://cmi.ga.gov.au/collection/geoscience-australia-landsat-collection-3>`_,
also available through `OWS <https://ows.dea.ga.gov.au/>`_. Other Collection 3
products will soon follow, including DEA Water Observations (WOfS), and DEA
Fractional Cover.
 
`DEA Notebooks <https://github.com/GeoscienceAustralia/dea-notebooks/tree/develop/DEA_datasets>`_ 
and the `User Guide`_ have been updated with Collection 3 code examples to reflect the upgrade, 
and our `Content Management Interface <https://cmi.ga.gov.au/>`_ and 
`DEA Maps platforms <https://maps.dea.ga.gov.au/>`_ are also being updated.
 
Users of Collection 2 are encouraged to use Collection 3 data.
A staged decommissioning of Collection 2 is underway and will continue into 2022.
Questions can be raised to dea@ga.gov.au.

.. _User Guide: ../notebooks/Beginners_guide/README.rst


2021-04-15
==========

Added a new guide to accessing DEA data via `Amazon Web Services`_.

.. _Amazon Web Services: ../access/AWS/data_and_metadata.rst


2020-01-09
==========

The `DEA Notebooks repository <https://github.com/GeoscienceAustralia/dea-notebooks/>`_ 
and the DEA user guide received a `major update <https://github.com/GeoscienceAustralia/dea-notebooks/releases/tag/notebooks_refresh>`_ which includes a simplified directory structure and set of improved and easier to use Jupyter notebooks.

These updated notebooks include a new Beginner's Guide aimed at introducing users to DEA and the Open Data Cube. To view these
new notebooks, navigate to the `Beginner's Guide <https://docs.dea.ga.gov.au/notebooks/Beginners_guide/README.html>`_ section of the User Guide.

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
