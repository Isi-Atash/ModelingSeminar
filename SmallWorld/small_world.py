import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv

# Function to create a Watts-Strogatz small-world network
def create_small_world_network(n, k, p):
    return nx.watts_strogatz_graph(n, k, p)

# Function to calculate network properties
def network_properties(G):
    if nx.is_connected(G):
        diameter = nx.diameter(G)
    else:
        diameter = float('inf')  # Infinite diameter for disconnected graphs
    clustering_coeff = nx.average_clustering(G)
    degrees = [G.degree(n) for n in G.nodes()]
    degree_distribution = np.unique(degrees, return_counts=True)
    return diameter, clustering_coeff, degree_distribution

# Function to save network properties to CSV and TXT files
def save_results(data, csv_filename="network_properties.csv", txt_filename="network_properties.txt"):
    with open(csv_filename, 'w', newline='') as csv_file, open(txt_filename, 'w') as txt_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Network_Name', 'N', 'K', 'P', 'Diameter', 'Clustering_Coefficient', 'Degree_Distribution'])
        
        for row in data:
            csv_writer.writerow(row)
            txt_file.write(', '.join(map(str, row)) + '\n')

def small_world(n_values, k_values, p_values_list):
    csv_data = []

    for n in n_values:
        for k in k_values:
            for p_values in p_values_list:
                for p in p_values:
                    G = create_small_world_network(n, k, p)
                    diameter, clustering_coeff, degree_distribution = network_properties(G)

                    degree_dist_str = ', '.join([f"{degree}:{count}" for degree, count in zip(*degree_distribution)])
                    csv_data.append([f"Network_{p}", n, k, p, diameter, clustering_coeff, degree_dist_str])

                    # Plotting (optional, can be commented out or removed)
                    plt.figure(figsize=(5, 5), num=f"Network with p={p}")
                    nx.draw(G, node_size=50, node_color="blue", edge_color="gray")
                    plt.title(f"Network with p={p}")
    plt.show()
    
    save_results(csv_data)

if __name__ == "__main__":
    
    # Example call to the main method
    n_values = [25,50, 100, 150]  # Different n values
    k_values = [4, 5, 10]     # Different k values
    p_values_list = [[0, 0.1, 1]]  # Different sets of p values
    
    small_world(n_values, k_values, p_values_list)