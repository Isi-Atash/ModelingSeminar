import numpy as np
import networkx as nx
import argparse

parser=argparse.ArgumentParser(description='')
parser.add_argument('-g', '--graph', dest='graph', action='store', default=None)
args=parser.parse_args()

if not args.graph:
    print ("need a graph as input")
    exit()

def read_graph(graph_file):
    with open(graph_file, encoding='utf-8-sig') as f:
        n=int(f.readline())
        m=int(f.readline())
        A=[[0]*n for _ in range(n)]
        for _ in range(m):
            [u,v]=map(int, f.readline().split())
            A[u][v]=1
            A[v][u]=1
    G=nx.Graph(np.array(A))
    return G

def max_comp_size(G):
    return max([len(c) for c in nx.connected_components(G)])

# del_list=[]    
# G=read_graph(args.graph)
# n=len(G.nodes)
# while max_comp_size(G) > n/2:
#     u=np.random.choice(G.nodes)
#     if u not in del_list:
#         del_list.append(u)
#         G.remove_node(u)

best_del_list= []
G=read_graph(args.graph)
n=len(G.nodes)

for _ in range(10):
    del_list = []

    G_temp = G.copy()  # Create a copy of the graph for each iteration

    while max_comp_size(G_temp) > n/2:
        u = np.random.choice(G_temp.nodes)
        if u not in del_list:
            del_list.append(u)
            G_temp.remove_node(u)

    # Check if the current solution is better than the previous best
    if len(del_list) < len(best_del_list) or len(best_del_list) == 0 :
        best_del_list = del_list
        best_comp_size = max_comp_size(G_temp)
#print len(del_list), del_list


for u in best_del_list:
    print (u)

print("Best solution:")
print("Number of nodes to remove:", len(best_del_list))
print("Size of the largest connected component:", best_comp_size)

with open('GBA1000dh.txt','w',encoding='utf-8-sig') as file:
    for u in best_del_list:
        file.write(str(u)+'\n')