for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(a[0])
        continue

    a.sort(reverse=True)

    # Extract the max even from a and max odd
    # Use this to calculate the max odd and even sum
    max_even = -1
    max_odd = -1
    for i in range(n):
        if a[i] % 2 == 1:
            max_odd = max(max_odd, a[i])
        if a[i] % 2 == 0:
            max_even = max(max_even, a[i])

    odds = [i for i in a if i % 2 == 1]
    evens = [i for i in a if i % 2 == 0]

    if not evens:
        print(max_odd)
        continue
    if not odds:
        print(max_even)
        continue
    
    # [9, 5, 3]
    # [4, 2]
    # I will calculate both for max even and max odd and then will take max
    # 9 is chosen
    # now can either directly add 4 to 9 or do some manipulation
    # If we add 4 to 9, we get 13
    # However, 4 + 5 = 9 and 9 + 3 = 12
    # So we can add 12 to 9 and get 21

    if n == 2:
        print(max_odd + max_even)
        continue

    total = sum(a)

    candidate_odd = total - len(odds) + 1
    if candidate_odd % 2 == 0:
        candidate_odd -= 1

    candidate_even = total - len(odds)
    if candidate_even % 2 == 1:
        candidate_even -= 1

    best = max(candidate_odd, candidate_even)
    print(best)

    # print(sum(a)-2)
    
