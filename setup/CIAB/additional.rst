Prerequisite additional help
============================

Cube in a Box provides a useful reference implementation of the ODC. This page will take you through installing Docker and setting up your Amazon Web Services credentials, both of which are required to use the Cube in a Box.

Docker
------

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. This ensures that the application will run on any other machine regardless of any customised settings that machine might have.

Installing
----------

Once you have a `Docker Hub <https://hub.docker.com/>`_ account, you can install:

* `Docker Desktop <https://docs.docker.com/install/>`_ (for recent versions of Windows, macOS)

* `Docker Toolbox <https://docs.docker.com/toolbox/overview/>`_ (for older versions of Windows, macOS)

Try Docker Desktop first, then follow the Docker Toolbox instructions if your machine doesn't meet the system requirements.

Once downloaded, run the executable which will install Docker on your machine.

Verifying 
---------

Once Docker is installed open your terminal for Mac/Linux or Windows Powershell for Windows and type the following command:

.. code-block:: bash
    
    docker ps

You should see an output similar to below:

For Windows Powershell:

.. image:: /_static/ciab-images/ciab-requirements-ps-screenshot.webp
   :align: left
   :alt: Powershell Docker PS command

For Mac/Linux Terminal:

.. image:: /_static/ciab-images/ciab-requirements-terminal-screenshot.webp
   :align: left
   :alt: Terminal Docker PS command

You are now ready to go with Docker

Amazon Web Services (AWS)
-------------------------

Amazon Web Services (AWS) is a cloud service from Amazon that provides services in the form of building blocks, which can be used to create and deploy any type of application in the cloud.

Cube in a Box only requires access to AWS Simple Storage Service (S3). S3 is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface. S3 is one place that houses DEA data.

To be able to access S3 you require an active AWS account with programmatic access and valid keys.

Steps
-----

First, sign up for an AWS account at https://aws.amazon.com/console/. As part of the sign-up, you will need to provide a credit card. However, this will only be charged for resources used. You can check the Disclaimer section on the `DEA S3 Bucket <http://dea-public-data.s3-ap-southeast-2.amazonaws.com/index.html>`_ to understand potential resource charges.

Once you have competed the sign up process you will see this landing page. Type "IAM" into the search based as shown by the red arrow and click on IAM.

.. image:: /_static/ciab-images/ciab-requirements-aws-home-screenshot.webp
   :align: left
   :alt: AWS Home

Now click the "Users" link in the left hand side panel:

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-screenshot.webp
   :align: left
   :alt: AWS IAM Console

Then click the "Add user" button:

.. image:: /_static/ciab-images/ciab-requirements-aws-adduser-screenshot.webp
   :align: left
   :alt: AWS Add User
Select a username for yourself and select "Programmatic access":

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-programic-screenshot.webp
   :align: left
   :alt: AWS programic access

Now add permissions to your user.

Click the "Attach existing policies directly" button.

Enter in "s3" in the search area.

Click the "AmazonS3ReadOnly" Policy.

Then click the "Next:Tags" button

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-permissions-screenshot.webp
   :align: left
   :alt: AWS IAM Permissions

Click "Next: Review" button:

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-review-screenshot.webp
   :align: left
   :alt: AWS IAM Review Screen

Click "Create user" button:

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-createuser-screenshot.webp
   :align: left
   :alt: AWS Create User

Finally note down your "Access key ID" and "Secret access key". These will be used for your ODC environment to access the S3 data:

.. image:: /_static/ciab-images/ciab-requirements-aws-iam-creds-screenshot.webp
   :align: left
   :alt: AWS Credentials

You have now installed and set-up the necessary tools and services required to run Cube-in-a-Box.
