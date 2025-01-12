t = int(input())

final = []
for i in range(t):
    temp = list(map(int, input().split()))
    n = temp[0]
    k = temp[1]

    a = list(map(int, input().split()))

    gold = 0
    count = 0
    for i in a:
        if i == 0 and gold > 0:
            gold -= 1
            count += 1
        elif i >= k:
            gold += i
            i = 0
    final.append(count)

for i in final:
    print(i)
    
