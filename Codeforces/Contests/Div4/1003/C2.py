# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import bisect

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
for _ in range(inint()):
    n, m = invars()
    a, b = inlist(), inlist()
    valid = True
    current = -1 * float('inf')
    
    b.sort()
    inf = float('inf')
    
    for i in range(n):
        candidate = inf
        
        if a[i] >= current:
            candidate = a[i]
        
        required = current + a[i]
        idx = bisect.bisect_left(b, required)
        if idx < m:
            candidate_flip = b[idx] - a[i]
            candidate = min(candidate, candidate_flip)
        
        if candidate == inf:
            valid = False
            break
        
        current = candidate
    
    print("YES" if valid else "NO")