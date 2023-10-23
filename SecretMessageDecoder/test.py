def q(n, m):
    def g(x, y):
        if x == 0:
            return 0, 1
        a, b = g(y % x, x)
        return b - (y // x) * a, a

    x, _ = g(n, m)
    return x % m

def g(u, o, t, w):
    for c in range(w):
        v = q(u[c][c], t)
        for j in range(w):
            u[c][j] = (u[c][j] * v) % t
            o[c][j] = (o[c][j] * v) % t
        for r in range(w):
            if r != c:
                f = u[r][c]
                for i in range(w):
                    u[r][i] = (u[r][i] - f * u[c][i]) % t
                    o[r][i] = (o[r][i] - f * o[c][i]) % t
    return o

def p(u, a):
    decoded_parts = []
    for i in range(w):
        decoded_part = []
        for j in range(e):
            decoded_char = 0
            for k in range(w):
                decoded_char = (decoded_char + a[i][k] * u[k][w + j]) % t
            decoded_part.append(decoded_char)
        decoded_parts.append(decoded_part)
    return decoded_parts

def n():
    return ''.join(chr(c) for p in p(r, g(r, [[1 if i == j else 0 for i in range(w)] for j in range(w)], t, w)) for c in p)

w = int(input())
e = int(input())
r = [list(map(ord, input().strip())) for _ in range(w)]
t = 127

print(n())
