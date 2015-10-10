#!/usr/bin/env python
from setuptools import setup

# version_tuple = __import__('xadmin.version').VERSION
# version = ".".join([str(v) for v in version_tuple])

setup(
    name='django-xadmin-1.8',
    version='0.1.0',
    description='Django xadmin support django version 1.8',
    long_description=open('README.rst').read(),
    author='A425',
    author_email='liu1700@gmail.com',
    license=open('LICENSE').read(),
    url='http://www.xadmin.io',
    download_url='https://github.com/A425/django-xadmin-1.8/archive/master.zip',
    packages=['xadmin', 'xadmin.plugins', 'xadmin.templatetags', 'xadmin.views'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django>=1.7',
        'django-crispy-forms>=1.4.0',
    ],
    extras_require={
        'Excel': ['xlwt', 'xlsxwriter'],
        'Reversion': ['django-reversion'],
    },
    zip_safe=False,
    keywords=['admin', 'django', 'xadmin', 'bootstrap'],
    classifiers=[
        'Development Status :: 1 - Beta',
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
