n, q = map(int, input().split())
a = list(map(int, input().split()))

# Build a prefix sum array and then simply calculate the sum from a to b

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

for i in range(q):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])