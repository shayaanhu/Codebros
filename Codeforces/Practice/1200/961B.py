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
	return(list(s))

def invars():
	return(map(int,input().split()))

# -- TESTING SECTION -- #

if os.path.exists("input.txt"):
	sys.stdin = open("input.txt", "r")

# --- END TEMPLATE --- #

n, k = invars()
a = inlist()
t = inlist()

# Calculate the base number of theorems that Mishka writes when he is awake
base = 0
for i in range(n):
	if t[i] == 1:
		base += a[i]

# For each minute, compute the additional theorems we can add if Mishka were woken up (i.e., if he was asleep)
extra = [0] * n
for i in range(n):
	if t[i] == 0:
		extra[i] = a[i]
	else:
		extra[i] = 0

# Build prefix sums of the extra array
prefix = [0] * (n + 1)
for i in range(n):
	prefix[i + 1] = prefix[i] + extra[i]

# Find the block of k consecutive minutes that yields the maximum additional theorems
max_extra = 0
for i in range(n - k + 1):
	current_extra = prefix[i + k] - prefix[i]
	if current_extra > max_extra:
		max_extra = current_extra

# The answer is the base plus the maximum extra theorems we can gain
print(base + max_extra)