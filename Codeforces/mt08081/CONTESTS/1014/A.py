for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # We can take two sheeps and see what the max gcd would be if we add some d to them
    # I feel like there is some trick here
    # 1 and 3 gives 2
    # 5 4 3 2 1 gives 4
    # 5 6 7 gives 2
    # 1 10 11 gives 10
    # Is it just max - min?

    print(max(a) - min(a))
