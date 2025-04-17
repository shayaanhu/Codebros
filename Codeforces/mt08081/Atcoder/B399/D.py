# for _ in range(int(input())):
#     N = int(input())
#     A = list(map(int, input().split()))

#     first_occurence = [-1] * (N + 1)
#     last_occurence = [-1] * (N + 1)
#     for i, x in enumerate(A):
#         if first_occurence[x] == -1:
#             first_occurence[x] = i
#         else:
#             last_occurence[x] = i
#     # print(first_occurence, last_occurence)

#     couples = []
#     for i in range(1, N + 1):
#         if last_occurence[i] - first_occurence[i] > 1:
#             # Not adjacent (enter into couples)
#             couples.append((first_occurence[i], last_occurence[i]))
#     # print(couples)
#     if not couples:
#         print(0)
#         continue
#     couples.sort()
#     # print(couples)

#     # We have the couples now
#     # How do we count the number of swaps necessary to make them adjacent?

    

#     # We can iterate over couples or something

#     # ans = 0

#     # for i in range(1, len(couples)):
#     #     if couples[i][0] > couples[i - 1][1]:
#     #         ans += couples[i][0] - couples[i - 1][1] - 1
#     #     else:
#     #         ans += couples[i][1] - couples[i - 1][0] - 1
        
#     # print(ans)

    
#     ans = 0
#     for i in range(len(couples) - 1):
#         cur_first, cur_last = couples[i]
#         nxt_first, nxt_last = couples[i+1]
#         if nxt_first == cur_first + 1 and nxt_last == cur_last + 1:
#             ans += 1
#     print(ans)

# import sys
# input_data = sys.stdin.read().strip().split()
# it = iter(input_data)
# T = int(next(it))
# res = []
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    
    first = [-1] * (N + 1)
    second = [-1] * (N + 1)
    for i, x in enumerate(A):
        if first[x] == -1:
            first[x] = i
        else:
            second[x] = i

    couples = []  
    for a in range(1, N + 1):
        if second[a] - first[a] > 1:
            couples.append((first[a], second[a]))
    couples.sort()

    ans = 0
    for i in range(len(couples) - 1):
        f1, s1 = couples[i]
        f2, s2 = couples[i+1]
        if f2 == f1 + 1 and abs(s1 - s2) == 1:
            ans += 1
    print(ans)
