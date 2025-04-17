# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a.sort()

#     print(sum(a[n-k-1:]))


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Sort in descending order
    sorted_a = sorted(a, reverse=True)
    sum_first_k = sum(sorted_a[:k])
    
    # Build dictionaries for first and last occurrence of each value in sorted_a
    first_occ = {}
    last_occ = {}
    prev = None
    for i, x in enumerate(sorted_a):
        if x != prev:
            first_occ[x] = i
            prev = x
        last_occ[x] = i
    
    max_candidate = 0
    for x in a:
        i = first_occ[x]
        if i >= k:
            candidate = sum_first_k + x
        else:
            j = last_occ[x]
            last_pos = min(j, k - 1)
            count = last_pos - i + 1
            if count >= 2:
                candidate = sum_first_k + x
            else:
                candidate = sum_first_k + (sorted_a[k] if k < n else x)
        max_candidate = max(max_candidate, candidate)
    
    print(max_candidate)
