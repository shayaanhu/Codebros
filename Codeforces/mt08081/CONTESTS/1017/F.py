# for _ in range(int(input())):
#     n, m, k = map(int, input().split())

#     grid = []
#     # We can fill the grid diagonally with the numbers from 1 to k
#     # This can allow for the numbers to be unique and under k
#     for i in range(n):
#         row = [(j+i) % k + 1 for j in range(m)]
#         grid.append(row)

#     for row in grid:
#         print(*row)

# for _ in range(int(input())):
#     n, m, k = map(int, input().split())
    
#     # Each number needs to appear exactly (n*m)/k times
#     # The pattern (i+j)%k+1 naturally ensures equal distribution when n*m is divisible by k
#     grid = []
#     for i in range(n):
#         row = [(i + j) % k + 1 for j in range(m)]
#         grid.append(row)
    
#     for row in grid:
#         print(*row)

for _ in range(int(input())):
    n = int(input())