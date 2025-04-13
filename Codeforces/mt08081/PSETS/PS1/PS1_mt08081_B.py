
t = int(input())

for _ in range(t):
    numList = list(map(int, input().split()))
    games = 0
    if (numList[0] > numList[2] and numList[1] > numList[3]): # a1 > b1 and a2 > b2
        games += 2
    if (numList[1] > numList[2] and numList[0] > numList[3]): # a2 > b1 and a1 > b2
        games += 2
    if (numList[0] > numList[2] and numList[1] == numList[3]): # a1 > b1 and a2 = b2
        games += 2
    if (numList[0] == numList[2] and numList[1] > numList[3]): # a1 = b1 and a2 > b2
        games += 2
    if (numList[1] == numList[2] and numList[0] > numList[3]): # a2 = b1 and a1 > b2
        games += 2
    if (numList[1] > numList[2] and numList[0] == numList[3]): # a2 > b1 and a1 = b2
        games += 2
    
    # elif not(numList[0] < numList[2] and numList[1] < numList[3]) or (numList[1] < numList[2] and numList[0] < numList[3]):
    print(games)