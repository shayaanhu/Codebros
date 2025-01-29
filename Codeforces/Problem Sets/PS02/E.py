for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    inc, dec = a[0], a[0]
    valid = True
    for i in range(1, n):
        # print(inc, dec, a[i])
        
        if a[i] == inc + 1:
            inc += 1
            continue
        
        elif a[i] == dec - 1:
            dec -= 1
            continue
        
        else:
            valid = False
            break
    
    if valid:
        print("YES")
    else:
        print("NO")