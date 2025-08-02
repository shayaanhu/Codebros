# l --> a -> b --> r
# a mod b is max
 
# any l below the half of r would have r-1 // 2 as the answer since l is smaller than this value.
# any l above this half would simply be r - l
# This follows from the the largest mod is always half but since that doesn't exist in the range
# we use the closest value to half which can be found by performing r - l
 
 
for _ in range(int(input())):
    l, r = map(int, input().split())
    if l <= (r//2) + 1:
        print((r-1)//2)
    else:
        print(r - l)