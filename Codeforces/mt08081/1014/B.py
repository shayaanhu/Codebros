# I think this is simple as well
# If we have 1 in the top string and 101 in the next index of the lower string, then its not possible


for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()

    # for i in range(n-2):
    #     if s[i] == '1' and t[i+1:i+4] == '101':
    #         print('No')
    #         break
    # else:
    #     print('Yes')

    # for i in range(n):
    #     if s[i] == '0':
    #         continue


    # S = 10101
    # T = 01010
    # So its not possible to make S all 0s
    # S = 01010
    # T = 10101
    # Here as well its not possible
    # Hence, we have to check the number of 1s in complimentary positions
    # What I mean is that if 0th idx of S is 1, then 1st idx of T shouldn't be 1

    # If a certain number of such mismatches are there, then its not possible

    odds = 0 # This checks even indices of S and odd indices of T
    evens = 0 # This checks odd indices of S and even indices of T
    for i in range(n):
        # if s[i] == '1' and t[i] == '0':
        #     if i % 2 == 0:
        #         evens += 1
        #     else:
        #         odds += 1
        # elif s[i] == '0' and t[i] == '1':
        #     if i % 2 == 0:
        #         odds += 1
        #     else:
        #         evens += 1

        if i % 2 == 0:
            if s[i] == '1':
                evens += 1
            if t[i] == '1':
                odds += 1
        else:
            if s[i] == '1':
                odds += 1
            if t[i] == '1':
                evens += 1

    # Oh the number of mismatches should be less than n // 2
    # This is because if there are more then, we can't make them all 0s

    if evens > n // 2 or odds > (n+1) // 2:
        print('NO')
    else:
        print('YES')