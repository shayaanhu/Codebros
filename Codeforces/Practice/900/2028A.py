for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    x, y, valid = 0, 0, False

    for i in range(20):
        if valid:
            break
        for j in s:
            if j == "N":
                y += 1
            elif j == "S":
                y -= 1
            elif j == "E":
                x += 1
            elif j == "W":
                x -= 1
            if x == a and y == b:
                valid = True
                break
    
    if valid:
        print("YES")
    else:
        print("NO")
