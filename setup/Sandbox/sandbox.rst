.. _sandbox:

DEA Sandbox
===========

The Digital Earth Australia (DEA) Sandbox is a learning and analysis environment 
for getting started with DEA data and our `Open Data Cube`_. The Sandbox includes 
sample data and Jupyter notebooks that allow you to experiment with DEA’s Earth 
Observation datasets and explore proof-of-concept applications. 

The Sandbox is free to use, and provides you with a managed environment with 2 
cores with 16GB of RAM, 10GB of storage, and regularly used Python packages 
pre-installed. The Sandbox also includes Jupyter notebook user guides to help you 
get started with DEA and the Open Data Cube.

.. _Open Data Cube: https://www.dea.ga.gov.au/about/open-data-cube

Register
--------

The DEA Sandbox is free to use. Visit https://app.sandbox.dea.ga.gov.au to sign up
for a new account, or sign in if you have an existing account. A verification
code will be sent to the email address you register with.

Access
------

After signing in, the DEA Sandbox will prepare a JupyterLab environment for you.
All necessary software is provided as part of this environment, so no additional
installation or configuration is required.

Navigate
--------

The JupyterLab interface consists of the main work area (right-hand panel), the
left sidebar (containing a file browser and other useful features), and a menu
bar along the top. The main work area is where Jupyter notebooks will be displayed 
once opened. By default, the Launcher is displayed, which allows you to create new files.

.. image:: /_static/Sandbox/sandbox-jupyterlab-startup.png
   :align: center
   :alt: JupyterLab Start Up

The Sandbox comes pre-loaded with Jupyter notebooks from the `DEA Notebooks repository`_. 
These notebooks are automatically updated every time you start your DEA Sandbox environment.
These include:

- `Beginner's guide`_: An introduction to Jupyter Notebooks and how to load, plot and interact with DEA data

- `DEA datasets`_: An introduction to DEA's satellite datasets and derived products, including how to load each product

- `Frequently used code`_: A recipe book of simple code examples demonstrating how to perform common analysis tasks using DEA

- `Real world examples`_: More complex case studies demonstrating how DEA can be used to address real-world problems

To open an existing Jupyter notebook, double-click through the folders to find a
notebook you're interested in, then double-click the notebook to
open it in the main work area. Notebooks are indicated by the ``.ipynb`` file
extension. The JupyterLab interface also supports plain text and Markdown files.

To learn more about JupyterLab, visit the `JupyterLab Documentation`_.

Some things to know about The Sandbox
-------------------------------

The Sandbox is not a production environment and should be used for protyping and exploring
DEA's data and tools. Changes made to Jupyter notebooks in the DEA Sandbox may be automatically 
overwritten as part of the automatic update process. To avoid this, we recommend advanced 
users use Git to clone a new copy of ``dea-notebook`` into the Sandbox (`see guide here`_).
and the default notebooks provided. We strongly encourage you to back up your work (e.g. 
to GitHub, or by downloading it to your local machine) each time you log in. 

You are able to download any of the files in your Sandbox environment by right-clicking them in the left side bar
navigation panel and selecting 'download'. This download function is limited to 10 files at a time so you
may need to download your files in batches if you have more than 10.

Please note that if you have not logged into your account in the past 90 days, 
we consider this account inactive and reserve the right to remove any data you 
have saved in your account. 

.. _JupyterLab Documentation: https://jupyterlab.readthedocs.io/en/stable/user/interface.html
.. _DEA Notebooks repository: https://github.com/GeoscienceAustralia/dea-notebooks/
.. _Beginner's guide: ../../notebooks/Beginners_guide/README.rst
.. _DEA datasets: ../../notebooks/DEA_datasets/README.rst
.. _Frequently used code: ../../notebooks/Frequently_used_code/README.rst
.. _Real world examples: ../../notebooks/Real_world_examples/README.rst
.. _see guide here: https://github.com/GeoscienceAustralia/dea-notebooks/wiki/Guide-to-using-DEA-Notebooks-with-git

Available Data
--------------

The available data for the DEA Sandbox can be viewed through the
`DEA Sandbox Explorer`_ tool.

.. _DEA Sandbox Explorer: https://explorer.sandbox.dea.ga.gov.au

Where can I get help?
---------------------

You can ask questions (and view previously asked questions) on the `Open Data Cube Stack Exchange`_ page. 
When asking a question, tag it with `open-data-cube`.

You can also `join our Slack community`_ for help setting up or using Digital Earth Australia.

.. _Open Data Cube Stack Exchange: https://gis.stackexchange.com/questions/tagged/open-data-cube
.. _join our Slack community: http://slack.opendatacube.org/
