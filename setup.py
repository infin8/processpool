from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='processpool',
      version=version,
      description="reusable multiprocessing pool class for python",
      long_description="""\
see README here http://github.com/infin8/processpool
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='multiprocess pool manager',
      author='n8',
      author_email='yo.its.n8@gmail.com',
      url='http://github.com/infin8/processpool',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
