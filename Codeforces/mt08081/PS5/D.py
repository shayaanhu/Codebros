
import sys
sys.setrecursionlimit(10**6)

with open('wormsort.in') as fin, open('wormsort.out', 'w') as fout:

    N, M = map(int, fin.readline().split())
    p = list(map(int, fin.readline().split()))

    # find maximum wormhole width.
    wormholes = []
    max_width = 0
    # print('x')
    for _ in range(M):
        a, b, w = map(int, fin.readline().split())
        wormholes.append((a-1, b-1, w))
        if w > max_width:
            max_width = w

    # If all cows are already sorted, output -1.
    all_sorted = True
    for i in range(N):
        if p[i] != i+1:
            all_sorted = False
            break
    if all_sorted:
        # print(-1)
        fout.write('-1\n')
        exit()

    # union-find data structure
    parent = list(range(N))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        pa = find(a)
        pb = find(b)
        if pa != pb:
            parent[pb] = pa

    # We can use binary search on the threshold X: candidate wormhole width.
    def can_sort(X):
        for a, b, w in wormholes:
            if w >= X:
                union(a, b)
        for i in range(N):
            if find(i) != find(p[i]-1):
                return False
        return True

    # Binary search for the maximum X
    lo, hi = 1, max_width + 1
    ans = 0
    while lo < hi:
        parent = list(range(N))
        mid = (lo + hi) // 2
        if can_sort(mid):
            ans = mid 
            lo = mid + 1 
        else:
            hi = mid

    # print(ans)
    fout.write(str(ans) + '\n')


# import sys
# # input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# with open('wormsort.in') as fin, open('wormsort.out', 'w') as fout:

#     # Read N (number of cows/locations) and M (number of wormholes)
#     # N, M = map(int, input().split())
#     # p = list(map(int, input().split()))

#     N, M = map(int, fin.readline().split())
#     p = list(map(int, fin.readline().split()))


#     # Read wormhole info: (a, b, w) and determine maximum wormhole width.
#     wormholes = []
#     max_width = 0
#     for _ in range(M):
#         # a, b, w = map(int, input().split())
#         a, b, w = map(int, fin.readline().split())
#         # convert to 0-indexed
#         wormholes.append((a-1, b-1, w))
#         if w > max_width:
#             max_width = w

#     # If all cows are already sorted, output -1.
#     all_sorted = True
#     for i in range(N):
#         if p[i] != i+1:
#             all_sorted = False
#             break
#     if all_sorted:
#         print(-1)
#         fout.write('-1\n')
#         exit()

#     # union-find data structure
#     parent = list(range(N))
#     # find with path compression
#     def find(a):
#         while parent[a] != a:
#             parent[a] = parent[parent[a]]
#             a = parent[a]
#         return a
#     def union(a, b):
#         pa = find(a)
#         pb = find(b)
#         if pa != pb:
#             parent[pb] = pa


#     # We'll use binary search on the threshold X: candidate wormhole width.
#     def can_sort(X):
#         for a, b, w in wormholes:
#             if w >= X:
#                 union(a, b)
#         for i in range(N):
#             if find(i) != find(p[i]-1):
#                 return False
#         return True

#     # Binary search for the maximum X
#     lo, hi = 1, max_width + 1 
#     ans = 0
#     while lo < hi:
#         parent = list(range(N))
#         mid = (lo + hi) // 2
#         if can_sort(mid):
#             ans = mid 
#             lo = mid + 1 
#         else:
#             hi = mid

#     print(ans)
#     fout.write(str(ans) + '\n')

