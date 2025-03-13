import math
# n, m = map(int, input().split())
# print(math.perm(n, m) % (10**9 + 7))

n = int(input())
counti = 0
for i in range(1, n):
    counti += math.factorial(i)
    
    
print(counti)