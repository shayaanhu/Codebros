from collections import Counter

for i in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    aList.sort()
    cList = []
    # count = {}
    # for num in aList:
    #     if num in count:
    #         count[num] += 1
    #     else:
    #         count[num] = 1
    # cList = [key for key, value in count.items() if value > 1]
    count = Counter(aList)
    cList = [key for key, value in count.items() if value > 1]
    if (not cList):
        print(-1)
        continue
    
    # Make permutations of 4 numbers of the list
    # Isosceles Trapezoid has to be formed by 4 distinct points from the list
    # Longer base (b) has to be less than shorter base(a) + 2*side(c)
    # Shorter base must be greater than b - 2*c
    # c must be greater than (a - b)/2

    # a, b, c, d = 0, 1, 2, 3
    # cList is the list of all the possible values of c (sides)

    # find index_c1 and index_c2 from the aList
    # index_c1 = aList.index(cList[0])
    # index_c2 = aList.index(cList[1])


    # Make a dictionary to store the indices of the 2 occurences of all c's
    cDict = {}
    for c in cList:
        cDict[c] = [aList.index(c), aList.index(c, aList.index(c)+1)]
        # aList.remove(c)
        # aList.remove(c)
        # n -= 2
    
    check2 = False
    for a in range(n-1):
        for b in range(a+1, n):
            for c in cList:
                index_c1, index_c2 = cDict[c]
                if (index_c1 in (a, b) or index_c2 in (a, b)):
                    continue
                if (aList[b] < aList[a] + 2*c and aList[a] > aList[b] - 2*c and c > (aList[b] - aList[a])//2):
                    check2 = True
                    print(f"{aList[b]} {aList[a]} {c} {c}")
                    break
            if (check2):
                break
        if (check2):
            break
    if (not check2):
        print(-1)
    
        