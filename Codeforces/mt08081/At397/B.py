s = input()

i = 0      
cnt = 0    
res = 0    

while i < len(s):
    expected = 'i' if cnt % 2 == 0 else 'o'
    if s[i] == expected:
        
        
        cnt += 1
        i += 1
    else:
        res += 1
        cnt += 1

if cnt % 2 == 1:
    res += 1

print(res)
