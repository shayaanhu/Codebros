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

MOD = 998244353

# Read prime factorization for X
N = inint()              # Number of distinct primes in X
A = inlist()             # List of primes in X
B = inlist()             # Their exponents

# Read prime factorization for Y
M = inint()              # Number of distinct primes in Y
C = inlist()             # List of primes in Y
D = inlist()             # Their exponents

# Build dictionaries for X and Y: prime -> exponent
primeX = {}
for i in range(N):
    primeX[A[i]] = B[i]

primeY = {}
for j in range(M):
    primeY[C[j]] = D[j]

# Count the number of primes for which exponent in X is greater than exponent in Y.
# For any prime k, let:
#   a = f_k(X) (defaulting to 0 if k is not present)
#   b = f_k(Y) (defaulting to 0 if k is not present)
# If a < b then it's impossible; if a == b then only one way; if a > b then two ways.
count_two_ways = 0

# Consider the union of primes in X and Y.
all_primes = set(primeX.keys()).union(set(primeY.keys()))
for k in all_primes:
    a = primeX.get(k, 0)
    b = primeY.get(k, 0)
    if a < b:
        print(0)
        sys.exit(0)
    if a > b:
        count_two_ways += 1

# The answer is 2^(count_two_ways) modulo MOD.
result = pow(2, count_two_ways, MOD)
print(result)