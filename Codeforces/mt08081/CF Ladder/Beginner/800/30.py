# Casimir's String Solitaire

from collections import Counter

for _ in range(int(input())):
    s = input()
    cnt = Counter(s)
    # print(cnt)
    print('YES' if cnt['A'] + cnt['C'] == cnt['B'] else 'NO')