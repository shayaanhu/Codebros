# This is a precomputation problem as far as I can tell.
# Precompute gcds and lcms uptil n//2 where n is max 10**7

from math import gcd

# taken from TRD
def sieve(n):
    """
    Returns a tuple (is_prime, primes) where:
      - is_prime is a list of booleans for 0..n,
      - primes is a list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return is_prime, primes


N = 10**7

is_prime, primes = sieve(N)

for _ in range(int(input())):
    n = int(input())
    count = 0
    for p in primes:
        if p > n:
            break
        count += n // p
    print(count)