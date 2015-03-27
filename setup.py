from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='processpool',
      version=version,
      description="reusable multiprocessing pool class for python",
      long_description="""\
# ProcessPool
reusable multiprocessing pool class for python

## Install

```
pip install processpool
```

## Usage

```
from processpool import ProcessPool
from time import sleep, time
import sys, random

def dowork(workstuff):
    sleep(random.randint(2,5))
    return 'Sum of %s: %d' % (workstuff, sum(workstuff))
    
p = ProcessPool(3,num=3)
iterable = range(100)

start = time() 

for i, result in enumerate(p.run(iterable, dowork)):
    i+=1
    seconds = time() - start
    persecond = i/seconds
    
    sys.stdout.write("\rWork Processed: %d" % i)
    sys.stdout.write("\r\t\t\t\t%.2f per second" % persecond)
    sys.stdout.flush()
    
sys.stdout.write("\n")
sys.stdout.flush()
```
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
