# s - n - 1

# n is high (sum of all nums in arr)
# s is len of arr
# mid is (s + 1) // 2

# 0 0 0 0 .... median .... highest number
# median to highest number == n
# n//2 - 1 numbers are set to 0 and n // 2 + 1 are all included in the sum
# Hence, we know that s = n // 2 + 1
# Since we want median to be maximum, we can partition s into equal parts
# The value of this part should be as high as possible and therefore is equal to median
# s - median is divided into the partitioned parts respectively. 


for _ in range(int(input())):
    n, s = map(int, input().split())
    # x = s - n + 1
    # if x < 0:
    #     print(0)
    # else:
    #     print(x)

    nums_after_median_inclusive = n // 2 + 1

    print(s // nums_after_median_inclusive)

    # if x < mid:
    #     print(0)
    # else:
    #     print(x - mid + 1)
    #     # print(x - mid + 1)

    
