# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math

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

n = int(input())
a = inlist()

max_element = max(a)
already_seen = set()
second_elements = set()
for i in a:
    if i == max_element:
        continue
    elif i in already_seen:
        second_elements.add(i)
    else:
        already_seen.add(i)
        
print(already_seen)
print(second_elements)
print(max_element, max(second_elements))