# t = int(input())

# for _ in range(t):
#     nList = list(map(int, input().split()))
#     a_3 = nList[0] + nList[1]
#     nList.insert(2, a_3)
#     print(nList)
#     fib = 0
#     length = len(nList)
#     while fib < length - 2 and nList[fib] + nList[fib + 1] == nList[fib + 2]:
#         fib += 1
#     print(fib)


t = int(input())

for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    
    max_fibonacciness = 0
    
    # Try different values for a3
    for a3 in range(-100, 101):
        fibonacciness = 0
        nList = [a1, a2, a3, a4, a5]
        
        if nList[2] == nList[0] + nList[1]:
            fibonacciness += 1
        if nList[3] == nList[1] + nList[2]:
            fibonacciness += 1
        if nList[4] == nList[2] + nList[3]:
            fibonacciness += 1
        
        max_fibonacciness = max(max_fibonacciness, fibonacciness)
    
    print(max_fibonacciness)