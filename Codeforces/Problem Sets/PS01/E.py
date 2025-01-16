t = int(input())

class Node:
    def __init__(self, value, depth=0):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth

    def insert(self, p, left_index, right_index, depthDict, depth=0):
        if left_index > right_index:
            return

        maxValue = max(p[left_index:right_index + 1])
        maxIndex = p.index(maxValue, left_index, right_index + 1)

        depthDict[maxValue] = depth

        if maxIndex > left_index:  
            self.left = Node(p[left_index:maxIndex][0], depth)
            self.left.insert(p, left_index, maxIndex - 1, depthDict, depth + 1)

        if maxIndex < right_index:
            self.right = Node(p[maxIndex + 1:right_index + 1][0], depth)
            self.right.insert(p, maxIndex + 1, right_index, depthDict, depth + 1)

final = []
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))

    rootValue = max(permutation)
    maxIndex = permutation.index(rootValue)

    depthDict = {}
    depthDict[rootValue] = 0

    root = Node(rootValue)
    root.insert(permutation, 0, len(permutation) - 1, depthDict)
    
    depthList = []
    for i in permutation:
        depthList.append(depthDict[i])

    final.append(depthList)

for i in final:
    print(*i)