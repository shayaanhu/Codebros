# a is an array of n zeros
# 
# choose two  

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    # if all numbers are the same then we get 1 as the answer
    
    # lets try sorting b

    # b.sort(reverse=True)

    # # take the last occuring 1 and output its index + 1
    # # rfind? string tho
    # last_one_index = -1
    # for i in range(n-1, -1, -1):
    #     if b[i] == 1:
    #         last_one_index = i
    #         break

    # if b[0] == 0:
    #     print(0)
    # elif b[last_one_index] == 1 and b[0] == 1:
    #     print(1)
    # elif last_one_index == -1:
    #     print(n)
    # else:
    #     print(min(n, sum(b) - n + 1))

    # idkkkk running out of ideas...

    b.sort(reverse=True)

    nonZeross = sum(1 for x in b if x != 0)
    total = sum(b)

    print(min(nonZeross, total - n + 1))
