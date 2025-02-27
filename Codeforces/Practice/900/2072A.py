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

t = inint()
for _ in range(t):
    n, k, p = inlist()

    if k == 0:
        print(0)
        continue
    
    ops = (abs(k) + p - 1) // p
    
    if ops <= n:
        print(ops)
    else:
        print(-1)