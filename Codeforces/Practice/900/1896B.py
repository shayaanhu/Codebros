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

# Alternate 1
# from pathlib import Path
# base_path_2 = Path(__file__).parent
    
# Alternate 2
# if os.path.exists("input.txt"):
#     sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

for _ in range(inint()):
    n = inint()
    s = instr()

    firstA = -1
    for i in range(n):
        if s[i] == 'A':
            firstA = i
            break

    lastB = -1
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            lastB = i
            break

    if firstA == -1 or lastB == -1:
        print(0)
    else:
        print(max(0, lastB - firstA))