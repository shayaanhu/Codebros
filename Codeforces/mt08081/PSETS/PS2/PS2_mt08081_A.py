import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    # check if total is a square number
    if (math.sqrt(total).is_integer()):
        print("YES")
    else:
        print("NO")
