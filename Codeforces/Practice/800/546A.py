temp = list(map(int, input().split()))
k, n, w = temp[0], temp[1], temp[2]

cost = 0
for i in range(1, w + 1):
    cost += i * k
    
print(cost - n if (cost - n) > 0 else 0)