for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # mx = max(a)
    # idx = a.index(mx)
    # calc = mx - idx - 1
    # print(calc if calc > 0 else 0)

    # idx = a.index(mx)
    # for i in range(n-1, 0, -1):
    #     if a[i] > i+1:
    #         idx = a.index(a[i])
    #         print(a[i] - i-1) if idx == i else print(a[i] - idx-1)
    #         break
    # else:
    #     print(a[0]-1)

    pos = 1
    ans = 0
    for x in a:
        # pos = max(pos + 1, x)
        ans = max(ans, x - pos)
        pos += 1
    # print(max(0, pos - n))
    print(ans)

    # 1 3 4