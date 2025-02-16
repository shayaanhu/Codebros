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

prefix = [0] * (m + 1)
for i in range(m):
    prefix[i + 1] = prefix[i] + b[i]

for k in range(n):
    low = max(0, k - (m - 1))
    high = min(k, n - m)

    aIndex = k - high
    bIndex = k - low

    addition = prefix[bIndex + 1] - prefix[aIndex]
    a[k] = (a[k] + addition) % c

print(' '.join(map(str, a)))