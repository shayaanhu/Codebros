
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    b = ''.join(map(str, b))
    # print(b)
    if b.find('101') == -1:
        print('YES')
    else:
        print('NO')
# n = int(input())
# b = list(map(int, input().split()))
# # b contains 0,1
# # b is from index 2 to n-1
# # If b[i] = 1, then array a contains elements equal to its neighbours.
# # If b[i] = 0, then array a contains elements not equal to its neighbours.
# # e.g if b = [0, 1]
# # a = [1, 2, 2, 2]
# # If array a exists then print YES, else NO

# # b = [0, 1, 0, 1, 1, 0, 0, 1]
# # a = [1, 2, 2, 2, 1, 1] (Invalid)

# # convert b to string
# b = ''.join(map(str, b))
# if b.find('101'):
#     print('YES')
# else:
#     print('NO')