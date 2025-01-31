for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    max_sum = 0
    for min_element in range(k + 1):
        max_element = k - min_element
        remaining_elements = 0

        if min_element == 0:
            remaining_elements = prefix_sum[n - max_element]
        else:
            remaining_elements = prefix_sum[n - max_element] - prefix_sum[2 * min_element]

        max_sum = max(max_sum, remaining_elements)

    print(max_sum)
