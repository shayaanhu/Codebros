# ()(())

# print(dir(str))

for _ in range(int(input())):
    n = int(input())
    # forming parantheses

    # v = []

    for i in range(n):
        s = "(" * (n) + ")" * (n-1)
        # s[i] = ')'
        s = s[:i+1] + ')' + s[i+1:]
        print(s)
        # v.append(s)

        