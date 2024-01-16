.. highlight:: console

.. _jupyter:

Jupyter Notebooks
=================

Jupyter Notebooks are one of the primary tools for developing analyses with DEA.
The ability to combine code with easy-to-read Markdown makes them useful for both developing and sharing work.
Jupyter Notebooks can be used on both the `DEA Sandbox </guides/setup/Sandbox/sandbox/>`_ and the `NCI </guides/setup/NCI/README/>`_.

In addition to the documentation found in the following `DEA Notebooks User Guide </notebooks/README/>`_ section, please see the `dea-notebooks wiki on GitHub <https://github.com/GeoscienceAustralia/dea-notebooks/wiki>`_ for more details on interacting and developing code with Jupyter Notebooks.

.. contents:: In this guide
   :local:
   :backlinks: none

Opening a notebook
------------------

After launching JupterLab on the Sandbox or NCI (see the respective guides), double-click through the available folders to view notebooks (indicated by the ``.ipynb`` file extension).
Then, double-click the notebook to open it in the main work area.

Read more about opening files in the `JupyterLab Documentation`_.

.. _JupyterLab Documentation: https://jupyterlab.readthedocs.io/en/stable/user/files.html

Working with notebooks
----------------------

For an in-depth guide on running and editing notebooks, see the `introduction to Jupyter notebooks`_ section of the Beginner's guide.

.. _introduction to Jupyter notebooks: /notebooks/Beginners_guide/01_Jupyter_notebooks/

Closing a notebook
------------------

Simply closing the notebook browser tab, will not shut down its "computational engine" (called the kernel). To shut down a kernel, go to the associated notebook and click on menu **File -> Close and Halt**. Alternatively, the Notebook Dashboard has a tab named Running that shows all the running notebooks (i.e. kernels) and allows shutting them down (by clicking on a Shutdown button).

Shutting down the Jupyter Notebook App
--------------------------------------

Closing the browser (or the tab) will not close the Jupyter Notebook App. To completely shut it down you need to close the associated terminal.

For more information about Jupyter Notebooks, see http://jupyter.org/.
