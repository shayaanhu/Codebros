for i in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    # n is the number of attacks
    # h is the health of the monster
    # a is the list of attacks
    # a_i is the i-th second the player attacks the monster
    # The player is trying to kill the monster
    # The player uses a poisoned weapon
    # The poison does 1 damage each second for k seconds
    # Find the smallest value of k such that the monster dies
    # The monster dies if the sum of the attacks is greater than or equal to h

    # k should be at least the largest difference between consecutive numbers in the list of attacks

    # k <= max(a_i - a_i-1) for i in range(1, n)

    # k = max([a[i] - a[i-1] for i in range(1, n)])
    # print(k)
    
    # Deal with the case of a single attack
    if n == 1:
        print(h)
        continue

    # prefix_sub = [0] * n
    # prefix_sub[0] = a[0]
    # for i in range(1, n):
    #     prefix_sub[i] = a[i] - a[i-1]
    # prefix_sub.pop(0)

    prefix_sub = [a[i] - a[i-1] for i in range(1, n)]

    # print(prefix_sub)

    # the calculated k is the roof of the minimum value of k
    # We can apply binary search to find the minimum value of k

    low, high = 1, h
    while low < high:
        mid = (low + high) // 2
        total_damage = 0
        for i in prefix_sub:
            total_damage += min(mid, i)
        total_damage += mid
        if total_damage >= h:
            high = mid
        else:
            low = mid + 1
    print(low)