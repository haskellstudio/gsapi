from setuptools import setup, find_packages
from distutils.extension import Extension
# from Cython.Distutils import build_ext

# import distutils.ccompiler
# import utils.parallelComp

# distutils.ccompiler.CCompiler.compile = utils.parallelComp.parallelCCompile

def checkLazySetupCommands():
      # utility when compiling from IDE, last uncommented executes desired action
    toAppend = ['clean', '--all']
    toAppend = ['build']
    toAppend = ['install']
    toAppend = ['test']; import logging;gsapi.GSLogging.setDefaultLoggingLevel(logging.ERROR)

    # toAppend  = ['sdist', 'bdist_wheel', 'install']

    # remainder for pip maintainers
    # (once .pypirc edited)
    # bump the GSAPIFullVersion in __init__.py then : python setup.py sdist bdist_wheel upload

    if len(sys.argv) == 1:
        for s in toAppend:
            sys.argv.append(s)
    print sys.argv


if __name__ == '__main__':
    import sys
    import gsapi  # TODo moved gsapi from line 44 to line 24
    checkLazySetupCommands()



setup(name='gsapi',
      version=gsapi.getGSAPIFullVersion(),
      description='Python Symbolic Music Manipulation Tools',
      long_description="",
      author='Martin Hermant, Angel Faraldo, Pere Calopa',
      author_email='angel.faraldo@upf.edu',
      url='https://github.com/Giantsteps/gsapi',
      license='',
      packages=find_packages(exclude=['utils', 'gen', 'test', 'docs']),
      # ext_modules=[gsapiModule],
      # package_data={'gsapi': package_data},
      exclude_package_data={'': ['tests', 'docs']},
      # scripts=scripts,
      # cmdclass={'build_ext': build_ext},
      test_suite='nose.collector',
      install_requires=['python-midi', 'midiutil'],
      zip_safe=True
      # classifiers=classifiers
      )
