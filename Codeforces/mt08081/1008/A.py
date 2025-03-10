for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    summ = sum(a)
    avg = summ/n

    if avg == x:
        print("YES")
    else:
        print("NO")