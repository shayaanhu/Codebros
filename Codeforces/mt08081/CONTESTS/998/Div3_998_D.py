t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # a is a list of numbers
    # Sort the list by using subtract min sort technique
    # index = 1 to n
    # a[i] and a[i+1] both are subtracted by min(a[i], a[i+1])
    # if the list gets sorted using this technique, then print YES else NO
    # print the sorted list

    # Sort the list by using subtract min sort technique
    
    # for j in range(2):
    for i in range(1, n):
        mini = min(a[i], a[i - 1])
        # if mini == 0:
        #     break
        a[i] -= mini
        a[i - 1] -= mini

    check = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            # print("NO")
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")

        # while a[i] > a[i + 1]:
        #     mini = min(a[i], a[i - 1])
        #     if mini == 0:
        #         break
        #     a[i] -= mini
        #     a[i - 1] -= mini
        # if (a[i] == 1):
        #     a[i] = 0
        #     a[i + 1] -= 1

            # print(a[i], a[i - 1])
        # if a[i] > a[i + 1]:
        #     while a[i] > a[i + 1]:
        #         mini2 = min(a[i], a[i - 1])
        #         if mini2 == 0:
        #             break
        #         a[i] -= mini2
        #         a[i - 1] -= mini2
        #         # print(a[i], a[i - 1])

    # print(*a)
