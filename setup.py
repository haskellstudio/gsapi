#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages

# from distutils.extension import Extension

# LEGACY IMPORTS
# ==============
# from Cython.Distutils import build_ext
# import distutils.ccompiler
# import utils.parallelComp
# distutils.ccompiler.CCompiler.compile = utils.parallelComp.parallelCCompile


def checkLazySetupCommands():
    # utility when compiling from IDE, last uncommented executes desired action
    toAppend = ['clean', '--all']
    toAppend = ['build']

    # remainder for pip maintainers:
    # (once .pypirc edited)
    # bump the GSAPI_FULL_VERSION in GSAPI_FULL_VERSION.py
    # then: python setup.py sdist bdist_wheel upload

    if len(sys.argv) == 1:
        for s in toAppend:
            sys.argv.append(s)
    print (sys.argv)


if __name__ == '__main__':
    import sys
    from gsapi import *
    print("gsapi value%s" % getGsapiFullVersion())
    checkLazySetupCommands()

setup(name='gsapi',
      version=getGsapiFullVersion(),
      description='Python Symbolic Music Manipulation Tools',
      url='https://github.com/angelfaraldo/gsapi',
      author='Martin Hermant, Ángel Faraldo, Pere Calopa',
      author_email='angel.faraldo@upf.edu',
      license='',
      packages=find_packages(exclude=['utils', 'gen', 'tests', 'docs_old']),
      # ext_modules=[gsapiModule],
      # package_data={'gsapi': package_data},
      # exclude_package_data={'': ['tests', 'docs_old']},
      # scripts=scripts,
      # cmdclass={'build_ext': build_ext},
      test_suite='nose.collector',
      install_requires=['numpy', 'sphinx_rtd_theme'],
      zip_safe=True)
      # classifiers=classifiers)
