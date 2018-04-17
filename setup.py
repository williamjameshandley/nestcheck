#!/usr/bin/env python
"""nestcheck setup."""
import setuptools


setuptools.setup(name='nestcheck',
                 version='0.0.0',
                 author='Edward Higson',
                 author_email='ejhigson@gmail.com',
                 description=('Diagnostic tests for nested sampling '
                              'calculations'),
                 url='https://github.com/ejhigson/nestcheck',
                 install_requires=['numpy>=1.13',
                                   'scipy>=1.0.0',
                                   'matplotlib>=2.1.0',
                                   'fgivenx>=1.1.4',
                                   'pandas>=0.21.0',
                                   'tqdm>=4.11'],
                 test_suite='nose.collector',
                 tests_require=['nose', 'coverage'],
                 extras_require={'docs': ['numpydoc', 'sphinx-rtd-theme']},
                 packages=['nestcheck'])
