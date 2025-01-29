for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    check = False
    fiora = [a[0]]
    for i in range(1, n-1):
        # print(a[i] - 1, a[i] + 1)
        if (a[i] - 1 not in fiora and a[i] + 1 not in fiora):
            check = True
            break
        if a[i] not in fiora:
            fiora.append(a[i])
    if check:
        print("NO")
    else:
        print("YES")