
.. _install:

=======================================
Basics - JupyterLab and Virtual Desktop
=======================================

.. contents:: In this guide
   :local:
   :backlinks: none

Australian Research Environment
===============================

The easiest way to access Digital Earth Australia on the NCI is via the
:term:`Australian Research Environment<ARE>`. ARE has full access to the
NCI Gadi_ :term:`HPC` Supercomputer, allowing you to run analyses using
DEA at scale through your web browser via either an interactive JupyterLab
session, or a Virtual Desktop environment.

For more information on ARE see the `NCI's
ARE User Guide <https://opus.nci.org.au/display/Help/ARE+User+Guide>`_.

.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
   
Launching JupyterLab from ARE
-----------------------------

.. note:: To run an ARE session you must be part of a project at
   NCI with compute capacity. DEA does not currently
   provide access to such a project.

ARE allows you to run code directly using Jupyter Notebooks via a JupyterLab interface. This
is the recommended and simplest way to interact with ARE.

To launch a JupyterLab session, follow the instructions in `Starting JupyterLab
App (ARE User Guide) <https://opus.nci.org.au/display/Help/3.1+Starting+JupyterLab+App>`_ 
page in the NCI Help. See below for the settings required to use DEA.

Launching Virtual Desktops with ARE
-----------------------------------
Another option for accessing the NCI via ARE is to launch an interactive Virtual Desktop. This
allows you to run your analyses using a similar interactive interface to your personal computer.

To launch an Virtual Desktop, follow the instructions in `Connecting to
the VDI <https://opus.nci.org.au/display/Help/2.1.+Connecting+to+the+VDI>`_ page in the 
NCI Help. See below for the settings required to use DEA.

DEA access settings
-------------------

The first time you start a JupyterLab or Virtual Desktop session, there are some settings required
to access DEA.

**Storage**

To access data on the NCI's filesystem, you need to list all NCI projects containing data
you wish to access. Most importantly, this includes the ``v10`` NCI project that contains
files required to set up Datacube.

Type `gdata/v10` into the :guilabel:`Storage` box, then use the dropdown to select other
projects containing data you wish to access. See :ref:`nci_data_access`.

.. figure:: /_files/nci/are_highlight_v10_storage_setting.png

**DEA Environment**

DEA provides a pre-packaged NCI environment containing all important Python packages required
to run a Datacube analysis. To use this environment, we need to specify it when we launch a
JupyterLab or Virtual Desktop session.

Scroll down and expand :guilabel:`Advanced options...`.

Set :guilabel:`Module directories` to ``/g/data/v10/public/modules/modulefiles``.

Set :guilabel:`Modules` to ``dea``.


.. raw:: html

   <video loop autoplay nocontrols muted>
      <source src="/_static/nci/are_jupyterhub_launch_setup.webm" type="video/webm">
   </video>


.. dropdown:: Troubleshooting: 'fe_sendauth: no password supplied'

   When the ``dea`` module is first run, a Datacube database role and ``.pgpass`` password
   file is automatically created for you in your home directory. If you used a previous
   version of the NCI's Virtual Desktop software (e.g. VDI, OOD), you may need to copy
   this original ``.pgpass`` file into your new ARE home directory. If you cannot locate
   your ``.pgpass`` file, please contact earth.observation@ga.gov.au to request for your
   DEA database account to be reset.


Setting up Digital Earth Australia
==================================

You will need to install DEA the first time you launch a session.

In a terminal window in either JupyterLab or the ARE Virtual Desktop, run the command::

   sh /g/data/v10/public/digitalearthau/install.sh

This will download the latest version of the `Digital Earth Australia notebooks
repository <https://github.com/GeoscienceAustralia/dea-notebooks/tree/stable>`_
into your home directory (e.g. :file:`~/dea-notebooks`).

.. note:: DEA Notebooks is a large repository that will take up a large proportion of
   available storage space in your home directory. We recommend cloning a new copy 
   of the repository to a location on ``/g/data/`` when possible. (Learn how to `clone
   DEA Notebooks <https://github.com/GeoscienceAustralia/dea-notebooks/wiki/Edit-a-DEA-Notebook>`_.)



