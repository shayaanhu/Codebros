for _ in range(int(input())):
    k, l1, r1, l2, r2 = map(int, input().split())
    ans = 0
    p = 1
    while True:
        # x must be at least ceil(l2 / power) and at most floor(r2 / power), 
        # and also between l1 and r1.
        low2 = (l2 + p - 1) // p
        high2 = r2 // p
        low = max(l1, low2)
        high = min(r1, high2)
        if low <= high:
            ans += (high - low + 1)
        # If multiplying by k would push even the smallest x out of range, we're done.
        if p > r2 // k:
            break
        p *= k
    print(ans)