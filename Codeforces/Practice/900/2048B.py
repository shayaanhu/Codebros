t = int(input())

final = []
for _ in range(t):
    temp = list(map(int, input().split()))
    n, k = temp[0], temp[1]
    permutation = [0] * n

    unused = list(range(1, n + 1))

    j = 1
    for i in range(k - 1, n, k):
        permutation[i] = j
        j += 1

    unused = unused[j - 1:]
    
    j = 0
    for i in range(1, n + 1):
        if permutation[i - 1] == 0:
            permutation[i - 1] = unused[j]
            j += 1

    final.append(permutation)

for i in final:
    for j in i:
        print(j, end=" ")
    print()


