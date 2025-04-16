for _ in range(int(input())):
    n, m, l, r = map(int, input().split())

    l2 = min(0, r-m)
    r2 = l2 + m
    print(l2, r2)