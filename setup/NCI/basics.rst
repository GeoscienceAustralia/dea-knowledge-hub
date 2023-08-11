
.. _install:

===================================================
Basics - Using JupyterLab and Virtual Desktop (ARE)
===================================================


Australian Research Environment
===============================

The easiest way to use Digital Earth Australia on the NCI is to use their
:term:`Australian Research Environment<ARE>`. It allows you to sign in and access
Virtual Desktop and JupyterLab Notebook environments via a web browser.

It is possible to run on the NCI's Gadi_ :term:`HPC` Supercomputer, but unless
you're experience with :term:`SSH` and HPC systems, it's a lot easier to get
started on :term:`ARE` first.

High Performance Computing
==========================

The DEA environment can be accessed within the High Performance Computing (HPC)
environment (i.e. Gadi_). This will require compute and storage quota
allocations to be made via NCI's Allocation Scheme processes, on a per-project
basis. This does not need to be specific to DEA – all users with computing
capabilities on Gadi are able to access DEA through the HPC system.


.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
   
Launching JupyterLab from ARE
=============================

The NCI's Australian Research Environment (ARE) online portal allows users to
quickly connect to Digital Earth Australia from a web browser. 

To get started with the ARE portal, please follow the following NCI guide:

   `ARE User Guide <https://opus.nci.org.au/display/Help/ARE+User+Guide>`_

After successfully logging into ARE, you will see the ARE Dashboard. The following NCI guide introduces how to connect to the VDI for the first time:


Setting up Digital Earth Australia
==================================

In the terminal window run the command::

   sh /g/data/v10/public/digitalearthau/install.sh

This will download the latest version of the `Digital Earth Australia notebooks repository <https://github.com/GeoscienceAustralia/dea-notebooks/tree/stable>`_ into your VDI home directory (e.g. ``~/dea-notebooks``).


