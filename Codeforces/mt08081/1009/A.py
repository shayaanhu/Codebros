for _ in range(int(input())):
    l, r, d,u = map(int, input().split())
    #  (−l,0), (r,0), (0,−d), (0,u)
    # Check if its a square
    if r != l or u != d or r != u:
        print("NO")
    else:
        print("YES")