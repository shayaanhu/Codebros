import math

n = int(input())
# N = math.log2(n)
# N2 = N - round(N, 0)
# N3 = 2**N2
# print(n, N, N2, N3)

# 5 = 0101
# 5 has 2 days

# 8 = 1000
# 8 has 1 day

# 2 = 0010
# 2 has 1 day

# 3 = 0011
# 3 has 2 days

# 14 = 1110
# 14 has 3 day

mini = bin(n).count('1')
print(mini)