# s = input().split("+")

# sorted_s = sorted(s)

# for i in range(len(sorted_s)-1):
#     if (i == len(sorted_s)):
#         break
#     print(sorted_s[i], end= "+")

# print(sorted_s[-1])

s = input().split("+")
print("+".join(sorted(s)))