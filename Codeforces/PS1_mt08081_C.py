
t = int(input())

for _ in range(t):
    n = int(input())
    aList = list(map(int, input().split()))

    valleys = 0
    r, l = 0, 0

    '''
    0 <= l <= r <= n - 1
    a_l = a_l+1 = ... = a_r-1 = a_r
    l = 0 or a_l-1 > a_l
    r = n-1 or a_r < a_r+1
    Only one valley
    '''

    while (r < n):
        # print("L:", l, "R:", r)
        while(r < n - 1 and aList[r] == aList[r + 1]): # find the whole singular valley
            r += 1
        if (l == 0 or aList[l - 1] > aList[l]) and (r == n - 1 or aList[r + 1] > aList[r]): # Check if its a valley
            valleys += 1
        l = r + 1 # move to the next index in front of the valley
        r += 1
    
    # print("Valleys:", valleys)

    if valleys == 1:
        print("YES")
    else:
        print("NO")
