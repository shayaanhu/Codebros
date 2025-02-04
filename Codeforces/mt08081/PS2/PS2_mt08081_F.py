for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(input())
    # print(arr)
    if (n == k):
        count = arr.count('W')
        print(count)
        continue
    
    # val = arr[:k].count('W')
    # val = float('inf')
    wCount = arr[:k].count('W')
    val = wCount

    low = 0; high = k
    while high < n:
        # wCount = arr[low:high].count('W')
        if arr[low] == 'W':
            wCount -= 1
        if arr[high] == 'W':
            wCount += 1
        val = min(val, wCount)
        low += 1
        high += 1
    print(val)

# import math
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     s = input()
#     # print(s)
#     # j = k
#     # newN = len(s)
#     # x = math.ceil(newN / k)
#     # print(x)
    
#     i, j = 0, 0
#     x = 0
#     while i < n:
#         if s[i] == 'B':
#             x += 1
#             # i += k
#         # else:
#         i += 1
#     print(x)
