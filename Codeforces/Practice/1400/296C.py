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
a = inlist()

# --- READ THE OPERATIONS ---
# We'll store operations using 1-indexing for convenience.
operations = [None]  # dummy element at index 0
for _ in range(m):
    li, ri, di = invars()
    operations.append((li, ri, di))

# --- COUNT HOW MANY TIMES EACH OPERATION IS USED ---
# Create a difference array for operations (size m+2 so we can mark y+1 safely)
op_count = [0] * (m + 2)
for _ in range(k):
    x, y = invars()
    op_count[x] += 1
    op_count[y + 1] -= 1

# Prefix-sum op_count so that op_count[i] holds the total number of times the i-th operation is applied.
for i in range(1, m + 1):
    op_count[i] += op_count[i - 1]

# --- APPLY OPERATIONS TO THE ARRAY USING A DIFFERENCE ARRAY ---
# Create a difference array for the array a (using 1-indexing for ease; size n+2)
a_diff = [0] * (n + 2)
for i in range(1, m + 1):
    li, ri, di = operations[i]
    # Each operation i is applied op_count[i] times.
    total_effect = di * op_count[i]
    a_diff[li] += total_effect
    a_diff[ri + 1] -= total_effect

# Compute the prefix sum of a_diff to get the cumulative additions for each position.
for i in range(1, n + 1):
    a_diff[i] += a_diff[i - 1]

# --- UPDATE THE ORIGINAL ARRAY ---
# Note: a is 0-indexed while a_diff uses 1-indexing.
result = [a[i] + a_diff[i + 1] for i in range(n)]
print(" ".join(map(str, result)))