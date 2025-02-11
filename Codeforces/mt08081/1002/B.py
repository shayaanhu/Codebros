# Incorrect sol (Deepseek/Copilot)

import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        pos = {}
        current = 1
        max_j = 0
        
        # Find positions of elements in increasing order
        for idx in range(n):
            if a[idx] == current:
                pos[current] = idx
                current += 1
        max_j = current - 1
        
        if max_j == 0:
            print(1)
            continue
        
        block_count = [0] * (max_j + 1)
        block_count[1] = 1
        
        # Calculate block counts
        for j in range(2, max_j + 1):
            if j-1 in pos and j in pos and pos[j] == pos[j-1] + 1:
                block_count[j] = block_count[j-1]
            else:
                block_count[j] = block_count[j-1] + 1
        
        target_blocks = k // 2
        possible_j = max_j
        
        # Find the maximum possible j such that block_count[j] <= target_blocks
        while possible_j > 0 and block_count[possible_j] > target_blocks:
            possible_j -= 1
        
        candidate = possible_j + 1
        
        current_element = 1
        earliest_mismatch = None
        
        # Find the earliest mismatch
        for num in a:
            if num == current_element:
                current_element += 1
            if current_element > candidate:
                break
        earliest_mismatch = current_element
        
        # Adjust candidate based on the earliest mismatch
        if earliest_mismatch <= candidate:
            candidate = min(candidate, earliest_mismatch - 1)
        
        print(candidate + 1 if earliest_mismatch > candidate else candidate)

if __name__ == "__main__":
    main()