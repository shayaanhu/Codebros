N = int(input())

P = list(map(int, input().split()))

# Q = sorted(P, reverse=True)

# ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if P[i] < P[j]:
            rank += 1
    print(rank)