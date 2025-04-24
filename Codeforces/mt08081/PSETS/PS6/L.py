s = input()
t = input()

# LCS problem
# Studied in Algos

n, m = len(s), len(t)

dp = []
for i in range(n+1):
    dp.append([0] * (m+1))

for i in range(1, n+1):
    si = s[i-1]
    dpi = dp[i]
    dpj = dp[i-1]
    for j in range(1, m+1):
        if si == t[j-1]:
            dpi[j] = dpj[j-1] + 1
        else:
            dpi[j] = max(dpj[j], dpi[j-1])

# print(dp[n][m])


# Now we can backtrack by starting from the end of the dp array
# And going to the start of the strings
i, j = n, m
lcs = []
while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        lcs.append(s[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(*reversed(lcs), sep='')