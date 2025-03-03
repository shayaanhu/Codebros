# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

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

sys.set_int_max_str_digits(int(1e9))

for _ in range(inint()):
    n, d = invars()
    ans = [1]
    n = min(n, 7)
    fact = int(str(d) * math.factorial(n))

    for i in range(3, 10, 2):
        if fact % i == 0:
            ans.append(i)

    print(*ans)


    # if d == 1:
    #     if n > 2:
    #         ans += [3, 7]
    #     if n > 5:
    #         ans.append(9)

    # elif d == 3:
    #     ans.append(3)
    #     if n > 2:
    #         ans += [7, 9]

    # elif d == 5:
    #     ans.append(5)
    #     if n > 2:
    #         ans += [3, 7]
    #     if n > 5:
    #         ans.append(9)

    # elif d == 7:
    #     ans.append(7)
    #     if n > 2:
    #         ans.append(3)
    #     if n > 5:
    #         ans.append(9)

    # elif d == 9:
    #     ans += [3, 9]
    #     if n > 2:
    #         ans.append(7)

    # elif d in (2, 4, 8):
    #     if n > 2:
    #         ans += [3, 7]
    #     if n > 5:
    #         ans.append(9)

    # elif d == 6:
    #     ans.append(3)
    #     if n > 2:
    #         ans += [7, 9]
            
    # ans.sort()
    # print(*ans)