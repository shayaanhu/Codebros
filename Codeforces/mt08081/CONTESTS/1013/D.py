for _ in range(int(input())):
    n, m, k = map(int, input().split())
    # Ignore m lol
    distribute = -(-k // n)
    # Max number of participants in a row is distribute

    # I guess now we use columns to see if we can space out the participants in the max row
    # final_dist = distribute - (-(-distribute // m))
    # print(distribute)
    # print(final_dist)

    # How to minimize them...
    # for i in range(m):
        # Put 1st desk in 1st col, then take a break
        # Put 2nd desk in 3rd col, then take break ...
        # Do this until m-i < distribute
        # if m-i < distribute:
        #     break

        # The above won't work cause we might want [1, 1, 0, 1, 1]
        # Instead of [1, 0, 1, 1, 1]

    groups = m - distribute + 1
    # print(groups)
    ans = -(-distribute // groups)
    print(ans)