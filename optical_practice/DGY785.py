import numpy as np
import argparse
import sys

parser=argparse.ArgumentParser(description='')
parser.add_argument('-g', '--graph', dest='graph', action='store', default=None)
parser.add_argument('-m', '--mtrail', dest='mtrail', action='store', default=None)
args=parser.parse_args()

if not args.graph or not args.mtrail:
    print('need graph and mtrail as argument -g and/or -m', file=sys.stderr)
    exit()
    
with open(args.graph) as ing:
    n=int(ing.readline().rstrip())
    A=[]
    for _ in range(n):
        A.append(list(map(int,ing.readline().rstrip().split())))
    B=[]
    for _ in range(n):
        B.append(list(map(int,ing.readline().rstrip().split())))
    m=len(B[0])
    P=[]
    for _ in range(n):
        P.append(list(map(float,ing.readline().rstrip().split())))

with open(args.mtrail) as inm:
    neptuns=inm.readline().rstrip().split()
    M=[]
    for _ in range(m):
        M.append(list(map(int,inm.readline().rstrip().split())))

A=np.array(A)
B=np.array(B)
M=np.array(M)



b_=True
for i in range(m):
    if (M[i]==[0]*len(M[i])).all():
        b_=False
        break
    for j in range(i+1,m):
        if (M[i]==M[j]).all():
            b_=False
            break
    if not b_:
        break
if not b_:
    print('wrong m-trails', file=sys.stderr)
    exit()

noc=0
for i in range(len(M[0])):
    M_=np.array([x[i] for x in M])
    B_=B[:,np.where(M_==1)[0]]
    B_=np.array([x for x in B_ if (x != [0]*len(x)).any()])
    r=np.linalg.matrix_rank(B_)
    noc+=len(B_)-r
print(noc)
