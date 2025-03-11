for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    summ = sum(a)
    x = summ - (n-1)
    print(x)