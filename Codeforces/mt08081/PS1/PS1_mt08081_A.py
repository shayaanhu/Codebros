t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    aList = list(map(int, input().split()))
    robin = 0
    count = 0
    for i in aList:
        if (i >= k):
            robin += i
        elif (robin > 0 and i == 0):
            count += 1
            robin -= 1
    print(count)
