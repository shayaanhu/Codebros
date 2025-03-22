for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # x = max(a)
    # a.sort()
    # x = max(a)
    # y = min(a)
    # if x == y:
    #     print(0)
    #     continue

    # avg = sum(a) // n
    # # print(avg)
    # xy = int((x+y)/2)
    # # print(xy)
    # print(xy - avg)

    summ = sum(a)
    if summ % n == 0:
        print(0)
    else:
        print(1)