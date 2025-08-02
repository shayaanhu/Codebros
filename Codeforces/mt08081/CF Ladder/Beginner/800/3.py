for _ in range(int(input())):
    n, k = map(int, input().split())

    checkers = -(-n//2)
    if k > checkers:
        print(-1)
        continue

    # matrix = [["."]*n]*n
    # print(matrix)

    # i = 0
    # j = 0
    # while k > 0:
    #     matrix[i][j] = "R"
    #     k -= 1
    #     i += 2
    #     j += 2
    #     print(matrix)

    temp = k
    i = 0
    j = 0
    while k > 0:
        print("."*i + "R" + "."*(n-i-1)) if j % 2 == 0 else print("."*n)
        k -= 1 if j % 2 == 0 else 0
        i += 2 if j % 2 == 0 else 0
        j += 1

    for i in range(n-(2*temp-1)):
        print("."*n)

    # print(matrix)
    # for i in range(n):
    #     print("."*i + "R" + "."*(n-i-1))