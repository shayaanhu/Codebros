# n = int(input())
# A = list(map(int, input().split()))

# # # Check if all values in A are negative
# # if all(x < 0 for x in A):
# #     print(max(A))
# #     exit()

# # # If A_i is non-negative, then add it to sum and increment operation_count by 1
# # # Else add 2 to operation_count
# # # Operation_count cannot exceed n

# # operation_count = 0
# # summ = 0
# # for i in range(n):
# #     if A[i] >= 0:
# #         summ += A[i]
# #         operation_count += 1
# #     else:
# #         operation_count += 2

# #     if operation_count >= n:
# #         break

# # print(summ)

# # The above solution is incorrect
# # The correct solution is to keep track of the maximum sum using two pointers
# i = 0
# j = 0
# summ = 0
# max_sum = float('-inf')
# while j < n:
#     # print(f"j = {j}, summ = {summ}, max_sum = {max_sum}")
#     if A[j] < 0 and j+1 < n and abs(A[j]) > A[j+1]:
#         j += 2
#         continue
#     summ += A[j]
#     j += 1
#     max_sum = max(max_sum, summ)
#     # print(f"j = {j}, j+1, summ = {summ}, max_sum = {max_sum}")

# # 3 -1 -4 5 -9 2
# # j = 0, j+1, summ = 3, max_sum = 3
# # j = 1, j+2, summ = 3, max_sum = 3
# # j = 3, j+1, summ = 8, max_sum = 8
# # j = 4, j+2, summ = 8, max_sum = 8
# # j = 6, j >= n, summ = 8, max_sum = 8
# print(max_sum)

# n = int(input())
# A = list(map(int, input().split()))

# stack = []
# for x in A:
#     if x < 0 and stack:
#         stack.pop()
#     else:
#         stack.append(x)

# print(sum(stack))

# import sys
# sys.setrecursionlimit(10**7)

n = int(input())
A = list(map(int, input().split()))

# memo = {}

# def dfs(i, stack, s):
#     if i == n:
#         return s
#     key = (i, tuple(stack))
#     if key in memo:
#         return memo[key]
#     ans = dfs(i + 1, stack + [A[i]], s + A[i])
#     if stack:
#         ans = max(ans, dfs(i + 1, stack[:-1], s - stack[-1]))
#     memo[key] = ans
#     return ans

# print(dfs(0, [], 0))

from collections import deque

q = deque()
q.append((0, [], 0))
ans = float('-inf')

while q:
    i, st, s = q.pop()
    if i == n:
        ans = max(ans, s)
        continue

    # Operation 1: append A[i]
    q.append((i + 1, st + [A[i]], s + A[i]))

    # Operation 2: remove the last element if possible
    if st:
        q.append((i + 1, st[:-1], s - st[-1]))

print(ans)