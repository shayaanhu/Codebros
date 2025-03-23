for _ in range(int(input())):
    # a_1, a_2, a_3 = map(int, input().split())
    a, b, c = map(int, input().split())
    # minimize abs(a + c - 2b) by incrementing and decrementing by 1 in an op
    # val = max(a + c, 2*b)

    print(0 if (a+b+c) % 3 == 0 else 1)

    # print(abs(a+c-2*b) % 3)
    # if 2*b >= a+c:
    #     print(0)
    #     continue
    # calc = abs(a+c-2*b) % 3
    # print(calc) if calc != 2 else print(1)
    # print(1)
