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

for _ in range(inint()):
    n = inint()
    s = input()
    setS = set(s)

    if len(setS) == 1:
        if '1' in setS:
            print(1)
        else:
            print(0)
        continue

    count = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            count += 1

    print(count + 1 if s[0] == '1' else count)