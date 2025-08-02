# Infinity table

# We can go left and up. Whichever reaches the square is the guider.

# 1 (1 value, i = 1)
# 2 3 4 (3 values, i = 2)
# 5 6 7 8 9 (5 values, i = 3)
# 10 11 12 13 14 15 16 (7 values, i = 4)
# ...

# k is in any i-th layer
# Smallest value of i-th layer is sum of no of values in each layer till (i - 1)th layer + 1
# i will be equal to either row or column for that specific k
# How to find the other value (row/column)?
# Lets try to find minimum value of each layer

# 

for _ in range(int(input())):
    k = int(input())

    i = 1
    countValues = 1
    mini = 1

    found = False
    while not found:
        if k < mini + countValues:
            break

        i += 1
        mini += countValues
        countValues += 2

    # print(mini, i)

    # Now lets find the highest number in the row/layer.
    mini2 = mini + countValues
    maxi = mini2 - 1

    # print(mini2, maxi)

    # Now we find average of the layer which will be the center of layer (We can do this through median as well since all layers have odd values)
    avg = (maxi + mini)//2
    # print(avg)

    # if k <= avg:
    #     print("col =", i)
    # else:
    #     print("row =", i)

    # How to find the other component...
    # There should be one formula which probably does this for both cases
    # lets just run a loop lol to reach the end
    # I think I figured it out
    # i - (avg - k) for the first case
    # i + (avg - k) for the second case
    # Lets test this xD

    if k <= avg:
        val = i - (avg - k)
        print(val, i)
    else:
        val = i + (avg - k)
        print(i, val)
