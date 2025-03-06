

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

    # However, the above will fail since we might have a very small y and a very large x and k
    # Consider y = 2, x = 10^8, k = 10^9
    # We can't perform 10^9 operations on x!!!
