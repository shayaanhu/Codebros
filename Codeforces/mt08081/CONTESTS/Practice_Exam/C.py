for _ in range(int(input())):
    n = input()

    if "0" not in n:
        print("cyan")
        continue

    if n.count("0") == len(n):
        print("red")
        continue

    n = n.replace("0", "", 1)


    # Lets form permutations of n-1 digits and check if they are
    # divisible by 6 or not

    # If a number is divisible by 6, it must be divisible by 2 and 3

    div2 = False
    div3 = False

    # print(n)
    val = 0
    for i in n:
        if int(i) % 2 == 0:
            div2 = True
            # break
        val += int(i)

    # print(val)
    if val % 3 == 0:
        div3 = True

    if div2 and div3:
        print("red")
    else:
        print("cyan") 