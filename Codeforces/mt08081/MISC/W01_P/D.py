n, k = map(int, input().split())
a = list(map(int, input().split()))
b = a.copy()
b.sort(reverse=True)
# maxes = []
indices = []
# for i in range(k):
#     maxi = max(b)
#     maxes.append(maxi)
#     indices.append(a.index(maxi)+1)
#     b.remove(maxi)

# print(b)

print(sum(b[:k]))
# print(indices)

# count = 0
temp = b[:k]
for i, val in enumerate(a):
    if val in temp:
        indices.append(i)
        temp.remove(val)
        if len(temp) == k:
            break
        # count += 1

# 5 4 2 6 5 1 9 2
# 5 stored at 0th index (take 1 values from a (5))
# 6 stored at 3rd index (take 3 values from a (4,2,6))
# 9 stored at 6th index (take 4 values from a (5,1,9,2))
# 5 + 6 + 9 = 20

indices.sort()
# print(indices)
# if len(indices) == 1:
#     print(n)
#     exit()

# print(indices[0]+1, end=" ")

# if len(indices) > 2:
#     for i in range(1, k-1):
#         print(indices[i] - indices[i-1], end=" ")

# print(n - indices[k-2]-1)

prev = -1
for i in range(k-1):
    print(indices[i] - prev, end=" ")
    prev = indices[i]
print(n - prev-1)

# print(n)

# indices.sort()
# count = 0
# for i in indices:
#     print(i-count+1, end=" ")
#     count += i+1

# cases = -(-n // k)
# print cases k-1 times and then print cases - n%k

# for i in range(k-1):
#     print(cases, end=" ")
# if cases == n:
#     print(cases)
# else:
#     print(cases - (k - cases))

# for i in range(k-1):
#     print(1, end=" ")
# print(n - (k-1))

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# # Compute the maximum profit: sum of the k largest elements.
# # (Make a copy and sort descending)
# b = sorted(a, reverse=True)
# total_profit = sum(b[:k])
# print(total_profit)

# # Let x be the k-th largest value (smallest among the selected ones)
# x = b[k-1]

# # Select the first k indices (1-indexed) where a[i] is >= x.
# indices = []
# count = 0
# for i, val in enumerate(a):
#     if val >= x and count < k:
#         indices.append(i + 1)
#         count += 1

# # Sort the indices (they will be in increasing order)
# indices.sort()

# # Compute partition sizes:
# # For the first day, the segment covers from 1 to indices[0]
# # For subsequent days, it covers from (previous index + 1) to the current index.
# res = []
# prev = 0
# for pos in indices[:-1]:
#     res.append(pos - prev)
#     prev = pos
# # The last segment goes from the last boundary to n.
# res.append(n - prev)

# print(" ".join(map(str, res)))

# Copilot solution
def solve():
    import sys

    data = sys.stdin.read().strip().split()
    n, k = map(int, data[:2])
    a = list(map(int, data[2:]))

    # Edge case: if k == 1, everything must be in one segment
    if k == 1:
        print(max(a))
        print(n)
        return

    # Pair each difficulty with its index
    arr = [(val, idx) for idx, val in enumerate(a)]
    # Sort by difficulty descending
    arr.sort(key=lambda x: x[0], reverse=True)

    # Take the top k values
    best_k = arr[:k]
    # Sum of those k values is the maximum total profit
    total_profit = sum(x[0] for x in best_k)

    # Sort by original indices to figure out segment boundaries
    indices = [x[1] for x in best_k]
    indices.sort()

    # Print the total profit
    print(total_profit)

    # Calculate and print the segment sizes
    # First segment is from 0..indices[0]
    sizes = []
    prev = -1
    for i in range(k - 1):
        sizes.append(indices[i] - prev)
        prev = indices[i]
    # Last segment goes to the end
    sizes.append(n - prev - 1)

    print(" ".join(map(str, sizes)))

# solve()