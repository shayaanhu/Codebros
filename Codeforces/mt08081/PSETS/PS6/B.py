n = int(input())
a = list(map(int, input().split()))

# We can try to do this in a way like fib
# Store the first two values and build up

dp_prev1 = 0
dp_prev2 = abs(a[1] - a[0])

for i in range(2, n):
    # Calculating previous 2 costs and then taking min (kinda greedy)
    cost1 = dp_prev1 + abs(a[i] - a[i - 2])
    cost2 = dp_prev2 + abs(a[i] - a[i - 1])
    dp_curr = min(cost1, cost2)
    dp_prev1 = dp_prev2
    dp_prev2 = dp_curr
print(dp_prev2)