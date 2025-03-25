def func(a, b, c):
    return (max(max(b,c)-a+1, 0))

for _ in range(int(input())):
    a = list(map(int, input().split()))
    mx = max(a)
    mx_count = a.count(mx)
    final = []
    for i in a:
        final.append(mx - i + 1) if i != mx or mx_count > 1 else final.append(0)

    print(*final)

    # Second approach
    # a, b, c = map(int, input().split())
    # print(func(a, b, c), func(b, a, c), func(c, a, b))

# print(func(10, 75, 15))
