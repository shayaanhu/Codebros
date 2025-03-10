for _ in range(int(input())):
    n = int(input())
    l, r = 1, 1
    for gate in range(n):
        signP, plus, signM, mult = input().split()
        plus = int(plus)
        mult = int(mult)
        # ignore signP and signM as they are irrelevant

        # Option A: l + plus, r * (mult-1)
        # Option B: l * (mult-1), r + plus
        # Choose the option that gives the maximum value
        # If both options give the same value, choose the first option
        # optionA = l + plus, r * (mult-1)
        # optionB = l * (mult-1), r + plus
        # l, r = max(optionA, optionB)
        if r >= l:
            l = l + plus
            r = r * mult
        else:
            l = l * mult
            r = r + plus
    print(max(l, r))