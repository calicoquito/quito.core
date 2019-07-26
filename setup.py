# -*- coding: utf-8 -*-
"""Installer for the quito.core package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='quito.core',
    version='1.0a1',
    description="The core installation for the quito project",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='phillip',
    author_email='phillipjunior95@gmail.com',
    url='https://github.com/collective/quito.core',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/quito.core',
        'Source': 'https://github.com/collective/quito.core',
        'Tracker': 'https://github.com/collective/quito.core/issues',
        # 'Documentation': 'https://quito.core.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['quito'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
	'requests',
	'dexterity.membrane',
	'Products.membrane',
	'plone.app.registry',
	'plone.app.z3cform',
	'node.ext.zodb',
	'souper.plone',
	'souper',
	'cryptography',
	
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = quito.core.locales.update:update_locale
    """,
)
