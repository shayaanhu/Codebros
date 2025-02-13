# The store sells n items
# The i-th item costs a[i] dollars
# The following q lines will contain x and y
# if a customer purchases at least x items, y cheapest of them are free.
# All queries are independent
# Determine max total value for free for each query

n,q = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

# for _ in range(q):
#     x,y = map(int, input().split())
#     # # newlst = a[x-y:x]
#     # # sumo = sum(newlst[x-y:])
#     # sumo = sum(a[x-y:x])
#     # print(sumo)

#     da = [0] * (x + 1)
#     da[0] = a[0]
#     for i in range(1, x):
#         da[i] = a[i] - a[i - 1]
#     # print(da)

#     prefix_sum = [0] * (x + 1)
#     prefix_sum[0] = a[0]
#     for i in range(1, x):
#         prefix_sum[i] = prefix_sum[i-1] + da[i]

#     sumo = 0
#     for j in range(x, x-y-1, -1):
#         sumo += prefix_sum[j]


#     # # print(prefix_sum)
#     print(sumo)

# SOlUTION
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
 
 
for _ in range(q):
    x, y = map(int, input().split())
    print(prefix[x] - prefix[x - y])