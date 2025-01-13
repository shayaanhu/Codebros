# t = int(input())

# for i in range(t):
#     n = int(input())
#     aList = list(map(int, input().split()))
#     bList = list(map(int, input().split()))

#     total_surplus = 0
#     total_deficit = 0
    
#     for a, b in zip(aList, bList):
#         if a >= b:
#             total_surplus += 1
#         else:
#             total_deficit += 1
    
#     if total_surplus >= total_deficit:
#         print("YES")
#     else:
#         print("NO")

'''
# This isn't the solution. I didn't pay too much attention to the contest.
'''

t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of materials
    a = list(map(int, input().split()))  # Available materials
    b = list(map(int, input().split()))  # Required materials

    # Calculate total available and total needed materials
    total_available = sum(a)
    total_needed = sum(b)

    # Check if the total available materials are enough
    if total_available < total_needed:
        print("NO")
        continue

    # Calculate the deficit for individual materials
    deficit = 0
    for ai, bi in zip(a, b):
        if ai < bi:
            deficit += bi - ai

    # Check if the surplus is sufficient to cover the deficit
    surplus = total_available - total_needed
    if surplus >= deficit:
        print("YES")
    else:
        print("NO")
