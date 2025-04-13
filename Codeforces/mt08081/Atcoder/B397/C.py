from collections import Counter

n = int(input())

A = list(map(int, input().split()))
# val = A.pop(0)
if n == 2:
    print(2)
    exit()
    
B = Counter([A[0]])
C = Counter(A[1:])

# C_count = n - 1
# maxi = n - 1


maxi = len(B) + len(C)
for i in range(1, n-1):
    x = A[i]
    B[x] += 1
    C[x] -= 1
    if C[x] == 0:
        del C[x]
        
    maxi = max(maxi, len(B) + len(C))
    
print(maxi)
    
    
