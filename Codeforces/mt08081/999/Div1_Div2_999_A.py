final = []
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    even = [n for n in a if n % 2 == 0]
    odd = [n for n in a if n % 2 != 0]
    s = 0
    points = 0
    # for i in a:
    #     s += i
    #     if s % 2 == 0:
    #         points += 1
    #     while s % 2 == 0:
    #         s //= 2
    # final.append(points)

    for i in even:
        s += i
        if s % 2 == 0:
            points += 1
        while s % 2 == 0:
            s //= 2
    for i in odd:
        s += i
        if s % 2 == 0:
            points += 1
        while s % 2 == 0:
            s //= 2
    final.append(points)

for i in final:
    print(i)