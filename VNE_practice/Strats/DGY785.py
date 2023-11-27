# DGY785.py
from VNE_classes import Graph, Claim
from itertools import permutations

def decision(claim, G, nodes_cap, nodes_load):
    best_mapping = None
    best_profit = -float('inf')  # Initialize with a very low profit

    for mapping in generate_all_possible_mappings(claim.G.n, G.n):
        if is_valid_mapping(mapping, claim, nodes_cap, nodes_load):
            profit = calculate_profit(mapping, claim, G)
            if profit > best_profit:
                best_profit = profit
                best_mapping = mapping

    return best_mapping

def generate_all_possible_mappings(num_virtual_nodes, num_substrate_nodes):
    # Generate all possible mappings of virtual nodes to substrate nodes
    return permutations(range(num_substrate_nodes), num_virtual_nodes)

def is_valid_mapping(mapping, claim, nodes_cap, nodes_load):
    for vn, sn in enumerate(mapping):
        if nodes_cap[sn] - nodes_load[sn] < claim.nodes_perf[vn]:
            return False
    return True

def calculate_profit(mapping, claim, G):
    price = 0
    for e in claim.G.E:
        price += 10 * G.D[mapping[e[0]]][mapping[e[1]]]

    return claim.value - price

