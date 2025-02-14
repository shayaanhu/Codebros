# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os

# -- INPUT SECTION -- #

def inint():
    return int(input())

def inlist():
    return list(map(int, input().split()))

def instr():
    s = input()
    return list(s[:len(s) - 1])

def invars():
    return map(int, input().split())

# -- TESTING SECTION -- #

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

n, m, c = invars()
a = inlist()
b = inlist()

# Precompute prefix sum for b.
# pb[i] will be the sum of b[0] + b[1] + ... + b[i-1] (with pb[0]=0).
pb = [0] * (m + 1)
for i in range(m):
    pb[i + 1] = pb[i] + b[i]

# We'll use 0-indexing.
# There are n-m+1 steps (from i=0 to i=n-m) that add b[0..m-1] to a sliding window.
# For each message position k (0-indexed), it is affected by all steps i satisfying:
#     i in [max(0, k-(m-1)), min(k, n-m)]
# For each such i, the key element added is b[k - i].
# Changing variable: let k' = k - i.
# Then k' runs from A = k - min(k, n-m) to B = k - max(0, k-m+1).
# So the total added to a[k] is pb[B+1] - pb[A].

for k in range(n):
    # i runs from I_low to I_high, where:
    I_low = max(0, k - (m - 1))
    I_high = min(k, n - m)
    # Changing variable: k' = k - i.
    # Then k' runs from:
    A = k - I_high  # smallest k' when i is largest
    B = k - I_low   # largest k' when i is smallest
    addition = pb[B + 1] - pb[A]
    a[k] = (a[k] + addition) % c

print(' '.join(map(str, a)))
