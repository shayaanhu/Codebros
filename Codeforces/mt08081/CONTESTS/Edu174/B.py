for _ in range(int(input())):
    n, m = map(int, input().split())
    # n*m matrix
    # n rows and m columns
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    # print(matrix)

    # Count the occurrences of each color
    color_count = {}
    for row in matrix:
        for color in row:
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1

    # Find the maximum count of any single color
    max_color_count = max(color_count.values())

    # Calculate the minimum number of steps
    total_cells = n * m
    min_steps = total_cells - max_color_count

    print(min_steps)