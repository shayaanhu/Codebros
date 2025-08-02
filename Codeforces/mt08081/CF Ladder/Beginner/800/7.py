for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    # print(a)

    s = a[0]
    inserted = False
    for i in range(len(a)):
        if i == 0:
            continue

        if s[-1] != a[i][0]:
            s += a[i]
            inserted = True
        else:
            s += a[i][1]

    # if len(a) > 1:
    #     s += a[-1]
    # else:
    #     s += "a"

    if not inserted:
        s += "a"

    print(s)