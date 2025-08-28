n = int(input())

steps = 0
i = 0

choices = [5, 4, 3, 2, 1]

while n != 0:
    modu = n % choices[i]
    mult = n // choices[i]
    # subtract mult*choices[i] from n
    n -= mult * choices[i]
    # print(n)
    steps += mult
    # i += 1
    if modu != 0:
        i += 1

print(steps)
