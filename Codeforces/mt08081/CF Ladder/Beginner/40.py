# 1 <-> 2 (n/2 = 1)
# 1 <-> 3 | 2 <-> 4 (n/2 = 2)
# 1 <-> 4 | 2 <-> 5 | 3 <-> 6 (n/2 = 3)
# 1 <-> 5 | 2 <-> 6 | 3 <-> 7 | 4 <-> 8 (n/2 = 4)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    maxi = max(a, b)
    mini = min(a, b)
    # if maxi < mini*2 or (mini == 1 and maxi == 2 and c == 3):
    #     print(-1)
    #     continue


    d = abs(maxi - mini)
    n = 2 * d

    if max(a, b, c) > n:
        print(-1)
        continue
        
    final = c + d

    if final > n:
        final = final - n
    print(final)
    

    # matching exists
    # check if c is in the range of matching
    # We have to identify the layer
    # layer as in the n/2 value
    # val = maxi - mini
    # final = c + val if c <= val else c - val
    # if final > val*2:
    #     print(-1)
    # else:
    #     print(final)