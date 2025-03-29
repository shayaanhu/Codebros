# lol

# sieve of eratosthenes
def sieve(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    return prime

primes = sieve(20001)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # a.sort()

    summ = sum(a)

    # minn = min(a)
    # idx = a.index(minn)

    if primes[summ]:
        # summ -= a[0]
        print(n-1)
        for i in range(n):
            if not primes[summ - a[i]]:
                # print(i+1, end = ' ')
                idx = i
                break
            # print(i, end = ' ')
        # print(n)
        # print()
        # continue
        # print(idx)
        for j in range(n):
            if idx == j:
                continue
            print(j+1, end = ' ')
        print()
        continue
    print(n)
    for i in range(n):
        print(i+1, end = ' ')
    print()