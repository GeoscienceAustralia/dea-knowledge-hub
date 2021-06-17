
.. _account:

======================
 Account Registration
======================

.. image:: nci_user_registration.png
   :alt: description
   :align: right
   :scale: 20%

The Digital Earth Australia analysis environment is currently available for
Australian government and academic users eligible for accounts on `National
Computational Infrastructure`_ (NCI).

Use the `NCI Account Sign Up`_ page with your government or academic
institutional email address.


.. important::
   When signing up, you will need to join at least the ``v10`` project for
   access to the DEA code environment and ``wd8`` for VDI access.

   You **also** need to join some of the :ref:`data_access` projects listed
   below to access the DEA data.



.. _National Computational Infrastructure: https://www.nci.org.au/
.. _NCI Account Sign Up: https://my.nci.org.au/mancini/signup/

Commercial access
=================

Commercial entities wanting to participate in project partnerships or training
with DEA should contact earth.observation@ga.gov.au.

NCI can also provision compute and storage resources to commercial entities
under contract for those looking to leverage DEA resources. It is suggested that
commercial entities contact DEA in the first instance through
earth.observation@ga.gov.au to help determine requirements.

Virtual Desktop Analysis
========================

The easiest way to use Digital Earth Australia is to connect to a remote desktop
at the NCI called :term:`VDI`. (It is also possible to run on the NCI's Gadi_
HPC cluster, but it's recommended that you prototype on VDI first.)

Your NCI account will need to be a member of a VDI project. You can view your
project memberships at https://my.nci.org.au/. If you do not already have access to
a VDI project, you can request to join the **wd8** project. Once approved, you
will be a member of the project and able to access DEA through the VDI.

.. _data_access:

Data Access
===========

DEA Data is store in a variety of locations on the NCI, knows as *projects*. You
need to request access to projects individually, depending on the data you will
need to access.

Do this by using the same process as joining a VDI Project as described above.

.. list-table:: NCI Data Access Projects
   :header-rows: 1

   * - Project
     - Contents

   * - rs0_
     - Analysis Ready Surface Reflectance Data from Landsat satellites.
     
   * - xu18_
     - GA Landsat Analysis Ready Data (Collection 3) is a foundation product enabling delivery of Digital Earth Australia.

   * - if87_
     - Sentinel-2 Analysis Ready Data

   * - fk4_
     - Derivative EO data. WOfS, Fractional Cover, NIDEM, statistical summaries.

   * - fj7_
     - Copernicus Hub data. Sentinel 1-3

   * - u39_
     - IMOS and TERN-AusCover Satellite Products (MODIS)

   * - rr5_
     - Bureau of Meteorology. Rainfall grids, Himawari 8, etc.

   * - rr2_
     - Geophysics reference data

.. _rs0: https://my.nci.org.au/mancini/project/rs0
.. _xu18: https://my.nci.org.au/mancini/project/xu18
.. _if87: https://my.nci.org.au/mancini/project/if87
.. _fk4: https://my.nci.org.au/mancini/project/fk4
.. _fj7: https://my.nci.org.au/mancini/project/fj7
.. _u39: https://my.nci.org.au/mancini/project/u39
.. _rr5: https://my.nci.org.au/mancini/project/rr5
.. _rr2: https://my.nci.org.au/mancini/project/rr2

High Performance Computing
==========================

The DEA environment can be accessed within the High Performance Computing (HPC)
environment (i.e. Gadi_). This will require compute and storage quota
allocations to be made via NCI's Allocation Scheme processes, on a per-project
basis. This does not need to be specific to DEA – all users with computing
capabilities on Gadi are able to access DEA through the HPC system.

This guide focuses on accessing and exploring DEA via the VDI environment.


.. _Gadi: https://nci.org.au/our-systems/hpc-systems/
