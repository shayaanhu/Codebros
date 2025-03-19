for _ in range(int(input())):
    s = input()
    # if s == "EN" or s == "NE" or s == "ENE":
    #     print("NO")
    # else:
    #     print("YES")

    if s.count("N") == 1:
        print("NO")
    else:
        print("YES")


# N1 N2 E1
# N1 E2 N2
# E1 N1 N2
# E1 E1 N2
# N1 E2 E2
# E1 N1 E2
# N N N
# E E E
# E E E N (Chain of E's with a single N.)
# Single N is a problem.
