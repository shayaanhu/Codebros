# Div 2


for _ in range(int(input())):
    n, a = map(int, input().split())
    v = list(map(int, input().split()))

    less = sum(1 for x in v if x < a)
    greater = sum(1 for x in v if x > a)

    if less < greater:
        b = a + 1 
    else:
        b = a - 1 

    print(b)