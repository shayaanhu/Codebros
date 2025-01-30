for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(input())
    # print(arr)
    if (n == k):
        count = arr.count('W')
        print(count)
        continue
    
    # val = arr[:k].count('W')
    val = float('inf')
    low = 0; high = k
    while high < n:
        wCount = arr[low:high].count('W')
        if (wCount < val):
            val = wCount
        low += 1
        high += 1
    print(val)
