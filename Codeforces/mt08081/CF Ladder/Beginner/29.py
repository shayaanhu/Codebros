from itertools import permutations
import math

# Precomputation
MOD = 10**9 + 7
fact = [1] * (200001)
fact[0] = 1
for i in range(2, 100001):
    fact[i] = (fact[i-1] * (i-1)) % MOD

# print(fact)

for _ in range(int(input())):
    n = int(input())
    # x = math.perm(n*2, n)
    # x = pow(x, 1, MOD)
    # print(x)
    print(fact[2*n])
