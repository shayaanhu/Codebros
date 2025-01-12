t = int(input())
final = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    valleys = 0
    i = 1
    while(i < len(a) - 1):
        if (a[i] == a[i + 1] and a[i] == 1) or ((a[i - 1] > a[i] < a[i + 1])):
            l = i - 1
            while (i < len(a) - 2 and a[i] == a[i + 1]):
                r = i + 2
                print("l", l, "r", r)
                if (a[r] > a[l]):
                    valleys += 1
                i += 1
        # elif (a[i - 1] > a[i] < a[i + 1]):
        #     valleys += 1
        i += 1

    final.append(valleys)

print(final)


