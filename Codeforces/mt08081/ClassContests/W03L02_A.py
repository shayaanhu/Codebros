for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # Sort using the largest at the bottom

    # a contains the number of candies each child has
    # n is the number of candies
    # q is the number of queries
    # print the lowest number of candies that the user has to use to use in order to consume query amount of sugar
    # print -1 if the user does not have enough candies

    prefix_sums = [0] * (n)
    prefix_sums[0] = a[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + a[i]

    # totalCandies = sum(a)
    for __ in range(q):
        x = int(input())
        if x > prefix_sums[-1]:
            print(-1)
            # continue
        else:
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if prefix_sums[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            print(left + 1)


        