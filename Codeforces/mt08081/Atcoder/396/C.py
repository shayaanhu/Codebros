# N, M = map(int, input().split())

# B = list(map(int, input().split()))
# W = list(map(int, input().split()))

# B.sort()
# W.sort()

# # print(B, W)
# # Remove all the negatives from both lists
# B = [x for x in B if x > 0]
# W = [x for x in W if x > 0]

# # If there are no black balls, then the answer is zero
# if len(B) == 0:
#     print(0)
#     exit()

# if len(B) > len(W):
#     S = sum(B) + sum(W)
#     print(S)
#     exit()
# print(B, W)

N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

# Sort descending so the best balls are first.
B.sort(reverse=True)
W.sort(reverse=True)

# Precompute prefix sums for black balls.
prefixB = [0] * (N + 1)
for i in range(1, N + 1):
    prefixB[i] = prefixB[i - 1] + B[i - 1]

# Additional sum: from index i onward, add black balls only if they are positive.
# This is to maximise final answer
additional = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if B[i] > 0:
        additional[i] = additional[i+1] + B[i]
    else:
        additional[i] = additional[i+1]

# Precompute prefix sums for white balls (only add if positive)
prefixW = [0] * (M + 1)
for i in range(1, M + 1):
    if W[i - 1] > 0:
        prefixW[i] = prefixW[i - 1] + W[i - 1]
    else:
        prefixW[i] = prefixW[i - 1]

max_possible_k = min(N, M)
ans = 0

for k in range(max_possible_k + 1):
    # Mandatory takes the k best black balls (even if some are negative)
    # Additional adds any extra black balls (only positive ones) from index k onward
    candidate = prefixB[k] + additional[k] + prefixW[k]
    if candidate > ans:
        ans = candidate

print(ans)