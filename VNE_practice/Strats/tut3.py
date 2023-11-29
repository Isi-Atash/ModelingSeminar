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
    if len(mapping) < claim.G.n:
        #print claim.G.n, mapping
        return None
    price=0.0
    #print G.n, mapping, claim.G.E
    for e in claim.G.E:
        price += 10*G.D[mapping[e[0]]][mapping[e[1]]]
    #print mapping, price, claim.value
    if price < claim.value:
        #print mapping
        return mapping
    return None
