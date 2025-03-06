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

# --- END TEMPLATE --- #

MOD = 1000000007

# Read input values
a, b, n = invars()
# Precompute factorials and inverse factorials modulo MOD.
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [1] * (n + 1)
invfact[n] = pow(fact[n], MOD - 2, MOD)  # Using Fermat's little theorem.
for i in range(n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD
# Allowed digits (as characters) for a "good" number.
allowed = {str(a), str(b)}
def is_good(x):
    """Check if every digit in x (in its decimal representation) is either a or b."""
    for ch in str(x):
        if ch not in allowed:
            return False
    return True
answer = 0
# Loop over possible count i of digit a (and n-i count of digit b)
for i in range(n + 1):
    # Sum of digits for the current distribution: i copies of a and (n-i) copies of b.
    s = i * a + (n - i) * b
    # If s is "good", then add the binomial coefficient C(n, i) to the answer.
    if is_good(s):
        comb = fact[n] * invfact[i] % MOD * invfact[n - i] % MOD
        answer = (answer + comb) % MOD
print(answer)