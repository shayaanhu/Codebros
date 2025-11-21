for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print("NO")
        continue
    print("YES")
    k = n // 2
    if n % 2 == 0:
        for i in range(k):
            print(1, end = " ")
            print(-1, end = " ")
        print()
    else:
        for i in range(k):
            print(1 - k, end = " ")
            print(k, end = " ")
        print(1 - k)