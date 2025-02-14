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

t = inint()
for _ in range(t):
    n, k = invars()
    a = inlist()
    
    peaks = [0] * n
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            peaks[i] = 1
            
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + peaks[i]
    
    best = -1  # Maximum number of peaks found in any segment.
    best_l = 0  # Starting index (0-indexed) of the optimal segment.
    for i in range(n - k + 1):
        current_peaks = prefix[i + k - 1] - prefix[i + 1]
        if current_peaks > best:
            best = current_peaks
            best_l = i
            
    # The door breaks into (number of peaks + 1) pieces.
    # Convert best_l to 1-indexed by adding 1.
    print(best + 1, best_l + 1)