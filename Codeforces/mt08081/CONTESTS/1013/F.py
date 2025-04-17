# This is a traversal problem
# In hindsight it seems simple but its actually quite complicated
# This is because of the arm span of Igor

mod = 998244353

for _ in range(int(input())):
    n, m, d = map(int, input().split())

    mountain = []
    for i in range(n):
        mountain.append(input())

    mountain.reverse()
    # We can either trickle down from the top or go up from the bottom
    # print(mountain)

    # Check if there are holds in the rows

    holds = []
    possible = True
    for row in mountain:
        row_holds = []
        for i in range(m):
            if row[i] == 'X':
                row_holds.append(i)
        if not row_holds:
            possible = False
            break
        holds.append(row_holds)
    if not possible:
        print(0)
        continue

    limit = d*d - 1
    # print(holds)
    # print(limit)

    # We can store states of the climber
    # First store the states of the first row
    cur_states = {}
    for j in holds[0]:
        cur_states[j] = (cur_states.get(j, 0) + 1) % mod
    # print(cur_states)


    # But we might be able to use 2 holds in row 0
    for x in holds[0]:
        for y in holds[0]:
            if x != y and abs(x - y) <= d:
                cur_states[y] = (cur_states.get(y, 0) + 1) % mod

    # print(cur_states)
    
    # Now we can go through the rest of the rows
    for i in range(1, n):
        new_states = {}
        # for j in holds[i]:
        #     for k in cur_states:
        #         if abs(j - k) <= d:
        #             new_states[j] = (new_states.get(j, 0) + cur_states[k]) % mod
        # cur_states = new_states
        # single hold
        # for prev in cur_states:
        #     for j in holds[i]:
        #         if abs(j - prev) <= d:
        #             new_states[j] = (new_states.get(j, 0) + cur_states[prev]) % mod
        # # Solve for 2 holds in the same row
        # for x in holds[i]:
        #     for y in holds[i]:
        #         if x != y and abs(x - y) <= d:
        #             new_states[y] = (new_states.get(y, 0) + cur_states[x]) % mod
        # cur_states = new_states

        for prev_col, ways in cur_states.items():
            # Sngle hold
            for col in holds[i]:
                if (prev_col - col)**2 <= limit:
                    new_states[col] = (new_states.get(col, 0) + ways) % mod
            # Two holds in a row
            for col in holds[i]:
                if (prev_col - col)**2 <= limit:
                    for col2 in holds[i]:
                        if col != col2 and abs(col - col2) <= d:
                            new_states[col2] = (new_states.get(col2, 0) + ways) % mod
        cur_states = new_states
        # print(new_states)
    # print(cur_states)

    ans = sum(cur_states.values()) % mod
    print(ans)