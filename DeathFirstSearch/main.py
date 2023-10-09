import sys

# Read initialization data
n, l, e = map(int, input().split())
links = []  # Store information about links between nodes
gateways = set()  # Store the indices of gateway nodes

for i in range(l):
    n1, n2 = map(int, input().split())
    links.append((n1, n2))

for i in range(e):
    ei = int(input())
    gateways.add(ei)

# Initialize a dictionary to track the number of links connected to each node
node_links = {i: 0 for i in range(n)}

# Game loop
while True:
    si = int(input())  # Current position of the Bobnet agent

    # Implement the strategy to decide which link to sever
    chosen_link = None

    # Look for links connected to the agent's current position that lead to gateways
    for link in links:
        n1, n2 = link
        if (n1 == si and n2 in gateways) or (n2 == si and n1 in gateways):
            chosen_link = link
            break

    if chosen_link is None:
        # If no direct links to gateways are found, sever a link connected to a node with the fewest links
        min_links = min(node_links.values())
        for link in links:
            n1, n2 = link
            if node_links[n1] == min_links or node_links[n2] == min_links:
                chosen_link = link
                break

    if chosen_link:
        c1, c2 = chosen_link
        links.remove(chosen_link)  # Remove the chosen link from the list
        node_links[c1] -= 1
        node_links[c2] -= 1
    else:
        # If no links are left to sever, you can choose any valid link
        c1, c2 = 0, 1

    # Output the indices of the nodes to sever the link between
    print(f"{c1} {c2}")
