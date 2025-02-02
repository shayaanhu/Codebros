# --- TEMPLATE --- #

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

# if os.path.exists("input.txt"):
#     sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

for _ in range(inint()):
    n = inint()
    a = sorted(inlist())
    b = inlist()

    distinct_elements = set()
    for i in range(n):
        for j in range(n):
            distinct_elements.add(a[i] + b[j])

    if len(distinct_elements) >= 3:
        print("YES")
    else:
        print("NO")
        

