# n numbers in q and r
# perform operations as many times as possible
# choose x and y such that
# q_i = x // y
# r_j = x % y
# remove both from their arrays

# I think I have seen a similar problem before hmmm...

for _ in range(int(input())):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    # We can try to match the pairs between q and r
    # Then we can count them out

    # q is quotients and r is remainders
    # q * y + r = x
    # put this into the constraint eq
    # 1 <= y < q * y + r <= k
    # We can see that y <= k - r / q
    # We can also see that y * (1 - q) < r
    # q can be from 1 to idk any number so 1 - 1 = 0 ... 1 - 2 = - 1

    # what if we write it like this:
    # y * (q - 1) >= -r
    # Now y must always be greater than -r / (q - 1) ... This can get 1 - 1 
    # in the denominator :(

    # x % y = r ... hence y > r

    # so we have two constraints on y
    # r < y <= (k - r) / q
    # r + 1 < (k - r) / q (Replacing y with r + 1 for minimum)
    # r * q + q + r <= k
    # (q+1)(r+1) <= k + 1

    # r <= (k + 1) / (q + 1) - 1

    # Since we have a bound between 1 and this value... we can just match relevant pairs...
    # i guess so :/

    r_bounds = []
    for val in q:
        bound = (k + 1) // (val + 1) - 1
        r_bounds.append(bound)
    r_bounds.sort()
    r.sort()

    count = 0
    j = 0
    for bound in r_bounds:
        if j < n and r[j] <= bound:
            count += 1
            j += 1
    print(count)