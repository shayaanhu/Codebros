for _ in range(int(input())):
    n = input()
    # if n < 10:
    #     print(0)
    #     continue

    # go from the right of n to left
    nonZero = False
    counti = 0
    for i in range(len(n) - 1, -1, -1):
        if n[i] == '0' and not nonZero:
            counti += 1
            continue
        else:
            nonZero = True
        
        if n[i] != '0':
            counti += 1

    print(counti-1)

