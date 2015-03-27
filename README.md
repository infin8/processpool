# ProcessPool
reusable pool class for simplifying the use of multiprocessing in python

## Install

```
pip install processpool
```

## Usage

```python
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
