import math

t = int(input())
final = []

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    if math.sqrt(sum(nums)).is_integer():
        final.append("YES")
    else:
        final.append("NO")

for i in final:
    print(i)