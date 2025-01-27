import bisect

for _ in range(int(input())):
    n, m, q = map(int, input().split())
    mList = list(map(int, input().split()))
    qList = list(map(int, input().split()))
    # n is the number of cells in a one-dimensional array
    # m is the number of teachers
    # q is the number of queries of David who has to run from the teachers
    # mList is the location of all the teachers in the one-dimensional array
    # qList is the location of all the queries of David
    # David has to run from the teachers
    # David can run in both directions or stay in his spot
    # David can only run one cell at a time

    # print the minimum number of steps it takes for teachers to catch David

    # Sort the list of teachers
    mList.sort()
    
    for query in qList:
        # Find the position to insert the query in the sorted list of teachers
        pos = bisect.bisect_left(mList, query)

        # Calculate the minimum distance to the nearest teacher
        if pos == 0:
            min_steps = abs(mList[0] - query)
        elif pos == m:
            min_steps = abs(mList[-1] - query)
        else:
            min_steps = min(abs(mList[pos] - query), abs(mList[pos - 1] - query))
        
        # Consider the edges of the array
        min_steps = min(min_steps, query - 1, n - query)

        print(min_steps)