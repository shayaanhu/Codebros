for _ in range(int(input())):
    n, c = map(int, input().split())
    paintings = list(map(int, input().split()))
    pList = [i**2 for i in paintings]
    # Sum the squares of paintings to get the sizes
    pSize = sum(pList)

    # print(pSize)
    # sqrtC = c**0.5
    c -= pSize
    # print(sqrtC)
    val = c/4
    # a*b = w(s_i+w)
    # s_i*s_i is the size of the side of one painting from the paintings list
    # w is the width of the border
    # a and b are the dimensions of the painting with the border
    

    # for i in pList:
