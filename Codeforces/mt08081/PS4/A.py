# n! number of d digits
# e.g: if n = 2 and d = 6, then the num is 66.
# Write the digit d n! number of times.

# Output only the odd digits that divide the num

# Testing of all possible combinations.
# x = "8"*720
# print(int(x)%9 == 0)

flag = True

if flag:
    for _ in range(int(input())):
        n, d = map(int, input().split())

        arr = [1]

        if d == 1:
            if n > 2:
                arr.append(3)
                arr.append(7)
            if n > 5:
                arr.append(9)

        if d == 3:
            arr.append(3)
            if n > 2:
                arr.append(7)
                arr.append(9)

        # num will only be divisible by 5 if d is 5
        if d == 5:
            arr.append(5)
            if n > 2:
                arr.append(3)
                arr.append(7)
            if n > 5:
                arr.append(9)

        if d == 7:
            arr.append(7)
            if n > 2:
                arr.append(3)
            if n > 5:
                arr.append(9)
        
        if d == 9:
            arr.append(3)
            arr.append(9)
            if n > 2:
                arr.append(7)

        # Even Cases

        if d == 2:
            if n > 2:
                arr.append(3)
                arr.append(7)
            if n > 5:
                arr.append(9)

        if d == 4:
            if n > 2:
                arr.append(3)
                arr.append(7)
            if n > 5:
                arr.append(9)

        if d == 6:
            arr.append(3)
            if n > 2:
                arr.append(7)
                arr.append(9)
         
        if d == 8:
            if n > 2:
                arr.append(3)
                arr.append(7)
            if n > 5:
                arr.append(9)

        print(*sorted(arr))