for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 998244353

    # Find beautiful sequences.
    # Beautiful subsequences can only exist if numbers are either [1], [1, 2] or [1, 2, 3]

    count1 = 0 # Count starting 1s
    count12 = 0 # Count of 1, 2 ... 2
    count123 = 0 # Count of 1, 2, 2, ... , 3 ... 3

    for i in a:
        if i == 1:
            count1 = (count1 + 1) % MOD
        elif i == 2:
            count12 = (2 * count12 + count1) % MOD
        else:
            count123 = (count123 + count12) % MOD
    
    # Beautiful Sequences can only be in the case when 1, 2 and 3 all exist in the chain

    print(count123)