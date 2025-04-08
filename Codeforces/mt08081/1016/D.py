def find_value_at_position(row, col, row_start, col_start, size, start_num):
    if size == 2:
        # Base case: 2×2 grid
        if row == row_start and col == col_start:  # Top left
            return start_num
        elif row == row_start+1 and col == col_start+1:  # Bottom right
            return start_num + 1
        elif row == row_start+1 and col == col_start:  # Bottom left
            return start_num + 2
        elif row == row_start and col == col_start+1:  # Top right
            return start_num + 3
    
    half_size = size // 2
    smallSize = (half_size * half_size)
    
    if row < row_start + half_size and col < col_start + half_size:
        # Top left
        return find_value_at_position(row, col, row_start, col_start, half_size, start_num)
    elif row >= row_start + half_size and col >= col_start + half_size:
        # Bottom right
        return find_value_at_position(row, col, row_start + half_size, col_start + half_size, 
                                    half_size, start_num + smallSize)
    elif row >= row_start + half_size and col < col_start + half_size:
        # Bottom left
        return find_value_at_position(row, col, row_start + half_size, col_start, 
                                    half_size, start_num + 2 * smallSize)
    else:
        # Top right
        return find_value_at_position(row, col, row_start, col_start + half_size, 
                                    half_size, start_num + 3 * smallSize)

def find_position_of_number(number, row_start, col_start, size, start_num):
    if size == 2:
        # Base case: 2×2 grid
        if number == start_num:  # Top left
            return row_start, col_start
        elif number == start_num + 1:  # Bottom right
            return row_start+1, col_start+1
        elif number == start_num + 2:  # Bottom left
            return row_start+1, col_start
        elif number == start_num + 3:  # Top right
            return row_start, col_start+1
    
    half_size = size // 2
    smallSize = (half_size * half_size)
    
    if number < start_num + smallSize:
        # Top left
        return find_position_of_number(number, row_start, col_start, half_size, start_num)
    elif number < start_num + 2 * smallSize:
        # Bottom right
        return find_position_of_number(number, row_start + half_size, col_start + half_size, 
                                     half_size, start_num + smallSize)
    elif number < start_num + 3 * smallSize:
        # Bottom left
        return find_position_of_number(number, row_start + half_size, col_start, 
                                     half_size, start_num + 2 * smallSize)
    else:
        # Top right
        return find_position_of_number(number, row_start, col_start + half_size, 
                                     half_size, start_num + 3 * smallSize)

for _ in range(int(input())):
    n = int(input())  # The grid is 2^n x 2^n
    size = 2**n
    
    q = int(input())
    for ques in range(q):
        a = list(map(str, input().split()))
        
        if a[0] == '->':
            # Find value at position (row, col)
            row, col = int(a[1]) - 1, int(a[2]) - 1
            value = find_value_at_position(row, col, 0, 0, size, 1)
            print(value)
        else:
            # Find position of number
            number = int(a[1])
            row, col = find_position_of_number(number, 0, 0, size, 1)
            print(row + 1, col + 1)