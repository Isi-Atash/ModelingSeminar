from collections import deque
import sys
import math

def find_shortest_path(graph, start, end):
    # Create a dictionary to store the parent node of each node in the path.
    parent = {}
    
    # Create a queue for BFS and enqueue the start node.
    queue = deque([start])
    
    # Initialize the parent of the start node as None.
    parent[start] = None
    
    while queue:
        current_node = queue.popleft()
        
        # If we've reached the end node, reconstruct and return the path.
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return list(reversed(path))
        
        # Explore neighbors of the current node.
        for neighbor in graph[current_node]:
            if neighbor not in parent:
                parent[neighbor] = current_node
                queue.append(neighbor)
    
    # If no path is found, return None to indicate no path exists.
    return None


# Read the initial inputs
n, l, e = map(int, input().split())
graph = {i: [] for i in range(n)}

# Build the graph based on link information
for i in range(l):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# Store the gateway nodes
gateway_nodes = set()
for i in range(e):
    ei = int(input())
    gateway_nodes.add(ei)

# Game loop
while True:
    si = int(input())  # T5he index of the node on which the Bobnet agent is positioned this turn
    
    # Find the nearest gateway node from the current position
    nearest_gateway = None
    shortest_distance = float('inf')
    
    for gateway_node in gateway_nodes:
        path = find_shortest_path(graph, si, gateway_node)
        if path and len(path) < shortest_distance:
            shortest_distance = len(path)
            nearest_gateway = gateway_node
    
    # Output the next move (the first two nodes in the path)
    
    path = find_shortest_path(graph, si, nearest_gateway)
    print(f'{path[0]} {path[1]}')