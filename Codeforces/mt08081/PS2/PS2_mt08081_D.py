for _ in range(int(input())):
    n, k = map(int, input().split())

    # a = [0]*n
    # a[0] = k
    # for i in range(1, n):
    #     a[i] = a[i-1] + 1
    # print(*a)
    low = k
    high = k + n - 1
    total = (high+1)*(high)//2 - (low)*(low-1)//2
    # mid = (low + high) // 2
    # lowerTotal = (mid+1)*(mid)/2 - (low)*(low-1)/2
    # upperTotal = (high+1)*(high)/2 - (mid+1)*(mid)/2
    # mini = abs(lowerTotal - upperTotal)
    mini = float('inf')
    while low <= high:
        mid = (low + high) // 2
        # Add all values from k to mid
        # Subtract all values from mid+1 to high
        # Find the minimum value of the sum of the values

        # sum of the first n integers = n(n+1)/2
        # sum of integers from low to mid = (mid-low+1)(mid+low)/2

        lowerTotal = (mid+1)*(mid)//2 - (k)*(k-1)//2
        # upperTotal = (k+n)*(k+n-1)/2 - (mid+1)*(mid)/2
        upperTotal = total - lowerTotal

        finalTotal = abs(lowerTotal - upperTotal)
        mini = min(finalTotal, mini)

        if lowerTotal == upperTotal:
            break
        elif lowerTotal < upperTotal:
            low = mid + 1
        else:
            high = mid - 1
    print(int(mini))