# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os

# -- INPUT SECTION -- #

def inint():
    return(int(input()))

def inlist():
    return(list(map(int,input().split())))

def instr():
    s = input()
    return(list(s[:len(s) - 1]))

def invars():
    return(map(int,input().split()))

# -- TESTING SECTION -- #

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

n, k, q = invars()
max = int(2e5) + 2
frequencies = [0] * max

for i in range(n):
    li, ri = invars()
    frequencies[li] += 1
    frequencies[ri + 1] -= 1

count = 0
for i in range(max):
    count += frequencies[i]
    if count >= k:
        frequencies[i] = 1
    else:
        frequencies[i] = 0

prefix_sum = [0] * max
for i in range(1, max):
    prefix_sum[i] = prefix_sum[i - 1] + frequencies[i - 1]
    
for i in range(q):
    li, ri = invars()
    print(prefix_sum[ri + 1] - prefix_sum[li])