# n cows playing a card game
# n*m cards (numbered 0 to n*m-1)
# 1 card per round for each cow
# checking for permutation
# The farmer wants to find the permutation in which his cows would be able to empty their hands
# The cows can only play a larger card than the center pile top card

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # n is cows and m is the number of cards received in each line
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    for i in range(n):
        cards[i] = sorted(cards[i])
    # sorted(cards)
    # print(cards)
    # The center pile top card is -1 initially
    # The cards are numbered from 0 to n*m-1
    center_pile = -1
    # The permutation is possible
    permutation_possible = True

    card_to_cow = {}
    
    for cow_index in range(n):
        for card in cards[cow_index]:
            card_to_cow[card] = cow_index
    # print(card_to_cow)
    permutation = []
    for i in range(n):
        permutation.append(card_to_cow.get(i))
    # print(permutation)

    # index = 0
    for round in range(m):
        for cow_index in permutation:
        #     # if not cards[cow_index]:
        #     #     continue
        #     if cards[cow_index][0] > center_pile:
        #         center_pile = cards[cow_index].pop(0)
        #     else:
        #         permutation_possible = False
        #         break
        # if not permutation_possible:
        #     break
            # Remove all invalid cards from this cow's deck
            while cards[cow_index] and cards[cow_index][0] <= center_pile:
                cards[cow_index].pop(0)
            
            if cards[cow_index]:  # If there's a valid card to play
                center_pile = cards[cow_index].pop(0)
            else:  # No valid card to play
                permutation_possible = False
                break
        
        if not permutation_possible:
            break
    
    # increment values of permutation by 1
    for i in range(n):
        permutation[i] += 1
    if permutation_possible:
        print(*permutation)
    else:
        print(-1)
