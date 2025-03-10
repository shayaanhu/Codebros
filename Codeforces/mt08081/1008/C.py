for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()
    set_b = set(b)

    # if n == 1:
    #     print()

    group1 = b[:n]   # assign to odd indices 
    group2 = b[n:]   # assign to even indices 
    # Interleave group2 and group1.
    a = []
    for i in range(n):
        a.append(group2[i])
        a.append(group1[i])
    # print(" ".join(str(x) for x in a))
    # The missing number is the difference between the sums of the two groups.
    X = sum(group2) - sum(group1)
    # if X in a:
    print(X, *a)
