for _ in range(int(input())):
    a, b = map(int, input().split())
    n, m = map(int, input().split())

    # a is the cost of 1 kg potato
    # b is the price on the next day (prices alternate)
    # n is the required kgs of potato
    # m is the amount of potatoes required for promotion (i.e buy m kg to get m + 1 kg)
    # find the min no of coins to buy at least n kgs of potatoes

    lowCost = min(a, b)

    total_cost = 0
    total_cost2 = 0
    # We can use the promotion
    promo_sets = n // (m + 1)
    remaining = n % (m + 1)

    total_cost += promo_sets * m * a
    total_cost += remaining * lowCost

    total_cost2 = n * lowCost
    print(min(total_cost, total_cost2))