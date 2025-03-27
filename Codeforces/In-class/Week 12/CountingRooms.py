from collections import deque

n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(input()))

visited = []
for i in range(n):
    visited.append([False] * m)

def bfs(i, j):
    q = deque()
    # append the position i,j into the deque
    q.append((i, j))
    # Make visited true cause we are at that point
    visited[i][j] = True
    # While the deque is not empty
    while q:
        # Pop the visited node (we are standing on it)
        x, y = q.popleft()
        # Four directions for movement (down, up, left, right)
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            # nx, ny are the new positions after movement
            nx, ny = x + dx, y + dy
            # if the new positions are within the grid then they can be accessed
            if 0 <= nx < n and 0 <= ny < m:
                # if the new positions are not visited and the position is a floor
                if not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))

rooms = 0
for i in range(n):
    for j in range(m):
        # visit all positions if a . is found and not visited and increment rooms
        if grid[i][j] == '.' and not visited[i][j]:
            bfs(i, j)
            rooms += 1

print(rooms)