# NEPTUN.py
from VNE_classes import Graph, Claim

def decision(claim, G, nodes_cap, nodes_load):
    """
    Makes a decision on whether to serve a request and how to map it.
    Args:
    - claim: The request claim with details of the graph.
    - G: The substrate graph.
    - nodes_cap: List of capacities of each node in the substrate graph.
    - nodes_load: Current load on each node in the substrate graph.
    Returns:
    - A list of node indices in the substrate graph if the claim is to be served, otherwise None.
    """
    v = 0
    mapping = []
    for u in range(claim.G.n):
        while v < G.n:
            if claim.nodes_perf[u] <= nodes_cap[v] - nodes_load[v]:
                mapping.append(v)
                v += 1
                break
            v += 1

    if len(mapping) < claim.G.n:
        return None

    price = 0.0
    for e in claim.G.E:
        price += 10 * G.D[mapping[e[0]]][mapping[e[1]]]

    if price < claim.value:
        return mapping

    return None
