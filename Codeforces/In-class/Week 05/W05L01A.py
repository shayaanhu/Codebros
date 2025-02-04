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
    n = inint()
    l = n.bit_length()
    k = 2 ** (l - 1)
    
    print(k - 1)
    
    # x = n
    # i = 0
    # while x != 0:
    #     i += 1
    #     x = (x & (n - i))
    #     if i == n or x == 0:
    #         break
        
    # print(n - i)
    