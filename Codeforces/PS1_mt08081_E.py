class Node:
    def __init__(self, value, depth=0):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth

    def insert(self, p, left_index, right_index, depthDict, depth=0):
        if left_index > right_index:
            return

        # Find the maximum value and its index in the current range
        maxIndex = max(range(left_index, right_index + 1), key=lambda i: p[i])
        maxValue = p[maxIndex]

        # Record the depth of the current maximum value
        depthDict[maxValue] = depth

        # Recursively create left and right subtrees
        if maxIndex > left_index:
            self.left = Node(p[maxIndex], depth + 1)
            self.left.insert(p, left_index, maxIndex - 1, depthDict, depth + 1)

        if maxIndex < right_index:
            self.right = Node(p[maxIndex], depth + 1)
            self.right.insert(p, maxIndex + 1, right_index, depthDict, depth + 1)

    def print_depth(self, depthDict, originalList):
        for num in originalList:
            print(depthDict[num], end=" ")
        print()

t = int(input())

for _ in range(t):
    n = int(input())
    aList = list(map(int, input().split()))


    # Pick the max of aList
    # Put that at the root of the tree
    # Find the max in the left and right subarrays
    # Repeat the process for the left and right subarrays until exhausted
    # Print the depth of each element in the array

    '''
    Inputs:
    3
    5
    3 5 2 1 4
    1
    1
    4
    4 3 1 2
    '''
    # print the depth of each element in the array

    depthDict = {}

    root = Node(max(aList), 0)
    root.insert(aList, 0, n - 1, depthDict)

    root.print_depth(depthDict, aList)



