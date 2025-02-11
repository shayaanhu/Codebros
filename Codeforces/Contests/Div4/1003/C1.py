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
for _ in range(inint()):
    n, m = invars()
    a, b = inlist(), inlist()
    valid = True
    current = -1 * float('inf')
    x = b[0]

    for i in range(n):
        mini = min(a[i], x - a[i])
        maxi = max(a[i], x - a[i])
        
        if mini >= current:
            current = mini
        elif maxi >= current:
            current = maxi
        else:
            valid = False
            break

    print("YES" if valid else "NO")
