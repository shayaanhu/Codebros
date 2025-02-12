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
n, l, r, x = invars()
c = inlist()
ans = 0

for i in range(1 << n):
    summ = 0
    temp = []
    for j in range(n):
        if i & (1 << j) != 0:
            summ += c[j]
            temp.append(c[j])
    if l <= summ <= r and max(temp) - min(temp) >= x:
        ans += 1

print(ans)