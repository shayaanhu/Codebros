for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    print(a)

    i, j = 0, n - 1
    while k > 0:

        if a[i] + a[i + 1] < a[j]:
            i += 2
        else:
            j -= 1
        
        k -= 1

    print(sum(a[i : j + 1]))
