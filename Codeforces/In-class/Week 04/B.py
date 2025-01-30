for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    
    i, count = 0, 0
    while i <= n - m:
        if s[i:i + m] == '0' * m:
            count += 1
            i += m + k - 1
        else:
            i += 1
        
    print(count)