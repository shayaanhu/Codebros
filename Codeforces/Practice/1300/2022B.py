t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    
    a = list(map(int, input().split()))

    left = max(a)
    right = int(1e15)
    total_cars = sum(a)

    def check(X):
        return (total_cars + X - 1) // X <= x

    answer = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
