for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    
    i, count = 0, 0
    while i < n:
        if s[i] == "W":
            i += 1
        elif s[i] == "B":
            i += k
            count += 1
            
    print(count)
            