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

MOD = 1000000007

n, k = invars()
divs = [[] for _ in range(n + 1)]
for d in range(1, n + 1):
    for j in range(d, n + 1, d):
        divs[j].append(d)
dp = [0] * (n + 1)
for x in range(1, n + 1):
    dp[x] = 1
for _ in range(1, k):
    dp = [0] + [sum(dp[d] for d in divs[j]) % MOD for j in range(1, n + 1)]
answer = sum(dp[1:]) % MOD
print(answer)
