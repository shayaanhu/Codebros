import math


for _ in range(int(input())):
    n = int(input()) 
    a = list(map(int, input().split()))

    # Find two numbers with the largest i + j such that a_i and a_j are coprime
    # If they don't exist, print -1
    # Otherwise, print i+j
    # Have to check gcd of the numbers which can only be 1

    dict = {}
    # Store distinct occurences of the first numbers in the dictionary
    # Use these numbers along with the second number to check if they are coprime
    # The dictionary will store the index of the first number
    for i in range(n):
        if a[i] not in dict:
            dict[a[i]] = i

    # Now use the dictionary to check if the numbers are coprime
    # If they are, store the maximum i+j
    # If they are not, continue

    

    i, j = n-1, n-1
    flag = False
    maxi = 0
    while i >= 0:
        j = i
        while j >= 0:
            # print(i, j, a[i], a[j])
            if math.gcd(a[i], a[j]) == 1:
                # print(i+1+j+1)
                if i+1+j+1 > maxi:
                    maxi = i+1+j+1
                # flag = True
                break
            j -= 1
        # else:
        i -= 1
        continue
        # break
    # else:
    if maxi == 0:
        print(-1)
    else:
        print(maxi)