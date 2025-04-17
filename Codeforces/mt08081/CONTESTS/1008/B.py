for _ in range(int(input())):
    n, k = map(int, input().split())

    # 1 2 3
    # teleporter 1: 2 -> 1
    # teleporter 2: 3 -> 2
    # teleporter 3: 1 -> 3

    if n == 2:
        print(2, 1)
        continue
    
    # put the value of n in n-1 positions
    # put the value of n-1 in the nth position

    # print(n-1, end=" ")
    # # Print alternating values on n and n-1 until n
    # for i in range(1, n):
    #     if i % 2 == 0:
    #         print(n-1, end=" ")
    #     else:
    #         print(n, end=" ")
    # print("")

    if k % 2 == 0:
        mapping = [n-1] * (n-2) + [n] + [n-1]
    else:
        mapping = [n] * (n-2) + [n] + [n-1]

    print(*mapping)
    
    