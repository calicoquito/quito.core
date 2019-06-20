.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==========
quito.core
==========

Quito is an open source project to manage the operations of Organisation, with an initial focus on churches. The software will enable churches to automate common administrative, management and reporting tasks. This will help the Church Leadership Team to improve communications, streamline daily operations and support collaboration.The system would be modular which would make developing the software and customizing the software easier for the users.

Features
--------

- Creation of projects/Events
- creation of a tasks list for the project
- creation of tasks for various task list
- Workflow Setup
- Thre user group with varying permissions (organizer, volunteer, participant)



Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar

Latest Release
---------------
The latest Release for quito.core is currently pre-alpha v00001. 
This version is not for production and mainly for testing procedure. It includes the documentation on how to installl Quito.core using docker on wither Linux or windows. It has troubleshooting techniques that can be used to mnually install quito. It contains both data volume for the docker installation as well as an insomina file explaining the various api comands that can be used to managed the platform. This release Only focuses on the creation and viewing of projects with its various tasks using three types of user with different permisiions. 

Setup with Docker
-----------------
To setup quito.core download the installation file for the latest release version and follow the installation instructions.
On startup you would be greeted with the homepage along with some test data that was previously installed to the system. The system can be left like this or customize base on your preference.
- The latest installation version currently is pre-alpha v00001

Installation
------------

Source File
************


Setup virtualenv, install requirements and build::

    virtualenv --clear .
    ./bin/pip install -r requirements.txt
    ./bin/buildout

Launch with the following command::

    ./bin/instance fg


Create Docker Image
*******************

From the root folder of this addon run:

::

     docker build .

The output will generate a unique docker image (note the image hash)
Then you can launch it with (replace <imagehash> with your docker image hash:

::

   docker run -it -p 8080:8080 <imagehash>

How to use API
...............
An Insomnia file relating to the use of the quito.core api can be found under the guide directory. 
It cantains the api calls as well as the relating documentations on how to use them.

Installation of Addon To A Plone Site
--------------------------------------

Install quito.core by adding it to your buildout::

    [buildout]

    ...

    eggs =
        quito.core


and then running ``bin/buildout``

Contribute
----------

- Issue Tracker: https://github.com/calicoquito/quito.core/issues
- Source Code: https://github.com/calicoquito/quito.core
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
