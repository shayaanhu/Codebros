weights = list(map(int, input().split()))
count = 0
while (weights[0] <= weights[1]):
    count += 1
    weights[0] *= 3
    weights[1] *= 2
print(count)
