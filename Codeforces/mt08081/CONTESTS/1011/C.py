# x + k + y + k == (x+k) ^ (y+k)
# A + B is equal to A ^ B is only true when there is no carry bit
# DLD knowledge lol
# Hence x + k + y + k == (x+k) ^ (y+k) is only true when x and y have no common 1s
# So, (x+k) & (y+k) == 0
# How do we find k though?

for _ in range(int(input())):
    x, y = map(int, input().split())
    k = 0
    if x == y:
        print(-1)
        continue

    k = min(x, y)
    while k > 0:
        if (x+k) & (y+k) == 0:
            break
        k -= 1
        # if k > 10**9:
        #     i -= 1
        #     k = 0


    print(k)