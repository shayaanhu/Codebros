
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()

    for i in range(n):
        if c[i] != a[i] and c[i] != b[i]:
            print("YES")
            break
    else:
        print("NO")