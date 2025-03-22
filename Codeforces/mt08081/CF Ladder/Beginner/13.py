for _ in range(int(input())):
    x, y = map(int, input().split())
    d = x + y
    if d % 2 != 0:
        print(-1, -1)
        continue
    d //= 2

    c_x = -(-x // 2)
    c_y = y // 2

    print(c_x, c_y)

