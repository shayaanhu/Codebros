n, m, k = map(int, input().split())
lst = []
for i in range(m+1):
    lst.append(int(input()))

fedor = lst.pop()
# print(fedor)

# fedor can be a friend if 
# if there are at most k differences in bits

count = 0
for i in lst:
    # Find the differing bits by using xor.
    # Differing bits give 1 after xor
    val = bin(fedor ^ i).count('1')
    if val <= k:
        count += 1


print(count)