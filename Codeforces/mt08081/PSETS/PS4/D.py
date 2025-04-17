import math

def is_prime(n):
    if n < 2:
        return False
    r = int(math.sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    
    # Base cases:
    if n == 1:
        print("FastestFinger")
    elif n == 2 or n % 2 == 1:
        # n == 2 is winning; odd numbers > 1 are winning.
        print("Ashishgup")
    else:
        # n is even and greater than 2
        # If n is a power of two, it has no odd divisor greater than 1.
        if n & (n - 1) == 0:
            print("FastestFinger")
        # If n = 2 × (odd prime), then the only move forces n to become 2.
        elif n % 4 != 0 and is_prime(n // 2):
            print("FastestFinger")
        else:
            print("Ashishgup")