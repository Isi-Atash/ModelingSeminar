w=int(input())
e=int(input())
r=[list(map(ord,input().strip()))for _ in range(w)]
t=127
def q(n):
    def g(x,y):
        if x==0:
            return 0,1
        a,b=g(y%x,x)
        return b-(y//x)*a,a
    x,_=g(n,t)
    return x%t
def g(u,o):
    for c in range(w):
        v=q(u[c][c])
        for j in range(w):
            u[c][j]=(u[c][j]*v)%t
            o[c][j]=(o[c][j]*v)%t
        for r in range(w):
            if r!=c:
                f=u[r][c]
                for i in range(w):
                    u[r][i]=(u[r][i]-f*u[c][i])%t
                    o[r][i]=(o[r][i]-f*o[c][i])%t
    return o
def p(a):
    return [[sum(a[i][k]*r[k][w+j]%t for k in range(w))%t for j in range(e)] for i in range(w)]

print(''.join(chr(c) for p in p(g(r,[[1 if i==j else 0 for i in range(w)] for j in range(w)])) for c in p))
