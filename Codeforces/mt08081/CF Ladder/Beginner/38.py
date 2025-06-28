def solve(n, a):
    sorted_a = sorted(a)
    # if sorted_a == a:
    #     return 0
    count = 0
    while sorted_a != a:
        x = 0 if count % 2 == 0 else 1
        count += 1
        for i in range(x, n - 1, 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
 
        # print(sorted_a, a, x)
        
    return count
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))