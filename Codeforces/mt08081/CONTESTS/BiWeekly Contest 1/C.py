# k bottles of soft drink
# n friends
# l mililiters in each drink (k*l = total volume)
# c limes
# d slices per lime (c*d = total slices)
# p grams of salt
# each friend needs nl militers of the drink, one slice of lime and np grams of salt


n, k, l, c, d, p, nl, np = map(int, input().split())

totalVol = k * l
totalSlices = c * d
totalSalt = p

print(min(totalVol // (n * nl), totalSlices // n, totalSalt // (n * np)))
