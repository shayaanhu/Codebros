# 800

# Card Exchange

for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    count = {}

    for i in c:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # Where ever the count is more than k, we can easily cut it down to k
    # This seems trivial
    # If we can perform the operation even once, then the answer is k - 1 else n

    if max(count.values()) >= k:
        print(k - 1)
    else:
        print(n)