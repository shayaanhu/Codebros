n, q = map(int, input().split())
s = input()

for query in range(q):
    # print()
    posA = s.find('a')
    posB = s.find('b')
    posC = s.find('c')

    if posA < posB and posB < posC:
        print(0)
    elif posA < posB and posB > posC:
        print(1)
    elif posB < posA and posA < posC:
        print(2)