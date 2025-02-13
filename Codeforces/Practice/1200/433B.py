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

n = inint()
v = inlist()
sorted_v = sorted(v)
m = inint()

prefix_sum_array = [0] * (n + 2)
prefix_sum_array[1] = v[0]
for i in range(2, n + 1):
    prefix_sum_array[i] = prefix_sum_array[i - 1] + v[i - 1]

u_prefix_array = [0] * (n + 2)
u_prefix_array[1] = sorted_v[0]
for i in range(2, n + 1):
    u_prefix_array[i] = u_prefix_array[i - 1] + sorted_v[i - 1]

for _ in range(m):
    t, l, r = invars()
    if t == 1:
        print(prefix_sum_array[r] - prefix_sum_array[l - 1])
    elif t == 2:
        print(u_prefix_array[r] - u_prefix_array[l - 1])