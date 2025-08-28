# Infection spreads each day to one adjacent house
# n houses
# m days
# l leftmost house
# r rightmost house
# Print any segment of houses that can be infected
# l is negative

for i in range(int(input())):
    n, m, l, r = map(int, input().split())
    # if m > n:
    #     print(l, r)
    #     continue
    # # leftmost house is infected
    # if l <= -m:
    #     print(l, l+m)
    #     continue
    # if r >= m:
    #     print(0, r-m)
    #     continue
    # # print(-m, 0)

    # take the leftmost as infected
    # then add l or m to the right of that house...

    l_2 = max(l, -m)
    r_2 = l_2 + m
    print(l_2, r_2)