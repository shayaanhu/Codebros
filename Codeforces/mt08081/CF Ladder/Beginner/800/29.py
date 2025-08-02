from itertools import permutations
import math

# Precomputation
MOD = 10**9 + 7
MAX = 2*10**5 + 5
fact = [1] * (MAX)
# fact[0] = 1
for i in range(1, MAX):
    fact[i] = fact[i-1] * i % MOD

# print(fact)
inv2 = (MOD + 1) // 2  # Modular inverse of 2 under MOD (I dont understand this...)

for _ in range(int(input())):
    n = int(input())
    # x = math.perm(n*2, n)
    # x = pow(x, 1, MOD)
    # print(x)
    print(fact[2*n] * inv2 % MOD)
    # print(n*(math.comb(n*2, n)) % MOD)
