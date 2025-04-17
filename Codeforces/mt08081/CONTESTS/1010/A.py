for _ in range(int(input())):
    n, m = map(int, input().split())
    # Form the binary matrix of size n x m
    # Input in each line

    complete = []
    for i in range(n):
        a = list(map(int, input().split()))
        # xor all the values in a
        complete.append(a)

    total = 0
    for i in complete:
        val = 0
        for num in i:
            val ^= num
        total += val

    print(total)


    # Idk how to do these questions :( 
    # I am kinda done for the day
    # Did the atcoder thing

