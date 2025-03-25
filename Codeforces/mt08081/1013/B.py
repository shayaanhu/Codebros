for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    teams = 0
    group_size = 0
    # idx = a.index(x)
    # teams += n - idx
    # for i in range(idx):
    for skill in a:
        group_size += 1
        if skill * group_size >= x:
            teams += 1
            group_size = 0
    print(teams)
