for _ in range(int(input())):
    S = input()
    T = input()
    # if S not in T:
    #     print(S)
    #     print(2)
    #     continue
    # if T == "abc":
    #     print("".join(sorted(S, reverse=True)))
    #     # print(S)
    # else:
    #     print("".join(sorted(S)))
    #     # print(S)

    S = "".join(sorted(S))
    # if T in S:
    #     # Swap positions of the first b and first c

    if T == "abc" and "a" in S and "b" in S and "c" in S:
        # b = S.index("b")
        # c = S.index("c")
        # S = S[:b] + "c" + S[b+1:c] + "b" + S[c+1:]
        # Put the cs before bs
        # S = S.replace("c", ".")
        # S = S.replace("b", "c")
        # S = S.replace(".", "b")
        # S = S.replace(",", "b")

        # How to put cs before bs
        # The replace method fails because the count of bs and cs can be different

        b = S.index("b")
        c = S.rindex("c")
        temp = S[b:c+1]
        temp = "".join(sorted(temp, reverse=True))
        # print(temp)
        temp2 = S
        S = S[:b] + "".join(temp) 
        if c < len(temp2) - 1:
            S += temp2[c+1:]
        # S += S[c:]
        # print(2)


    print(S)
