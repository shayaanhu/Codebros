n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 1
while i < t:
    i += a[i - 1]
    if i == t:
        print("YES")
        break
    if i > t:
        print("NO")
        break