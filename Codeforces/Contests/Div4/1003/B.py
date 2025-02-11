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
    s = input()
    n = len(s)
    valid = False
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            valid = True
            break
    if valid:
        print(1)
    else:
        print(n)
