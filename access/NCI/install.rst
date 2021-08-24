
.. _install:

Installation and Software Setup
*******************************

Required Software
=================

Install TurboVNC and Strudel according to the instructions at http://vdi.nci.org.au/help.

.. note::
   The NCI released a new version of the Virtual Desktop Infrastructure (VDI) on 28/10/2020. 
   If you are having trouble connecting to the VDI after this date (and did not have trouble
   before this date) please consult the most recent 
   `VDI FAQ help <https://opus.nci.org.au/display/Help/4.+VDI+FAQ>`_
   
.. note::
   The NCI instructions recommend specific versions of 
   `TurboVNC <https://sourceforge.net/projects/turbovnc/files/>`_ and
   `Strudel <https://cvl.massive.org.au/launcher_files/stable/>`_.
   More recent versions may or may not be compatible with the VDI.

.. note::
   Your institution may provide this software to be installed via an internal process.
   For example at Geoscience Australia, the software can be requested from the
   `Software Service Management System (SSMS) <http://intranet.ga.gov.au/CherwellPortal/SSMS>`_
   [internal link only].

Connecting to the VDI
=====================

To setup Strudel to connect to the NCI, run the Strudel application, then:

* Select **File** -> **Manage Sites**
* Click **New**
* Enter the details:

  - Name: **NCI Virtual Desktops**
  - URL: **https://vdi.nci.org.au/strudel.json**

* Click **OK**
* Make sure the **Active** checkbox is ticked.
* Click **OK**

To connect:

* Site: **NCI Virtual Desktops**
* Username: Your NCI username (eg ``abc123`` or ``ab1234``)
* Click **Login**

.. note::
   If the drop-down site list in Strudel remains empty, it most likely means 
   that the software is unable to retrieve the ``strudel.json`` URL, 
   such as due to firewall or network proxy configuration.

Setting up DEA
==============

Once you have logged on to the VDI, you can install Digital Earth Australia.

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

Shutting Down VDI
=================

After you have finished working on the VDI, any open terminals can be closed using the x in
the corner of the tab and the VDI can be closed by clicking your name displayed in the top
right corner of the VDI interface and selecting Quit. The Strudel window will subsequently also
close after a few moments.

If you wish to disconnect from the VDI but keep the session running you can close the VDI
window using the x in the top right corner of the window and select keep the session running
when prompted by the Strudel window. Later you can reconnect to the VDI and resume the previous
session.
