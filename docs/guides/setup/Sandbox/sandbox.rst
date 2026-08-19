.. _sandbox:

DEA Sandbox
===========

The Digital Earth Australia (DEA) Sandbox is an Earth observation (EO) learning and analysis environment supporting Australian government and education users to get started with `DEA Data Products </data/>`_. The Sandbox includes sample data and Jupyter notebooks that allow you to experiment with DEA’s EO datasets and explore proof-of-concept applications.  

The Sandbox is available to eligible users, is free to use, and provides you with a managed environment with 2 cores with 16GB of RAM and 10GB of storage. It has regularly-used Python packages pre-installed. The Sandbox also includes the `DEA Notebooks Jupyter notebook user guides </dea-notebooks/>`_ to help you get started. 

.. .. admonition:: Get started
..    :class: note
..
..    Open the `DEA Sandbox <https://app.sandbox.dea.ga.gov.au>`_

.. contents:: In this guide
   :local:
   :backlinks: none

.. _sandbox-eligibility:
.. _eligibility:

Eligibility
-----------

The DEA Sandbox service is available to Australian government and education users who have recognised Australian government or education institute email addresses (``.gov.au`` or ``.edu.au`` or equivalent).  

Industry who are working directly with Australian government on government-directed outcomes will be able to put forward their use-case application for consideration. In these cases, a government sponsor needs to be provided.  

Account sponsorship
~~~~~~~~~~~~~~~~~~~

All users requesting an account will need to provide the details of a sponsor for the account. The sponsor information is collected to verify identity, and as a secondary point of contact for the account. The sponsor will be asked to acknowledge the :any:`DEA Sandbox disclaimer <sandbox-disclaimer>` alongside the user. The sponsor: 

* Should be a supervisor or line manager to the account requestor (or at least have familiarity with the role of the account requestor to be able to speak on their behalf) 
* Must be a senior executive/SES1 (for government and industry users) or professor, lead lecturer or course convenor (for education users). 

.. _sandbox-register:
.. _register:

Register 
--------

Visit `https://app.sandbox.dea.ga.gov.au <https://app.sandbox.dea.ga.gov.au>`_ to sign up for a new account or sign in if you have an existing account.  

Click the blue “Login or Sign up" button.  

Select “Sign up” to be taken to the sign up page where you will be asked to enter: 

* Your email address 
* Your phone number 
* Your given name 
* Your family name 
* Password (must contain) ...

  * A lower case letter 
  * An upper case letter 
  * A number 
  * At least 8 characters 
  * Must not contain a leading or trailing space 

.. image:: /_files/sandbox/sandbox-sign-up-page.jpg
   :alt: The 'Sign up' page of the DEA Sandbox.

.. raw:: html

   <br />

Once you have entered your details, they will be verified. If you do not meet our :any:`eligibility criteria <sandbox-eligibility>`, you will not be able to complete this step.  

An automated email will be sent to the email address you have entered. You will need to click on the verification link in the email.  

.. image:: /_files/sandbox/sandbox-email-verification-instructions-page.png
   :alt: A page that provides instructions on email verification.

.. raw:: html

   <br />

When your email has been verified, you will be sent a PDF form that will need to be completed and emailed back to `earth.observation@ga.gov.au <mailto:earth.observation@ga.gov.au>`_

The PDF form will ask for:

* Your name 
* Your professional affiliation 
* Your period of access required for the DEA Sandbox 
* What is your intended use of the DEA Sandbox? 
* How does the DEA Sandbox contribute to the outcomes of your work? 
* Who (if anyone) are you collaborating with at Geoscience Australia? 
* Your sponsor’s information (name, title, affiliation, email and phone number) 
* Both yourself and your sponsor to agree to the :any:`DEA Sandbox disclaimer <sandbox-disclaimer>` and `Privacy Policy <https://www.ga.gov.au/privacy>`_

Your DEA Sandbox account will be “pending” until the PDF form is received and processed by the DEA team. Once your request has been assessed, we will contact you to let you know your account is active and ready to be utilised.  

Access
------

When you log into your account you will be sent a SMS with a verification code to the mobile number you provided in your application, that you will need to enter on the sign in screen. You will be prompted to enter a new SMS verification code each time you log into your account. 

