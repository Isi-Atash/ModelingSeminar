# Define variables to store the graph information
num_nodes = 0
num_edges = 0
edges = []

# Specify the filename of your GBAXXX.txt file
filename = 'GBA1000.txt'

# Open and read the file
with open(filename, 'r', encoding='UTF-8-sig') as file:
    lines = file.readlines()
    if len(lines) >= 2:
        num_nodes = int(lines[0].strip())
        num_edges = int(lines[1].strip())
        
        # Read the edges and store them in a list
        edges = []
        for line in lines[2:]:
            edge = line.strip().split()
            if len(edge) == 2:
                edges.append((int(edge[0]), int(edge[1])))

# Now, you have the number of nodes, number of edges, and the list of edges in the variables.

# Print the number of nodes and edges, and the list of edges
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("List of edges:")
for edge in edges:
    print(edge)
