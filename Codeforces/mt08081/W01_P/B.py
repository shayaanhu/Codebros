space_x = []
space_y = []
space_z = []
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    space_x.append(x)
    space_y.append(y)
    space_z.append(z)

sum_x = sum(space_x)
sum_y = sum(space_y)
sum_z = sum(space_z)
if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")