inputList = input().split()
n = int(inputList[0])
k = int(inputList[1])

scores = input().split()
scores = list(map(int, scores))

tally = 0
for i in scores:
    if i > 0 and i >= scores[k - 1]:
        tally += 1

print(tally)
