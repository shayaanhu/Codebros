for _ in range(int(input())):
    s = input()
    if len(s) % 2 != 0:
        print("NO")
        continue

    half = len(s) // 2
    if s[:half] == s[half:]:
        print("YES")
    else:
        print("NO")