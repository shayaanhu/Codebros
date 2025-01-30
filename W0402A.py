import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip('W')
    # print(s)
    # j = k
    newN = len(s)
    # x = math.ceil(newN / k)
    # print(x)
    
    i = 0
    x = 0
    while i < newN:
        if s[i] == 'B':
            x += 1
            i += k
        else:
            i += 1
    print(x)
