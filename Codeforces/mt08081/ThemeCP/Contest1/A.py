# 800 rated

# Prime Deletion

for _ in range(int(input())):
    n = int(input())
    s = str(n)

    # Check if 3 comes before 1 in sequence
    # If yes, then print 31
    # ELSE print 13

    if s.index('3') < s.index('1'):
        print(31)
    else:
        print(13)
