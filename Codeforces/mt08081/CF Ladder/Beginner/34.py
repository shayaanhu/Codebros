# U --- D
# L --- L
# R --- R

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    x = ""
    for i in s:
        x += i if i != 'U' and i != 'D' else 'D' if i == 'U' else 'U'

    print(x)