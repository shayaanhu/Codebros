for _ in range(int(input())):
    s = input()
    a, b, ab, ba = map(int, input().split())

    # size = len(s)
    maxi = max(ab, ba)
    ab_count = 0
    ba_count = 0
    if maxi == 0:
        pass
    elif maxi == ab:
        ab_count = s.count('AB')
        # size -= ab_count * 2
        s = s.replace('AB', '', ab)
        # Now count the alternate
        ba_count = s.count('BA')
        # size -= ba_count * 2
        s = s.replace('BA', '', ba)
    else:
        ba_count = s.count('BA')
        # size -= ba_count * 2
        s = s.replace('BA', '', ba)
        # Now count the alternate
        ab_count = s.count('AB')
        # size -= ab_count * 2
        s = s.replace('AB', '', ab)

    # Now count a and b
    count_a = s.count('A')
    count_b = s.count('B')

    if count_a <= a and count_b <= b and ab_count <= ab and ba_count <= ba:
        print("YES")
    else:
        print("NO")


