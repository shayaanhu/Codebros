for _ in range(int(input())):
    n = int(input())
    
    # Even cases are a problem
    # After a cycle shift you might not have exactly one fixed point
    if n % 2 == 0:
        print(-1)
        continue

    # Now what...?
    # perm = [1]
    # for i in range(2, n+1):
    #     print(i, end=" ")

    # vals = [i for i in range(1, n+1)]

    # We can emulate cycles by using mod
    # I guess we can fix 1 everytime
    # Then we can go through the rest of the elements in some way
    perm = []
    for i in range(n):
        # print(2*i)
        # print((2*i) % n)
        val = (2 * i) % n
        perm.append(val + 1)
        # print(perm)
    print(*perm)