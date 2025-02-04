for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    # prefix_sub = [0] * (n-1)
    # # prefix_sub[0] = a[0]
    # for i in range(1, n):
    #     prefix_sub[i-1] = a[i] - a[i-1]
    # print(prefix_sub)
    # count = 0
    # for i in range(k):
    #     if (a[0]+a[1] > a[-1] and prefix_sub[0] > prefix_sub[-1]):
    #         a = a[2:]
    #         prefix_sub = prefix_sub[2:]
    #     elif (a[0]+a[1] > a[-1] and prefix_sub[0] < prefix_sub[-1]):    
    #         a.pop()
    #         prefix_sub.pop()
    #         # count += 1
    #     elif (a[0]+a[1] < a[-1] and prefix_sub[0] > prefix_sub[-1]):
    #         a = a[2:]
    #         prefix_sub = prefix_sub[2:]
    #         # count += 1
    #     else:
    #         a.pop()
    #         prefix_sub.pop()
            # count += 1
        # print(a)
        # print(prefix_sub)

    # print(a)

    prefix_sum = [0] * (n+1)
    prefix_sum[1] = a[0]
    for i in range(2, n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]

    # print(prefix_sum)
    i, j = 0, n-k
    mini = -float('inf')
    while j <= n:
        # totalSum = sum(a[:i]) + sum(a[j:])
        # totalSum = sum(a[i:j])
        totalSum = prefix_sum[j] - prefix_sum[i]
        # print(totalSum)
        mini = max(mini, totalSum)
        i += 2
        j += 1
    print(mini)
    # print(sum(a))