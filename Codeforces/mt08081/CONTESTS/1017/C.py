for _ in range(int(input())):
    n = int(input())
    G = [list(map(int, input().split())) for _ in range(n)]
    # print(G)

    perm = []
    seen = set()

    for i in range(n):
        for j in range(n):
            if G[i][j] not in seen:
                perm.append(G[i][j])
                seen.add(G[i][j])

    # perm.sort()
    for extra in range(1, 2*n+1):
        if extra not in seen:
            perm.insert(0, extra)
            seen.add(extra)

    print(*perm)