arr = [list(map(int, input().split())) for _ in range(5)]

# list comprehension
# positions = [(i, row.index(target)) for i, row in enumerate(matrix) if target in row]

for i, row in enumerate(arr):
    if 1 in row:
        position = (i, row.index(1))
        break
        
a = abs(position[0] - 2) + abs(position[1]-2)

print(a)