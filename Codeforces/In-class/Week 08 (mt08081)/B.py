n = int(input())
a = list(map(int, input().split()))
# Count the number of occurences in a of each number
count_dict = {}
for i in range(n):
    if a[i] not in count_dict:
        count_dict[a[i]] = 1
    else:
        count_dict[a[i]] += 1

# Multiply the numbers which have occured more than once to find one of the numbers x
# The max number in a will be y

maxi = max(a)
x = 1
# print(count_dict)
for num, count in count_dict.items():
    # numbers can occur in powers of 2 since they are factors of both x and y
    # if the number has occured more than once, then it is a factor of x
    if count > 1:
        # print(a[i], dict[a[i]])
        x *= (num ** (count - 1))

# Check if a multiple of x is present in a
# If it is then x is that multiple

for i in range(n):
    if a[i] % x == 0 and x < a[i]:
        x = a[i]
        
    
print(x, maxi)