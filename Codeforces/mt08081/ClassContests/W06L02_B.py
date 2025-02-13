for _ in range(int(input())):
    # n is the total number of days
    # d is the duration of the visits
    # k is the number of jobs
    n,d,k = map(int, input().split())
    for i in range(k):
        # l is the start and r is the end of the job
        l, r = map(int, input().split())

#   For each test case, output two integers, the best starting days of Robin's brother and mother respectively. 
#   Both visits must fit between day 1 and n inclusive.