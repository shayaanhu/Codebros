n, k = map(int, input().split())

# even
if k > (n + 1) // 2:
    print((k - (n // 2)) * 2 if n % 2 == 0 else (k - 1 - (n // 2)) * 2)

# odd
else:
    print(k * 2 - 1)