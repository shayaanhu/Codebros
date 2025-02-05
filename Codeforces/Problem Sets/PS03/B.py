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
players = []
for i in range(m):
    players.append(inint())
fedor = inint()

friends = 0
for i in players:
    if (i ^ fedor).bit_count() <= k:
        friends += 1
print(friends)