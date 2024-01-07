import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def barabasi_albert_graph(n, m0, m):
    """Generates a network using the Barabási-Albert (BA) model.

    Parameters:
    n (int): Total number of nodes in the graph.
    m0 (int): Initial number of nodes.
    m (int): Number of edges to attach from a new node to existing nodes.

    Returns:
    G (networkx.Graph): The generated graph.
    """
    # Initialize a graph with m0 nodes
    G = nx.complete_graph(m0)

    for node in range(m0, n):
        # For each new node, connect it to m existing nodes
        # The probability of connecting to a node is proportional to its degree
        targets = _select_targets(G, m)
        G.add_node(node)
        for target in targets:
            G.add_edge(node, target)

    return G

def _select_targets(G, m):
    """Selects target nodes based on preferential attachment.

    Parameters:
    G (networkx.Graph): The current graph.
    m (int): Number of targets to select.

    Returns:
    targets (list): List of selected target nodes.
    """
    # Compute the sum of degrees
    degree_sum = sum(dict(G.degree()).values())

    # Probabilities for each node
    probabilities = [G.degree(node) / degree_sum for node in G.nodes()]

    # Choose nodes based on their probability
    targets = np.random.choice(G.nodes(), size=m, replace=False, p=probabilities)
    return targets

# Parameters
n = 100  # Total number of nodes
m0 = 5    # Initial number of nodes
m = 3     # Number of edges to attach from a new node to existing nodes

# Generate the graph
ba_graph = barabasi_albert_graph(n, m0, m)

# Plot the graph
plt.figure(figsize=(12, 8))
nx.draw(ba_graph, node_size=50, node_color='blue', with_labels=False)
plt.title("Barabási-Albert Model Graph")
plt.show()
