for _ in range(int(input())):
    n, c = map(int, input().split())
    paintings = list(map(int, input().split()))
    pList = [i**2 for i in paintings]
    # Sum the squares of paintings to get the sizes
    pSize = sum(pList)
    pSideSize = sum(paintings)

    # print(pSize)
    # sqrtC = c**0.5
    # c -= pSize
    # print(sqrtC)
    # val = c/4
    # a*b = w(s_i+w)
    # s_i*s_i is the size of the side of one painting from the paintings list
    # w is the width of the border
    # a and b are the dimensions of the painting with the border
    

    # for i in pList:

    # n is the total number of paintings
    # c is the total area of the used cardboard in sq. units
    # paintings is the list of sizes of the paintings
    # pList is the list of the squares of the paintings
    # pSize is the sum of the squares of the paintings
    # w has to be found where w is the width of the border
    # w is considered to be the same for all paintings
    # w+p_i is the side of the painting with the border
    # (w+p_i)^2 is the area of the painting with the border


    rem_area = c - pSize

    # sum((side+2w)^2) <= c
    # sum(side^2 + 4w*side + 4w^2) <= c
    # sum(side^2) + 4w*sum(side) + 4nw^2 <= c
    # sum(side^2) + 4w*sum(side) + 4nw^2 - c <= 0
    # pSize + 4w*sum(paintings) + 4nw^2 - c <= 0
    # pSize + 4w*pSideSize + 4nw^2 - c <= 0
    # 4nw^2 + 4w*pSideSize + pSize - c <= 0
    # 4nw^2 + 4w*pSideSize - rem_area <= 0

    discriminant = 16*pSideSize*pSideSize + 16*rem_area*n

    w = (-4*pSideSize + discriminant**0.5)/(8*n)
    print(round(w))

