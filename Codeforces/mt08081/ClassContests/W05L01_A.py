# for _ in range(int(input())):
#     n = int(input())
#     x = n
#     for i in range(n):
#         # check if n & n-1 & n-2 ... k = 0
#         # output k
#         x = x & (n - i)
#         # print('x:', x)
#         if (x == 0):
#             print(n - i)
#             break

import math

for _ in range(int(input())):
    n = int(input())
    # If n is 0100, then 0011 is the answer
    # If n is 0010, then 0001 is the answer
    # If n is 1000, then 0111 is the answer
    # so n is 1 less than n for such cases.
    # If n is 0001, then 0000 is the answer
    # If n is 0011, then 0001 is the answer (cause 0010 makes the value of 3 into 2 after and)
    # If n is 0101, then 0011 is the answer 
    # This is because 0100 makes 5 into 4 and 4 has 3 as the answer
    # So the answer is 1 less than the closest power of 2 under n
    k = int(math.log2(n))
    print(2**k-1)