.. image:: /_files/sandbox/sandbox-sms-verification-page.png
   :alt: Enter your SMS verification code into this DEA Sandbox page.

After signing in, the DEA Sandbox will prepare a JupyterLab environment for you.
All necessary software is provided as part of this environment, so no additional
installation or configuration is required.

Navigate
--------

The JupyterLab interface consists of the main work area (right-hand panel), the
left sidebar (containing a file browser and other useful features), and a menu
bar along the top. The main work area is where Jupyter notebooks will be displayed
once opened. By default, the Launcher is displayed, which allows you to create new files.

.. image:: /_files/sandbox/sandbox-jupyterlab-startup.png
   :align: center
   :alt: JupyterLab Start Up

The Sandbox comes pre-loaded with Jupyter notebooks from the `DEA Notebooks repository`_.
These notebooks are automatically updated every time you start your DEA Sandbox environment.
These include:

- `Beginner's guide`_: An introduction to Jupyter Notebooks and how to load, plot and interact with DEA data

- `DEA products`_: An introduction to DEA's satellite datasets and derived products, including how to load each product

- `How-to guides`_: A recipe book of simple code examples demonstrating how to perform common analysis tasks using DEA

- `Interactive apps`_: Interactive apps and widgets that require little or no coding to run

- `Real world examples`_: More complex case studies demonstrating how DEA can be used to address real-world problems

To open an existing Jupyter notebook, double-click through the folders to find a
notebook you're interested in, then double-click the notebook to
open it in the main work area. Notebooks are indicated by the ``.ipynb`` file
extension. The JupyterLab interface also supports plain text and Markdown files.

To learn more about JupyterLab, visit the `JupyterLab Documentation`_.

Important information about The Sandbox
---------------------------------------

The Sandbox is not a production environment and should be used for protyping and exploring
DEA's data and tools. Changes made to Jupyter notebooks in the DEA Sandbox may be automatically
overwritten as part of the automatic update process, meaning any changes you make to these notebooks
may be lost. To avoid this, we recommend advanced
users use Git to clone a new copy of ``dea-notebooks`` into the Sandbox (`see guide here`_).
and the default notebooks provided. We strongly encourage you to back up your work (e.g.
to GitHub, or by downloading it to your local machine) each time you log in.

You are able to download any of the files in your Sandbox environment by right-clicking them in the left side bar
navigation panel and selecting 'download'. This download function is limited to 10 files at a time so you
may need to download your files in batches if you have more than 10.

Please note that if you have not logged into your account in the past 90 days,
we consider this account inactive and reserve the right to remove any data you
have saved in your account. Please read the DEA Sandbox disclaimer below for more information.

.. _JupyterLab Documentation: https://jupyterlab.readthedocs.io/en/stable/user/interface.html
.. _DEA Notebooks repository: https://github.com/GeoscienceAustralia/dea-notebooks/
.. _Beginner's guide: /notebooks/Beginners_guide/README/
.. _DEA products: /notebooks/DEA_products/README/
.. _How-to guides: /notebooks/How_to_guides/README/
.. _Interactive apps: /notebooks/Interactive_apps/README/
.. _Real world examples: /notebooks/Real_world_examples/README/
.. _see guide here: https://github.com/GeoscienceAustralia/dea-notebooks/wiki/Guide-to-using-DEA-Notebooks-with-git

Available Data
--------------

The available data for the DEA Sandbox can be viewed through the
`DEA Explorer`_ tool.

.. _DEA Explorer: ../explorer_guide.rst

Where can I get help?
---------------------

You can ask questions (and view previously asked questions) on the `Open Data Cube Stack Exchange`_ page.
When asking a question, tag it with `open-data-cube`.

You can also join our `Open Data Cube Discord chat`_ for help setting up or using Digital Earth Australia.

.. _Open Data Cube Stack Exchange: https://gis.stackexchange.com/questions/tagged/open-data-cube
.. _Open Data Cube Discord chat: https://discord.com/invite/4hhBQVas5U

.. _dea-sandbox-disclaimer:
.. _sandbox-disclaimer:

