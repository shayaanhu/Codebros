for _ in range(int(input())):
    a,b,c = map(int, input().split())
    A, B, C = a, 2*b, 3*c
    summ = A + B + C
    print(summ % 2)

    # print(0) if a == b == c else print(1)

# We can state that combinations of A, B, C are 0-6 when they are all 1-3 respectively
# We can somehow extend this to state that we can form all positive integers using A, B and C
# Hence, the answer is 0 if summ is divisible by 2. This is because:
# you can form two groups of summ/2 using A, B and C
# Otherwise it will always be 1

# This is not entirely intuitive but I guess it works!!!
