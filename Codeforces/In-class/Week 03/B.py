from bisect import bisect_left, bisect_right

t = int(input())

for _ in range(t):
    n, m, q = map(int, input().split())
    teachers = sorted(list(map(int, input().split())))
    queries = list(map(int, input().split()))
    for query in queries:
        index = bisect_right(teachers, query)
        if index == 0:
            print(teachers[0] - 1)
        elif index == m:
            print(n - teachers[-1])
        else:
            print((teachers[index] - teachers[index - 1]) // 2)
