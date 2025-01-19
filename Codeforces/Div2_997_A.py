# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     for i in range(n):
#         x_i, y_i = map(int, input().split())
#         # Size m*m stamp is placed at (x_i, y_i)
#         # The stamp is placed on the paper
#         # find the perimeter of the shape formed by the stamp

#         lst = []

#         for x in range(x_i, x_i + m):
#             for y in range(y_i, y_i + m):
#                 lst.append((x, y))

#         # for x in range(x_i, x_i + m):
#         #     lst.append((x, y_i))
#         #     lst.append((x, y_i + m - 1))
        
#         # for y in range(y_i, y_i + m):
#         #     lst.append((x_i, y))
#         #     lst.append((x_i + m - 1, y))
        
#     final_lst = list(set(lst))
#     perimeter = 0
#     for x, y in final_lst:
#         if (x + 1, y) not in final_lst:
#             perimeter += 1
#         if (x - 1, y) not in final_lst:
#             perimeter += 1
#         if (x, y + 1) not in final_lst:
#             perimeter += 1
#         if (x, y - 1) not in final_lst:
#             perimeter += 1

#     # print(len(final_lst))
#     print(perimeter)
            

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    colored_cells = set()
    
    for i in range(n):
        x_i, y_i = map(int, input().split())

        for x in range(x_i, x_i + m):
            for y in range(y_i, y_i + m):
                colored_cells.add((x, y))
    
    
    perimeter = 0
    for x, y in colored_cells:
        if (x - 1, y) not in colored_cells:
            perimeter += 1
        if (x + 1, y) not in colored_cells:
            perimeter += 1
        if (x, y - 1) not in colored_cells:
            perimeter += 1
        if (x, y + 1) not in colored_cells:
            perimeter += 1
    
    if n != 1:
        perimeter = 2 * perimeter
    print(perimeter)