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

MOD = 10**9 + 7
s = instr()
n = len(s)
counts = Counter(s)

# Precompute factorials mod MOD up to n
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

# Precompute modular inverses of factorials using Fermat's little theorem
inv_fact = [1] * (n + 1)
inv_fact[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# Compute the answer: fact[n] multiplied by the inverse factorials for each repeated letter
ans = fact[n]
for count in counts.values():
    ans = ans * inv_fact[count] % MOD
    
print(ans)
