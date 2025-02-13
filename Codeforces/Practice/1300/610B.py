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
    return list(input())

def invars():
    return map(int, input().split())

# -- TESTING SECTION -- #
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

n = inint()
a = inlist()

# 1. Compute the minimum amount of paint m.
m = min(a)

# 2. Build an indicator array b: b[i] = 1 if a[i] > m, else 0.
b = [1 if x > m else 0 for x in a]

# 3. Find the maximum number of consecutive 1's in b, treating b as cyclic.
max_block = 0
current = 0

# Linear scan over b:
for x in b:
    if x == 1:
        current += 1
    else:
        if current > max_block:
            max_block = current
        current = 0
if current > max_block:
    max_block = current

# Now check wrap-around: count ones at beginning and at end.
prefix = 0
for x in b:
    if x == 1:
        prefix += 1
    else:
        break

suffix = 0
for x in reversed(b):
    if x == 1:
        suffix += 1
    else:
        break

wrap_block = prefix + suffix
if wrap_block > max_block:
    max_block = wrap_block

# 4. The answer is: m full cycles plus extra squares equal to the maximum block.
answer = m * n + max_block
print(answer)