Academic and university courses using the DEA Sandbox
-----------------------------------------------------

Currently, Geoscience Australia supports use of the DEA Sandbox as a learning tool for tertiary education courses.

To utilise the DEA Sandbox as part of a university course, TAFE course, or other tertiary course, course leadership should first engage Digital Earth to articulate intent and seek agreement. This should occur for each occasion the DEA Sandbox is sought.

To give us enough time to prepare and to fix any sign-up issues, we recommend starting this process **at least one month before the start date of the course**.

#. Contact us at earth.observation@ga.gov.au in advance of the course start date. Please provide the following details:

   #. The **name of the academic course**.
   #. The **course code**.
   #. The **start date** of the course.
   #. The **census date** of the course.
   #. The **end date** of the course.
   #. The **expected number of sign-ups**; i.e. the number of teachers plus the number of students in the cohort who will be signing up for a DEA Sandbox account.
   #. The **email address domains of the teachers and students**; e.g. they will be signing up with ``@example.edu.au`` and ``@student.example.edu.au`` email addresses.

#. We will send you a PDF form which you will need to complete and then email back to earth.observation@ga.gov.au which asks for some details about your affiliation and use case. It also requires a professor, lead lecturer, or course convenor to sign it as a sponsor.
#. We will assess the form that you submitted to us and will notify you of our decision of whether we have approved it. If approved, we will move onto the next step. Once endorsed, the following steps should be followed.
#. We will temporarily ‘whitelist’ the email address domains that you provided to us. This will allow your cohort to sign up to the DEA Sandbox and gain express approval without needing to fill out the standard PDF request form. Please ensure your cohort don’t sign up to the DEA Sandbox before we implement the whitelist; otherwise, they will need to contact us for support at earth.observation@ga.gov.au
#. After we notify you that we have implemented the whitelist, you can then instruct your student cohort to sign up for a DEA Sandbox account. Please do this in advance of the start date of your course to give enough time for us to fix any sign-up issues that may occur. Here are the necessary instructions to communicate to your staff and students:

   ::

      #. Go to the DEA Sandbox: https://app.sandbox.dea.ga.gov.au/hub/login
      #. Click **Login or Sign Up** then on the next page, click the **Sign up** link at the bottom.
      #. Enter your details to sign up. Importantly, ensure to use your student email address and double-check that you enter your phone number correctly!
      #. Ignore the email that you receive asking you to fill out a PDF form. Don’t fill out the PDF form because it is not needed.
      #. Return to the DEA Sandbox and log in using the email address and password that you entered when signing up. Please check that you are able to log in before the course start date!
      #. If you encounter any issues during this process, please email Digital Earth at earth.observation@ga.gov.au for technical assistance.
      #. Note that your DEA Sandbox account will be deactivated after the end date of this course, so please back up any work that you save in your DEA Sandbox account.

#. The teaching staff of this cohort (e.g. the lecturer and tutors) can sign up using the same method as the students.
#. The class can now be conducted using the DEA Sandbox.
#. After the census date (which you provided earlier), we will remove the ‘whitelist’ on your email domains. This means that any additional staff or students who want to sign up for a DEA Sandbox account after this date will need to go through a separate approval process.
#. We will then request the class list of this cohort — the list of email addresses of students and teachers. We will use this to deactivate accounts after the course end date.
#. After the course end date (which you provided earlier), we will deactivate the DEA Sandbox accounts of the class list that you provided in the previous step.

Please note, the DEA Sandbox is not an assured offering. It is an R&D solution designed to enable exploration of Earth Observation data and is maintained with best efforts.

DEA Sandbox disclaimer
----------------------

.. admonition:: DEA Sandbox disclaimer

   To the maximum extent permitted by law, your use of the Digital Earth Australia Sandbox (including any associated
   data or services):
   
   - Is on an 'as is' and 'as available' basis with all faults, and the Commonwealth of Australia disclaims all warranties, guarantees or representations of any kind, and
   - Is entirely at your own risk, and the Commonwealth of Australia disclaims any liability to you or anyone else for any liability whatsoever (including, without limitation, any liability for negligence).
   
   The Commonwealth of Australia does not intend to create any contractual legal relations with you in relation to your
   registration for, or use of, the Digital Earth Australia Sandbox (including any associated data or services).

