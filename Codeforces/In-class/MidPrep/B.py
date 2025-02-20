for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    L_i, R_i = map(int, input().split())
    # For each test case print q pairs of numbers Li≤l≤r≤Ri such that the value f(l,r) is maximum and among such the length r−l+1 
    # is minimum. If there are several correct answers, print any of them.
    # q is 1 (fixed)

    max_value = float('-inf')
    best_l = L_i - 1
    best_r = L_i - 1
    
    # We can calculate the prefix sum and prefix xor of the array a.
    prefix_sum = [0] * (n + 1)
    prefix_xor = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
        prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]

    for l in range(L_i, R_i + 1):
        for r in range(l, R_i + 1):
            current_sum = prefix_sum[r] - prefix_sum[l - 1]
            current_xor = prefix_xor[r] ^ prefix_xor[l - 1]
            current_value = current_sum - current_xor

            if (current_value > max_value) or (current_value == max_value and (r - l < best_r - best_l)):
                max_value = current_value
                best_l = l
                best_r = r
    print(best_l, best_r)