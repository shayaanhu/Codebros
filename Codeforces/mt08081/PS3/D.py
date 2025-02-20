n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))

count = 0
for i in range(1 << n):
    sum = 0
    min = 1e9
    max = 0
    for j in range(n):
        if i & (1 << j):
            sum += c[j]
            if c[j] < min:
                min = c[j]
            if c[j] > max:
                max = c[j]
    if sum >= l and sum <= r and max - min >= x:
        count += 1
print(count)