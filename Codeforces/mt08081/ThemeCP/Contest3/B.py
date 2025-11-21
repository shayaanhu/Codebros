for _ in range(int(input())):
    n = int(input())

    x = 2
    sums = {}
    while x <= n:
        temp = 0
        k = 1
        while k * x <= n:
            temp += k * x
            k += 1
        sums[temp] = x
        x += 1
    print(sums[max(sums.keys())])
    # print(sums)