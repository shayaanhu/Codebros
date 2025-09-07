# 800

# Simple Design

def func(x):
    x2 = str(x)
    num = 0
    for i in x2:
        num += int(i)
    return num

for _ in range(int(input())):
    x, k = map(int, input().split())

    # to find a y which is k-beautiful and y <= x

    # if x <= k:
    #    print(k)
    #    continue

    # x2 = str(x)
    # num = 0
    # for i in x2:
    #     num += int(i)
    # y = (num % k) + x
    # print(y)

    # print(1 % 10)
    # print("yes")


    while True:
        if func(x) % k == 0:
            print(x)
            break
        x += 1
