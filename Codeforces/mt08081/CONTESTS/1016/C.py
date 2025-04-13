# from math import gcd

# # taken from TRD
# def sieve(n):
#     """
#     Returns a tuple (is_prime, primes) where:
#       - is_prime is a list of booleans for 0..n,
#       - primes is a list of prime numbers up to n.
#     """
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(n**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False
#     primes = [i for i, prime in enumerate(is_prime) if prime]
#     return is_prime, primes


# N = 10**7

# is_prime, primes = sieve(N)

# Taken
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for _ in range(int(input())):
    x, k = map(int, input().split())
    y = str(x)
    # The number is probably prime if k is not 1
    # This is seen from the test case but could be false

    if k == 1:
        if is_prime(x):
            print("YES")
        else:
            print("NO")
    elif y.count('1') == len(str(x)):
            y = int(y*k)
            if is_prime(y):
                print("YES")
            else:
                print("NO")
    else:
        print("NO")


    



    