for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    if s < s[::-1]:
        print('YES')
        continue

    if k == 0 or n == 1:
        print('YES') if s[-1] > s[0] else print('NO')
        continue
    if s.count(s[0]) == n:
        print('NO')
        continue
    # find the largest char in s
    max_char = max(s)
    # print(max_char)
    # if s[-1] == max_char:
    #     print('YES')
    # else:
    #     print('NO')

    if k >= 2:
        print('YES')
        continue

    # The only weird case is if k == 1 and s is not universal
    # We have to find a swap such that the reverse is lexicographically larger
    # than the original string
    
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if s[i] == max_char:
    #             if s[j] < s[i]:
    #                 print('YES')
    #                 break
    #         else:
    #             if s[j] > s[i]:
    #                 print('YES')
    #                 break
    #     else:
    #         continue
    #     break
    # else:
    #     print('NO')

    found = False
    s_list = list(s)
    for i in range(n):
        for j in range(i + 1, n):
            s_list[i], s_list[j] = s_list[j], s_list[i]
            new_s = "".join(s_list)
            if new_s < new_s[::-1]:
                found = True
                break
            s_list[i], s_list[j] = s_list[j], s_list[i]
        if found:
            break
    print("YES" if found else "NO")
