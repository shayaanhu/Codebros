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

# bitmask checks all possible combinations
# 000 -> all -
# 001 -> last one +, rest -
# 111 -> all +
# bitmask & (1 << bit) checks if a specific bit is set to 1
# if it is 1 (number could be more than 1, like 1000 == 8),
# then it's added to the sum (+)
# if it's 0, then it's subtracted (-)


n = inint()
angles = []
for i in range(n):
    angles.append(inint())
ans = False

for bitmask in range(1 << n):                    
    total_angle = 0
    for bit in range(n):
        if bitmask & (1 << bit) == 0:
            total_angle -= angles[bit]
        else:
            total_angle += angles[bit]
    if total_angle == 0 or total_angle % 360 == 0:
        ans = True
        break

if ans:
    print("YES")
else:
    print("NO")