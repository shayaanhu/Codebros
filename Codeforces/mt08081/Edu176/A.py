for _ in range(int(input())):
    n, k = map(int, input().split())
    # Take k and k-1 and see how many of them combined form n
    # Whatever remains behind has to be manipulated to zero

    # ak + b(k-1) = n
    # ak + bk - b = n
    # the above approach might work
    # but since k is odd we might just check for the parity of n

    if n % 2 == 0:
        steps = n // (k-1) # k is odd
        # Check for remainders xD
        if n % (k-1) != 0:
            steps += 1
        print(steps)

    else:
        steps = 1
        rem = n-k
        steps += rem // (k-1)
        if rem % (k-1) != 0:
            steps += 1
        print(steps)