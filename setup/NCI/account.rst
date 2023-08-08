
.. _account:

======================
 Account Registration
======================

.. image:: /_static/NCI/nci_user_registration.png
   :alt: description
   :align: right
   :scale: 20%

The Digital Earth Australia analysis environment is currently available for
Australian government and academic users eligible for accounts on `National
Computational Infrastructure`_ (NCI).

Use the `NCI Account Sign Up`_ page with your government or academic
institutional email address.


.. important::
   When signing up, you need to join some :ref:`data_access` projects 
   to access the DEA data.



.. _National Computational Infrastructure: https://www.nci.org.au/
.. _NCI Account Sign Up: https://my.nci.org.au/mancini/signup/

Commercial access
=================

Commercial entities wanting to participate in project partnerships or training
with DEA should contact the |DEA Helpdesk|.

NCI can also provision compute and storage resources to commercial entities
under contract for those looking to leverage DEA resources. It is suggested that
commercial entities contact the  |DEA Helpdesk| to help determine requirements.

.. |DEA Helpdesk| replace:: `DEA Helpdesk <mailto:earth.observation@ga.gov.au>`_

Australian Research Environment
===============================

The easiest way to use Digital Earth Australia on the NCI is to use their
:term:`Australian Research Environment<ARE>`. It allows you to sign in and access
Virtual Desktop and JupyterLab Notebook environments via a web browser.

It is possible to run on the NCI's Gadi_ :term:`HPC` Supercomputer, but unless
you're experience with :term:`SSH` and HPC systems, it's a lot easier to get
started on :term:`ARE` first.

.. _data_access:

Data Access
===========

DEA Data is stored on several "GData filesystems" on the NCI. To access the data you 
need to request access to one or more of the **Projects** listed below.

Use `MyNCI <https://my.nci.org.au/>`_ to view and manage your project memberships.

.. list-table:: NCI Data Access Projects
   :header-rows: 1

   * - Project
     - Contents

   * - xu18_
     - Geoscience Australia Landsat Analysis Ready Data (Collection 3)
 
   * - ka08_
     - Geoscience Australia Sentinel-2 Analysis Ready Data (Collection 3)
     
   * - jw04_
     - Geoscience Australia Landsat Derivatives (Collection 3), e.g. WO, FC

   * - fk4_
     - Legacy Geoscience Australia Landsat Derivatives (Collection 2), e.g. NIDEM, ITEM, HLTC
 
   * - if87_
     - Legacy Geoscience Australia Sentinel-2 Analysis Ready Data (Collection 1)
     
.. _wd8: https://my.nci.org.au/mancini/project/wd8
.. _xu18: https://my.nci.org.au/mancini/project/xu18
.. _if87: https://my.nci.org.au/mancini/project/if87
.. _jw04: https://my.nci.org.au/mancini/project/jw04
.. _fk4: https://my.nci.org.au/mancini/project/fk4
.. _rs0: https://my.nci.org.au/mancini/project/rs0
.. _ka08: https://my.nci.org.au/mancini/project/ka08

High Performance Computing
==========================

The DEA environment can be accessed within the High Performance Computing (HPC)
environment (i.e. Gadi_). This will require compute and storage quota
allocations to be made via NCI's Allocation Scheme processes, on a per-project
basis. This does not need to be specific to DEA – all users with computing
capabilities on Gadi are able to access DEA through the HPC system.

This guide focuses on accessing and exploring DEA via the VDI environment.


.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
