from bisect import bisect_left

t = int(input())
final = []

for _ in range(t):
    temp = list(map(int, input().split()))
    n, q = temp[0], temp[1]
    
    candies = list(map(int, input().split()))
    candies.sort(reverse=True)

    prefix_sum = [0] * n
    prefix_sum[0] = candies[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + candies[i]
        
    for i in range(q):
        query = int(input())
        
        index = bisect_left(prefix_sum, query)
        if index < n:
            final.append(index + 1)
        else:
            final.append(-1)
            
for i in final:
    print(i)