for _ in range(int(input())):
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # summc = sum(c)
    # summa = sum(a)

    # if summc == summa:
    #     print("YES")
    # else:
    #     print("NO")

    for i in range(len(c)):
        c[i] = c[i] - a[i]

    # print(a, c)

    neg_check = False
    for i in c:
        if i < 0:
            # print("NO")
            # break
            neg_check = True

    if neg_check:
        print("NO")
        continue

    # summc = sum(c)
    # summa = sum(a)
    # First is paper
    # Second is plastic
    # Third is general

    # a1 is paper (c1)
    # a2 is plastic (c2)
    # a3 is general (c3)
    # a4 is partial paper (c1, c3)
    # a5 is partial plastic (c2, c3)

    # # More paper
    # if a[3] >= c[0]:
    #     a[3] -= c[0]
    #     c[0] = 0
    #     if a[3] > c[2]:
    #         neg_check = True
    #     else:
    #         c[2] -= a[3]
    #         a[3] = 0

    # # More plastic
    # if a[4] >= c[1]:
    #     a[4] -= c[1]
    #     c[1] = 0
    #     if a[4] > c[2]:
    #         neg_check = True
    #     else:
    #         c[2] -= a[4]
    #         a[4] = 0

    # # More general
    # if a[2] >= c[2]:
    #     a[2] -= c[2]
    #     c[2] = 0
    #     if a[2] > c[0]:
    #         neg_check = True
    #     else:
    #         c[0] -= a[2]
    #         a[2] = 0

    c3_from_a4 = max(0, a[3] - c[0])
    c3_from_a5 = max(0, a[4] - c[1])

    if c3_from_a4 + c3_from_a5 > c[2]:
        neg_check = True

    if neg_check:
        print("NO")
    else:
        print("YES")



