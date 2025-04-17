class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


# Input
n, q = map(int, input().split())
a = list(map(int, input().split()))

# Initialize Fenwick Tree
fenwick = FenwickTree(n)

# Build the Fenwick Tree with the initial array
for i in range(n):
    fenwick.update(i + 1, a[i])

# Process queries
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # Query type 1: Update value at index k to u
        k, u = query[1], query[2]
        current_value = fenwick.range_sum(k, k)
        fenwick.update(k, u - current_value)
    elif query[0] == 2:
        # Query type 2: Find the sum from a to b
        a, b = query[1], query[2]
        print(fenwick.range_sum(a, b))