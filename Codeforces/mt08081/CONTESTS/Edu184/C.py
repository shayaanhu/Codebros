# Range question...

# Maximum possible total array sum

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # This probably has some standard TRD kinda code...
    # I remember seeing something like this before in my CP classes...
    # lemme search up my TRD notes...

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    Sumo = prefix[n]

    # (l, r) = (1, 1) => [2, ....] 
    # (1, 2) => [3, 3, ....]
    # (2, 4) => [x, 6, 6, 6, ....]
    # We need to make sure that this gain in values is maximised
    # We can take the difference between these values and the original values
    # then maybe we can check where the sum of these differences is maximised?
    # diffs = [0] * n
    # for i in range(n):
    #     diffs[i] = (i + 1) - a[i]
    # # Now we need to find the maximum subarray sum in diffs
    # max_ending_here = 0
    # max_so_far = 0
    # for x in diffs:
    #     max_ending_here = max(0, max_ending_here + x)
    #     max_so_far = max(max_so_far, max_ending_here)
    # print(Sumo + max_so_far)

    # Terrible attempt lol...
    # My TRD had some notes on "Gain" for a range.

    # Gain of (l, r) = (r^2 + r - prefix[r]) - (l^2 - l - prefix[l-1])

    # I guess we can iterate over all r and all l for it
    # max_total = Sumo
    # r_values = [0] * (n + 1)
    # l_values = [0] * (n + 1)
    # for r in range(1, n + 1):
    #     # calculate the r part of gain
    #     r_part = (r * r + r) - prefix[r]
    #     # now the l part
    #     l_part = (r*r - r) - prefix[r-1]
    #     r_values[r] = r_part
    #     l_values[r] = l_part
    # for r in range(1, n + 1):
    #     for l in range(1, r + 1):
    #         gain = r_values[r] - l_values[l]
    #         max_total = max(max_total, Sumo + gain)

    # the above solution is correct but its O(n^2)...
    # Maybe we can reduce the second loop somehow...
    max_total = Sumo
    min_l_score = float('inf')
    for i in range(1, n+1):
        l_score = (i * i - i) - prefix[i - 1]
        min_l_score = min(min_l_score, l_score)
        r_score = (i * i + i) - prefix[i]
        gain = r_score - min_l_score
        max_total = max(max_total, Sumo + gain)

    print(max_total)