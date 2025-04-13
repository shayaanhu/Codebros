for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))


    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count5 = 0

    check = False
    turns = 0
    for i in a:
        turns += 1
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
        elif i == 5:
            count5 += 1
        if count0 >= 3 and count1 >= 1 and count2 >= 2 and count3 >= 1 and count5 >= 1:
            check = True
            break

    if turns == n and not check:
        print(0)
    else:
        print(turns)