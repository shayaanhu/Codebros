# We want to find the min value inside the array from a to b

n, q = map(int, input().split())
a = list(map(int, input().split()))

# This requires a sparse table
# Lets build a sparse table
# Build the sparse table
log = [0] * (n + 1)
for i in range(2, n + 1):
    log[i] = log[i // 2] + 1

# print(log)

k = log[n] + 1  # Maximum power of 2 needed
sparse_table = [[0] * n for _ in range(k)]

# Initialize the first row of the sparse table with the array values
for i in range(n):
    sparse_table[0][i] = a[i]

# Fill the sparse table
for i in range(1, k):
    for j in range(n - (1 << i) + 1):
        sparse_table[i][j] = min(sparse_table[i - 1][j], sparse_table[i - 1][j + (1 << (i - 1))])

# print(sparse_table)

def query(l, r):
    # l and r are inclusive
    # If l and r are exclusive, then length = r - l - 1
    length = r - l + 1
    j = log[length]
    return min(sparse_table[j][l], sparse_table[j][r - (1 << j) + 1])

for i in range(q):
    a, b = map(int, input().split())
    print(query(a - 1, b - 1))

