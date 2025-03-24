import math
from collections import defaultdict

# Constants
inf, neg_inf, mod = float('inf'), float('-inf'), 10**9 + 7
sum_form = lambda n: n * -~n // 2  # ~n == -(n+1)
pow2 = lambda n: n != 0 and (n & (n - 1)) == 0
perf_sqr = lambda n: n >= 0 and int(n**0.5)**2 == n
even, odd = lambda n: (n & 1) == 0, lambda n: not even(n)
quad_form = lambda a, b, c: ((-b + math.isqrt(b**2 - 4*a*c)) // (2*a))

# Aliases
E, L, P, R = enumerate, len, print, range
inp = lambda: int(input())
inps = lambda: input().strip()
inpm = lambda: map(int, input().split())
inpl = lambda: list(map(int, input().split()))

import sys  # Uncomment before submission
# sys.stdin = open('input.txt', 'r')

def dfs(u, p, w, sz, f):
    f[u][1] = sz[u] = 1
    for v in w[u]:
        if v != p:
            dfs(v, u, w, sz, f)
            for j in range(sz[u], -1, -1):
                for k in range(sz[v], -1, -1):
                    f[u][j + k] = max(f[u][j + k], f[u][j] * f[v][k])
            sz[u] += sz[v]
    for i in range(1, sz[u] + 1):
        f[u][0] = max(f[u][0], f[u][i] * i)

def logic() -> None:
    n = inp()
    w = defaultdict(list)
    sz = [0] * (n + 1)
    f = [[0] * (n + 1) for _ in range(n + 1)]
    
    for _ in R(n - 1):
        x, y = inpm()
        w[x].append(y)
        w[y].append(x)
    
    dfs(1, 0, w, sz, f)
    P(f[1][0])

def main() -> None:
    logic()

if __name__ == "__main__": 
    main()
