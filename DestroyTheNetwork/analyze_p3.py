import numpy as np
import networkx as nx
import argparse
import sys

parser=argparse.ArgumentParser(description='')
parser.add_argument('-g', '--graph', dest='graph', action='store', default=None)
parser.add_argument('-d', '--destroy', dest='destroy', action='store', default=None)
parser.add_argument('-n', '--node', dest='isnode', action='store_const', const=False, default = True)
args=parser.parse_args()

if not args.graph or not args.destroy:
    print >> sys.stderr, 'need graph and destroylist as argument -g and/or -m'
    exit()

D=[]
with open(args.destroy) as inf:
    for line in inf:
        D.append(int(line))



with open(args.graph, encoding='utf-8-sig') as ing:
    n=int(ing.readline())
    m=int(ing.readline())
    A=[[0]*n for _ in range(n)]
    for _ in range(m):
        if not args.isnode:
            if _ in D:
                continue
        [u,v]=map(int, ing.readline().split())
        if args.isnode:
            if u in D or v in D:
                continue    
        A[u][v]=1
        A[v][u]=1
    G=nx.Graph(np.array(A))

print (len(D), [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)] )
