for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Kill all the monsters with b = 0 first
    # total_time = 0
    # i = 0
    # maxB = max(b)
    # while i < n:
    #     if b[i] == 0:
    #         total_time += a[i]
    #     else:
    #         total_time += a[i]
    #         j = i + 1
    #         while j < n and b[j] == 0:
    #             j += 1
    #         if j < n:
    #             a[j] += b[i]
    #     i += 1

    #     # print(total_time, i, a, b)


    total_time = sum(a) + sum(b) - max(b)
    print(total_time)

    # print(total_time - maxB + b[-1])