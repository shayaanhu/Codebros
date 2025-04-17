# --- TEMPLATE 1 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter, deque
import time

# -- LOCAL DEBUG SETUP -- #
LOCAL = os.environ.get("TERM_PROGRAM", "").lower() == "vscode"

def debug(*args, **kwargs):
    if LOCAL:
        print("DBG:", *args, **kwargs)

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

# -- START TIMER FOR EXECUTION TIME TRACKING -- #
if LOCAL:
    start_time = time.perf_counter()
    
# --- BEGIN PROBLEM LOGIC --- #

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(arr, 0, 0, n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = min(self.tree[left_child], self.tree[right_child])

    def propagate(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:  # Propagate laziness to children
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += self.lazy[node]
                self.lazy[right_child] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, l, r, value, node, start, end):
        self.propagate(node, start, end)

        # No overlap
        if start > r or end < l:
            return

        # Total overlap
        if l <= start and end <= r:
            self.tree[node] += value
            if start != end:
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += value
                self.lazy[right_child] += value
            return

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        self.update_range(l, r, value, left_child, start, mid)
        self.update_range(l, r, value, right_child, mid + 1, end)
        self.tree[node] = min(self.tree[left_child], self.tree[right_child])

    def query_range(self, l, r, node, start, end):
        self.propagate(node, start, end)

        # No overlap
        if start > r or end < l:
            return float('inf')

        # Total overlap
        if l <= start and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_min = self.query_range(l, r, left_child, start, mid)
        right_min = self.query_range(l, r, right_child, mid + 1, end)
        return min(left_min, right_min)


# Input handling
import sys
input = sys.stdin.read
data = input().split()

n, q = int(data[0]), int(data[1])
a = list(map(int, data[2:n+2]))
queries = data[n+2:]

seg_tree = SegmentTree(a)
output = []

idx = 0
for _ in range(q):
    query_type = int(queries[idx])
    if query_type == 1:
        # Update query: update index k to value u
        k, u = int(queries[idx+1]) - 1, int(queries[idx+2])
        seg_tree.update_range(k, k, u - a[k], 0, 0, n - 1)
        a[k] = u
        idx += 3
    elif query_type == 2:
        # Range minimum query: find min from a to b
        l, r = int(queries[idx+1]) - 1, int(queries[idx+2]) - 1
        output.append(seg_tree.query_range(l, r, 0, 0, n - 1))
        idx += 3

sys.stdout.write('\n'.join(map(str, output)) + '\n')


# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #