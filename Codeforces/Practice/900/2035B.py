# GPT
# For loops can also have an else statement
# It occurs if it completes normally, meaning did not break

t = int(input())
final = []

for _ in range(t):
    n = int(input())

    if n == 1:
        final.append(-1)
        continue

    num = "3" * n

    found = False
    while True:
        if int(num) % 33 == 0 and int(num) % 66 == 0:
            final.append(num)
            found = True
            break
        num = list(num)
        for i in range(n - 1, -1, -1):
            if num[i] == "3":
                num[i] = "6"
                break
            else:
                num[i] = "3"
        else:
            break
        num = "".join(num)

    if not found:
        final.append(-1)

for i in final:
    print(i)


