for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[2] == a[1] + a[0]:
        print(a[0], a[1], a[3])
    else:
        print(a[0], a[1], a[2])