
from collections import Counter 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # a.sort()
    a = [-i if i < 0 else i for i in a]
    # print(a)
    c = Counter(a)
    counti = 0
    for i in c:
        # if i == 0:
        #     counti += 1
        #     continue
        if i == 0 or c[i] == 1:
            counti += 1
        else:
            counti += 2

    print(counti)

