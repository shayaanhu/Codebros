# Updated hack test-case generator for Problem D with reduced n (and m) to decrease file size

t = 1
n = 65500     # Reduced n to cut down output file size
m = 100000    # Adjusted m so that m <= 2*n and we can keep the same logic

# Provided snippet centers (16 numbers)
centers_first = [
    88772, -92782, -175870, -113923,
    -175246, -93210, -30889, 170881,
    13431, -60001, 72301, -75125,
    -46870, 137447, 39738, -157216
]

# Fill the rest of the centers with 0 to make a total of n centers
remaining_centers_count = n - len(centers_first)
centers = centers_first + [0] * remaining_centers_count

# We want sum of radii = m.
# Let x = m - n => number of circles that have radius 2.
# Let the remaining (n - x) circles have radius 1.
#
# Here, m = 100000 and n = 50000, so x = 50000.
# This means all 50000 circles have radius 2 (and zero have radius 1).
x = m - n
radii = [2] * x + [1] * (n - x)

# Verification
assert len(radii) == n, "Radii array must have length n"
assert sum(radii) == m, "Sum of radii must equal m"

# Write the test case to a file
with open("test_case.txt", "w") as f:
    f.write(str(t) + "\n")        # Number of test cases
    f.write(f"{n} {m}\n")         # n and m
    f.write(" ".join(map(str, centers)) + "\n")
    f.write(" ".join(map(str, radii)) + "\n")

print("Test file 'test_case.txt' generated with reduced n = 50000 and m = 100000.")