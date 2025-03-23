for _ in range(int(input())):
    keys = input()
    s = input()


    time = 0
    for i in range(len(s)-1):
        if s[i] not in keys:
            print(0)
            break
        time += abs(keys.index(s[i]) - keys.index(s[i+1]))

    print(time)