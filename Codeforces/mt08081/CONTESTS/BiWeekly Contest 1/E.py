# You could either swap the right most with the largest
# or the left most with the smallest to get the largest value of a_n - a_1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue
    
    minA = min(a)
    maxA = max(a)
    # print(maxA - minA)

    # print(max(maxA - a[0], a[-1] - minA))
    # print()

    hmmm = max(a[1:]) - a[0]
    hmmmmm = a[-1] - min(a[:-1])
    # print(max(hmmm, hmmmmm))

    # 2 1 8 1 case failing
    # This should be 8 1 2 1 after rotation
    # we can rotate the whole array...

    # hmmmmmm = max(a) - min(a)
    hmmmmmm = 0
    for i in range(n-1):
        hmmmmmm = max(hmmmmmm, a[i] - a[i+1])
    # print(hmmmmmm)

    print(max(hmmm, hmmmmm, hmmmmmm))
