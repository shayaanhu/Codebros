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

s = instr()
n = len(s)

prefix_array = [0] * (n + 1)
for i in range(2, n + 1):
    prefix_array[i] = 1 if s[i - 2] == s[i - 1] else 0
    # [i - 2] and [i - 1] because of 0-indexing

prefix_sum = [0] * (n + 1)
for i in range(2, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + prefix_array[i]

for _ in range(inint()):
    l, r = invars()
    print(prefix_sum[r] - prefix_sum[l])