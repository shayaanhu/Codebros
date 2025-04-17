def unsetKthBit(n, k):
    return n & ~(1 << (k - 1))

for _ in range(int(input())):
    x = int(input())
    # Find y
    # y is strictly less than x
    # x, y, x^y is a non-degenerate triangle
    # Output -1 if no such y exists

    # -1 only happens in these cases
    if x <= 4:
        print(-1)
        continue
    # Flip the second bit from the left
    # 1010 -> 1110

    # If x is a power of 2, then -1 is the answer
    if (x & (x-1)) == 0:
        print(-1)
        continue
    # Otherwise, find the second 1 from the left and flip it
    # 1010 -> 1000

    # If x+1 is a power of 2, then -1 is the answer
    if (x & (x+1)) == 0:
        print(-1)
        continue

    # Find the position of the second 1 from the left
    # bin_str = bin(x)[2:]            
    # idx2 = bin_str.find('1', 1)     
    # length = len(bin_str)
    # k = length - idx2             
    # y = unsetKthBit(x, k)  
    # print(y)

    # if x is even, y can be x-1
    if x % 2 == 0:
        print(x-1)
        continue

    # print(x-2)
    # Lol lets just go from x // 2 up until val & x == 0 so that xor is maximized
    y = x // 2
    while y & x != 0:
        y += 1
    print(y)

# print(11^7)