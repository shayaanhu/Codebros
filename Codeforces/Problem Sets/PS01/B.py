t = int(input())

final = []
for i in range(t):
    temp = list(map(int, input().split()))
    a1, a2, b1, b2 = temp[0], temp[1], temp[2], temp[3]

    # # case 1, suneet picks 1st and slavic picks 1st
    # count_case1 = 0
    # if a1 > b1:
    #     count_case1 += 1
    # if a2 > b2:
    #     count_case1 += 1

    # # case 2, suneet picks 1st and slavic picks 2nd
    # count_case2 = 0
    # if a1 > b2:
    #     count_case2 += 1
    # if a2 > b1:
    #     count_case2 +=1

    # # case 3, suneet picks 2nd and slavic picks 1st
    # count_case3 = 0
    # if a2 > b1:
    #     count_case3 += 1
    # if a1 > b2:
    #     count_case3 += 1

    # # case 4, suneet picks 2nd and slavic picks 2nd
    # count_case4 = 0
    # if a2 > b2:
    #     count_case4 += 1
    # if a1 > b1:
    #     count_case4 += 1

    # final_count = sum(1 for count in [count_case1, count_case2, count_case3, count_case4] if count == 2)
    # final.append(final_count)

    final_count = 0
    if (a1 >= b1 and a2 > b2) or (a1 > b1 and a2 >= b2):
        final_count += 2
    if (a1 >= b2 and a2 > b1) or (a1 > b2 and a2 >= b1):
        final_count += 2

    final.append(final_count)

for i in final:
    print(i)


