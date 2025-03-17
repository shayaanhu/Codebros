for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    check = False
    while not check:
        if a[0] + a[-1] < n:
            a.pop()
        else:
            check = True
    print(a)

    