
# If a union of a component fails then there is a cycle in the component.


class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        self.parent[pb] = pa
        return True

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

dsu = DSU(N)
to_delete = 0
for u, v in edges:
    if not dsu.union(u, v):
        to_delete += 1

print(to_delete)