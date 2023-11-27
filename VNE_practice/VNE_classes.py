import numpy as np

class Graph:
    def __init__(self,A):
        self.n = len(A)
        self.A = A
        self.distM()
        self.edgelist()
        
    def distM(self):
        n = len(self.A)
        D = [[0]*n for _ in range(n)]
        Am = [[0]*n for _ in range(n)]
        for u in range(n):
            for v in range(n):
                if u==v:
                    Am[u][v] = 0
                elif self.A[u][v] == 1:
                    Am[u][v] = 1
                else:
                    Am[u][v] = np.inf
        for u in range(n):
            for v in range(n):
                D[u][v] = Am[u][v]
        for _ in range(n):
            for u in range(n):
                for v in range(n):
                    D[u][v] = min([D[u][w]+Am[w][v] for w in range(n)])
        self.D = D
        
    def edgelist(self):
        n = len(self.A)
        self.E=[]
        for u in range(n):
            for v in range(u+1,n):
                if self.A[u][v] == 1:
                    self.E.append([u,v]) 

class Claim:
    def __init__(self,G,dur,val,nodes_perf,time):
        self.dur = dur
        self.G = G
        self.n = G.n
        self.nodes_perf = nodes_perf
        self.value = val
        self.init_time = time
        self.end_time = time+self.dur
        self.mapping = None

