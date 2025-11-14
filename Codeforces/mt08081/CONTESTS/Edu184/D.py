# This seems easy... lemme try it...
# lol 11 min left...

for _ in range(int(input())):
    x, y, k = map(int, input().split())

    # if x >= y:
    #     print(-1)
    #     continue

    # Space left in pattern would be y - x
    # space = y - x
    # Now we need to find that k fits in this space essentially

    # What if instead of forward we go backwards...
    # We start from the current given k and move back...

    if y == 1:
        print(-1)
        continue

    for i in range(x):
        jump = (k-1)//(y-1)
        k = k + jump

        if k > 10**12:
            k = -1
            break   

    print(k)