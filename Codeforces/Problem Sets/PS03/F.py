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

n, q = invars()
a = inlist()
max = int(2e5) + 1
difference_array = [0] * (n + 1) # n + 1 for dummy zero so (n - 1)th value works
frequency_array  = [0] * (n + 1)
sum = 0

# difference array
for i in range(q):
    li, ri = invars()
    difference_array[li - 1] += 1 # 0-based indexing
    difference_array[ri] -= 1

# convert difference array to frequency array using prefix/cumulative sum
frequency_array[0] = difference_array[0]
for i in range(1, n):
    frequency_array[i] += frequency_array[i - 1] + difference_array[i]

# remove the last dummy 0
frequency_array = frequency_array[:n]

# sort both a and frequency array
# this is because least frequent elements will have lowest numbers
# so sum is maximized
a.sort()
frequency_array.sort()

# can now calculate sum by pairing the least frequent elements with lowest numbers
for i in range(n):
    sum += a[i] * frequency_array[i]

print(sum)