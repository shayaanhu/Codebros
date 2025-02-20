for _ in range(int(input())):
    n = int(input()) # length of array and string
    a = list(map(int, input().split())) # int array
    s = input() # Binary string
    q = int(input()) # number of queries
    results = []
    for query in range(q):
        # each query will contain two types
        # if the tp is 1, then the parameters ahead will be l and r
        # if the tp is 2, then the parameter ahead will be g
        # Each line contains tp and then g or (l, r) depending on the type
        data = list(map(int, input().split()))
        tp = data[0]
        if tp == 1:
            l, r = data[1], data[2]
            # negate all characters from l to r in s_i
            for i in range(l-1, r):
                if s[i] == '0':
                    s = s[:i] + '1' + s[i+1:]
                else:
                    s = s[:i] + '0' + s[i+1:]
        else:
            g = data[1]
            result = 0
            for i in range(n):
                if s[i] == g:
                    result ^= a[i]
            # print(result)
            results.append(result)
    print(*results)
    
        # Outputs will only happen in type 2 queries
        # if type 1, then negate all characters from l to r in s_i
        # If type 2, calculate bitwise xor of the numbers a_i for all indices i such that s_i = g.
        # Note that the empty set of numbers is 0.
        