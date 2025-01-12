num = int(input())
 
matrix = []
 
for i in range(num):
    row = map(int, input().split())
    matrix.append(row)
 
# transpose = [list(row) for row in zip(*matrix)]
 
tally = 0
for i in matrix:
    if sum(i) > 1:
        tally += 1
    
print(tally)