Purpose
~~~~~~~

The Digital Earth Australia (DEA) Sandbox is a learning and analysis environment for getting started with DEA data and our `Open Data Cube`_. It is intended to enable you to experiment and learn how to use DEA's Earth Observation datasets and enable you to explore proof-of-concept applications that you may wish to implement in your own production environment.

Availability
~~~~~~~~~~~~

Geoscience Australia makes no guarantee on the availability of the DEA Sandbox and may discontinue offering the DEA Sandbox without notice. We may change the features and datasets offered in response to user feedback and future assessments of budget and security.

Geoscience Australia currently has no limits on the number of persons who can create an account for the DEA Sandbox. However, there is a technical limit on the number of concurrent users who can be logged into the DEA Sandbox and if this limit is reached other users will receive an error message and be unable to login.

We may remove your files at any time without warning. If you need files hosted in the Sandbox you should download or export them regularly.

We define an account as inactive if it has not been logged into for the last 90 days and may remove the data of inactive accounts. After this data is removed, new logins will result in a fresh workspace.

In the event that a user's environment becomes unstable, it will be replaced with a fresh environment and all work/data may be lost.

As explained below, we may suspend accounts that we consider have misused the DEA Sandbox.

You can view the current system status `here`_. If you are experiencing an issue with the Sandbox that isn't identified on the status page, please submit this issue to `earth.observation@ga.gov.au`_ as we may be able to assist you to the extent we consider appropriate.

Security
~~~~~~~~

Geoscience Australia cannot guarantee the security of data in your account and you should not use your account with sensitive or confidential data.

Misuse of the DEA Sandbox
~~~~~~~~~~~~~~~~~~~~~~~~~

Geoscience Australia will consider that the following is misuse of the DEA Sandbox and may choose to suspend your account:

    - knowingly running malicious code.
    - running applications that are not related to Earth observation data exploration.
    - uploading any sensitive or restricted data or code to your Sandbox account.

Collection of personal information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your personal information provided at sign up is collected under the Privacy Act 1988 (Cth) (Privacy Act). We will only use and disclose your personal information to administer, evaluate and improve the DEA Sandbox, unless you provide consent or we are otherwise required or authorised by law to use or disclose it. Your files will not be intentionally shown to other users or shared with third parties but as explained above we cannot guarantee the security of your account.

The information we collect may, for example, be used to:

* Send you information relating to the service (via email) which may include but is not limited to notification of any major changes to the DEA Sandbox or your account.
* Evaluate how the service is being used.
* Improve the service offerings.

For more information please see `Geoscience Australia's privacy policy`_.

Intellectual Property
~~~~~~~~~~~~~~~~~~~~~

The pre-loaded notebooks provided in the DEA Sandbox are provided under the `Creative Commons by Attribution 4.0 license`_. They are provided as a starting point for Sandbox users, and can be shared and adapted as required. If the notebooks are used, they should be cited:

    Krause, C., Dunn, B., Bishop-Taylor, R., Adams, C., Burton, C., Alger, M., Chua, S., Phillips, C., Newey, V., Kouzoubov, K.,
    Leith, A., Ayers, D., Hicks, A., DEA Notebooks contributors 2021. Digital Earth Australia notebooks and tools repository.
    Geoscience Australia, Canberra. https://doi.org/10.26186/145234

Account closure
~~~~~~~~~~~~~~~

You can close your account at any time by emailing the DEA team (`earth.observation@ga.gov.au`_).

As above we may restrict access to, or close accounts at our discretion, including in instances where we consider that the DEA Sandbox has been misused.

.. _Open Data Cube: https://www.dea.ga.gov.au/about/open-data-cube
.. _here: https://status.dea.ga.gov.au/
.. _earth.observation@ga.gov.au: mailto:earth.observation@ga.gov.au
.. _Geoscience Australia's privacy policy: http://www.ga.gov.au/privacy
.. _Creative Commons by Attribution 4.0 license: https://creativecommons.org/licenses/by/4.0/
