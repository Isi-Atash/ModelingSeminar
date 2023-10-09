import networkx as nx
import numpy as np

# Load your graph from a file (replace 'your_graph_file.txt' with your file)
G = nx.read_edgelist('GBA1000.txt')

# Calculate betweenness centrality for each node
betweenness_centrality = nx.betweenness_centrality(G)

# Sort nodes by betweenness centrality in descending order
sorted_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

# Set the desired number of nodes to remove
nodes_to_remove = len(G.nodes) - 500  # Adjust as needed

# Keep track of the removed nodes
removed_nodes = set()

# Remove nodes with the highest betweenness centrality first
for node, _ in sorted_nodes[:nodes_to_remove]:
    G.remove_node(node)
    removed_nodes.add(node)

# You can now use G with the remaining nodes and edges
print("Remaining number of nodes:", len(G.nodes()))
print("Remaining number of edges:", len(G.edges()))
print("Nodes to delete:", list(removed_nodes))
