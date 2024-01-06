import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv

# Function to calculate network properties
def network_properties(G):
    """
    Calculate the diameter, clustering coefficient, and degree distribution of the network G.
    """
    # Diameter (we calculate the approximate diameter for large networks)
    if nx.is_connected(G):
        diameter = nx.diameter(G)
    else:
        diameter = float('inf')  # Infinite diameter for disconnected graphs

    # Clustering Coefficient
    clustering_coeff = nx.average_clustering(G)

    # Degree Distribution
    degrees = [G.degree(n) for n in G.nodes()]
    degree_distribution = np.unique(degrees, return_counts=True)

    return diameter, clustering_coeff, degree_distribution

# Function to create a Watts-Strogatz small-world network
def create_small_world_network(n, k, p):
    """
    n: number of nodes
    k: Each node is joined with its `k` nearest neighbors in a ring topology
    p: The probability of rewiring each edge
    """
    return nx.watts_strogatz_graph(n, k, p)

# Function to save network properties to a CSV file
def save_to_csv(data, filename="network_properties.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['N', 'K', 'P', 'Network_Name', 'Diameter', 'Clustering_Coefficient', 'Degree_Distribution'])
        # Write the data
        for row in data:
            writer.writerow(row)

def small_world(n, k, p_values):
    networks = {p: create_small_world_network(n, k, p) for p in p_values}

    # Calculate properties for each network
    network_properties_data = {p: network_properties(G) for p, G in networks.items()}

    csv_data = []

    for p, G in networks.items():
        plt.figure(figsize=(5, 5), num=f"Network with p={p}")
        nx.draw(G, node_size=50, node_color="blue", edge_color="gray")
        plt.title(f"Network with p={p}")

        # Calculate properties for the current network
        diameter, clustering_coeff, degree_distribution = network_properties_data[p]

        # Prepare data for CSV
        degree_dist_str = ', '.join([f"{degree}:{count}" for degree, count in zip(*degree_distribution)])
        csv_data.append([n, k, p, f"Network_{p}", diameter, clustering_coeff, degree_dist_str])

        # Create information text for the current network
        info_text = f"Network name: {p}\n"
        info_text += f"Diameter: {diameter}\n"
        info_text += f"Clustering Coefficient: {clustering_coeff}\n"
        info_text += "Degree Distribution:\n"
        for degree, count in zip(*degree_distribution):
            info_text += f"  Degree {degree}: {count} nodes\n"

        # Add the information to the plot using plt.text()
        plt.text(0.05, 0.05, info_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='bottom', bbox={'facecolor': 'white', 'alpha': 0.7})

    # Save the CSV data
    save_to_csv(csv_data)

if __name__ == "__main__":
    
    # Network parameters
    n = 100 # number of nodes
    k = 5   # each node is connected to k nearest neighbors in ring topology
    p_values=[0, 0.1, 1]
    
    small_world(n, k, p_values)
