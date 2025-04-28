n = int(input())
s = input()

count_L = 0
count_O = 0

for i in range(n):
    if s[i] == 'L':
        count_L += 1
    elif s[i] == 'O':
        count_O += 1


# if count_L % 2 != 0 or count_O % 2 != 0 and count_L <= 1 and count_O <= 1:
#     print(2)
# else:
#     print(-1)

# simply count prefix and suffix of L and O
# and check if they are equal or not

prefix_L = 0
prefix_O = 0

# print(3)
for i in range(n):
    if s[i] == 'L':
        prefix_L += 1
    elif s[i] == 'O':
        prefix_O += 1

    k = i + 1
    if k == n:
        break
    suffix_L = count_L - prefix_L
    suffix_O = count_O - prefix_O
    if prefix_L != suffix_L and prefix_O != suffix_O:
        print(k)
        exit()
print(-1)