django-xadmin-1.8 |Build Status| |Build Status2|
============================================

.. |Build Status| image:: https://travis-ci.org/A425/django-xadmin-1.8.png?branch=master
   :target: https://travis-ci.org/A425/django-xadmin-1.8

.. |Build Status2| image:: https://drone.io/github.com/sshwsfc/django-xadmin/status.png
   :target: https://drone.io/github.com/sshwsfc/django-xadmin/latest

Source project is here: https://github.com/sshwsfc/django-xadmin


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

.. figure:: https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/action.png
   :alt: Actions
   
.. figure:: https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/filter.png
   :alt: Filter

.. figure:: https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/chart.png
   :alt: Chart

.. figure:: https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/export.png
   :alt: Export Data

.. figure:: https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/editable.png
   :alt: Edit inline

Get Started
-----------

Install
^^^^^^^

Install Xadmin from source, run:

.. code:: bash

    clone or download zip file
    cd django-xadmin
    python setup.py clean
    python setup.py build
    python setup.py install


Install Requires 
----------------

-  `django`_ >=1.4

-  `django-crispy-forms`_ >=1.2.3 (For xadmin crispy forms)

-  `django-reversion`_ ([OPTION] For object history and reversion feature, please select right version by your django, see `changelog`_ )

-  `xlwt`_ ([OPTION] For export xls files)

-  `xlsxwriter`_ ([OPTION] For export xlsx files)

.. _django: http://djangoproject.com
.. _django-crispy-forms: http://django-crispy-forms.rtfd.org
.. _django-reversion: https://github.com/etianen/django-reversion
.. _changelog: https://github.com/etianen/django-reversion/blob/master/CHANGELOG.rst
.. _xlwt: http://www.python-excel.org/
.. _xlsxwriter: https://github.com/jmcnamara/XlsxWriter


Run Demo Locally
----------------

.. code:: bash

    cd demo_app
    ./manage.py runserver

Open http://127.0.0.1:8000 in your browser, the admin user password is ``admin``

