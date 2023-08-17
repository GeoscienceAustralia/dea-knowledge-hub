
.. _install:

=======================================
Basics - JupyterLab and Virtual Desktop
=======================================


Australian Research Environment
===============================

The easiest access to Digital Earth Australia on the NCI is via their
:term:`Australian Research Environment<ARE>`. It lets you use your web browser to
run a complete Virtual Desktop or execute code in JupyterLab Notebooks.

It's also possible to access DEA on the NCI's Gadi_ :term:`HPC` Supercomputer, but unless
you're experienced with :term:`SSH` and HPC systems, it's much easier to get
started on :term:`ARE`.



.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
   
Launching JupyterLab from ARE
=============================

The NCI's Australian Research Environment (ARE) online portal allows users to
quickly connect to Digital Earth Australia from a web browser. 

To get started with the ARE portal, please follow the NCI 
`ARE User Guide <https://opus.nci.org.au/display/Help/ARE+User+Guide>`_.

1. After successfully logging into ARE, you will see the ARE Dashboard. 

2. From here, choose **JupyterHub** to launch a new session.

3. The first time you start a session, there are a few options you need to configure.

   **Storage**

   Type `gdata/v10` into the **Storage**, then use the dropdown to select other
   projects containing data you wish to access.

   .. figure:: are_highlight_v10_storage_setting.png

   **DEA Environment**

   Scroll down and expand the **Advanced** options, and set:

   **Module directories** to ``/g/data/v10/public/modules/modulefiles``.

   **Modules** to ``dea``.

   As seen here:

   .. video:: /_static/are_jupyterhub_launch_setup.webm
      :loop:
      :autoplay:
      :nocontrols:
      :muted:


Virtual Desktops with ARE
=========================



Setting up Digital Earth Australia
==================================

In the terminal window run the command::

   sh /g/data/v10/public/digitalearthau/install.sh

This will download the latest version of the `Digital Earth Australia notebooks repository <https://github.com/GeoscienceAustralia/dea-notebooks/tree/stable>`_ into your VDI home directory (e.g. ``~/dea-notebooks``).


