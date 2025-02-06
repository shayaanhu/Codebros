# # # # # 1A
# # # # # Counting set bits
# b = bin(int(input()))
# print(b)
# print(b.count('1'))

# # # # # 1B
# # # # Toggle the kth bit (zero-based) of a given number n
# n, k = map(int, input().split())
# print(n ^ (1 << (k - 1)))

# # # # # 1C
# # # # # Check Power of 2
# n = int(input())
# print(n & (n - 1) == 0)

# # # 1D
# # # Unique Number Finder: Given a list of numbers where every number occurs twice except one number, find that unique number
# n = int(input())
# a = list(map(int, input().split()))
# res = 0
# for i in a:
#     res ^= i
# print(res)

# # 1E 
# # Unset kth bit of a number
# n, k = map(int, input().split())
# print(n & ~(1 << (k-1)))

# 2
# Write a function to encode or decode information using bitwise operations
# def encode(data, key):
#     if isinstance(data, str):
#         return ''.join([chr(ord(c) ^ key) for c in data])
#     return data ^ key
# def decode(data, key):
#     if isinstance(data, str):
#         return ''.join([chr(ord(c) ^ key) for c in data])
#     return data ^ key


# k = encode(7, 8)
# print(k)
# print(decode(k, 8))
# print(encode('Hello', 8))
# print(decode(encode('Hello', 8), 8))

# # 3A
# def has_even_parity(n) :
#     count = 0
#     while n:
#         count += n & 1
#         n = n >> 1
#     return count % 2 == 0

# # 3B
# def clear_3rd_bit(n):
#     # 15 = 1111
#     # 11 = 1011
#     # n & ~(1 << (k-1)) will clear the kth bit
#     return n & ~(1 << 2)


# # 3C
# def multiply_by_4(n):
#     return n << 2

# # print(clear_3rd_bit(15))

# # 4
# # Subset Generation using bitwise operations
# def generate_subsets(a):
#     n = len(a)
#     vec = []
#     for i in range(1 << n):
#         new = []
#         for j in range(n):
#             if i & (1 << j):
#                 # print(a[j], end=' ')
#                 new.append(a[j])
#         vec.append(new)
#         # print()
#     return vec

# # v = sorted(generate_subsets([1, 2, 3]))

# # print(v)