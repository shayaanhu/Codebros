num = int(input())

x = 0

for i in range(num):
    str = input()
    for i in str:
        if i == "+":
            x += 1
            break
        elif i == "-":
            x -= 1
            break

print(x)

