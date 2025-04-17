from collections import deque

# Use bfs to simulate graph traversal
# I guess we can check all possible paths from the start to the end
# If G and B in the same path, then it is impossible
# If G is not reachable, then it is impossible
# Otherwise, it is possible

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    
    possible = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == '.':
                            grid[ni][nj] = '#'  
                        elif grid[ni][nj] == 'G':
                            possible = False
    if not possible:
        print("No")
        continue

    visited = [[False]*m for _ in range(n)]
    q = deque()
    if grid[n-1][m-1] != '#':
        q.append((n-1, m-1))
        visited[n-1][m-1] = True
        
    while q:
        i, j = q.popleft()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] != '#':
                visited[ni][nj] = True
                q.append((ni, nj))
                
    valid = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G' and not visited[i][j]:
                valid = False
            if grid[i][j] == 'B' and visited[i][j]:
                valid = False
    print("Yes" if valid else "No")