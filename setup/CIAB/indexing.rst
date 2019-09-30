How to index data in the Cube in a Box environment
==================================================

Once you have your own Open Data Cube (ODC) environment up and running, the next step is to "index" satellite data in your environment. 
When you index a data product, you provide the database with a description of the product (and its location) so that it can be loaded later. 
During the indexing step, no data is copied, downloaded or transformed. After this is completed you will be able to load and perform analysis on the product.

In this example we are indexing the `Annual Water Observations from Space (WOfS) <https://www.dea-learning-portal.test.frontiersi.io/water-observations-from-space>`_ product. 
If you would like to index another DEA product, go to the `Available Data <https://www.dea-learning-portal.test.frontiersi.io/available-data>`_ page to find the product definition and prefix location, then complete the same steps.

Step 1 - Get the product defintion
----------------------------------

The product definition is a file that contains all the required metadata for the product. 
Many product definitions for `DEA data <https://github.com/GeoscienceAustralia/dea-config/tree/master/dev/products>`_ can be found in the dea-config GitHub repository.

In this example, we will use the product definition for the `WOfS Annual Summary product <https://github.com/GeoscienceAustralia/dea-config/blob/master/dev/products/wofs/wofs_annual_summary.yaml>`_. 
To get a copy of this file, either download or clone it from the `dea-config <https://github.com/GeoscienceAustralia/dea-config/tree/master/dev/products>`_ GitHub repository using the "Clone or download" button:

.. image:: /_static/ciab-images/ciab-index-clone-screenshot.webp
   :align: left
   :alt: Cloning

Using your file explorer or terminal, copy the WOfS Annual Summary product file "wofs_annual_summary.yaml" from the following location within the dea-config folder:

.. code-block:: bash
    
    <path>\<to>\dea-config\dev\products\wofs

To:

.. code-block:: bash
    
    <path>\<to>\cube-in-a-box\data

Your Cube in a Box installation will now be able to access the product definition during the indexing step.

Step 2 - Note down the AWS bucket and prefix location
-----------------------------------------------------

The prefix location is where the data is stored in Amazon's Simple Storage Service (S3). For this example

the bucket is **dea-public-data**

the prefix is **WOfS/annual_summary/v2.1.5/combined/**

Note these down these as they will be used in the indexing script.

Step 3 - Connect to the Jupyter terminal
----------------------------------------

Go back to your running Jupyter environment in your browser.

Click the "New" button then secondly the "Terminal":

.. image:: /_static/ciab-images/ciab-index-new-terminal-screenshot.webp
   :align: left
   :alt: New Terminal

You should see a new tab open up that looks like this:

.. image:: /_static/ciab-images/ciab-index-terminal-screenshot.webp
   :align: left
   :alt: Terminal

Now in this tab enter bash to enable the bash shell:

.. image:: /_static/ciab-images/ciab-index-terminal-bash-screenshot.webp
   :align: left
   :alt: Terminal bash


This functions like a normal terminal, but interfaces directly with the Cube in a Box environment. This makes it easier to work directly with the ODC datacube package, without needing to use additional Docker commands.

Step 4 - Initialise your Datacube environment
---------------------------------------------

Now run the below command from the terminal to initialise the environment:

.. code-block:: bash
    
    datacube -v system init

You should an output similar to the below:

.. image:: /_static/ciab-images/ciab-index-datacube-init-screenshot.webp
   :align: left
   :alt: Datacube init

Step 5 - Add the product defintion
----------------------------------

We now add the previously downloaded product definition. This allows the ODC library to understand what the data is and should look like. Every data product will require a product definition. It is a yaml file containing all the required metadata the ODC needs to understand the data.

Add the product with the following command:

.. code-block:: bash
    
    datacube product add /opt/odc/data/wofs_annual_summary.yaml

You should see similar to this output showing that product was added:

.. image:: /_static/ciab-images/ciab-index-product-add-screenshot.webp
   :align: left
   :alt: Datacube product add

Step 6 - Run the indexing
-------------------------

Now you are ready to run the indexing script. This will search through the prefix location and index the location of data that matches the product you added in the previous step. 
This script takes in the s3 location dea-public-data, the prefix, start_date and end_date. 

Enter the following command to index the WOfS product from 2010 to 2019, this process can take up to **40mins** complete as it searches under the prefix location and adds datasets that match:

.. code-block:: bash
    
    python3 /opt/odc/scripts/ls_public_bucket.py dea-public-data 
    --prefix=WOfS/annual_summary/v2.1.5/combined/ 
    --start_date=2010-01-01 --end_date=2019-01-01

You should see an outputs as the indexing process runs:

.. image:: /_static/ciab-images/ciab-index-running-indexing-screenshot.webp
   :align: left
   :alt: Indexing

You can continue with the new steps while you wait for indexing to complete.

Step 7 - Download analysis notebook
-----------------------------------

Open the following `notebook <https://nbviewer.jupyter.org/github/frontiersi/dea-sandbox-notebooks/blob/master/01_DEA_Datasets/WaterObservationsfromSpace_AnnualSummary.ipynb>`_ and save to your local file system right clicking on the download button:

.. image:: /_static/ciab-images/ciab-index-download-notebook.webp
   :alt: Download Notebook

Then click "save as" to save on your local filesystem:

.. image:: /_static/ciab-images/ciab-index-saveas-notebook-screenshot.webp
   :alt: Save as


Now go back to your Jupyter environment in your browser and upload the downloaded notebook to your environment:

.. image:: /_static/ciab-images/ciab-index-upload-notebook-screenshot.webp
   :alt: Confirm Upload

Confirm the upload by clicking the blue "upload" button:

.. image:: /_static/ciab-images/ciab-index-confirm-upload-screenshot.webp
   :alt: Confirm Upload

Step 7 - Run your analysis
--------------------------

You are now ready to load the data and run some analysis

Click on the "WaterObservationsfromSpace_AnnualSummary" notebook.

Read through and run the cells to explore the data.

You should be able to see an output similar to this:

.. image:: /_static/ciab-images/ciab-index-notebook-output-screenshot.webp
   :align: left
   :alt: Notebook output

To index other products, you'll need to know their metadata and Amazon S3 prefix locations. 
This information is provided for each product listed on the `Available Data <https://www.dea-learning-portal.test.frontiersi.io/available-data>`_ page.
