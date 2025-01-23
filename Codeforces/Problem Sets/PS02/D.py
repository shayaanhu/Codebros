t = int(input())
final = []

for _ in range(t):
    temp = list(map(int, input().split()))
    n, k = temp[0], temp[1]

    array = list(range(k, k + n))
    final.append(array)

for i in final:
    print(i)