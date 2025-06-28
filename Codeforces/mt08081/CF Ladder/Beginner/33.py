# Simply check for the existence of "ba" or "ab"
# Print their positions if found else -1 -1


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    pos_a = s.find('ba')
    pos_b = s.find('ab')

    # if pos_a != -1 and pos_b != -1:
    #     if abs(pos_a - pos_b) == 1:
    #         print(min(pos_a, pos_b) + 1, max(pos_a, pos_b) + 1)
    #     else:
    #         print(-1, -1)
    # else:
    #     print(-1, -1)

    if pos_a != -1:
        print(pos_a + 1, pos_a + 2)
    elif pos_b != -1:
        print(pos_b + 1, pos_b + 2)
    else:
        print(-1, -1)