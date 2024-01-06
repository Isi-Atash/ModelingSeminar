import networkx as nx
import matplotlib.pyplot as plt
import os

# Function to create a Watts-Strogatz small-world network
def create_small_world_network(n, k, p):
    return nx.watts_strogatz_graph(n, k, p)

# Network parameters
n = 50  # number of nodes
k = 5    # each node is connected to k nearest neighbors in ring topology
p_values = [0, 0.1, 1]  # Probabilities for rewiring

# Generate networks
networks = {p: create_small_world_network(n, k, p) for p in p_values}

# Create a directory for the pictures if it doesn't exist
pictures_dir = 'pictures'
if not os.path.exists(pictures_dir):
    os.makedirs(pictures_dir)

# Plotting and saving the networks
for p, G in networks.items():
    plt.figure(figsize=(5, 5))
    nx.draw(G, node_size=50, node_color="blue", edge_color="gray")
    plt.title(f"Network with p={p}")
    
    # Save the figure to the pictures directory
    plt.savefig(f'{pictures_dir}/network_nkp_{n}_{k}_{p}.png')

    # Clear the current figure to avoid overlapping plots
    plt.clf()
