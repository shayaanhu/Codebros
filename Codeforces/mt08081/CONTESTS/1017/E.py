# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))


#     # This might cause problems...
#     # b = set(a)

#     # if len(b) != n:
#     #     print(0)
#     #     continue

#     # a.sort()

#     # # Lets try binary search
#     # l, r = 0, n-1

#     # max_sum = 0
#     # while l < r:
#     #     # print(l, r)
#     #     # print(a[l], a[r])
#     #     current_sum = 0
#     #     ak = a[l]
#     #     for i in range(n):
#     #         current_sum += (ak ^ a[i])
        
#     #     max_sum = max(max_sum, current_sum)
#     #     l += 1
#     #     r -= 1
#     # print(max_sum)

#     a.sort(reverse=True)
#     ak = a[0]
#     max_sum = 0
#     for j in range(2001):
#         current_sum = 0
#         if j < n:
#             ak = a[j]
#         for i in range(n):
#             current_sum += (ak ^ a[i])
#         max_sum = max(max_sum, current_sum)
        
#     print(max_sum)

#     # max_sum = 0
#     # for k in range(n):
#     #     ak = a[k]
#     #     # print(ak)
#     #     current_sum = 0

#     #     for i in range(n):
#     #         current_sum += (ak ^ a[i])
        
#     #     max_sum = max(max_sum, current_sum)
#     #     # print(max_sum)

#     # print(max_sum)


#     # Nothing else works so we can try going over all the bits one by one
#     # There are only 30 bits 
#     # and we can check if the bit is set or not

#     # max_sum = 0
#     # for bit in range(30):
#     #     count_ones = sum(1 for i in a if (i & (1 << bit)))
#     #     count_zeros = n - count_ones

#     #     bits = max(count_ones, count_zeros) * (1 << bit)

#     #     max_sum += bits

#     #     # print(max_sum)

#     # print(max_sum)

# Had to take hints online

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Count set bits at all the positions
    bit_counts = [0] * 30
    for num in a:
        for bit in range(30):
            if num & (1 << bit):
                bit_counts[bit] += 1
    
    # Try each array element as ak
    max_sum = 0
    for ak in a:
        sum_with_ak = 0
        for bit in range(30):
            bit_value = 1 << bit
            if ak & bit_value:  # 1 bit
                # XOR with elements having bit=0 contributes 1
                sum_with_ak += (n - bit_counts[bit]) * bit_value
            else:  # 0 bit
                # XOR with elements having bit=1 contributes 1
                sum_with_ak += bit_counts[bit] * bit_value
        
        max_sum = max(max_sum, sum_with_ak)
    
    print(max_sum)