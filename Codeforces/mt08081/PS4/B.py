
def process_test_case(x, y, k):
    while k > 0:
        if x < y:
            # When x is in the range {1,2,...,y-1}, cycle through the values
            x = ((x - 1 + k) % (y - 1)) + 1
            k = 0
            break
        
        remainder = x % y
        if remainder != y - 1:
            delta = (y - 1) - remainder
            if k <= delta:
                x += k
                k = 0
                break
            else:
                x += delta
                k -= delta
        
        # Now x % y == y - 1, find highest power of y dividing x+1
        temp, m = x + 1, 0
        while temp % y == 0:
            m += 1
            temp //= y
        
        x = (x + 1) // (y ** m)
        k -= 1
    
    return x


for _ in range(int(input())):
    x, y, k = map(int, input().split())

    # k operations
    # x is the original num
    # In one operation: x is first incremented by 1
    # Then if it is divisible by y, it is divided by y until it is not divisible

    # Consider the x = 76, y = 7, k = 7
    # k = 1: x = 77, x is divisible so x becomes 11
    # k = 2: x = 12, x is not divisible
    # k = 3: x = 13, x is not divisible
    # k = 4: x = 14, x is divisible so x becomes 2
    # k = 5: x = 3, x is not divisible
    # k = 6: x = 4, x is not divisible
    # k = 7: x = 5, x is not divisible

    # After a certain number of operations, x will become bound by mod y
    # This means that x will be in the range of 0 to y-1

    # Hence, we can calculate the number of operations required to reach the bound
    # We also store the value resulting in the bound when this happens
    # Then, we can easily calculate what the final value of x would be after k operations

    # However, the above will fail when we have a very small y and a very large x and k
    # Consider y = 2, x = 10^8, k = 10^9
    # We can't perform 10^9 operations on x!!!

    print(process_test_case(x, y, k))

    # for i in range(k):
    #     x += 1
    #     if pow(x, 1, y) == 0:
    #         x = x // y
    #         break
    # print(x)

