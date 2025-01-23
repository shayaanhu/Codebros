t = int(input())
final = []

for _ in range(t):
    temp = list(map(int, input().split()))
    n, c = temp[0], temp[1]
    paintings = list(map(int, input().split()))

    low, high = 0, int(1e10)
    while low <= high:
        mid = (low + high) // 2
        sum = 0

        for p in paintings:
            sum += (2 * mid + p) ** 2
            
        if sum == c:
            break
        elif sum < c:
            low = mid + 1
        elif sum > c:
            high = mid - 1

    final.append(int(mid))

for i in final:
    print(i)