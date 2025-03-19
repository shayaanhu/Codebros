for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    # if l[0] != l[1] and l[1] != l[2]:
    #     print("NO")
    #     continue

    val = l[2] if l[1] != l[2] else l[0]
    check = False
    if l[0] == val and val == l[1] + l[2]:
        check = True
    elif l[2] == val and val == l[0] + l[1]:
        check = True
    # print(val)
    elif l[0] == val and val % 2 == 0 and l[1] == l[2]:
        check = True
    elif l[2] == val and val % 2 == 0 and l[0] == l[1]:
        check = True

    if check:
        print("YES")
    else:
        print("NO")

    # if l[0] + l[1] == l[2]:
    #     # largest stick can be broken into the sum of the other two
    #     print("YES")
    # elif l[0] == l[1] and l[2] % 2 == 0:
    #     # two smaller sticks are equal, the largest is even
    #     print("YES")
    # elif l[1] == l[2] and l[0] % 2 == 0:
    #     # two larger sticks are equal, the smallest is even
    #     print("YES")
    # else:
    #     print("NO")

    # l = list(set(l))
    # if len(l) == 3:
    #     print("NO")
    #     continue

    
