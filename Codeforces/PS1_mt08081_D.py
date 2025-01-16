n = int(input())

for _ in range(n):
    s = input()
    t = input()

    check = True
    t_index = 0

    # i = "l" (2nd or more occurence of "l" in s consecutively)
    # t = "o"
    # Should print NO

    # i = "s"
    # t = ""
    # Should print NO

    # if (set(s) != set(t)):
    #     print("NO")
    #     continue

    for i in range(len(s)):
        t_len = len(t)
        if (t_index >= t_len):
            check = False
            break
        if (s[i] != t[t_index]):
            check = False
            break
        # if (t!= "" and i != t[0]):
        #     check = False
        #     break
        # print("S:", s, end = " ")
        # print("I:", s[i])
        # count = s.count(s[i])
        while (t_index < t_len and s[i] == t[t_index]):
            # print("T:", t)
            # t_loc = t.rfind(s[i])
            # t = t[1:] # Previous Approach
            t_index += 1
            if (i != len(s) - 1 and s[i] == s[i + 1]):
                break

    if (check and t_index == len(t)):
        print("YES")
    else:
        print("NO")