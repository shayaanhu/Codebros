N = int(input())
S = input()
T = input()

counti = 0
for i in range(N):
    if S[i] != T[i]:
        counti += 1
        
print(counti)