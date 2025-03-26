for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    h = 1
    prev = a[0]
    if prev == 1:
        h += 1
    for i in range(1, n):
        if a[i] == 1 and prev == 1:
            h += 5
        elif a[i] == 1:
            h += 1
        if prev == 0 and a[i] == 0:
            h = -1
            break
        prev = a[i]
    print(h)

