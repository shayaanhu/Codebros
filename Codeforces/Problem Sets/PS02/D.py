import math
t = int(input())
final = []

# sum of arithmetic series
# O(1) time complexity
def arithmetic_sum(a, b):
    return (b - a + 1) * (a + b) // 2


for _ in range(t):
    temp = list(map(int, input().split()))
    n, k = temp[0], temp[1]

    low, high = k, k + n - 1
    min_sum = math.inf

    while low <= high:
        mid = (low + high) // 2

        left_sum = arithmetic_sum(k, mid)
        right_sum = arithmetic_sum(mid + 1, k + n - 1)

        min_sum = min(min_sum, abs(left_sum - right_sum))

        if left_sum < right_sum:
            low = mid + 1
        else:
            high = mid - 1

    final.append(min_sum)

for i in final:
    print(i)