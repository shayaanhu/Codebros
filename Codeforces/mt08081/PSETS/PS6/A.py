# n = int(input())

# # We have to construct the num n by throwing a dice one or more times
# # We have to output the permutations of the ways n can be formed

# # Lets try to emulate dp
# # Maybe we can store something...
# # Since this is the first question, it should be easy
# # 1 can only be formed by 1 - 1 way
# # 2 can be formed by 1+1 or 2 - 2 ways
# # 3 can be formed by 1+1+1 or 1+2 or 2+1 or 3 - 4 ways
# # 4 can be formed by 1(4) or 3+1 or 2+2 or 2+1+1 or 1+2+1 or 1+1+2 or 1+3 or 4 - 8 ways
# # From this pattern, may be its just the power of 2

# print(2**(n-1))

# This works from 1 to 6, but not for 7
# 7 can be formed in 63 ways instead of 64 ways
# 8 can be formed in 125 ways instead of 128 ways and so on...
# Maybe we can try dividing this problem into two parts...
# One can be for n < 7 and the other for n >= 7
# The former can be solved by 2**(n-1)
# The latter can be solved by 2**(n-1) - k
# But what is k?
# 9 can be formed in 248 ways instead of 256 ways
# 10 can be formed in 492 ways instead of 512 ways
# 7 => 2**(7-1) - 1 (4 - 3)
# 8 => 2**(8-1) - 3 (8 - 5)
# 9 => 2**(9-1) - 8 (16 - 8)
# 10 => 2**(10-1) - 20 (32 - 12)
# Maybe there is no straightforward closed solution to this problem

# Lets say we put 1 at index 0
# Then we can put 1 at index 1
# Then we can add idx 0 and 1 to get 2 which can stored at idx 2
# Then add all previous indices to get 3 which can be stored at idx 3
# Then add all previous indices to get 4 which can be stored at idx 4
# And so on...

# We have to add previous 6 numbers only

mod = 10**9 + 7
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
# summ = 0

for i in range(1, n + 1):
    for dice in range(1, 7):
        if i - dice >= 0:
            dp[i] = (dp[i] + dp[i - dice]) % mod

# print(summ)
print(dp[n])