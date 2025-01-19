# t = int(input())
# final = []

# for _ in range(t):
#     temp = list(map(int, input().split()))
#     n, k = temp[0], temp[1]
#     cards = []

#     for i in range(n):
#         cards.append(sorted(input().split()))

#     card = -1
#     for i in range(0, n * k, n):
#         for j in range(len(cards)):
#             print("CARDS LIST:", cards)
#             if len(cards[j]) > 0  and int(cards[j][0]) > int(card):
#                 card = cards[j][0]
#                 print("CARD:", card)
#                 cards[j] = cards[j][1:]
#                 # break

#     final.append(cards)

# for i in final:
#     print(i)


# # for i in final:
# #     for j in i:
# #         print(j, end=" ")
# #     print()