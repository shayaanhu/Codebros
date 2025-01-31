for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    
    operations, count, i = 0, 0, 0
    while i < n:
        if s[i] == '0':
            count += 1
            if count == m:
                operations += 1
                count = 0
                i += k  
                continue
        else:
            count = 0
        i += 1
    
    print(operations)
    