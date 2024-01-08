.. highlight:: console

=======================================
Advanced Access - HPC, CLI, and THREDDS
=======================================

.. contents:: In this guide
   :local:
   :backlinks: none

High Performance Computing
==========================

The DEA environment can be accessed within the High Performance Computing (HPC)
environment (i.e. Gadi_). This will require compute and storage quota
allocations to be made via NCI's Allocation Scheme processes, on a per-project
basis. This does not need to be specific to DEA – all users with computing
capabilities on Gadi are able to access DEA through the HPC system.

.. _Gadi: https://nci.org.au/our-systems/hpc-systems/

Command Line Usage
==================

.. note:

   This section is intended for advanced users, and describes using DEA from
   a command line interface. This is mostly useful if you intend on running
   batch jobs on ``gadi`` and need to do some testing on the ``VDI``. Or simply if
   you're curious.


On ``VDI``, you can start a terminal window from **Applications** -> **System Tools**.

To manually use the modules on ``gadi`` or the ``VDI``, add the datacube module path

.. code-block:: bash

   $ module use /g/data/v10/public/modules/modulefiles/

(you can add the above to your ``.bashrc`` to avoid running it every time)

You should now be able to load the ``dea`` module by running

.. code-block:: bash

   $ module load dea

.. note::
   Behind the scenes this will load a second module called ``dea-env``
   which contains all required libraries and supporting software to use ``dea``.
   

You can see a list of available modules by running

.. code-block:: bash

   $ module avail


The first time you load the module, it will register your account with the datacube, granting you read-only access.

It will store your password in the file ``~/.pgpass``.

You can then launch a Jupyter notebook by running

.. code-block:: bash

   $ jupyter-lab <path_to_notebook>

.. note::
    ``VDI`` and ``gadi`` have separate home directories, so you must copy your pgpass to the other if
    you use both environments.

    You can push the contents of your pgpass file from the ``VDI`` to ``gadi`` by running on a terminal window in VDI

    .. code-block:: bash

       remote-hpc-cmd init
       ssh gadi "cat >> ~/.pgpass" < ~/.pgpass
       ssh gadi "chmod 0600 ~/.pgpass"

    You will most likely be prompted for your NCI password.

    To pull the contents of your pgpass from ``gadi`` to the ``VDI`` instead, run

    .. code-block:: bash

       ssh gadi "cat ~/.pgpass" >> ~/.pgpass
       chmod 0600 ~/.pgpass

.. warning::

    If you have created a ``.datacube.conf`` file in your home folder from
    early Data Cube betas, you should rename or remove it to avoid it
    conflicting with the settings loaded by the module.

THREDDS
=======

The THREDDS server is the National Computational Infrastructure (NCI)'s high-performance and high-availability installation of Unidata's Thematic Real-time Environmental Distributed Data Services (THREDDS).

THREDDS serves many of NCI's open data collections at the file level, as well as some aggregations. It provides many different types of services to allow individual files to be selected, as well as more advanced services such as OpenDAP, NetCDF subsetting, OGC WCS and WMS.

The THREDDS server is programmatically accessible, which is how many advanced tools and portals use the service.

If the data product features a THREDDS link, you can access the data in the following way:

#. Open `DEA Explorer <https://explorer.dea.ga.gov.au/>`_. Select the product of interest from the menu at the top. This will give you a tile map. The data in THREDDS is indexed according to this tile map.
#. Once you have located the tile that covers your region of interest, note the path and row numbers.
#. Open the THREDDS link for the data product.
#. The folders follow the sequence: product > path > row > year > month > day. Open each folder corresponding to the product, tile and date of interest.
