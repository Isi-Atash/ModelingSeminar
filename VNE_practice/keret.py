import numpy as np
import copy
from VNE_classes import Graph, Claim
import sys
import os
import event_gen as eg
import importlib

PP=10


class Sim:
    def __init__(self, G, nodes_cap):
        self.G = G
        self.nodes_cap = nodes_cap
        self.nodes_load = [0 for v in nodes_cap]
        self.money = 0
        self.queue = []
    
    def new(self, mapping, claim):
        #print claim.init_time, claim.end_time, mapping, self.nodes_load
        if len(set(mapping)) < claim.G.n:
            return
        if max(mapping) >= self.G.n:
            return
        for u in range(claim.G.n):
            """
            print mapping
            print self.nodes_cap
            print self.nodes_load
            print claim.nodes_perf
            """
            if self.nodes_cap[mapping[u]]-self.nodes_load[mapping[u]] < claim.nodes_perf[u]:
                return
        
        claim.mapping = mapping[:]
        self.queue.append(claim)
        for u in range(claim.G.n):
            self.nodes_load[claim.mapping[u]] += claim.nodes_perf[u]
        self.money+=claim.value
        for e in claim.G.E:
            self.money -= PP*self.G.D[claim.mapping[e[0]]][claim.mapping[e[1]]]    #here the price of the embedding is taken
        #print self.nodes_load
            
    def delet(self,claim):
        #print claim.end_time, self.nodes_load
        for u in range(claim.G.n):
            self.nodes_load[claim.mapping[u]] -= claim.nodes_perf[u]
        #print self.nodes_load
    
    def process(self,time):
        for i in range(len(self.queue)-1,-1,-1):
            if self.queue[i].end_time<=time:
                self.delet(self.queue[i])
                del self.queue[i]
    

#print G.D

results={}
folder='Strats'

sys.path.append(folder)
strats=os.listdir(folder)
strats_py=[x.split('.')[0] for x in strats if x.split('.')[-1]=="py"]
#strats_py=['tut2']

NN=10
for _ in range(NN):
    events=eg.event_gen(2000)
    for strat in strats_py:
        mod=importlib.import_module(strat)
        A=[[0,1,1,0,0,0,0,0], #Adjacency matrix of two 4 long circles connected by and edge
	[1,0,0,1,0,0,0,0],
	[1,0,0,1,0,0,0,0],
	[0,1,1,0,1,0,0,0],
        [0,0,0,1,0,1,1,0],
	[0,0,0,0,1,0,0,1],
	[0,0,0,0,1,0,0,1],
	[0,0,0,0,0,1,1,0]]
	#print A        
        G=Graph(A)
        #print G.D
        sim=Sim(G,[5]*G.n)
        for e in events:
            [time,claim]=e
            sim.process(time)
            G = copy.deepcopy(sim.G)
            nodes_cap = sim.nodes_cap[:]
            nodes_load = sim.nodes_load[:]
            claim0 = copy.deepcopy(claim)
            #print time, sim.nodes_load
            mapping=mod.decision(claim0, G, nodes_cap, nodes_load)
            if mapping:
                sim.new(mapping,claim)
            #print time, sim.nodes_load
        sim.process(time+1000)
        if not strat in results:
            results[strat]=0
        results[strat]+=sim.money
for key in results:
    results[key]/=(1.0*NN)
print(results)

