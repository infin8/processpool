# -*- coding: utf-8 -*-

import traceback, threading
from glob import glob
from multiprocessing import Pool, Manager
from itertools import islice

class ProcessPool(object):
    def __init__(self, concurrency=4, num=10000, qmax=None):
        self.concurrency = concurrency
        self.num = num
        
        self.qmax = qmax if qmax is not None else self.num*10
            
        self.manager = Manager()
        self.i = self.manager.JoinableQueue(qmax)
        self.o = self.manager.Queue()
        
        self.pool = Pool(processes=concurrency)
    
    def start(self):
        self.workers = [self.pool.apply_async(worker, args=(self.i,self.o)) 
            for i in xrange(self.concurrency)]
                
    def put(self, f, *args, **kwargs):
        return self.i.put((f, args, kwargs))
    
    def get(self):
        return self.o.get()

    def results(self):
        for result in iter(self.get, None):
            yield result
            
    def run(self, iterable, f, *args, **kwargs):
        self.start()
        
        for rows in xslice(iterable, self.num):
            self.put(f, *((rows,)+args), **kwargs)

        self.finish()
        
        t = threading.Thread(target=self.join)
        t.daemon = True
        t.start()
        
        return self.results()

    def finish(self, *args, **kwargs):
        [self.i.put(None) for w in self.workers]
    
    def join(self, *args, **kwargs):
        self.i.join()
        self.pool.close()
        self.pool.join()
        self.o.put(None)

def worker(i,o):
    try:
        work(i,o)
    except Exception as e:
        traceback.print_exc()
        
def work(i, o): 
    for w, args, kwargs in iter(i.get, None):
        if w: o.put(w(*args))
        i.task_done()
    i.task_done()

def xslice(iterable, size):
    x = iter(iterable)
    item = list(islice(x, size))
    while item:
        yield item
        item = list(islice(x, size))