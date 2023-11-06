import os
import numpy as np
import numpy.random as rnd
import sys
import importlib  
#import imp
import ctypes
import ctypes.util
from numpy.ctypeslib import ndpointer
import event_gen as eg

PPP=60
claim_types={'bronze':{'bw': 1, 'value': 2, 'damage':4, 'duration': 100, 'pr': 0.4}, 
        'silver': {'bw': 3, 'value': 5, 'damage':6, 'duration': 50, 'pr': 0.3}, 
        'gold':{'bw': 10, 'value': 30, 'damage':80, 'duration': 70, 'pr': 0.1}}


class Claim:
    def __init__(self,ty,time):
        self.ty = ty
        self.bw=claim_types[ty]['bw']
        self.val=claim_types[ty]['value']
        self.dam=claim_types[ty]['damage']
        self.dur=claim_types[ty]['duration']
        self.init_time=time
        self.end_time=time+self.dur

class Sim:
    def __init__(self,bw):
        self.queue=[]
        self.bw=bw
        self.free=bw
        self.budget=(-1)*PPP*self.bw
    
    def step(self, lista):
        self.budget-=sum([self.queue[i].dam for i in range(len(self.queue)) if lista[i]==0])
        self.queue = [self.queue[i] for i in range(len(self.queue)) if lista[i]==1]
        
    def new(self, item):
        if item.bw<=self.free:
            self.queue.append(item)
    
    def process(self,time):
        for i in range(len(self.queue)-1,-1,-1):
            if self.queue[i].end_time<=time:
                self.budget+=self.queue[i].val
                del self.queue[i]
        self.free=self.bw
        for item in self.queue:
            self.free-=item.bw
    
    def get_queue_list(self,time):
        lista=[]
        for item in self.queue:
            lista.append([item.ty,item.end_time-time])
        return lista

results={}
folder='Strats'

sys.path.append(folder)
strats=os.listdir(folder)
strats_py=[x.split('.')[0] for x in strats if x.split('.')[-1]=="py"]
#strats_py=['tut_mymy']

for _ in range(10):
    events=eg.event_gen(2000)
    """
    os.system('python event_gen.py >event1.txt')                    
    with open('event1.txt') as inf:
        for line in inf:
            a=line.split()
    #        print a
            if a:
                events.append([int(a[0]),a[1]])

    #print events
    """
    for strat in strats_py:
        mod=importlib.import_module(strat)
        sim=Sim(max(0,mod.init_bw()))
        for e in events:
            [time,claim]=e
            sim.process(time)
            [new,lista]=mod.decision(claim, sim.get_queue_list(time))
            sim.step(lista)
            if new==1:
                sim.new(Claim(claim,time))
        sim.process(time+1000)
        if not strat in results:
            results[strat]=0
        results[strat]+=sim.budget
for key in results:
    results[key]/=10.0
print(results)
