n, k = map(int, input().split())

# Vasya wants to at least write n lines of code
# "The Productivity Reduction Coefficient lol" is k

# Vasya wants to find the smallest v such that floor(v/k^p) >= n
# Where p is the number of cups of coffee
# Vasya drinks one cup after each time he writes a line of code and he writes until
# floor(v/k^p) == 0
# 

# Lets assume that v can be anything from 1 to inf
# Lets start to linearly search for the answer (brute force it)

# v = 1
# while True:
#     p = 0
#     while v // (k ** p) > 0:
#         p += 1
#     if v // (k ** p) >= n:
#         print(v)
#         break
#     v += 1

# Binary search for the answer

l = 1
r = n
while l < r:
    mid = (l + r) // 2
    total_lines = 0
    p = 0
    while mid // (k ** p) > 0:
        total_lines += mid // (k ** p)
        p += 1
    if total_lines >= n:
        r = mid
    else:
        l = mid + 1
print(l)