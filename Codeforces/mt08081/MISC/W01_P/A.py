for _ in range(int(input())):
    s = input()
    # Method A: Use a set to store the characters.
    set_s = list(set(s))
    if len(set_s) == 1:
        print("NO")
    else:
        print("YES")
        # If the string has duplicate characters, print the string with the characters sorted.
        # Rearrange s so that its not the same as the original string.
        # print new_s
        if s[0] == set_s[0]:
            new_s = s[1:] + s[0]
        else:
            new_s = s[:-1] + s[0]
        print(new_s)