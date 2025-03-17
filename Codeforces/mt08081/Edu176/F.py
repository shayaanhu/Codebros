for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(1)
        continue
    
    # if n == 2:
    #     print(2)
    #     continue

    min_val = min(a)
    max_val = max(a)
    first_min = a.index(min_val)
    last_max = len(a) - 1 - a[::-1].index(max_val)
    
    # print(first_min, last_max)
    if first_min > last_max:
        print(1)
        continue
    count = 0
    for num in a[first_min:last_max + 1]:
        if num > min_val and num < max_val:
            count += 1

    print(count + 2)



# import sys
# from collections import Counter

# def longest_beautiful_subsequence(n, a):
#     freq = Counter(a)  # Count occurrences of each element
#     unique_sorted = sorted(freq.keys())  # Get unique elements in sorted order

#     length = len(unique_sorted)  # First take unique elements
#     for x in unique_sorted:
#         if freq[x] > 1:
#             length += 1  # Add one more if the element appears more than once

#     return length


# results = []
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     results.append(str(longest_beautiful_subsequence(n, a)))
# print("\n".join(results))

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        if n == 1:
            print(1)
            continue
        
        min_val = min(a)
        max_val = max(a)
        
        first_min = a.index(min_val)
        last_max = len(a) - 1 - a[::-1].index(max_val)
        
        if first_min > last_max:
            print(1)
            continue
        
        count = 0
        for num in a[first_min:last_max + 1]:
            if num > min_val and num < max_val:
                count += 1
        
        print(count + 2)

if __name__ == "__main__":
    main()