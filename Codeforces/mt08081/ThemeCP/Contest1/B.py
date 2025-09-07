# 1000 rated problem

# Count the number of Pairs

# A pair would be a and A and so on

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    # for i in "abcdefghijklmnopqrstuvwxyz":
    #     k -= s.count(i) // 2
    # Can't do this since k or no of operations are defined and not infinite

    # First lets find out all pairs along with remaining single characters
    pairsSingles = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        # Count pairs by matching lower and upper case
        lower = s.count(i)
        upper = s.count(i.upper())
        pairCount = min(lower, upper)
        pairsSingles.append((pairCount, max(lower - pairCount, upper - pairCount)))
    # print(pairsSingles)
    pairs = sum(i[0] for i in pairsSingles)
    singles = sum(i[1] // 2 for i in pairsSingles)

    # Now we can perform k operations on the singles which are more than 2
    pairs += min(singles, k)

    print(pairs)