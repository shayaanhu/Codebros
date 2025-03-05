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

def is_prime(n):
    if n < 2:
        return False
    
    r = int(math.sqrt(n))
    for i in range(2, r + 1): # loop from 2 to sqrt(n)
        if n % i == 0:        # if n is divisible by any i, it's not prime
            return False
        
    return True               # else if no divisors found, it's prime

for _ in range(inint()):
    n = inint()

    # initially, if n is 1, ashish cannot make a move
    if n == 1:
        ashish_loses = True
    else:
        ashish_loses = False

    # if number is odd ashish will always win
    # because odd numbers always have odd divisors (itself)
    # for even numbers greater than 2, check specific conditions
    if n > 2 and n % 2 == 0:

        if n & (n - 1) == 0:    # if n is a power of two then it's a losing position
            ashish_loses = True # because it has no odd divisor. so they both have to keep subtracting 1

        elif n % 4 != 0 and is_prime(n // 2): # else if n = 2 * p where p is prime, it's also losing
            ashish_loses = True               # because ashish has to divide by the prime number and is
                                              # left with 2. so he loses. if it's divisible by 4, 
                                              # he can avoid this (use an odd divisor or divide by 2 multiple times)
    if ashish_loses:
        print("FastestFinger")
    else:
        print("Ashishgup")