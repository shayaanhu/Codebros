for _ in range(int(input())):
    u, v = map(int, input().split())
    # print(-u, v)
    # The above doesn't work for cases where u and v are different

    # (xv + yu)(u+v) = (x+y)(uv)
    # xuv + xv^2 + yu^2 + yuv = xuv + yuv
    # xv^2 + yu^2 = 0
    # xv^2 = -yu^2
    # x/y = -u^2/v^2

    # # Start k from 1 and then keep going until u-1 and 1-v both are non-zero

    # k = 1
    # while True:
    #     if (u-1) * k != 0 and (v-1) * k != 0:
    #         break
    #     k += 1

    # print(k * (u-1), k * (v-1) + k)

    # Incorrect attempt above

    # It was simply x/y = -u^2/v^2

    print(-u*u, v*v)