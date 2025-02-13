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
n, m, k = invars()
a = inlist()
size = int(1e5) + 2 # +1 for 0-based indexing, +1 for last index

difference_array = [0] * max
difference_array[0] = 0
for i in range(m):
    li, ri, di = invars()
    difference_array[li] += di
    difference_array[ri + 1] -= di
    
prefix_sum_array = [0] * max
prefix_sum_array[0] = difference_array[0]
for i in range(1, max + 2):
    prefix_sum_array[i] = prefix_sum_array[i - 1] + difference_array[i]

for i in range(k):
    pass


