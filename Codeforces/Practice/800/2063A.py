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

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):  
    sys.stdin = open(input_path, "r")

# --- END TEMPLATE --- #

t = inint()
for _ in range(t):
    l, r = invars()
    ans = 0

    if l <= 1 <= r:
        ans += 1

    start = max(l, 2)
    if start <= r - 1:
        ans += (r - start)

    print(ans)