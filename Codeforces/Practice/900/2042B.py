# t = int(input())
# final = []

# for _ in range(t):
#     n = int(input())
#     marbles = list(map(int, input().split()))

#     marbles.sort(reverse=True)

#     # print(marbles)

#     aliceScore = 0
#     aliceMarbles = []
#     bobMarbles = []
#     for i in range(len(marbles)):
#         if i == 0 or i % 2 == 0:
#             aliceMarbles.append(marbles[i])
#         elif i % 2 == 1:
#             bobMarbles.append(marbles[i])

#     # print(aliceMarbles, bobMarbles)

#     for i in range(len(aliceMarbles)):
#         if aliceMarbles[i] != "USED":
#             if aliceMarbles[i] not in bobMarbles:
#                 aliceScore += 2
#                 aliceMarbles = ["USED" if x == aliceMarbles[i] else x for x in aliceMarbles]
#                 # print(aliceMarbles, aliceScore)
#             else:
#                 aliceScore += 1
#                 aliceMarbles = ["USED" if x == aliceMarbles[i] else x for x in aliceMarbles]
#                 # print(aliceMarbles, aliceScore)

#     # print(aliceMarbles, aliceScore)

#     final.append(aliceScore)

# for i in final:
#     print(i)

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    marbles = list(map(int, input().split()))

    freq = Counter(marbles)
    single_count = sum(1 for v in freq.values() if v == 1)
    multiple_count = sum(1 for v in freq.values() if v > 1)

    alice_score = (single_count + 1) // 2 * 2 + multiple_count
    print(alice_score)
