django-nadmin |Build Status|
============================================

.. |Build Status| image:: https://travis-ci.org/A425/django-nadmin.png?branch=master
   :target: https://travis-ci.org/A425/django-nadmin
   

Django-xadmin Source project is here: https://github.com/sshwsfc/django-xadmin


Drop-in replacement of Django admin comes with lots of goodies, fully extensible with plugin support, pretty UI based on Twitter Bootstrap.


Features
--------

-  Drop-in replacement of Django admin
-  Twitter Bootstrap based UI with theme support
-  Extensible with plugin support
-  Better filter, date range, number range, etc.
-  Built-in data export with xls, csv, xml and json format
-  Dashboard page with widget support
-  In-site bookmarking
-  Full CRUD methods

Screenshots
-----------

.. figure:: https://raw.github.com/A425/django-nadmin/docs/images/1pic.jpg
   :alt: Export Data
   
.. figure:: https://raw.github.com/A425/django-nadmin/docs/images/2pic.jpg
   :alt: Actions

.. figure:: https://raw.github.com/A425/django-nadmin/docs/images/3pic.jpg
   :alt: Filter

.. figure:: https://raw.github.com/A425/django-nadmin/docs/images/4pic.jpg
   :alt: Chart

.. figure:: https://raw.github.com/A425/django-nadmin/docs/images/5pic.jpg
   :alt: Edit inline

Get Started
-----------

Install
^^^^^^^

Install Nadmin from source, run:

.. code:: bash

    clone or download zip file
    cd django-nadmin
    python setup.py clean
    python setup.py build
    python setup.py install

Or Install using PIP:

.. code:: bash
    pip install django-nadmin

Install Requires 
----------------

-  `django`_ >=1.7

.. _django: http://djangoproject.com
.. _changelog: https://github.com/etianen/django-reversion/blob/master/CHANGELOG.rst


Run Demo Locally
----------------

.. code:: bash

    cd demo_app
    ./manage.py runserver

Open http://127.0.0.1:8000 in your browser


You may need to ``migrate & syncdb`` to create DB and Admin User if you run this demo for the first time

