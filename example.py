#!/usr/bin/env python
# -*- coding: utf-8 -*-

from processpool import ProcessPool
from time import sleep, time
import sys, random

def dowork(workstuff):
    sleep(random.randint(2,5))
    return 'Sum of %s: %d' % (workstuff, sum(workstuff))
    
p = ProcessPool(3,num=3)
iterable = range(100)

start = time() 

p.run(iterable, dowork)

for i, result in enumerate(p.results()):
    i+=1
    seconds = time() - start
    persecond = i/seconds
    
    sys.stdout.write("\rWork Processed: %d" % i)
    sys.stdout.write("\r\t\t\t\t%.2f per second" % persecond)
    sys.stdout.flush()
    
sys.stdout.write("\n")
sys.stdout.flush()