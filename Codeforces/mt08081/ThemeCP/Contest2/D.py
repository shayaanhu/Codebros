# 900

# Perpendicular segments

# This seems simple
# Just create a square

for _ in range(int(input())):
    X, Y, K = map(int, input().split())

    mini = min(X, Y)

    # Form a square of side mini

    # And then output the coordinates of A, B, C, D which form the square

    # A is always at origin
    A = (0, 0)
    B = (mini, 0)
    C = (mini, mini)
    D = (0, mini)

    print(A[0], A[1], C[0], C[1])
    print(B[0], B[1], D[0], D[1])