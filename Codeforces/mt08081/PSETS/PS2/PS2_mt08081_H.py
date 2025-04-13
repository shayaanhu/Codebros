# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     if n <= 3:
#         print(-1)
#         continue
#     l, r = 0, 1
#     while l < n:
#         # print(arr[l:r+1])
#         subarr = arr[l:r+1]
#         maxi = max(subarr)
#         mini = min(subarr)
#         if (r < n) and (maxi == arr[r] or mini == arr[r]):
#             r += 1
#         elif maxi == arr[l] or mini == arr[l]:
#             l += 1
#             if l == r:
#                 r += 1
#         else:
#             print(l+1, r+1)
#             break
#     else:
#         print(-1)
#     # if r < n:
#     #     print(l+1, r+1)
#     # else:
#     #     print(-1)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    l, r = 0, n - 1
    
    # arr2 = arr[l:r+1]
    min_val, max_val = min(arr), max(arr)
    while l < r:
        
        if arr[l] == min_val:
            l += 1
            min_val += 1
        elif arr[l] == max_val:
            l += 1
            max_val -= 1
        elif arr[r] == min_val:
            r -= 1
            min_val += 1
        elif arr[r] == max_val:
            r -= 1
            max_val -= 1
        else:
            print(f"{l+1} {r+1}")
            break
    else:
        print("-1")