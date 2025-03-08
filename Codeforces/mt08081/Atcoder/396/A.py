n = int(input())

# The input is in the form of A1 A2 A3 ... An (in a single line)
# Form a string "A1A2A3...An"

# Form the string
s = "".join(input().split())

# if 3 characters in a line are similar print YES else NO

# Check if there are 3 similar characters in the string
for i in range(len(s) - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        print("Yes")
        break
else:
    print("No")
