t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    # print(a)

    # a is a list of numbers.
    # find all the pairs which equal k and pop them out of the list
    # increment the count of pairs as score
    # print the score
    score = 0
    # while a:
    #     if len(a) == 1:
    #         break
    #     if a[0] + a[-1] == k:
    #         score += 1
    #         a.pop(0)
    #         a.pop(-1)
    #     elif a[0] + a[-1] < k:
    #         a.pop(0)
    #     else:
    #         a.pop(-1)

    # Reduced number of list operations/accessing/popping etc.
    l = 0
    r = n - 1
    while l < r:
        if a[l] + a[r] == k:
            score += 1
            l += 1
            r -= 1
        elif a[l] + a[r] < k:
            l += 1
        else:
            r -= 1
    print(score)