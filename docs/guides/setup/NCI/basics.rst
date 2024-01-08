
.. _install:

=======================================
Basics - JupyterLab and Virtual Desktop
=======================================

.. contents:: In this guide
   :local:
   :backlinks: none

Australian Research Environment
===============================

The easiest access to Digital Earth Australia on the NCI is via the
:term:`Australian Research Environment<ARE>`. Through your web browser you can
access a Virtual Desktop environment or execute code in JupyterLab Notebooks.

For more information on ARE see the `NCI's
ARE User Guide <https://opus.nci.org.au/display/Help/ARE+User+Guide>`_.

It's also possible to use DEA on the NCI's Gadi_ :term:`HPC` Supercomputer,
however unless you're experienced with :term:`SSH` and HPC systems, it's much
easier to get started with :term:`ARE`.


.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
   
Launching JupyterLab from ARE
=============================

To launch a JupyterLab session, follow the instructions in `Starting JupyterLab
App (ARE User Guide) <https://opus.nci.org.au/display/Help/3.1+Starting+JupyterLab+App>`_ 
page in the NCI Help. See below for the settings required to use DEA .

.. note:: To run an ARE session you must be part of a project at
   NCI with compute capacity. DEA does not currently
   provide access to such a project.

Access to DEA
-------------

The first time you start a JupyterLab session, there are some settings required
to access DEA.

**Storage**

Type `gdata/v10` into the :guilabel:`Storage` box, then use the dropdown to select other
projects containing data you wish to access. See :ref:`nci_data_access`.

.. figure:: /_files/nci/are_highlight_v10_storage_setting.png

**DEA Environment**

Scroll down and expand :guilabel:`Advanced options...`.

Set :guilabel:`Module directories` to ``/g/data/v10/public/modules/modulefiles``.

Set :guilabel:`Modules` to ``dea``.


.. raw:: html

   <video loop autoplay nocontrols muted>
      <source src="/_static/nci/are_jupyterhub_launch_setup.webm" type="video/webm">
   </video>


Virtual Desktops with ARE
=========================



Setting up Digital Earth Australia
----------------------------------

In the terminal window run the command::

   sh /g/data/v10/public/digitalearthau/install.sh

This will download the latest version of the `Digital Earth Australia notebooks
repository <https://github.com/GeoscienceAustralia/dea-notebooks/tree/stable>`_
into your home directory (e.g. :file:`~/dea-notebooks`).


