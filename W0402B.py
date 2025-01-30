import math
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    i = 0

    # x = s.count('0'*m)
    # print(round(x/k))
    # y = s.count('0'*(m+1))
    # print(x)
    x = 0
    while i < n-m:
        if s[i:i+m] == '0'*m:
            x += 1
            i += m+k-1
        else:
            i += 1
    print(x)
        # x += s.count('0'*m, i, i+m)
        # i += m+k-1
        # if (i+m+1 < n and s[i+m+1] == '0'):
        #     x -= 1
            # i += m+k-1
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