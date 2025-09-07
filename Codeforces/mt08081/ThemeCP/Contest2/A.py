# 800

# Startup

for _ in range(int(input())):
    n, k = map(int, input().split())
    
    # bottles = []
    # for i in range(k):
    #     b, c = map(int, input().split())
    #     bottles.append((b, c))

    # bottles.sort(key=lambda x: x[1], reverse=True)

    # print(bottles)

    total = 0

    brands = [0]*(k+1)
    for i in range(k):
        b, c = map(int, input().split())
        brands[b] += c

    brandVal = sorted(brands, reverse=True)

    total = sum(brandVal[:n])

    # for b, c in bottles:
    #     if n <= 0:
    #         break
    #     total += c
    #     n -= 1

    print(total)