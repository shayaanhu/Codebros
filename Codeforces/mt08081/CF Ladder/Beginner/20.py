for _ in range(int(input())):
    # s = list(input())
    # s.sort(reverse=True)
    # print(s.pop(), "".join(s))
    s = input()
    mn = min(s)
    # print(mn)
    s = s.replace(mn, "", 1)
    print(mn, s)