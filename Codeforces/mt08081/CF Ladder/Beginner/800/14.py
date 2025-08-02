for _ in range(int(input())):
    a, b = map(int, input().split())
    max_pos = min(a,b)

    # Make sure that a is always less than or equals to b
    # if a > b:
    #     a, b = b, a

    print(min((a+b)//4, a, b))


    # val = (a+b)//max_pos if max_pos != 0 else 0
    # pos = min(val, max_pos)
    # print(pos)