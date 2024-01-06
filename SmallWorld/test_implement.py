import networkx as nx
import matplotlib.pyplot as plt

# Function to create a Watts-Strogatz small-world network
def create_small_world_network(n, k, p):
    """
    n: number of nodes
    k: Each node is joined with its `k` nearest neighbors in a ring topology
    p: The probability of rewiring each edge
    """
    return nx.watts_strogatz_graph(n, k, p)

def plot_small_world_networks(numnber_of_nodes, k_nearest_neighbors, topology = None):
    

    # Probabilities for rewiring
    p_values = [0, 0.1, 1]

    # Generate networks
    networks = {p: create_small_world_network(n, k, p) for p in p_values}

    # Plotting the networks
    # Adjusting the code to open a new figure for each probability
    
    for p, G in networks.items():
        plt.figure(figsize=(5, 5), num=f"Network with p={p}")
        if topology == "C":
            nx.draw_circular(G, node_size=50, node_color="blue", edge_color="gray")
        elif topology == "R":
            nx.draw(G, node_size=50, node_color="blue", edge_color="gray")
        else:
            nx.draw(G, node_size=50, node_color="blue", edge_color="gray")
        plt.title(f"Network with p={p}")
    plt.show()

# Main method
if __name__ == "__main__":
    
    # Network parameters
    n = 25  # number of nodes
    k = 4   # each node is connected to k nearest neighbors in ring topology
    topology = "R" # Network drawing. C = circular. 
    
    plot_small_world_networks(n, k, topology)
