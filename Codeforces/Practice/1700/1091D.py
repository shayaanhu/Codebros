# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

# -- INPUT SECTION -- #

def inint():
    return int(input())

def inlist():
    return list(map(int, input().split()))

def instr():
    s = input()
    return list(s)

def invars():
    return map(int, input().split())

# -- TESTING SECTION -- #

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):
    sys.stdin = open(input_path, "r")

# --- END TEMPLATE --- #

MOD = 998244353
n = inint()
# Precompute factorials mod MOD for 0..n.
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD
# Precompute inverse factorials mod MOD for 0..n.
invfact = [1] * (n + 1)
invfact[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

# The sum we need: sum_{r=1}^{n-1} (n! / r!) mod MOD.
# Note: fact[n] / r! mod MOD is computed as fact[n] * invfact[r] mod MOD.
sum_inv = 0
for r in range(1, n):
    sum_inv = (sum_inv + invfact[r]) % MOD

# The answer equals: n * n! - sum_{r=1}^{n-1} (n! / r!) mod MOD,
# i.e., answer = fact[n] * (n - sum_inv) mod MOD.
ans = fact[n] * ((n - sum_inv) % MOD) % MOD

print(ans)