for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(0)
        continue

    n = str(n)
    i = 0
    while i < len(n):
        if int(n[i]) % 2 == 0 and i == 0:
            print(1)
            break
        elif int(n[i]) % 2 == 0:
            print(2)
            break
        i += 1
    else:
        print(-1)
