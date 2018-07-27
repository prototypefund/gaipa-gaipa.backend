.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=============
gaipa.backend
=============

Setup Plone backend
===================

Required package on the maschine on Ubuntu/Debian:
--------------------------------------------------

- python-dev
- python-virtualenv
- poppler-utils
- libjpeg-dev
- libxslt1-dev

Install Plone
-------------

.. code-block:: sh

    git clone git@gitlab.com:gaipa/gaipa.backend.git
    cd gaipa.backend
    virtualenv .
    ./bin/pip install -r requirements.txt
    ./bin/buildout


To start Plone in debug mode
----------------------------

.. code-block:: sh

    ./bin/instance fg


To start Plone in daemon mode
-----------------------------

.. code-block:: sh

    ./bin/instance start


Open Plone in Browser on
------------------------

http://localhost:7080/

User: admin
Password: admin

Add a Plone site, keep defaul site ID.
Go to site setup and there to addons and install the gaipa.backend addon.

http://localhost:7080/Plone/@@prefs_install_products_form

Now create the needed gaipa content inside the app folder.
