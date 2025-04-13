# import random

# # Total number of test cases: 10^4
# t = 10**4

# # Open a file for writing the test input (or you can just print to stdout)
# with open("hack_input.txt", "w") as f:
#     f.write(str(t) + "\n")
#     for i in range(t):
#         # Alternate between a square case and a non-square case.
#         # For a square case (expected output "YES"), we use maximum values.
#         if i % 2 == 0:
#             # This always gives l = r = d = u = 10
#             f.write("10 10 10 10\n")
#         else:
#             # This is a non-square case, for example "1 2 3 4" (expected "NO")
#             f.write("10 9 8 10\n")


n = 200000

# Write the above test case to a file
with open("/mt08081/1009/hack_input2.txt", "w") as f:
    f.write("999\n")
    f.write(str(n) + "\n")
    # f.write(" ".join(["999"] * n) + "\n")
    # alternate with 999 and 998
    for i in range(n):
        f.write("999 " if i % 2 == 0 else "998 ")
