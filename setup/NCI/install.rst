
.. _install:

============================================================
Connecting to the NCI's Virtual Desktop Infrastructure (VDI)
============================================================

.. note::
   As of 2021, the Open OnDemand (OOD) online portal is now the recommended method for 
   accessing the NCI's Virtual Desktop Infrastructure (VDI), replacing the previous 
   Strudel/Turbo VNC method. This allows you more easily access NCI systems from a 
   browser without needing to install software.   

.. note::
   The NCI released a new version of the Virtual Desktop Infrastructure (VDI) on 28/10/2020. 
   If you are having trouble connecting to the VDI after this date (and did not have trouble
   before this date) please consult the most recent 
   `VDI FAQ help <https://opus.nci.org.au/display/Help/4.+VDI+FAQ>`_
   
The NCI's Open OnDemand (OOD) online portal allows users to quickly connect to Digital 
Earth Australia from a web browser. 
To get started with the OOD portal, please follow the following NCI guide:

* `Introduction to Open OnDemand (OOD) <https://opus.nci.org.au/display/OOD/0.+Introduction+to+OOD>`_

Launching the VDI from OOD
==========================

After successfully logging into the OOD, you will see the OOD Dashboard below. We recommend that most users select the "Virtual Desktop" option which will launch an interactive virtual desktop session that can be used to access DEA. 

The following NCI guide introduces how to connect to the VDI for the first time:

* `Connecting to the VDI <https://opus.nci.org.au/display/OOD/2.1.+Connecting+to+the+VDI>`_

.. figure:: https://opus.nci.org.au/download/attachments/116719863/image2021-7-12_12-33-36.png?version=1&modificationDate=1626057216773&api=v2
   :align: center
   :alt: Install DEA on NCI


Setting up Digital Earth Australia
==================================

Once you have successfully launched the VDI, you can install Digital Earth Australia.

From the **Applications** menu in the top left of the screen, choose **System Tools** -> **Terminal**.

.. figure:: /_static/NCI/vdi-launch-terminal.png
   :align: center
   :alt: Start Terminal Menu

In the terminal window run the command::

   sh /g/data/v10/public/digitalearthau/install.sh

This will download the latest version of the `Digital Earth Australia notebooks repository <https://github.com/GeoscienceAustralia/dea-notebooks/tree/stable>`_ into your VDI home directory (e.g. ``~/dea-notebooks``).

Once this has completed, click **Applications** menu in the top left of the screen, then **Science**.
This menu will now include a new program called **Digital Earth Australia**.

.. figure:: /_static/NCI/dea_install.jpg
   :align: center
   :alt: Install DEA on NCI

You can then click this icon to launch Jupyter Lab with the Digital Earth Australia environment preconfigured.
From within this environment you can access the notebooks from the User Guide, or create your own notebooks to work with Digital Earth Australia.

.. note::
   For more information about getting started with Digital Earth Australia on the NCI, refer to the `Digital Earth Australia Notebooks wiki page <https://github.com/GeoscienceAustralia/dea-notebooks/wiki#getting-started-on-the-ncivirtual-desktop-infrastructure>`_.

