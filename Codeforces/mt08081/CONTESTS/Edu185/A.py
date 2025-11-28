# n x n grid
# calculate highest cost which is equal to cell + 4-neighbour cells

# [1 2 3]
# [4 5 6]
# [7 8 9]

# cost of cell (1, 1) = 1 + 2 + 4 = 7

# 1 < t < 100
# 1 < n < 100
# the values are rather small... hence we should be able to brute force this

for _ in range(int(input())):
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    curr = 1
    for i in range(n):
        for j in range(n):
            grid[i][j] = curr
            curr += 1
    
    max_cost = 0
    
    for i in range(n):
        for j in range(n):
            cost = grid[i][j]
            # up
            if i > 0:
                cost += grid[i-1][j]
            # down
            if i < n - 1:
                cost += grid[i+1][j]
            # left
            if j > 0:
                cost += grid[i][j-1]
            # right
            if j < n - 1:
                cost += grid[i][j+1]
                
            max_cost = max(max_cost, cost)
    
    print(max_cost)
