
# * is no current
# < move one to the left
# > move one to the right

# The person ends their journey when they reach the start/end of the string.
# They can start from any position in the string.

for _ in range(int(input())):
    s = input()
    n = len(s)

    # # Just keeps rowing infinitely xD
    # countStar = s.count('*')
    # if countStar == n:
    #     if n > 1:
    #         print(-1)
    #         continue
    #     else:
    #         print(1)
    #         continue

    # use find and rfind to find first and last < or >
    # firstLeft = s.find('<')
    # lastRight = s.rfind('>')

    # if firstLeft != -1 and lastRight != -1 and lastRight < firstLeft:
    #     print(-1)
    #     continue

    # Check for inf
    # find a > (*) < pattern where there can be any number of * in between

    # i = 0
    # j = 0
    # inf = False
    # while i < n:
    #     if s[i] == '>':
    #         j = i + 1
    #         while j < n and s[j] == '*':
    #             j += 1
    #         if j < n and s[j] == '<':
    #             inf = True
    #             break
    #         i = j
    #     else:
    #         i += 1

    # if inf:
    #     print(-1)
    #     continue

    # Find the longest < or > sequence
    # maxMoves = 0
    # i, j = 0, 0
    # while i < n:
    #     if s[i] == '<':
    #         j = i
    #         while j < n and s[j] == '<':
    #             j += 1
    #         maxMoves = max(maxMoves, j - i)
    #         i = j
    #     else:
    #         i += 1

    # maxMoves = 0
    # # find the largest > sequence from the start
    # i = 0
    # while i < n and s[i] == '>':
    #     maxMoves += 1
    #     i += 1

    # # find the largest < sequence
    # j = n - 1
    # count = 0
    # while j >= 0 and s[j] == '<':
    #     count += 1
    #     j -= 1
    # maxMoves = max(maxMoves, count)

    # print(maxMoves-1) if maxMoves > 0 else print(1)

    # Sequences can be <<<<<<
    # or >>>>>> (6 moves)
    # or >>>>>****<<<<< # (infinite since >****< is a loop)
    # or ******** (infinite)
    # or <<<>>> (3 moves)
    # or <<>><<>>>><<< (infinite as there is at least one ><)
    # or * (1 move as the person only rows once)
    # or < (1 move)
    # or > (1 move)


    # * is no current
    # < move one to the left
    # > move one to the right

    # # Check for infinite: any '>' before any '<'
    # firstLeft = s.rfind('<')
    # lastRight = s.find('>')

    # if firstLeft != -1 and lastRight != -1 and lastRight < firstLeft:
    #     print(-1)
    #     continue
    
    # if '*' in s and n > 1:
    #     print(-1)
    #     continue

    # maxMoves = 0
    # i = 0
    
    # while i < n:
    #     if s[i] in '<>':
    #         j = i
    #         while j < n and s[j] == s[i]:
    #             j += 1
    #         maxMoves = max(maxMoves, j - i)
    #         i = j
    #     else:
    #         i += 1

    # print(maxMoves if maxMoves > 0 else 1)

    # # Wait lol... what if >* and <* are basically loops...

    # # Sheesh why did this dumbass question take so long :(


    # Attempt#69, i guess...

    if n == 1:
        print(1)
        continue

    is_infinite = False
    for i in range(n - 1):
        if (s[i] == '>' or s[i] == '*') and (s[i+1] == '<' or s[i+1] == '*'):
            is_infinite = True
            break
    
    if is_infinite:
        print(-1)
        continue

    max_left = 0
    i = 0
    while i < n and (s[i] == '<' or s[i] == '*'):
        max_left += 1
        i += 1


    max_right = 0
    j = n - 1
    while j >= 0 and (s[j] == '>' or s[j] == '*'):
        max_right += 1
        j -= 1

    print(max(max_left, max_right))