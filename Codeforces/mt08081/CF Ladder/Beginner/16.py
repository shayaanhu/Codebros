
# # precompute primes uptil 10^9
# def sieve(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False
#     return primes

# primes = sieve(8000)


# # print(primes[:10])
for _ in range(int(input())):
    n = int(input())
#     counti = 0
#     i = 0
#     while n > 0:
#         if primes[i]:
#             n -= 1
#             print(i, end=' ')
#         i += 1

#     print()

    if n == 1:
        print(1)
    elif n == 2:
        print(2, 3)
    else:
        for i in range(2, n+2):
            print(i, end=' ')
        print()


# There was no need for sieve lol
# I could have just printed the numbers from 2 to n+1 since a_i will never be divisble by a_(i-1) for n > 3