#neptun
from VNE_classes import Graph,Claim

def decision(claim, G, nodes_cap, nodes_load):
    v=0
    mapping=[]
    for u in range(claim.G.n):
        while v < G.n:
            if claim.nodes_perf[u] <= nodes_cap[v]-nodes_load[v]:
                mapping.append(v)
                v+=1
                break
            v+=1
    return mapping
