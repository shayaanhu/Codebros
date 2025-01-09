'''
[1, 2]

[3*3] = 4
[2*4] = 4

arr = [3, 3]

count = 0
while (arr[0] >= 2):
    arr[0] -= 2
    count += arr[1]
    # arr[1] -= 1
while (arr[1] >= 2):
    # arr[0] -= 1
    arr[1] -= 2
    count += arr[0]

[[split("0"*n, "")]*m]
"0000000"
"0", "0", ...
"0", "0", ...
.
.
.

[0, 0]
'''
arr = list(map(int, input().split()))

count = 0

multN = arr[0] // 2
multM = arr[1] // 2

count += (multN * arr[1]) + (multM * (arr[0] - 2 * multN))

# while (arr[0] >= 2):
#     arr[0] -= 2
#     count += arr[1]
#     # arr[1] -= 1
# while (arr[1] >= 2):
#     # arr[0] -= 1
#     arr[1] -= 2
#     count += arr[0]
    
    
print(count)