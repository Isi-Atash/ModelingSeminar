import numpy as np
import numpy.random as rnd
from VNE_classes import Claim, Graph

def event_gen(n):
    events=[]
    for t in range(n):
        r=rnd.choice(range(10))
        if r < 9:
            if r < 5:
                A=[[0,1,0],[1,0,1],[0,1,0]] #adjacency matrix of a path of length 2
            else:
                A=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]] #a clique on 4 points
            G=Graph(A)
            dur = 20 * rnd.random() #duration
            val = 30*len(G.E) * rnd.random() #profit if embedded
            nodes_perf = rnd.choice(range(1,4),G.n) #
            events.append([t, Claim(G, dur, val, nodes_perf, t)])
    return events

if __name__ == "__main__":
    events = event_gen(2000)
    for event in events:
        print (event[0], event[1])
