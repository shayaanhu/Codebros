t = int(input())
final = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    valleys = 0
    high = 0
    low = 0
    while (high < n):
        while(high < n - 1 and a[high] == a[high + 1]):
            high += 1
        if (low == 0 or a[low - 1] > a[low]) and (high == n - 1 or a[high + 1] > a[high]):
            # print("Low:", low, "High:", high)
            valleys += 1
        low = high + 1
        high += 1

    if valleys == 1:
        final.append("YES")
    else:
        final.append("NO")

for i in final:
    print(i)


