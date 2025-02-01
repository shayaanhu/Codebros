for _ in range(int(input())):
    s = input()
    n = len(s)
    if '1' not in s or '2' not in s or '3' not in s:
        print(0)
        continue

    count = {'1': 0, '2': 0, '3': 0}
    left = 0
    min_len = float('inf')

    for right in range(n):
        if s[right] in count:
            count[s[right]] += 1

        while all(count.values()):
            min_len = min(min_len, right - left + 1)
            if s[left] in count:
                count[s[left]] -= 1
            left += 1

    print(min_len)