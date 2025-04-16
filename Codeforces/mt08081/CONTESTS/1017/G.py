# from collections import deque

# def rizz(is_reversed):
#     total = 0
#     if is_reversed:
#         for i, val in enumerate(reversed(arr)):
#             total += val * (i + 1)
#     else:
#         for i, val in enumerate(arr):
#             total += val * (i + 1)
#     return total


# for _ in range(int(input())):
#     q = int(input())
#     queries = [list(map(int, input().split())) for _ in range(q)]
    
#     arr = deque()

#     # Instead of reversing and inserting, we can just use a flag and simplify everything
#     # A deque also should improve time for insertion and deletion
#     is_reversed = False

#     # To avoid reversing, we can keep a running sum

#     current_sum = 0
#     element_sum = 0
#     size = 0
    
#     for query in queries:
#         if query[0] == 3:
#             element_sum += query[1]
#             if is_reversed:
#                 arr.appendleft(query[1])
#                 current_sum += query[1]
#                 current_sum += size
#             else:
#                 arr.append(query[1])
#                 current_sum += query[1] * (size + 1)

#             size += 1
                
#         elif query[0] == 2:
#             if size > 0:
#                 is_reversed = not is_reversed
#                 current_sum = (size + 1) * element_sum - current_sum
            
#         elif query[0] == 1 and size > 0:
#             if is_reversed:
#                 val = arr.popleft()
#                 arr.append(val)
#                 current_sum = current_sum + element_sum + (val * (size-1)) - val
#             else:
#                 val = arr.pop()
#                 arr.appendleft(val)
#                 current_sum = current_sum + element_sum - (val * (size-1))
        
#         # total = 0
#         # print(rizz(is_reversed))
#         print(current_sum)
                
#         # print(total


# from collections import deque

# for _ in range(int(input())):
#     q = int(input())
#     queries = [list(map(int, input().split())) for _ in range(q)]
    
#     arr = deque()
#     is_reversed = False

#     current_sum = 0
#     element_sum = 0
#     size = 0
    
#     for query in queries:
#         if query[0] == 3:  # Add element
#             element_sum += query[1]
#             if is_reversed:
#                 arr.appendleft(query[1])
#                 current_sum += query[1]
#                 current_sum += size
#             else:
#                 arr.append(query[1])
#                 current_sum += query[1] * (size + 1)
#             size += 1
                
#         elif query[0] == 2:  # Reverse array
#             if size > 0:
#                 is_reversed = not is_reversed
#                 current_sum = (size + 1) * element_sum - current_sum
            
#         elif query[0] == 1 and size > 0:  # Move last to front or first to back
#             if is_reversed:
#                 val = arr.popleft()
#                 arr.append(val)
#                 # Update current_sum for reversed case
#                 current_sum = current_sum - val + val * size
#             else:
#                 val = arr.pop()
#                 arr.appendleft(val)
#                 # Update current_sum for normal case
#                 current_sum = current_sum - val * size + val
        
#         print(current_sum)

from collections import deque

for _ in range(int(input())):
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    
    arr = deque()  # To simulate the array
    is_reversed = False  # To track if the array is reversed
    rizziness = 0  # Current rizziness
    size = 0  # Current size of the array
    
    for query in queries:
        if query[0] == 3:  # Append an element
            k = query[1]
            size += 1
            if is_reversed:
                # If reversed, the new element is effectively added to the front
                arr.appendleft(k)
                rizziness += k * 1  # New element contributes as the first element
                rizziness += sum(arr) - k  # All other elements shift by +1
            else:
                # Normal case, append to the end
                arr.append(k)
                rizziness += k * size  # New element contributes as the last element
            print(rizziness)
        
        elif query[0] == 2:  # Reverse the array
            is_reversed = not is_reversed
            # Reverse the rizziness calculation
            rizziness = size * sum(arr) - rizziness
            print(rizziness)
        
        elif query[0] == 1:  # Perform a cyclic shift
            if is_reversed:
                # Cyclic shift in reversed array: move first to last
                val = arr.popleft()
                arr.append(val)
                # Update rizziness
                rizziness = rizziness - val + val * size
            else:
                # Cyclic shift in normal array: move last to first
                val = arr.pop()
                arr.appendleft(val)
                # Update rizziness
                rizziness = rizziness - val * size + val
            print(rizziness)
