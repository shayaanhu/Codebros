for _ in range(int(input())):
    n, m, rb, cb, rd, cd = map(int, input().split())

    r = rd - rb if rd - rb >= 0 else 2*n - rb - rd
    c = cd - cb if cd - cb >= 0 else 2*m - cb - cd

    print(r if r < c else c)
 