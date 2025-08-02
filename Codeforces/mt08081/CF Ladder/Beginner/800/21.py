for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    Trapped = False
    for i in range(n):
        if a[i] == '1' and b[i] == '1':
            Trapped = True
            break
    print("NO" if Trapped else "YES")

    # Another way is to sort both and see if the last element of both is 1 or not.
    # a = sorted(a)
    # b = sorted(b)
    # print("NO" if a[-1] == '1' and b[-1] == '1' else "YES")