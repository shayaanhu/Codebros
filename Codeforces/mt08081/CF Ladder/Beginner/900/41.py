# a + b + c = n
# n is given
# c = gcd(a,b)

# import sympy

# for _ in range(int(input())):
#     n = int(input())
#     ans = float('inf')
#     for c in range(1, n//2):
#         for a in range(1, n - c + 1):
#             b = n - a - c
#             if b < 1:
#                 continue
#             if c == sympy.gcd(a, b):
#                 ans = min(ans, a * b // c)
#     print(ans)

# The above doesn't work in due time as it has a time complexity of O(n^2)

# Using the hint from codeforces tutorial
# c = 1 is always there under the constraints
# This makes the problem easier as we can fix c = 1 and find a and b

# a and b would simply be n // 2 and n // 2 - 1 as this gives c = 1
# gcd(n // 2, n // 2 - 1) = 1
for _ in range(int(input())):
    n = int(input())
    a = n // 2
    b = n - a - 1 if n % 2 == 0 else n - a - 2
    print(a, b, 1)