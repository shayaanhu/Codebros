t = int(input())
final = []

for _ in range(t):
    temp = list(map(int, input().split()))
    n, h = temp[0], temp[1]

    attacks = list(map(int, input().split()))

    low, high = 0, 1e18
    while low <= high:
        mid = (low + high) // 2
        total_damage = 0

        for i in range(len(attacks) - 1):
            total_damage += min(mid, attacks[i + 1] - attacks[i])
        total_damage += mid # last attack
        
        if total_damage >= h:
            high = mid - 1
        elif total_damage < h:
            low = mid + 1

    final.append(int(low))

for i in final:
    print(i)