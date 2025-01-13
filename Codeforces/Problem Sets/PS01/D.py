n = int(input())
final = []

for t in range(n):
    s1 = input()
    s2 = input()

    i = 0
    j = 0
    valid = True

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1  
        elif j == 0 or s2[j] != s2[j - 1]:  
            valid = False
            break
        j += 1

    if i < len(s1):
        valid = False

    while j < len(s2):
        if s2[j] != s2[j - 1]:
            valid = False
            break
        j += 1

    if valid:
        final.append("YES")
    else:
        final.append("NO")

for result in final:
    print(result)
