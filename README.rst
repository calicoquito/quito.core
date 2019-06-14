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



Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

There are no translations currently

Installation
------------

Setup virtualenv, install requirements and build::

    virtualenv --clear .
    ./bin/pip install -r requirements.txt
    ./bin/buildout

Launch with the following command::

    ./bin/instance fg

The system provides a REST api for managing Projects and events.


Create Docker Image
-------------------
From the root folder of this addon run:

::

     docker build .

The output will generate a unique docker image (note the image hash)
Then you can launch it with (replace <imagehash> with your docker image hash:

::

   docker run -it -p 8080:8080 <imagehash>

Installation of Addon to a Plone site
--------------------------------------

Install quito.core by adding it to your buildout::

    [buildout]

    ...

    eggs =
        quito.core


and then running ``bin/buildout``

Prebuilded Docker Image
-----------------------
Run the docker image for quito.core using
::
   docker run -p 8080:8080 progsmart/quito.core:latest
::

Contribute
----------

- Issue Tracker: https://github.com/collective/quito.core/issues
- Source Code: https://github.com/collective/quito.core
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
