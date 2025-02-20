n, k, q = map(int, input().split())
lr_List = []
for _ in range(n):
    l, r = map(int, input().split())
    lr_List.append((l, r))

for _ in range(q):
    a, b = map(int, input().split())
    count = 0
    for l, r in lr_List:
        if a <= l <= b or a <= r <= b or l <= a <= r or l <= b <= r:
            count += 1
    print(count)


