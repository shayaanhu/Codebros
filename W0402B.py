import math
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    i = 0

    x = 0
    for i in range(0, n, m):
        if (i+m+1 < n and s[i+m+1] == '0'):
            x += 1
            i += m+k-1
        x += s.count('0'*m, i, i+m)
    # x = s.count('0'*m)
    print(x)
    print(math.floor(x/k))
    # while i < n:
    # x = 0
    # while i < n:
    #     if s[i:i + 2*m+1] == '0' * (2*m):
    #         x += 1
    #         i += m+k-1
        
    #     elif s[i:i+m] == '0'*m:
    #         x += 1
    #         i += m
    #     else:
    #         i += 1
    # print(x)