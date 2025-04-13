# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     left, right = 0, n + 1
#     ans = 0
#     while left <= right:
#         mid = (left + right) // 2
#         count = 0
#         current_seg = []
#         i = 0
        
#         freq = {}
        
#         while i < n:
#             current_seg.append(a[i])
#             freq[a[i]] = freq.get(a[i], 0) + 1
#             i += 1
            
#             mex = 0
#             while mex in freq:
#                 mex += 1
                
#             if mex >= mid:
#                 count += 1
#                 current_seg = []
#                 freq = {}
#                 if count == k:
#                     break
    
#         if count == k and i == n:
#             ans = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(ans)


def can_partition(a, x, k):
    if x == 0:
        return True
    count = 0
    missing = x
    freq = [0] * x
    for num in a:
        if num < x:
            if freq[num] == 0:
                missing -= 1
            freq[num] += 1
        if missing == 0:
            count += 1
            missing = x
            freq = [0] * x
            if count >= k:
                return True
    return count >= k

def full_array_mex(a):
    s = set(a)
    mex = 0
    while mex in s:
        mex += 1
    return mex

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    upper_bound = full_array_mex(a)
    lo, hi, ans = 0, upper_bound, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_partition(a, mid, k):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
