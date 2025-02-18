# --- TEMPLATE --- #

# -- IMPORTS -- #

import sys
import os
from pathlib import Path

# -- INPUT SECTION -- #

def inint():
    return(int(input()))

def inlist():
    return(list(map(int, input().split())))

def instr():
    s = input()
    return(list(s[:len(s) - 1]))

def invars():
    return(map(int, input().split()))

# -- TESTING SECTION -- #

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):  
    sys.stdin = open(input_path, "r")
    
# --- END TEMPLATE --- #

for _ in range(inint()):
    n, k = invars()
    s = input()
    
    i, count = 0, 0
    while i < n:
        if s[i] == "W":
            i += 1
        elif s[i] == "B":
            i += k
            count += 1
            
    print(count)