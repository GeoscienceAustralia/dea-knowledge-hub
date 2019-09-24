Cube in a box
==============

The Cube in a Box is a pre-configured option to run the Open Data Cube (ODC). 
It utilises `Docker <https://www.docker.com/>`_ and `Docker-compose <https://docs.docker.com/compose/>`_ to 
install and configure all of the components required to perform your own analyses.

Requirements
------------

To run Cube in a Box you are need to have the following tools and accounts:

   #. `Docker Desktop <https://docs.docker.com/install/>`_

      * Requires account on `Docker Hub <https://hub.docker.com/>`_

   #. A terminal program

      * `Powershell <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-6>`_ for Windows
   
      * Terminal for Mac/Linux

   #. Amazon Web Services credentials​

      * Requires account on `Amazon Web Services <https://aws.amazon.com/console/>`_

      * This is used to access the free satellite data stored in Amazon's Simple Storage Service (S3)

      * As part of the sign-up, you will need to provide a credit card. However, this will only be charged for resources used. You can check the Disclaimer section on the `DEA S3 Bucket <http://dea-public-data.s3-ap-southeast-2.amazonaws.com/index.html>`_ to understand potential resource charges.

Once you have downloaded the tools and have accounts on the necessary services, read the `additional guide <https://www.dea-learning-portal.test.frontiersi.io/more-help-docker-aws-setip>`_ for more information on the install and set-up processes.

Step 1 - Get and start the Cube in a Box environment
----------------------------------------------------

There are two options for installing the Cube in a Box repository: either clone or download and unzip it from the `Cube in a Box <https://github.com/opendatacube/cube-in-a-box>`_ GitHub repository using the "Clone or download" button:

.. image:: /_static/ciab-images/clone-screenshot.webp
   :align: left
   :alt: Cloning a GITHUB repo screenshot

Once you have the cube-in-a-box folder, enter it from your terminal program. You'll need to know the folder location and supply this in place of the <> arguments below

**Windows Powershell:**

.. code-block:: bash
    
    cd <path>\<to>\cube-in-a-box-master

**Mac/Linux Terminal:**

.. code-block:: bash
    
    cd <path>/<to>/cube-in-a-box-master

In your terminal program, set the environment variables for ODC_ACCESS_KEY and ODC_SECRET_KEY to your AWS account credentials (see the `additional guide <https://www.dea-learning-portal.test.frontiersi.io/more-help-docker-aws-setip>`_ for instructions on generating these):

**Windows Powershell:**

.. code-block:: bash
    
    $env:ODC_ACCESS_KEY = "<your_access_key_id>"
    $env:ODC_SECRET_KEY = "<your_secret_access_key>"

**Mac/Linux Terminal:**

.. code-block:: bash
    
    export ODC_ACCESS_KEY=<your_access_key_id>
    export ODC_SECRET_KEY=<your_secret_access_key>

Next start the environment with the docker-compose command:

.. code-block:: bash
    
    docker-compose up -d

This will create the Python Jupyter Notebook environment with the Open Data Cube (ODC) Python library ready to go alongside a PostgreSQL database. Note that there won't be any data in the database. This is done through the "indexing" step, covered below.

​
It may take a couple of minutes for the environment to build but when it's ready you should see:

.. image:: /_static/ciab-images/docker-compose-up-screenshot.webp
   :align: left
   :alt: Docker-compose up screenshot

Step 2 - Log in to the Jupyter environment
------------------------------------------

You can now access the Jupyter environment at http://localhost (for Docker Desktop) or http://192.168.99.100 (for Docker Toolbox) using the password "secretpassword". You'll need to manually type the appropriate address into your preferred browser to access the environment. 

Loging in will start the Jupyter environment, which looks like:

.. image:: /_static/ciab-images/jupyter-start-screenshot.webp
   :align: left
   :alt: Jupyter start screenshot

This environment has the ODC Python library ready to go, but the database doesn't contain any data (or references to where data is stored). To analyse data, you need to provide the database with a location and description of the data you want to work with. This is known as "indexing" data. Click the below link on instructions on how to index.

Now you can ready to `Index your first satellite dataset <cube-in-a-box-index.html>`_.

How to stop the environment
---------------------------

To stop the environment, run the following command:

.. code-block:: bash
    
    docker-compose down

To delete the environment, run the following command: 

.. code-block:: bash
    
    docker-compose down --remove-orphans --rmi 'all'

You should see output similar to:

.. image:: /_static/ciab-images/docker-compose-down-screenshot.webp
   :align: left
   :alt: Jupyter start screenshot

