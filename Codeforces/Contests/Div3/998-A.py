t = int(input())
final = []

for _ in range(t):
    nums = list(map(int, input().split()))
    a1, a2, a4, a5 = nums[0], nums[1], nums[2], nums[3]

    a3 = [a1 + a2, a4 - a2, a5 - a4]
    count = 0

    for i in a3:
        intermediate_count = 0
        if a1 + a2 == i:
            intermediate_count += 1
        if a2 + i == a4:
            intermediate_count += 1
        if i + a4 == a5:
            intermediate_count += 1
        
        if intermediate_count > count:
            count = intermediate_count

    final.append(count)


for i in final:
    print(i)
