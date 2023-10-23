# DGY785
# python3

def i(n, m):
    g, x, _ = g(n, m)
    if g == 1:
        return x % m
    else:
        return None

def g(x, y):
    if x == 0:
        return (y, 0, 1)
    else:
        r, a, b = g(y % x, x)
        return (r, b - (y // x) * a, a)

def v(h):
    o = [[0] * h for _ in range(h)]
    for i in range(h):
        o[i][i] = 1 
    return o

def g(e, h, m, s):
    for col in range(s):
        col_value = i(e[col][col], m)
        for j in range(s):
            e[col][j] = (e[col][j] * col_value) % m
            h[col][j] = (h[col][j] * col_value) % m
        for row in range(s):
            if row != col:
                factor = e[row][col]
                for i in range(s):
                    e[row][i] = (e[row][i] - factor * e[col][i]) % m
                    h[row][i] = (h[row][i] - factor * h[col][i]) % m
    return h

def d(e, g, h, s, m):
    # Decode the message parts using the inverse header
    decoded_parts = []
    for i in range(h):
        decoded_part = []
        for j in range(s):
            decoded_char = 0
            for k in range(h):
                decoded_char = (decoded_char + g[i][k] * e[k][h + j]) % m
            decoded_part.append(decoded_char)
        decoded_parts.append(decoded_part)
    return decoded_parts

def l(d):
    m = ''
    for p in d:
        for c in p:
            m += chr(c)
    return m

def j(h, m, e, a):
    i = v(h)
    
    v = g(e, i, a, h)

    s = d(e, v, h, m, a)

    c = l(s)

    return c

h = int(input())
s = int(input())
y = [list(map(ord, input().strip())) for _ in range(h)]
m = 127

u = j(h, s, y, m)

print(u)
