for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    # b has n-1 elements
    # A good array is one where b[i] = a[i] & a[i+1]
    # So a[i] & a[i+1] & a[i+2] = b[i] & b[i+1]
    # Hence, a[0] & ... & a[n-1] = b[0] & b[1] & ... & b[n-2]
    # If no such a exists, print -1
    
    # If b = [1], 0001 is the element.
    # To get 0001, we need 0011 and 0101 or 0001 and 0011
    # If b = [2], 0010 is the element.
    # To get 0010, we need 0011 and 0110
    # If b = [3], 0011 is the element.
    # To get 0011, we need 0011 and 0111

    # Essentially, we need the same number or shift left add 1
    # the second number will just be complimentary to give the value of b


# Copilot Solution
# for _ in range(int(input())):
#     n = int(input())
#     b = list(map(int, input().split()))
    
#     a = [0] * n
#     a[0] = b[0]
#     a[n-1] = b[n-2]
    
#     for i in range(1, n-1):
#         a[i] = b[i-1] | b[i]
    
#     # Verify if the constructed array a satisfies the condition
#     valid = True
#     for i in range(n-1):
#         if a[i] & a[i+1] != b[i]:
#             valid = False
#             break
    
#     if valid:
#         print(" ".join(map(str, a)))
#     else:
#         print(-1)