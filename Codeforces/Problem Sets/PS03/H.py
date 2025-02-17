# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os

# -- INPUT SECTION -- #

def inint():
    return int(input())

def inlist():
    return list(map(int, input().split()))

def instr():
    s = input()
    return list(s)

def invars():
    return map(int, input().split())

# -- TESTING SECTION -- #

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

for _ in range(inint()):
    n = inint()
    s = list(map(int, instr()))
    
    prefix_sum = 0
    ans = 0
    dict = {0:1} # could start at 0
    
    for i in range(n):
        prefix_sum += s[i]
        length = prefix_sum - (i + 1)

        previous_count = dict.get(length, 0)    # how many subarrays exist of this length
        ans += previous_count                   # adding because each means a valid subarray
        dict[length] = previous_count + 1       # +1 for future
    
    print(ans)