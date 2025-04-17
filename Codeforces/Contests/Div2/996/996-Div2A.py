t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    end = False
    while not(end):
        # print(a, b)
        if (a+1 == b or a-1 == b):
            print("NO")
            end = True
        elif(a < b):
            a += 1
        elif(a > b):
            a -= 1
        if (b+1 == a or b-1 == a):
            print("YES")
            end = True
        elif(b < a):
            b += 1
        elif(b > a):
            b -= 1