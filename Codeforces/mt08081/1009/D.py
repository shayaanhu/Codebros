import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    r = list(map(int, input().split()))
    # Sum of r is equal to m.
    # r is the radii of circle on the x-axis
    # x is the x-coordinates of the circles.

    # Find the number of integer points inside or on the border of the circles.

    # If r = 1, then number of integer points inside the circle would be 5

    # if r = 2, then number of integer points inside the circle would be 13

    # if r = 3, then number of integer points inside the circle would be 29

    # This shows that the number of integer points inside the circle are:
    # 4 + (2n-1)**2

    # We can start from leftmost circle and go to the rightmost circle
    # Form intervals and then merge the intervals

    intervals = {}

    for i in range(n):
        x_i = x[i]
        r_i = r[i]
        for y in range(-r_i, r_i+1):
            d = int(math.sqrt(r_i**2 - y**2))
            L = x_i - d
            R = x_i + d
            # if y in intervals:
            #     last_L, last_R = intervals[y][-1]
            #     if L <= last_R + 1:
            #     # extend the interval
            #         intervals[y][-1] = (last_L, max(last_R, R))
            #     else:
            #         intervals[y] = [(L, R)]
            # # print(intervals)
            if y in intervals:
                intervals[y].append((L, R))
            else:
                intervals[y] = [(L, R)]

    # total = 0
    # for y in intervals:
    #     for L, R in intervals[y]:
            # total += R - L + 1
    print(intervals)
    total = 0
    for y in intervals:
        intervals[y].sort()
        merged = []
        for L, R in intervals[y]:
            if not merged or merged[-1][1] < L:
                # No overlap
                merged.append([L, R])
            else:
                # Overlap
                merged[-1][1] = max(merged[-1][1], R)
        # print(merged)

        # L, R = intervals[y][0]
        # total += R - L + 1
        # print(y, total)

        for L, R in intervals[y]:
            total += R - L + 1

    print(total)