.. highlight:: console


Command Line Usage (Advanced)
=============================

.. note:

   This section is intended for advanced users, and describes using DEA from
   a command line interface. This is mostly useful if you intend on running
   batch jobs on ``gadi`` and need to do some testing on the ``VDI``. Or simply if
   you're curious.


On ``VDI``, you can start a terminal window from **Applications** -> **System Tools**.

To manually use the modules on ``gadi`` or the ``VDI``, add the datacube module path::

    $ module use /g/data/v10/public/modules/modulefiles/

(you can add the above to your ``.bashrc`` to avoid running it every time)

You should now be able to load the ``dea`` module by running::

    $ module load dea

.. note::
   Behind the scenes this will load a second module called ``dea-env``
   which contains all required libraries and supporting software to use ``dea``.
   

You can see a list of available modules by running::

    $ module avail


The first time you load the module, it will register your account with the datacube, granting you read-only access.

It will store your password in the file ``~/.pgpass``.

You can then launch a Jupyter notebook by running::

    $ jupyter-lab <path_to_notebook>

.. note::
    ``VDI`` and ``gadi`` have separate home directories, so you must copy your pgpass to the other if
    you use both environments.

    You can push the contents of your pgpass file from the ``VDI`` to ``gadi`` by running on a terminal window in VDI::

        remote-hpc-cmd init
        ssh gadi "cat >> ~/.pgpass" < ~/.pgpass
        ssh gadi "chmod 0600 ~/.pgpass"

    You will most likely be prompted for your NCI password.

    To pull the contents of your pgpass from ``gadi`` to the ``VDI`` instead, run ::

        ssh gadi "cat ~/.pgpass" >> ~/.pgpass
        chmod 0600 ~/.pgpass

.. warning::

    If you have created a ``.datacube.conf`` file in your home folder from
    early Data Cube betas, you should rename or remove it to avoid it
    conflicting with the settings loaded by the module.
