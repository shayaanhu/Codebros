for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # n is greater than 3
    # a and b are good arrays where for every x in a and y in b, x and y both are at least 2 in count
    # 
    A = set(a)
    B = set(b)
    if len(A) >= 3 or len(B) >= 3:
        print("YES")
        continue
    elif (len(A) == 2 and len(B) == 2):
        print("YES")
        continue
    else:
        print("NO")
        continue