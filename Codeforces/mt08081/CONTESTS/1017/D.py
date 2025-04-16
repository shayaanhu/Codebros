for _ in range(int(input())):
    p = input()
    s = input()

    # We can use two pointers here?
    # Check if there are 1 or 2 characters which are the same?
    # i, j = 0, 0
    # while i < len(p) and j < len(s):
    #     if j + 1 < len(s) and s[j] == s[j + 1] and p[i] == s[j]:
    #         j += 2
    #         i += 1
    #     elif p[i] == s[j]:
    #         i += 1
    #         j += 1
    #     else:
    #         break
    
    # if i == len(p) or j == len(s):
    #     print("YES")
    # else:
    #     print("NO")

    # The above approach fails for some reason but it seems perfect

    # Maintain a list with the counts of consecutive L and Rs
    # and then check if the counts are equal or not


    p_runs = []
    s_runs = []

    # Counting all the p-chars
    if p:
        curr_char = p[0]
        curr_count = 1
        for i in range(1, len(p)):
            if p[i] == curr_char:
                curr_count += 1
            else:
                p_runs.append((curr_char, curr_count))
                curr_char = p[i]
                curr_count = 1
        p_runs.append((curr_char, curr_count))
    # print(p_runs)

    # Counting all the s-chars
    if s:
        curr_char = s[0]
        curr_count = 1
        for i in range(1, len(s)):
            if s[i] == curr_char:
                curr_count += 1
            else:
                s_runs.append((curr_char, curr_count))
                curr_char = s[i]
                curr_count = 1
        s_runs.append((curr_char, curr_count))
    # print(s_runs)
    
    valid = True
    # If different sets exist, then its false
    if len(p_runs) != len(s_runs):
        valid = False
    else:
        for i in range(len(p_runs)):
            p_char, p_count = p_runs[i]
            s_char, s_count = s_runs[i]
            
            if p_char != s_char:
                valid = False
                break
            
            # The count of the s_char has to be between count and 2*count 
            if s_count < p_count or s_count > 2*p_count:
                valid = False
                break
    
    print("YES" if valid else "NO")

