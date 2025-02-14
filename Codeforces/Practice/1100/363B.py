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
    return(list(s))

def invars():
    return(map(int,input().split()))

# -- TESTING SECTION -- #

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

n, k = invars()
h = inlist()

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + h[i]

min_sum = float('inf')
min_index = 0
for i in range(n - k + 1):
    current_sum = prefix_sum[i + k] - prefix_sum[i]
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i

print(min_index + 1)