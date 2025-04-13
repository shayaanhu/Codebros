# Incorrect Sol (Deepseek/Copilot)

from collections import deque

def bfs(graph, start, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        s1 = int(data[index + 1])
        s2 = int(data[index + 2])
        index += 3
        
        m1 = int(data[index])
        index += 1
        graph1 = [[] for _ in range(n + 1)]
        for _ in range(m1):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            graph1[a].append(b)
            graph1[b].append(a)
        
        m2 = int(data[index])
        index += 1
        graph2 = [[] for _ in range(n + 1)]
        for _ in range(m2):
            c = int(data[index])
            d = int(data[index + 1])
            index += 2
            graph2[c].append(d)
            graph2[d].append(c)
        
        # Perform BFS from s1 in graph1 and s2 in graph2
        distances1 = bfs(graph1, s1, n)
        distances2 = bfs(graph2, s2, n)
        
        # Calculate the minimum possible total cost
        min_cost = float('inf')
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distances1[i] != -1 and distances2[j] != -1:
                    min_cost = min(min_cost, abs(i - j))
        
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()