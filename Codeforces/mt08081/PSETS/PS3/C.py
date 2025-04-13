n = int(input())
angles = []
for _ in range(n):
    # n number of rotations
    # n lines contain one int a_i which is 0 to 180
    # 0 <= a_i <= 180
    # 1 <= n <= 15
    # Rotations can happen clockwise or counter clockwise
    # If the value on the lock is 0 after all the rotations, the lock opens
    # Find if the lock can be opened
    # If the lock can be opened, print YES, else print NO
    

    angles.append(int(input()))


# Since n is small, we can use brute force
# We can try all possible combinations of rotations
# There are 2^n possible combinations
# For each combination, we can calculate the sum of the angles depending on the combination
# If the sum is divisible by 360, the lock can be opened
# Else, the lock cannot be opened

# n = 3
# i = 000 (First iteration)
# j = 00 (First j iteration)
# Subtract sum in this case
# j = 01 (Second j iteration)
# Subtract sum in this case
# Addition can happen when we have a single 1 in the and of i and 1 << j
for i in range(1 << n):
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += angles[j]
        else:
            sum -= angles[j]
    if sum % 360 == 0:
        print("YES")
        break
else:
    print("NO")