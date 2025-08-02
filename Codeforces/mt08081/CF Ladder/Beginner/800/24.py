for _ in range(int(input())):
    n, H = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    # prefix sum of a
    # prefix = [0] * n
    # prefix[0] = a[0]
    # for i in range(1, n):
    #     prefix[i] = prefix[i - 1] + a[i]

    # for i in range(len(prefix)):
    #     if prefix[i] >= H:
    #         # print(prefix.index(i) + 1)
    #         print(i + 1)
    #         break

    # mx = a[0]
    # mx2 = a[1]
    # pair = mx + mx2
    # turns = (H // pair) * 2
    # # turns = 0
    # rem = H % pair

    # if rem == 0:
    #     print(turns)
    # elif rem <= mx:
    #     print(turns + 1)
    # else:
    #     print(turns + 2)

    # Approach number 2
    mx = a[0]
    mx2 = a[1]
    calc = H % (mx + mx2)
    calc2 = 2 * (-(-H//(mx+mx2)))
    print(calc2) if calc <= 0 else print(calc2 + 1)

    # while H > 0:
    #     if turns % 2 == 0:
    #         H -= mx
    #     else:
    #         H -= mx2
    #     turns += 1
    # print(turns)