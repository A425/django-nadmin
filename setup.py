#!/usr/bin/env python
from setuptools import setup

# version_tuple = __import__('nadmin.version').VERSION
# version = ".".join([str(v) for v in version_tuple])

setup(
    name='django-nadmin',
    version='0.1.0',
    description='django nadmin support django version 1.8 based on django-xadmin',
    long_description=open('README.rst').read(),
    author='A425',
    author_email='liu170045@gmail.com',
    license=open('LICENSE').read(),
    download_url='https://github.com/A425/django-nadmin/archive/master.zip',
    packages=['nadmin', 'nadmin.plugins', 'nadmin.templatetags', 'nadmin.views'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django>=1.7',
        'django-crispy-forms>=1.4.0',
        'django-formtools',
        'xlsxwriter',
    ],
    extras_require={
        'Excel': ['xlwt'],
        'Reversion': ['django-reversion'],
    },
    zip_safe=False,
    keywords=['admin', 'django', 'xadmin', 'nadmin', 'bootstrap'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
