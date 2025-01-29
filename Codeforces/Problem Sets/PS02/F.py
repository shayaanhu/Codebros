for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    min_count = float('inf')
    w_count = 0
    i, j = 0, 0

    while j < k:
        if s[j] == "W":
            w_count += 1
        j += 1

    while j < n:
        min_count = min(min_count, w_count)

        if s[i] == "W":
            w_count -= 1
        
        if s[j] == "W":
            w_count += 1

        i += 1
        j += 1

    min_count = min(min_count, w_count)

    print(min_count)