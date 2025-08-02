import bisect

for _ in range(int(input())):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i >= l and i <= r]
    a.sort()
    # print(a)
    # prefix sum of a
    new_n = len(a)
    p_s = [0] * (new_n+1)
    for i in range(new_n):
        p_s[i+1] = p_s[i] + a[i]
    # print(p_s)
    
    # bisect and find the position where the sum is less than or equal to k
    ans = bisect.bisect_right(p_s, k)
    print(ans-1)

    